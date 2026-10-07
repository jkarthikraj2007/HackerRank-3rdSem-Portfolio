#!/bin/python3
"""
HackerRank: Birthday Cake Candles
Topic: Basic Implementation / Arrays

Problem:
Given the heights of candles on a cake, the tallest candle(s) can be
blown out in one breath. Count how many candles share the tallest
height.

Approach:
Single pass: track the current max height and a running count of how
many candles match it, resetting the count whenever a taller candle
is found.

Complexity:
Time:  O(N) -> one pass over the candles
Space: O(1) -> only a running max and count are kept
"""


def birthdayCakeCandles(candles):
    tallest = 0
    count = 0
    for h in candles:
        if h > tallest:
            tallest = h
            count = 1
        elif h == tallest:
            count += 1

    return count


if __name__ == "__main__":
    n = int(input().strip())
    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)
    print(result)