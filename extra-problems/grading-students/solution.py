#!/bin/python3
"""
HackerRank: Grading Students
Topic: Basic Implementation

Problem:
HackerLand University rounds student grades using these rules:
  - Grades less than 38 are never rounded (failing, no benefit).
  - Any grade >= 38: if the difference between it and the next
    multiple of 5 is less than 3, round up to that multiple of 5.
    Otherwise leave it unchanged.

Approach:
For each grade >= 38, compute the next multiple of 5 using
((grade // 5) + 1) * 5 and round up only if the gap is under 3.

Complexity:
Time:  O(N) -> one pass over the grades list
Space: O(N) -> output list of the same size as the input
"""


def gradingStudents(grades):
    result = []

    for grade in grades:
        if grade >= 38:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                grade = next_multiple
        result.append(grade)

    return result


if __name__ == "__main__":
    n = int(input().strip())
    grades = [int(input().strip()) for _ in range(n)]

    result = gradingStudents(grades)
    print("\n".join(map(str, result)))