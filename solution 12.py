#!/bin/python3
"""
HackerRank: Breaking the Records
Topic: Basic Implementation

Problem:
Given a list of scores from a player's games in order, count how
many times they broke their own best (highest) score and how many
times they broke their own worst (lowest) score, starting from the
first game as the initial best/worst.

Approach:
Single pass, tracking running best and worst (initialized to the
first score). Strictly greater than best -> increment best-count and
update best; strictly less than worst -> increment worst-count and
update worst.

Complexity:
Time:  O(N) -> one pass over the scores
Space: O(1) -> only running best/worst and two counters
"""


def breakingRecords(scores):
    best = worst = scores[0]
    best_count = worst_count = 0

    for score in scores[1:]:
        if score > best:
            best = score
            best_count += 1
        elif score < worst:
            worst = score
            worst_count += 1

    return [best_count, worst_count]


if __name__ == "__main__":
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(" ".join(map(str, result)))