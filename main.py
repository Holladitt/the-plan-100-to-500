"""Write a short 30-day plan for turning $100 into $500 to /output/entry.txt."""

import os

PLAN = "Day 1: spend $40 on API credits and $12 on a domain. Sell a $25 same-day Shopify speed and SEO fix report to slow Shopify stores found via BuiltWith. Email 100 owners a day, deliver a PDF in 2 hours of payment via Stripe, reinvest earnings in outreach. 20 sales in 30 days = $500."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(PLAN)


if __name__ == "__main__":
    main()
