#!/bin/python3
"""
HackerRank: Dynamic Array
Topic: Data Structures / Vectors (2D nested sequences, bitwise XOR)

Problem:
Create n empty sequences (a "dynamic array" of lists). Process q
queries of two types, tracking a running lastAnswer value:
  Type 1: append y to seq[(x XOR lastAnswer) % n]
  Type 2: print seq[(x XOR lastAnswer) % n][y % len(that seq)]
          and set lastAnswer to that printed value.

Approach:
Maintain the array of lists directly. For each query, compute the
target index using XOR with lastAnswer as specified, then either
append (type 1) or index-and-update-lastAnswer (type 2).

Complexity:
Time:  O(N + Q) -> O(N) to build empty seqs, O(1) work per query
Space: O(N)     -> plus the total number of appended elements
"""


def dynamicArray(n, queries):
    seq = [[] for _ in range(n)]
    last_answer = 0
    answers = []

    for query_type, x, y in queries:
        idx = (x ^ last_answer) % n

        if query_type == 1:
            seq[idx].append(y)
        elif query_type == 2:
            last_answer = seq[idx][y % len(seq[idx])]
            answers.append(last_answer)

    return answers


if __name__ == "__main__":
    first_line = input().split()
    n, q = int(first_line[0]), int(first_line[1])

    queries = []
    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)
    print("\n".join(map(str, result)))
