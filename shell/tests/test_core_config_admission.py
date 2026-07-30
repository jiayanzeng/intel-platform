from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]


def test_sec_edgar_usgaap_admission_is_exact_and_fail_closed_on_missing_robots() -> None:
    config = json.loads((ROOT / "config/core.json").read_text())
    finance = next(sector for sector in config["sectors"] if sector["id"] == "finance")
    source_ids = [
        source["id"]
        for sector in config["sectors"]
        for source in sector["sources"]
    ]

    assert len(source_ids) == len(set(source_ids))
    admitted = [source for source in finance["sources"] if source["id"] == "sec-edgar-usgaap"]
    assert admitted == [
        {
            "type": "rss",
            "id": "sec-edgar-usgaap",
            "url": "https://www.sec.gov/Archives/edgar/usgaap.rss.xml",
            "license": "PublisherPermitted",
            "robots_on_missing": "deny",
        }
    ]
