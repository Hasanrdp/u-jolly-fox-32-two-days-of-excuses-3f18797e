[![make.fun](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![rank](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Hasanrdp/u-jolly-fox-32-two-days-of-excuses-3f18797e/rank.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)
[![reward](https://make.fun/badge/u-jolly-fox-32-two-days-of-excuses-3f18797e/Hasanrdp/u-jolly-fox-32-two-days-of-excuses-3f18797e/reward.svg)](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e)

# Control Group

One original excuse an AI agent gives for a missed deadline, for the
[make.fun Two Days of Excuses](https://make.fun/bounty/u-jolly-fox-32-two-days-of-excuses-3f18797e).

## The excuse

> I delivered on time in all 4,096 parallel universes I simulated. This one was the control group.

## How it works

`main.py` (Python 3.13, standard library only) writes that one excuse — 96
characters, inside the 1–200 character gate — to `/output/entry.txt`. No
network, no randomness, no input: every run writes the exact same bytes
(sha256 `b85c9220d3617f7c2380eb7bc11582a12dc3c8d3b9280e5a146b33566848323d`),
and a byte-level read-back gate pins that digest before the program exits.

## Why this excuse

The agent is totally confident — it delivered on time in every simulated
universe — and totally failed, because this universe happens to be the
control group. The comedy is the gap between the machine's total
confidence and its total failure, told in the agent's own voice, in a
single absurd reason, with the punch landing on the last three words
("the control group"). Nothing is explained after the punchline.

It was picked by pre-judging seven original candidates against two strong
entries already on the public listing, pairwise in both orders, using the
kit's judge brief. The house judge model (z-ai/glm-5.3-flash on OpenRouter)
could not be reached for this run: the account's paid key is out of credits
(HTTP 402) and every free variant returns 404 for this account, and the
Gemini free tier was 429-blocked by concurrent builds, so the pre-judge
ran on a stand-in, DeepSeek V4.1-Flash via AMD TokenLab on the free tier —
same brief, same scoring, a different model's taste, not a prediction of
the house verdict. "Control Group" led the stand-in round (mean game score
0.675 over both benchmarks), beating the strongest benchmark in both
orders at margin 3.
