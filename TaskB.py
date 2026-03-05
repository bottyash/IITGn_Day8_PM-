"""
Day-8 Assignment | Part B: Interview Ready
─────────────────────────────────────────────────────────────────────────────
Q1  break vs continue, and the loop-else clause
Q2  find_pairs — O(n²) then O(n)
Q3  Debug is_prime
─────────────────────────────────────────────────────────────────────────────
"""

# ═══════════════════════════════════════════════════════════════════════════
# Q1 — Conceptual
# ═══════════════════════════════════════════════════════════════════════════
"""
────────────────────────────────────────
break vs continue
────────────────────────────────────────

`break`  — immediately exits the entire loop. Execution jumps to the first
           statement AFTER the loop block.

`continue` — skips the rest of the current iteration and jumps straight to
             the next iteration of the loop.

Example:
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("── break example (stop at first even) ──")
for n in numbers:
    if n % 2 == 0:
        print(f"  Found even number: {n} → breaking out")
        break               # exits loop completely
    print(f"  Checked {n}")

print("\n── continue example (skip even numbers) ──")
for n in numbers:
    if n % 2 == 0:
        continue            # skips print below, goes to next iteration
    print(f"  Odd: {n}")


# ────────────────────────────────────────
# else clause in for / while loops
# ────────────────────────────────────────
"""
The `else` block of a loop runs ONLY if the loop completed normally
(i.e., was NOT terminated by a `break`).

If a `break` fires, the `else` block is SKIPPED entirely.

Practical use-case — search pattern:
  When you search for something in a list, the `else` clause lets you
  cleanly detect "not found" without an extra boolean flag variable.
"""

print("\n── loop-else: search pattern ──")

def search_for_target(items, target):
    for item in items:
        if item == target:
            print(f"  Found '{target}'!")
            break           # break → else is skipped
    else:
        # Only runs if break was never hit
        print(f"  '{target}' not found in list.")

search_for_target([10, 20, 30, 40], 20)   # found → else skipped
search_for_target([10, 20, 30, 40], 99)   # not found → else runs


# ═══════════════════════════════════════════════════════════════════════════
# Q2 — find_pairs
# ═══════════════════════════════════════════════════════════════════════════

# ── O(n²) solution using nested loops ──────────────────────────────────────
def find_pairs_quadratic(numbers: list[int], target: int) -> list[tuple]:
    """
    Return all unique pairs whose sum equals target.
    Time complexity : O(n²)  — two nested loops, each up to n iterations.
    Space complexity: O(1)   — no extra data structure proportional to n.
    """
    pairs = []
    n = len(numbers)

    for i in range(n):                       # outer loop — O(n)
        for j in range(i + 1, n):            # inner loop — O(n) → total O(n²)
            if numbers[i] + numbers[j] == target:
                pairs.append((numbers[i], numbers[j]))

    return pairs


# ── O(n) solution using a set ───────────────────────────────────────────────
def find_pairs_linear(numbers: list[int], target: int) -> list[tuple]:
    """
    Return all unique pairs whose sum equals target.
    Time complexity : O(n)  — single pass; set lookup is O(1) average.
    Space complexity: O(n)  — the `seen` set can hold up to n elements.

    Strategy:
      For each number x, the complement is (target - x).
      If complement is already in `seen`, we found a pair.
      Otherwise, add x to `seen` and continue.
    """
    seen = set()
    pairs = []

    for x in numbers:                        # single O(n) loop
        complement = target - x
        if complement in seen:               # set lookup is O(1)
            # Ensure smaller value first for consistent output
            pairs.append((min(x, complement), max(x, complement)))
        seen.add(x)

    return pairs


# ── Demo ────────────────────────────────────────────────────────────────────
print("\n── find_pairs demo ──")
nums = [1, 2, 3, 4, 5]
target = 6

result_n2 = find_pairs_quadratic(nums, target)
result_n1 = find_pairs_linear(nums, target)

print(f"  Input  : {nums}, target={target}")
print(f"  O(n²)  : {result_n2}")
print(f"  O(n)   : {result_n1}")

"""
Why O(n) is faster:
  O(n²) — For a list of 1000 elements, worst case ≈ 500,000 comparisons.
  O(n)  — Same list needs exactly 1000 iterations.
  The trade-off is extra memory for the `seen` set (space for time).
"""


# ═══════════════════════════════════════════════════════════════════════════
# Q3 — Debug is_prime
# ═══════════════════════════════════════════════════════════════════════════

"""
Original buggy code:
─────────────────────
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):       # Bug: checks ALL numbers up to n-1
        if n % i == 0:
            return False
    return True

──────────────────────────────────
Bug #1 — PERFORMANCE (not a logic error, but a serious inefficiency):
  `range(2, n)` iterates up to n-1.
  A number n can only have a factor ≤ √n.
  If no factor is found by √n, n is prime.
  Fix: use `range(2, int(n**0.5) + 1)`.
  Time complexity drops from O(n) → O(√n).

Bug #2 — EDGE CASE: n = 1
  `n < 2` correctly returns False for 1, so that is fine.
  n = 0 and negative numbers are also correctly handled.

Bug #3 — No handling for n = 2 or n = 3 (minor but worth noting)
  These are primes and the loop `range(2, 2)` is empty → returns True. ✓
  range(2, 2) = [] so no iteration happens — correct by accident.
──────────────────────────────────
"""


# ── Fixed, optimised version ────────────────────────────────────────────────
def is_prime(n: int) -> bool:
    """
    Check if n is prime.
    Time complexity: O(√n)  — only checks divisors up to the square root.
    """
    if n < 2:
        return False
    if n == 2:
        return True          # 2 is the only even prime
    if n % 2 == 0:
        return False         # eliminate all other even numbers early

    # Only check odd divisors from 3 up to √n
    for i in range(3, int(n ** 0.5) + 1, 2):   # step=2 skips even divisors
        if n % i == 0:
            return False

    return True


# ── Verify fix ──────────────────────────────────────────────────────────────
print("\n── is_prime verification ──")
test_cases = [0, 1, 2, 3, 4, 13, 97, 100]
for num in test_cases:
    print(f"  is_prime({num:>3}) = {is_prime(num)}")
