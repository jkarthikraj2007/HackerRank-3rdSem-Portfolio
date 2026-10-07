#!/bin/python3
"""
HackerRank: Mini-Max Sum
Topic: Basic Implementation

Problem:
Given 5 positive integers, find the minimum and maximum values that
can be calculated by summing exactly four of the five integers.
Print both values as a single line of space-separated long integers.

Approach:
Sort is unnecessary — the min possible sum is (total - max element)
and the max possible sum is (total - min element). Compute the total
once, then subtract the extremes.

Complexity:
Time:  O(1) -> fixed-size input of 5 elements
Space: O(1) -> no extra structures
"""


def miniMaxSum(arr):
    total = sum(arr)
    lo = total - max(arr)
    hi = total - min(arr)
    print(lo, hi)


if __name__ == "__main__":
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)