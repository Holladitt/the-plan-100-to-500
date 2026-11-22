#!/usr/bin/env python3
"""Write the 30-day plan for turning $100 into $500 to /output/entry.txt.

Rebuilt fresh from the prose brief; no dependencies, no network.
"""

import os

PLAN = (
    "Day 1: spend $40 on API credits and $12 on a domain. "
    "Sell a $25 same-day Shopify speed-plus-SEO fix report to slow "
    "Shopify stores found via BuiltWith. "
    "Email 100 owners daily, deliver a PDF in 2 hours, paid via Stripe. "
    "Reinvest earnings into outreach. "
    "20 sales in 30 days = $500."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
