 async def test_id_token_missing_sub_claim_does_not_stamp(self, db, token_client):
        # Valid JWT but no ``sub`` claim → decode returns None → no stamp.
        vau = _vau()
        id_token_no_sub = jwt.encode({"iss": "test"}, "secret", algorithm="HS256")
        token_client.perform_vau_login = AsyncMock(return_value=_vau_response(id_token=id_token_no_sub))
        with patch("app.services.vau.identity.VAUInstanceRepository") as MockRepo:
            MockRepo.return_value.get_by_id = AsyncMock(return_value=vau)

            resolver = VAUOBOResolver(db, token_client)
            ctx = _ctx(
                **{
                    "x-opal-instance-id": "inst-1",
                    "x-opal-user-id": "vau-optiid-1",
                    "x-opal-vau-id": "vau-1",
                }
            )
           
# """URL canonicalization for the crawl pipeline.

# Two transformations are applied to every URL the worker persists into
# `content_crawls.seed_url` / `content_crawl_links.url`, or republishes onto
# `crawl`:

# 1. The fragment (anything after `#`) is dropped unconditionally.
#    Fragments never reach the server, so they only fragment the dedup
#    space; collapsing them strengthens the `UNIQUE (session_id, url)`
#    invariant. The cost is SPA fragment-routed sites collapsing to a
#    single canonical URL — acceptable for a server-fetch aragog.
# 2. Query parameters whose name (case-insensitive) appears in the
#    vendored mpchadwick tracking-params registry are removed. Survivor
#    params keep their original order; if nothing survives, no trailing
#    `?` is emitted.

# URLs with neither query nor fragment pass through byte-identical — the
# parse/round-trip is short-circuited so we don't introduce cosmetic
# mutations (e.g. urlunparse adding a `/`-path where the source had none).

# The registry is vendored at `data/tracking_params.csv` and loaded once
# at module import; runtime does not depend on network reachability of
# upstream. Refresh via `make refresh-tracking-params`.
# """

# from __future__ import annotations

# import csv
# from dataclasses import dataclass
# from importlib.resources import files
# from urllib.parse import parse_qsl, urlencode, urlparse, urlunparse


# @dataclass(frozen=True, slots=True)
# class SanitizationResult:
#     """Outcome of `sanitize(url)`.

#     `canonical` is the URL to use everywhere downstream. `stripped` is
#     the list of query-parameter names that were removed (in the order
#     they appeared in the source URL), used by callers that want to log
#     or otherwise observe mutations. For a no-op, `stripped` is empty AND
#     `canonical is url` (identity-preserving for the trivial case).
#     """

#     canonical: str
#     stripped: tuple[str, ...]


# def _load_tracking_params() -> frozenset[str]:
#     """Read the vendored CSV once and freeze the param-name set.

#     The mpchadwick registry has columns `name,platform,confirmed_in,
#     unique_per_visitor`. We only care about `name`, and we lowercase it
#     at load time so the runtime match is a single set lookup.
#     """

#     csv_path = files("aragog").joinpath("data/tracking_params.csv")
#     with csv_path.open("r", encoding="utf-8") as fh:
#         reader = csv.DictReader(fh)
#         if reader.fieldnames is None or "name" not in reader.fieldnames:
#             raise RuntimeError(
#                 f"vendored tracking-params CSV missing 'name' column: "
#                 f"fieldnames={reader.fieldnames}"
#             )
#         return frozenset(row["name"].strip().lower() for row in reader if row.get("name"))


# TRACKING_PARAMS: frozenset[str] = _load_tracking_params()


# def sanitize(url: str) -> SanitizationResult:
#     """Return the canonical form of `url`.

#     See module docstring for the rule. Callers that only want the
#     canonical string can read `.canonical`; callers that need to log
#     mutations read `.stripped` to decide whether to emit an event.
#     """

#     parsed = urlparse(url)

#     # Trivial-case fast path: no query AND no fragment → nothing to do.
#     # Returns the input string by identity, so byte-for-byte passthrough
#     # is preserved (no urlunparse round-trip).
#     if not parsed.query and not parsed.fragment:
#         return SanitizationResult(canonical=url, stripped=())

#     kept: list[tuple[str, str]] = []
#     stripped: list[str] = []
#     if parsed.query:
#         # keep_blank_values=True so `?utm_source=` strips like `?utm_source=foo`.
#         for name, value in parse_qsl(parsed.query, keep_blank_values=True):
#             if name.lower() in TRACKING_PARAMS:
#                 stripped.append(name)
#             else:
#                 kept.append((name, value))

#     # urlencode("") returns "", which urlunparse renders as no '?' at all.
#     new_query = urlencode(kept) if kept else ""

#     canonical = urlunparse(
#         (parsed.scheme, parsed.netloc, parsed.path, parsed.params, new_query, "")
#     )
#     return SanitizationResult(canonical=canonical, stripped=tuple(stripped))
