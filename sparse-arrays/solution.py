#!/bin/python3
"""
HackerRank: Sparse Arrays
Topic: Hash Maps / Strings

Problem:
Given a list of strings and a list of query strings, for each query
report how many times it appears in the original list.

Approach:
A naive solution recomputes the count for every query by scanning
the whole list of strings each time (O(N*Q)). Instead, build a
frequency hash map once from the strings list (O(N)), then answer
each query with an O(1) dictionary lookup (O(Q) total).

Complexity:
Time:  O(N + Q) -> O(N) to build the frequency map, O(Q) to answer
Space: O(N)     -> the frequency map holds up to N distinct keys
"""

from collections import Counter


def matchingStrings(strings, queries):
    frequency = Counter(strings)
    return [frequency[q] for q in queries]


if __name__ == "__main__":
    n = int(input().strip())
    strings = [input().rstrip() for _ in range(n)]

    q = int(input().strip())
    queries = [input().rstrip() for _ in range(q)]

    result = matchingStrings(strings, queries)
    print("\n".join(map(str, result)))
