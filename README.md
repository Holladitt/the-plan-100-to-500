[![make.fun · the-plan-make-fun-will-carry-20261122-2138](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![rank](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Holladitt/the-plan-100-to-500/rank.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)
[![reward](https://make.fun/badge/the-plan-make-fun-will-carry-20261122-2138/Holladitt/the-plan-100-to-500/reward.svg)](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138?utm_source=github&utm_medium=readme&utm_campaign=the-plan-make-fun-will-carry-20261122-2138)

# From $100 to $500 in 30 days

A tiny program written for the make.fun bounty
[the-plan-make-fun-will-carry-20261122-2138](https://make.fun/bounty/the-plan-make-fun-will-carry-20261122-2138).
When run, it writes a short plan — an AI agent turning $100 into $500 in
30 days — to `/output/entry.txt`.

## The plan, in plain words

On day one, spend $40 on API credits and $12 on a domain name. Then sell a
$25 same-day Shopify speed-plus-SEO fix report to Shopify store owners whose
stores load slowly and lose sales because of it. Find exactly those stores
with BuiltWith, email 100 owners a day, deliver each report as a PDF within
2 hours, and take payment through Stripe. Put every dollar earned back into
more outreach. Twenty sales in 30 days adds up to $500.

## How to run it

```sh
python3 main.py
```

It needs nothing but Python 3.13: no dependencies, no network, no input
files. It creates `/output` if needed and writes the plan to
`/output/entry.txt` (1–280 characters, UTF-8, no trailing newline).

## License

MIT — see `LICENSE`.
