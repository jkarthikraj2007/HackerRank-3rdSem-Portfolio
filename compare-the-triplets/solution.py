#!/bin/python3
"""
HackerRank: Compare the Triplets
Topic: Basic Implementation

Problem:
Given two triplets (each of fixed length 3) representing two
students' scores across three categories, award a point to whichever
student scores higher in each category (ties give no point). Return
the final [aliceScore, bobScore].

Approach:
Single pass over the 3 fixed positions, comparing a[i] to b[i] and
incrementing the corresponding score.

Complexity:
Time:  O(1) -> triplet length is fixed at 3
Space: O(1) -> only two score counters used
"""


def compareTriplets(a, b):
    alice_score = 0
    bob_score = 0

    for ai, bi in zip(a, b):
        if ai > bi:
            alice_score += 1
        elif bi > ai:
            bob_score += 1

    return [alice_score, bob_score]


if __name__ == "__main__":
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)
    print(" ".join(map(str, result)))
