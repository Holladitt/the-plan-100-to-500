#!/usr/bin/env python3
"""Write the v3 plan to /output/entry.txt.

v3: Google review rescue pack for low-rated local restaurants.
"""

import os

PLAN = "Day 1: $40 API credits, $12 domain. Sell a $30 same-day Google review rescue pack to restaurants rated 3.5 or less, via Google Maps: replies to bad reviews + 10 templates. Email 100/day, deliver in 2 hours, Stripe. Reinvest every dollar in outreach. 17 sales = $510 in 30 days."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
