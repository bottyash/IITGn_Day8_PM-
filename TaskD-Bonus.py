"""
Day-8 Assignment | Part D (Bonus): Daily Transaction Analyzer
Paytm Case Study — Mini Analytics Dashboard
"""


# ─────────────────────────────────────────────
#  CONSTANTS
# ─────────────────────────────────────────────
HIGH_VALUE_THRESHOLD = 10_000
BAR_SCALE = 1_000          # 1 star per ₹1000
VALID_TYPES = {"credit", "debit"}
VALID_CATEGORIES = {"food", "travel", "bills", "shopping", "other"}


# ─────────────────────────────────────────────
#  HELPER: Print a bar for the chart
# ─────────────────────────────────────────────
def amount_bar(amount: float) -> str:
    """Return a bar string: 1 * per ₹1000, min 1 star."""
    stars = max(1, int(amount // BAR_SCALE))
    return "*" * stars


# ─────────────────────────────────────────────
#  MAIN PROGRAM
# ─────────────────────────────────────────────
def main():
    transactions = []          # list of dicts: {amount, type, category, high_value}
    total_credit = 0.0
    total_debit = 0.0
    category_totals = {}       # {category: total_amount}  — bonus enhancement

    print("=" * 55)
    print("   💳  Paytm Mini Analytics Dashboard")
    print("=" * 55)
    print("  Enter transactions. Type 'done' to finish.\n")

    # ─────────────────────────────────────────
    # TODO 1 & 2: While loop — accept transactions until 'done'
    # ─────────────────────────────────────────
    while True:
        raw = input("Amount (or 'done'): ").strip().lower()

        if raw == "done":
            break

        # ── Validate amount ──
        try:
            amount = float(raw)
            if amount <= 0:
                print("  ⚠  Amount must be positive.\n")
                continue
        except ValueError:
            print("  ⚠  Invalid amount. Enter a number or 'done'.\n")
            continue

        # ── Validate type ──
        t_type = input("Type (credit/debit)  : ").strip().lower()
        if t_type not in VALID_TYPES:
            print(f"  ⚠  Type must be 'credit' or 'debit'.\n")
            continue

        # ── Category (bonus) ──
        category = input(
            f"Category ({'/'.join(VALID_CATEGORIES)}): "
        ).strip().lower()
        if category not in VALID_CATEGORIES:
            category = "other"

        # TODO 3: Flag high-value transactions
        is_high_value = amount > HIGH_VALUE_THRESHOLD
        if is_high_value:
            print(f"  🚨 HIGH-VALUE transaction flagged: ₹{amount:,.2f}\n")
        else:
            print(f"  ✅ Transaction recorded.\n")

        # ── Store transaction ──
        transactions.append({
            "amount": amount,
            "type": t_type,
            "category": category,
            "high_value": is_high_value,
        })

        # ── Running totals ──
        if t_type == "credit":
            total_credit += amount
        else:
            total_debit += amount

        # ── Category totals (bonus) ──
        category_totals[category] = category_totals.get(category, 0) + amount

    # ─────────────────────────────────────────
    #  Guard: no transactions entered
    # ─────────────────────────────────────────
    if not transactions:
        print("\n  No transactions recorded. Exiting.")
        return

    # ─────────────────────────────────────────
    # TODO 4: Calculate summary stats
    # ─────────────────────────────────────────
    amounts = [t["amount"] for t in transactions]
    transaction_count = len(amounts)
    highest_transaction = max(amounts)
    average_amount = sum(amounts) / transaction_count
    net_balance = total_credit - total_debit

    # ─────────────────────────────────────────
    # TODO 5: Bar chart of last 10 transactions
    # ─────────────────────────────────────────
    print("\n" + "=" * 55)
    print("   📊 Bar Chart — Last 10 Transactions (* = ₹1000)")
    print("=" * 55)

    last_10 = transactions[-10:]                 # slice last 10

    for idx, txn in enumerate(last_10, start=1):  # for loop with enumerate
        bar = amount_bar(txn["amount"])
        flag = " 🚨" if txn["high_value"] else ""
        direction = "+" if txn["type"] == "credit" else "-"
        print(
            f"  {idx:>2}. ₹{txn['amount']:>10,.2f} "
            f"[{direction}] [{txn['category']:<8}] {bar}{flag}"
        )

    # ─────────────────────────────────────────
    # TODO 6: Summary
    # ─────────────────────────────────────────
    print("\n" + "=" * 55)
    print("   📋 Transaction Summary")
    print("=" * 55)
    print(f"  Total transactions  : {transaction_count}")
    print(f"  Total credits       : ₹{total_credit:>12,.2f}")
    print(f"  Total debits        : ₹{total_debit:>12,.2f}")
    print(f"  Net balance         : ₹{net_balance:>12,.2f}")
    print(f"  Highest transaction : ₹{highest_transaction:>12,.2f}")
    print(f"  Average amount      : ₹{average_amount:>12,.2f}")

    high_value_count = sum(1 for t in transactions if t["high_value"])
    if high_value_count:
        print(f"  High-value flagged  : {high_value_count} transaction(s)")

    # ─────────────────────────────────────────
    # BONUS: Category spending breakdown
    # ─────────────────────────────────────────
    print("\n  📦 Spending by Category")
    print("  " + "-" * 35)

    for category, total in sorted(category_totals.items(),
                                  key=lambda x: x[1], reverse=True):
        percent = (total / sum(category_totals.values())) * 100
        print(f"  {category:<10}: ₹{total:>10,.2f}  ({percent:.1f}%)")

    print("=" * 55)


if __name__ == "__main__":
    main()
