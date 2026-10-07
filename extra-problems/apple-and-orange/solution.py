#!/bin/python3
"""
HackerRank: Apple and Orange
Topic: Basic Implementation / Number Line

Problem:
Given a house spanning [s, t] on a number line, an apple tree at
position a, and an orange tree at position b, determine how many
apples (distances from a) and how many oranges (distances from b)
land inside the house boundaries [s, t] inclusive.

Approach:
For each fruit's distance offset, compute its absolute landing
position (tree position + offset) and check if it falls within
[s, t]. Count apples and oranges separately.

Complexity:
Time:  O(M + N) -> one pass over apple drops, one over orange drops
Space: O(1)     -> only two running counters
"""


def countLanding(tree_position, distances, s, t):
    count = 0
    for d in distances:
        landing = tree_position + d
        if s <= landing <= t:
            count += 1
    return count


if __name__ == "__main__":
    s, t = map(int, input().split())
    a, b = map(int, input().split())
    m, n = map(int, input().split())
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    print(countLanding(a, apples, s, t))
    print(countLanding(b, oranges, s, t))