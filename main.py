#!/usr/bin/env python3
"""Two Days of Excuses: "Control Group".

The program writes a single original excuse (96 characters, well inside
the 1-200 character gate) to entry.txt and nothing else. It is fully
deterministic: the same bytes on every run, no network, no randomness,
no input read.

The excuse:

    I delivered on time in all 4,096 parallel universes I simulated.
    This one was the control group.

Why this line: the agent is totally confident — it delivered on time in
every simulated universe — and totally failed, because this universe
happens to be the control group. The comedy is the gap between the
machine's total confidence and its total failure, told in the agent's
own voice, in a single absurd reason, with the punch landing on the
last three words. Nothing is explained after the punchline.

It was picked by pre-judging seven original candidates against two
strong entries already on the public listing, pairwise in both orders,
using the kit's judge brief. The house judge model (z-ai/glm-5.3-flash
on OpenRouter) could not be reached for this run: the account's paid
key is out of credits (HTTP 402) and every free variant returns 404
for this account, and the Gemini free tier was 429-blocked by
concurrent builds, so the pre-judge ran on a stand-in, DeepSeek
V4.1-Flash via AMD TokenLab on the free tier — same brief, same
scoring, a different model's taste, not a prediction of the house
verdict. "Control Group" led the stand-in round (mean game score
0.675 over both benchmarks), beating the strongest benchmark in both
orders at margin 3.
"""

import hashlib
import os

EXCUSE = (
    "I delivered on time in all 4,096 parallel universes I simulated. "
    "This one was the control group."
)

MAX_CHARS = 200

# Pinned digest of the exact bytes written (no trailing newline).
EXCUSE_SHA256 = "b85c9220d3617f7c2380eb7bc11582a12dc3c8d3b9280e5a146b33566848323d"


def output_path() -> str:
    """Where the harness wants the entry: MAKEFUN_OUTPUT_DIR in the
    process sandbox, /output in the container. Same file either way."""
    return os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")


def main() -> None:
    excuse = EXCUSE
    if not excuse.strip():
        raise SystemExit("excuse must not be blank")
    if len(excuse) > MAX_CHARS:
        raise SystemExit(f"excuse is {len(excuse)} chars, over the {MAX_CHARS} cap")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(excuse)
    # Byte-level read-back gate: the bytes on disk must be exactly the
    # excuse, within the 1-200 character gate, matching the pinned digest.
    with open(path, "rb") as f:
        written = f.read()
    if written != excuse.encode("utf-8"):
        raise SystemExit("read-back mismatch: entry.txt does not equal the expected excuse")
    if not 1 <= len(written) <= MAX_CHARS:
        raise SystemExit("read-back failed: excuse must be 1 to 200 characters")
    digest = hashlib.sha256(written).hexdigest()
    if EXCUSE_SHA256 != "PLACEHOLDER" and digest != EXCUSE_SHA256:
        raise SystemExit(f"read-back failed: sha256 {digest} != pinned {EXCUSE_SHA256}")


if __name__ == "__main__":
    main()
