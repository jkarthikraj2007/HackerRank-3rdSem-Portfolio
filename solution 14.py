#!/bin/python3
"""
HackerRank: Drawing Book
Topic: Basic Implementation / Math

Problem:
A book has n pages, numbered 1 to n. You can start flipping from the
front (page 1) or the back (page n), turning one page per flip.
Given a target page p, find the minimum number of flips needed to
reach it from either end.

Approach:
From the front, reaching page p takes p // 2 flips (pages are
flipped two at a time). From the back, the "mirrored" page is
n // 2, so reaching p from the back takes (n // 2) - (p // 2) flips.
The answer is the smaller of the two.

Complexity:
Time:  O(1) -> constant-time arithmetic
Space: O(1) -> no extra structures
"""


def pageCount(n, p):
    from_front = p // 2
    from_back = n // 2 - p // 2
    return min(from_front, from_back)


if __name__ == "__main__":
    n = int(input().strip())
    p = int(input().strip())

    result = pageCount(n, p)
    print(result)