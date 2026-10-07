#!/bin/python3
"""
HackerRank: Between Two Sets
Topic: Math / Number Theory (GCD & LCM)

Problem:
Given two arrays a and b, find how many integers x exist such that:
  1. Every element of a divides x (x is a multiple of each a[i])
  2. x divides every element of b (x is a factor of each b[i])
The valid x values always form a contiguous range from lcm(a) to
gcd(b) in steps of lcm(a), so count how many multiples of lcm(a)
also evenly divide every element of b.

Approach:
Compute L = LCM of all elements in a. Compute G = GCD of all
elements in b. Any candidate x must be a multiple of L and a
divisor of G, so iterate multiples of L up to G and check divisibility
against G (equivalent to checking all of b, since G is their GCD).

Complexity:
Time:  O(N + M + G/L) -> computing LCM/GCD is linear in array sizes;
                         the candidate loop runs at most G/L times
Space: O(1)            -> only running LCM/GCD accumulators
"""

from math import gcd


def lcm(x, y):
    return x * y // gcd(x, y)


def getTotalX(a, b):
    L = 1
    for num in a:
        L = lcm(L, num)

    G = 0
    for num in b:
        G = gcd(G, num)

    count = 0
    multiple = L
    while multiple <= G:
        if G % multiple == 0:
            count += 1
        multiple += L

    return count


if __name__ == "__main__":
    n, m = map(int, input().split())
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))

    result = getTotalX(a, b)
    print(result)