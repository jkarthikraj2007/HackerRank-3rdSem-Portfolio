#!/bin/python3
"""
HackerRank: Electronics Shop
Topic: Basic Implementation / Arrays

Problem:
Monica wants to buy exactly one keyboard and one USB drive from the
given price lists, spending as much as possible without exceeding
her budget b. Return the maximum amount she can spend, or -1 if no
valid combination fits the budget.

Approach:
Brute force every (keyboard, drive) price pair -- the constraints on
HackerRank are small enough that O(N*M) is efficient. Track the best
total that is <= b.

Complexity:
Time:  O(N*M) -> N keyboard prices x M drive prices
Space: O(1)   -> only a running best total
"""


def getMoneySpent(keyboards, drives, b):
    best = -1

    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > best:
                best = total

    return best


if __name__ == "__main__":
    b, n, m = map(int, input().split())
    keyboards = list(map(int, input().rstrip().split()))
    drives = list(map(int, input().rstrip().split()))

    result = getMoneySpent(keyboards, drives, b)
    print(result)