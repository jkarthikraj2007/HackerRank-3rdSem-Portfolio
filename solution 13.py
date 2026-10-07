#!/bin/python3
"""
HackerRank: Birthday Chocolate (Subarray Division)
Topic: Sliding Window / Arrays

Problem:
Given a bar of chocolate as an array `s` of squares (each with a
number of chocolate pieces) and a target birthday number `d`, count
how many contiguous subarrays of length `month` (Lily's birth month)
sum exactly to `d` (her birth day).

Approach:
Classic fixed-size sliding window of width `month`: slide across the
array summing each window and compare it to d.

Complexity:
Time:  O(N) -> N - month + 1 windows, each summed in O(month);
               with a running-sum sliding window this is O(N) total
Space: O(1) -> only a running window sum and counter
"""


def birthday(s, d, month):
    count = 0
    window_len = month

    for i in range(len(s) - window_len + 1):
        if sum(s[i:i + window_len]) == d:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input().strip())
    s = list(map(int, input().rstrip().split()))
    d, month = map(int, input().split())

    result = birthday(s, d, month)
    print(result)