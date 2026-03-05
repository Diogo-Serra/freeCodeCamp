def create_spend_chart(categories):
    # 1) Spend per category (withdrawals only)
    spends = []
    for c in categories:
        spent = sum(-item["amount"] for item in c.ledger if item["amount"] < 0)
        spends.append(spent)

    total_spent = sum(spends) if spends else 0
    percentages = [0 if total_spent == 0 else (s / total_spent * 100) for s in spends]
    # Round down to nearest 10
    ticks = [int(p // 10) * 10 for p in percentages]

    # 2) Build lines without stripping spaces
    lines = []
    lines.append("Percentage spent by category")

    # 100..0 chart
    for level in range(100, -1, -10):
        line = f"{level:>3}| "
        for t in ticks:
            line += ("o  " if t >= level else "   ")
        lines.append(line)  # keep trailing spaces for fixed width

    # Separator
    lines.append("    " + "-" * (3 * len(categories) + 1))

    # 3) Vertical names (each line same length, 2 spaces between, plus 2 after final)
    names = [c.name for c in categories]
    maxlen = max((len(n) for n in names), default=0)
    for i in range(maxlen):
        line = "     "
        for n in names:
            ch = n[i] if i < len(n) else " "
            line += ch + "  "   # two spaces after each category (kept even after last)
        lines.append(line)

    # 4) Return with NO trailing newline at the very end
    return "\n".join(lines)
