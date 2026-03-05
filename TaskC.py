"""
Day-8 Assignment | Part C: AI-Augmented Task — Diamond Pattern
═══════════════════════════════════════════════════════════════

EXACT PROMPT USED:
──────────────────
"Write a Python program that prints a diamond pattern of asterisks.
 The user inputs the number of rows for the upper half.
 Include proper spacing and use nested loops only (no string multiplication tricks)."

AI'S OUTPUT (Claude / ChatGPT):
───────────────────────────────
n = int(input("Enter rows for upper half: "))

for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()

for i in range(n - 1, 0, -1):
    for j in range(n - i):
        print(" ", end="")
    for k in range(2 * i - 1):
        print("*", end="")
    print()


CRITICAL EVALUATION:
────────────────────
✅ Spacing correctness    — Correct. Spaces = (n - row), stars = (2*row - 1).
                            The formula is mathematically sound.

✅ Nested loops only      — Yes, uses nested for loops with print(end="").
                            No string multiplication (*) used — meets the brief.

✅ Readability            — Acceptable but not great. Variable names (i, j, k)
                            are generic and give no semantic meaning.
                            No comments or docstring explaining the logic.

⚠️ Edge case n = 0        — range(1, 1) is empty, prints nothing. Silent — OK,
                            but no user-facing message. Should warn the user.

⚠️ Edge case n = 1        — Prints a single "*". Correct, but the "lower half"
                            loop range(0, 0, -1) is empty — the star only
                            appears once, which is the right behaviour.

⚠️ No input validation    — Negative input or non-integer crashes with
                            ValueError or produces no output without explanation.

⏱ Time complexity         — O(n²). The outer loop runs n times; inner loops
                            run O(n) each → total O(n²). Acceptable for a
                            visual pattern generator where n is small.

IMPROVED VERSION (below):
"""


def print_diamond(n: int) -> None:
    """
    Print a diamond of asterisks whose upper half has `n` rows.

    Pattern for n=4:
       *
      ***
     *****
    *******
     *****
      ***
       *

    Time complexity : O(n²)  — two nested loops each O(n).
    Space complexity: O(1)   — no storage proportional to n.
    """
    if n <= 0:
        print("  ⚠  Please enter a positive integer.")
        return

    # ── Upper half (rows 1 → n) ──────────────────────────────────────────
    for row in range(1, n + 1):                  # row: 1, 2, ..., n

        # Leading spaces: decreasing as row increases
        for space in range(n - row):             # spaces = n - row
            print(" ", end="")

        # Stars: 1, 3, 5, ... (2*row - 1) per row
        for star in range(2 * row - 1):          # stars = 2*row - 1
            print("*", end="")

        print()   # newline at end of each row

    # ── Lower half (rows n-1 → 1) — mirror of upper half ────────────────
    for row in range(n - 1, 0, -1):             # row: n-1, n-2, ..., 1

        for space in range(n - row):
            print(" ", end="")

        for star in range(2 * row - 1):
            print("*", end="")

        print()


def main():
    print("=" * 40)
    print("   💎 Diamond Pattern Generator")
    print("=" * 40)

    # Input validation loop
    while True:
        try:
            n = int(input("\nEnter number of rows for upper half: "))
            if n <= 0:
                print("  ⚠  Must be a positive integer. Try again.")
                continue
            break
        except ValueError:
            print("  ⚠  Invalid input. Enter a whole number.")

    print()
    print_diamond(n)
    print()

    # ── Edge case demos ──────────────────────────────────────────────────
    print("── Edge case: n = 1 ──")
    print_diamond(1)

    print("── Edge case: n = 0 ──")
    print_diamond(0)


if __name__ == "__main__":
    main()
