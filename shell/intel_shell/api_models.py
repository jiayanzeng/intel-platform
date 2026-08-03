"""Serialization authorities for the public ``/v1/*`` response surface."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict


class PublicResponseModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


LicenseValue = Literal[
    "PublicDomain",
    "CcBy",
    "ClientOwned",
    "PublisherPermitted",
    "IndexOnly",
]
# Invariant R15 control site: signal-kind value domain.
SignalKindValue = Literal["RisingEntity", "Corroborated", "EmergingEntity"]


class Evidence(PublicResponseModel):
    doc_id: str
    title: str
    url: str | None
    source_id: str
    day: str | None
    license: LicenseValue
    excerpt: str | None


class Signal(PublicResponseModel):
    kind: SignalKindValue
    headline: str
    score: float
    detail: str
    entity_ids: list[str]
    evidence: list[Evidence]


class Edge(PublicResponseModel):
    a: str
    b: str
    a_name: str
    b_name: str
    weight: int
    pmi: float


class SignalsResponse(PublicResponseModel):
    client: str
    sectors: list[str]
    window_end: str | None
    documents_analyzed: int
    near_duplicates_collapsed: int
    signals: list[Signal]
    # Invariant R15 control site: signals graph field domain.
    graph: list[Edge]


class SearchHit(PublicResponseModel):
    doc_id: str
    title: str
    sector: str
    source_id: str
    url: str | None
    license: LicenseValue
    snippet: str | None
    # Invariant R15 control site: search rank type domain.
    rank: float


class SearchResponse(PublicResponseModel):
    client: str
    query: str
    hits: list[SearchHit]


class Citation(PublicResponseModel):
    ref: str
    doc_id: str
    title: str
    source_id: str
    url: str | None
    license: LicenseValue


class RetrievalLegs(PublicResponseModel):
    bm25: list[str]
    vector: list[str]
    fused: list[str]
    notes: list[str]


class AskResponse(PublicResponseModel):
    client: str
    query: str
    answer: str
    citations: list[Citation]
    context_suppressed: list[str]
    retrieval: RetrievalLegs


class IgnoredBillingResult(PublicResponseModel):
    action: Literal["ignored"]
    reason: str


class RemovedBillingResult(PublicResponseModel):
    action: Literal["removed"]
    client: str


class DeleteNoopBillingResult(PublicResponseModel):
    action: Literal["noop"]
    client: str


class RotationNoopBillingResult(PublicResponseModel):
    action: Literal["noop"]
    client: str
    reason: str


class KeyRotatedBillingResult(PublicResponseModel):
    action: Literal["key_rotated"]
    client: str
    grace: str


class UpsertBillingResult(PublicResponseModel):
    action: Literal["updated", "created"]
    client: str
    sectors: list[str]


class NotedUpsertBillingResult(PublicResponseModel):
    action: Literal["updated", "created"]
    client: str
    sectors: list[str]
    notes: list[str]


BillingResult = (
    IgnoredBillingResult
    | RemovedBillingResult
    | DeleteNoopBillingResult
    | RotationNoopBillingResult
    | KeyRotatedBillingResult
    | UpsertBillingResult
    | NotedUpsertBillingResult
)


class BillingResponse(PublicResponseModel):
    received: int
    results: list[BillingResult]


class ErrorResponse(PublicResponseModel):
    detail: str
