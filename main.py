#!/usr/bin/env python3
"""Write the v2 plan for the make.fun bounty to /output/entry.txt."""

# v2: WCAG accessibility audits — lawsuit-risk niche, $99 same-day service.
import os

PLAN = (
    "Day 1: spend $40 on APIs, $12 on a domain. "
    "Sell $99 same-day WCAG accessibility audits to e-commerce stores "
    "risking lawsuits, found via BuiltWith. "
    "Email 50 a day, deliver a PDF audit in 24 hours, paid by Stripe. "
    "Reinvest every dollar into outreach. "
    "5 sales = $495 in 30 days."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(PLAN)


if __name__ == "__main__":
    main()
