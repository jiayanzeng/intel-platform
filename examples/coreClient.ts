/**
 * coreClient.ts — a minimal typed TypeScript client for the Rust core.
 *
 * The point of this file: the core's contract is ten plain JSON/HTTP
 * endpoints, so the shell language is a free choice. This repo ships a
 * Python shell; swap in (or add) a TypeScript one — Next.js dashboard,
 * Bun API, CLI — by starting from this client. Nothing in the core changes.
 *
 *   const core = new CoreClient("http://127.0.0.1:8788");
 *   const view = await core.view(["science", "technology"]);
 */

export interface Evidence {
  doc_id: string;
  title: string;
  url: string | null;
  source_id: string;
  day: string | null;
  license: string;
  /** null when the source license forbids redistribution (gated in core) */
  excerpt: string | null;
}

export interface Signal {
  kind: "RisingEntity" | "Corroborated" | "EmergingEntity";
  headline: string;
  score: number;
  detail: string;
  entity_ids: string[];
  evidence: Evidence[];
}

export interface Edge {
  a: string;
  b: string;
  a_name: string;
  b_name: string;
  weight: number;
  pmi: number;
}

export interface View {
  window_end: string | null;
  documents_analyzed: number;
  kept_doc_ids: string[];
  mentions: number;
  near_duplicates: { dropped_id: string; kept_id: string; distance: number }[];
  signals: Signal[];
  edges: Edge[];
  discovered: { surface: string; doc_ids: string[] }[];
}

export interface ContextDoc {
  doc_id: string;
  sector: string;
  title: string;
  body: string;
  url: string | null;
  source_id: string;
  day: string | null;
  license: string;
  authors: string[];
  tags: string[];
}

export interface Retrieval {
  bm25: string[];
  vector: string[];
  fused: string[];
  notes: string[];
  context: ContextDoc[];
  suppressed: string[];
}

export class CoreClient {
  constructor(
    private baseUrl: string,
    private token?: string,
  ) {}

  private headers(): Record<string, string> {
    const h: Record<string, string> = { "Content-Type": "application/json" };
    if (this.token) h["x-core-token"] = this.token;
    return h;
  }

  private async get<T>(path: string, params?: Record<string, string>): Promise<T> {
    const url = new URL(path, this.baseUrl);
    for (const [k, v] of Object.entries(params ?? {})) url.searchParams.set(k, v);
    const r = await fetch(url, { headers: this.headers() });
    if (!r.ok) throw new Error(`core ${r.status}: ${await r.text()}`);
    return r.json() as Promise<T>;
  }

  private async post<T>(path: string, body: unknown): Promise<T> {
    const r = await fetch(new URL(path, this.baseUrl), {
      method: "POST",
      headers: this.headers(),
      body: JSON.stringify(body),
    });
    if (!r.ok) throw new Error(`core ${r.status}: ${await r.text()}`);
    return r.json() as Promise<T>;
  }

  health() {
    return this.get<{ status: string; documents: number; version: string }>("/health");
  }

  ingest(sectors: string[], sources?: string[]) {
    // `sources` (optional) runs exactly those source ids, each still validated
    // against `sectors`; omit it to run every source in the sectors.
    const body: { sectors: string[]; sources?: string[] } = { sectors };
    if (sources) body.sources = sources;
    return this.post<{ fetched: number; new: number; results: unknown[] }>(
      "/ingest",
      body,
    );
  }

  view(sectors: string[]) {
    return this.get<View>("/view", { sectors: sectors.join(",") });
  }

  search(q: string, sectors: string[], limit = 10) {
    return this.get<unknown[]>("/search", {
      q,
      sectors: sectors.join(","),
      limit: String(limit),
    });
  }

  retrieve(q: string, sectors: string[], k = 5, model?: string, queryVector?: number[]) {
    return this.post<Retrieval>("/retrieve", {
      q,
      sectors,
      k,
      model,
      query_vector: queryVector,
    });
  }
}
