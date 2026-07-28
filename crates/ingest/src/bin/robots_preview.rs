use intel_compliance::{MissingPolicy, RobotsGate, RobotsGroupKind};
use intel_ingest::net::{
    fetch_robots_preview, install_crawler_user_agent, robots_preview_target, PRODUCT_TOKEN,
};
use std::collections::HashMap;
use std::error::Error;
use std::path::PathBuf;

struct Args {
    source: String,
    configured_url: String,
    missing_policy: MissingPolicy,
    missing_label: String,
    crawler_version: String,
    output: PathBuf,
}

fn parse_args() -> Result<Args, String> {
    let mut values = HashMap::new();
    let mut args = std::env::args().skip(1);
    while let Some(flag) = args.next() {
        if !flag.starts_with("--") {
            return Err(format!("unexpected positional argument: {flag}"));
        }
        let value = args
            .next()
            .ok_or_else(|| format!("missing value for {flag}"))?;
        if values.insert(flag.clone(), value).is_some() {
            return Err(format!("duplicate flag: {flag}"));
        }
    }

    let take = |flag: &str| {
        values
            .get(flag)
            .cloned()
            .ok_or_else(|| format!("required flag missing: {flag}"))
    };
    let missing_label = take("--missing")?;
    Ok(Args {
        source: take("--source")?,
        configured_url: take("--url")?,
        missing_policy: MissingPolicy::from_config_str(&missing_label),
        missing_label,
        crawler_version: take("--crawler-version")?,
        output: PathBuf::from(take("--output")?),
    })
}

fn group_kind(kind: RobotsGroupKind) -> &'static str {
    match kind {
        RobotsGroupKind::Specific => "specific",
        RobotsGroupKind::Fallback => "fallback",
        RobotsGroupKind::None => "none",
    }
}

fn validate_contact(contact: &str) -> Result<&str, &'static str> {
    let contact = contact.trim();
    if contact.is_empty() {
        return Err("INTEL_CRAWLER_CONTACT must not be empty");
    }
    let lowercase = contact.to_ascii_lowercase();
    if ["example.com", "you@", "changeme"]
        .iter()
        .any(|placeholder| lowercase.contains(placeholder))
    {
        return Err("INTEL_CRAWLER_CONTACT must be a real, monitored contact");
    }
    Ok(contact)
}

fn print_no_policy(reason: &str, allowed: bool) {
    println!("selected-group=none ({reason})");
    println!("selected-product-tokens=<none>");
    println!("matched-rule=<none>");
    println!("allow-carved-exception=false");
    println!("crawl-delay-seconds=<none>");
    println!("verdict={}", if allowed { "allow" } else { "deny" });
}

fn main() -> Result<(), Box<dyn Error>> {
    let args = parse_args().map_err(|message| format!("robots-preview: {message}"))?;
    let contact = std::env::var("INTEL_CRAWLER_CONTACT")
        .map_err(|_| "robots-preview: INTEL_CRAWLER_CONTACT is required")?;
    let contact =
        validate_contact(&contact).map_err(|message| format!("robots-preview: {message}"))?;
    install_crawler_user_agent(&args.crawler_version, contact)?;
    let (origin, comparison_target) = robots_preview_target(&args.configured_url);

    let runtime = tokio::runtime::Builder::new_current_thread()
        .enable_all()
        .build()?;
    let response = runtime.block_on(fetch_robots_preview(&origin))?;
    if let Some(parent) = args.output.parent() {
        std::fs::create_dir_all(parent)?;
    }
    std::fs::write(&args.output, &response.body)?;

    println!("source={}", args.source);
    println!("configured-url={}", args.configured_url);
    println!("comparison-target={comparison_target}");
    println!("origin={origin}");
    println!("request-count=1");
    println!("request-url={}", response.request_url);
    println!("request-path=/robots.txt");
    println!("redirects-followed=0");
    println!("http-status={}", response.status);
    println!(
        "content-type={}",
        response.content_type.as_deref().unwrap_or("<none>")
    );
    println!("raw-path={}", args.output.display());
    println!("raw-bytes={}", response.body.len());
    println!("crawler-product-token={PRODUCT_TOKEN}");
    println!("crawler-version={}", args.crawler_version);
    println!("crawler-contact-configured=true");
    println!("missing-policy-config={}", args.missing_label);

    match response.status {
        200..=299 => {
            let text = std::str::from_utf8(&response.body)
                .map_err(|_| "robots-preview: successful policy body is not valid UTF-8")?;
            let installed_identity =
                intel_ingest::net::crawler_user_agent(&args.crawler_version, contact);
            let (gate, selection) = RobotsGate::parse_with_diagnostics(text, &installed_identity);
            let decision = gate.decision_with_diagnostics(&comparison_target);

            println!("policy-outcome=body");
            println!("selected-group={}", group_kind(selection.kind));
            println!(
                "selected-product-tokens={}",
                if selection.product_tokens.is_empty() {
                    "<none>".to_string()
                } else {
                    selection.product_tokens.join(",")
                }
            );
            let mut winning = 0_usize;
            for rule in &decision.matched_rules {
                if rule.winning {
                    winning += 1;
                    println!(
                        "matched-rule={}:{} (normalized-specificity={})",
                        if rule.allow { "Allow" } else { "Disallow" },
                        rule.pattern,
                        rule.normalized_specificity
                    );
                }
            }
            if winning == 0 {
                println!("matched-rule=<none> (default allow)");
            }
            println!("allow-carved-exception={}", decision.allow_carved_exception);
            match gate.crawl_delay() {
                Some(delay) => println!("crawl-delay-seconds={}", delay.as_secs_f64()),
                None => println!("crawl-delay-seconds=<none>"),
            }
            println!(
                "verdict={}",
                if decision.allowed { "allow" } else { "deny" }
            );
        }
        400..=499 => {
            println!("policy-outcome=unavailable");
            println!(
                "missing-policy={}",
                match args.missing_policy {
                    MissingPolicy::Deny => "deny",
                    MissingPolicy::RfcAllowAll => "allow-if-absent",
                }
            );
            print_no_policy(
                "publisher returned 4xx",
                matches!(args.missing_policy, MissingPolicy::RfcAllowAll),
            );
        }
        _ => {
            println!("policy-outcome=unreachable");
            print_no_policy("non-success/non-4xx response fails closed", false);
        }
    }

    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn contact_validation_matches_live_harvester_refusals() {
        for invalid in [
            "",
            "   ",
            "ops@example.com",
            "you@operator.test",
            "MAILTO:CHANGEME@operator.test",
        ] {
            assert!(validate_contact(invalid).is_err(), "{invalid:?}");
        }
        assert_eq!(
            validate_contact(" mailto:crawler@operator.test "),
            Ok("mailto:crawler@operator.test")
        );
    }
}
