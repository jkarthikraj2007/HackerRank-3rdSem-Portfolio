#!/bin/python3
"""
HackerRank: Diagonal Difference
Topic: 2D Arrays / Matrices

Problem:
Given a square matrix, find the absolute difference between the sums
of its two diagonals (primary and secondary).

Approach:
Walk the matrix once. For row i, the primary-diagonal element is
arr[i][i] and the secondary-diagonal element is arr[i][n-1-i].
Accumulate both sums in the same pass, then take the absolute
difference at the end.

Complexity:
Time:  O(N)  -> single pass over the n rows
Space: O(1)  -> only two running totals are kept
"""

import os


def diagonalDifference(arr):
    n = len(arr)
    primary_sum = 0
    secondary_sum = 0

    for i in range(n):
        primary_sum += arr[i][i]
        secondary_sum += arr[i][n - 1 - i]

    return abs(primary_sum - secondary_sum)


if __name__ == "__main__":
    n = int(input().strip())

    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)
    print(result)
