#!/bin/python3
"""
HackerRank: Number Line Jumps (Kangaroo)
Topic: Basic Implementation / Math

Problem:
Two kangaroos start at positions x1 and x2 and jump v1 and v2 units
per jump respectively (both move in the same direction). Determine
whether they will ever land on the same position at the same time.

Approach:
Solve algebraically: positions are equal after n jumps when
  x1 + n*v1 = x2 + n*v2  =>  n = (x2 - x1) / (v1 - v2)
This has a valid solution only if v1 != v2, n is a non-negative
integer (n >= 0 and the division has no remainder).

Complexity:
Time:  O(1) -> constant-time arithmetic check
Space: O(1) -> no extra structures
"""


def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return "YES" if x1 == x2 else "NO"

    diff = x2 - x1
    speed_diff = v1 - v2

    if diff % speed_diff != 0:
        return "NO"

    n = diff // speed_diff
    return "YES" if n >= 0 else "NO"


if __name__ == "__main__":
    x1, v1, x2, v2 = map(int, input().split())
    result = kangaroo(x1, v1, x2, v2)
    print(result)