# HackerRank-3rdSem-Portfolio

Portfolio repository for **Activity 8: HackerRank Algorithmic Problem-Solving & Portfolio Integration**  
*(Portfolio Building, B25CS0311 — 3rd Semester B.Tech Computer Science & Engineering)*.

- **Student Name:** J KARTHIK RAJ
- **HackerRank Profile:** [jkarthikraj2007](https://www.hackerrank.com/profile/jkarthikraj2007)
- **Badge Earned:** 3-Star Problem Solving Badge ⭐️⭐️⭐️

---

## Submission Screenshots

> Screenshots of "Accepted" submissions and earned HackerRank badge:

- `screenshots/diagonal-difference-accepted.png`
- `screenshots/dynamic-array-accepted.png`
- `screenshots/time-conversion-accepted.png`
- `screenshots/compare-the-triplets-accepted.png`
- `screenshots/sparse-arrays-accepted.png`
- `screenshots/badge.png`

---

## Problems & Complexity Summary

### Core 5 (Required)

| # | Problem | Topic / Category | Time Complexity | Space Complexity |
|---|---------|-------------------|------------------|-------------------|
| 1 | [Diagonal Difference](./diagonal-difference/solution.py) | 2D Arrays / Matrices | $O(N)$ | $O(1)$ |
| 2 | [Dynamic Array](./dynamic-array/solution.py) | Data Structures / Vectors | $O(N + Q)$ | $O(N)$ |
| 3 | [Time Conversion](./time-conversion/solution.py) | Strings & Logic | $O(1)$ | $O(1)$ |
| 4 | [Compare the Triplets](./compare-the-triplets/solution.py) | Basic Implementation | $O(1)$ | $O(1)$ |
| 5 | [Sparse Arrays](./sparse-arrays/solution.py) | Hash Maps / Strings | $O(N + Q)$ | $O(N)$ |

### Extra 10 (Bonus / Portfolio Depth)

| # | Problem | Topic / Category | Time Complexity | Space Complexity |
|---|---------|-------------------|------------------|-------------------|
| 6 | [Mini-Max Sum](./extra-problems/mini-max-sum/solution.py) | Basic Implementation | $O(1)$ | $O(1)$ |
| 7 | [Birthday Cake Candles](./extra-problems/birthday-cake-candles/solution.py) | Basic Implementation / Arrays | $O(N)$ | $O(1)$ |
| 8 | [Grading Students](./extra-problems/grading-students/solution.py) | Basic Implementation | $O(N)$ | $O(N)$ |
| 9 | [Apple and Orange](./extra-problems/apple-and-orange/solution.py) | Basic Implementation / Number Line | $O(M + N)$ | $O(1)$ |
| 10 | [Kangaroo (Number Line Jumps)](./extra-problems/kangaroo/solution.py) | Math | $O(1)$ | $O(1)$ |
| 11 | [Between Two Sets](./extra-problems/between-two-sets/solution.py) | Math / GCD & LCM | $O(N + M + (G/L))$ | $O(1)$ |
| 12 | [Breaking the Records](./extra-problems/breaking-the-records/solution.py) | Basic Implementation | $O(N)$ | $O(1)$ |
| 13 | [Birthday Chocolate](./extra-problems/birthday-chocolate/solution.py) | Sliding Window / Arrays | $O(N)$ | $O(1)$ |
| 14 | [Drawing Book](./extra-problems/drawing-book/solution.py) | Basic Implementation / Math | $O(1)$ | $O(1)$ |
| 15 | [Electronics Shop](./extra-problems/electronics-shop/solution.py) | Basic Implementation / Arrays | $O(N \times M)$ | $O(1)$ |

---

## Repository Structure

```
HackerRank-3rdSem-Portfolio/
├── diagonal-difference/
│   └── solution.py
├── dynamic-array/
│   └── solution.py
├── time-conversion/
│   └── solution.py
├── compare-the-triplets/
│   └── solution.py
├── sparse-arrays/
│   └── solution.py
├── extra-problems/
│   ├── mini-max-sum/
│   │   └── solution.py
│   ├── birthday-cake-candles/
│   │   └── solution.py
│   ├── grading-students/
│   │   └── solution.py
│   ├── apple-and-orange/
│   │   └── solution.py
│   ├── kangaroo/
│   │   └── solution.py
│   ├── between-two-sets/
│   │   └── solution.py
│   ├── breaking-the-records/
│   │   └── solution.py
│   ├── birthday-chocolate/
│   │   └── solution.py
│   ├── drawing-book/
│   │   └── solution.py
│   └── electronics-shop/
│       └── solution.py
├── screenshots/
│   └── .gitkeep
└── README.md
```

---

## Reflection on Algorithmic Optimization

Completing this HackerRank algorithmic portfolio provided deep practical insights into translating theoretical computational complexity into performant code. Moving beyond brute-force implementations required examining problem constraints, choosing optimal data structures, and balancing trade-offs between asymptotic time and auxiliary memory.

For instance, solving **Diagonal Difference** highlighted the power of single-pass index arithmetic to reduce runtime from $O(N^2)$ to $O(N)$ with $O(1)$ space. In **Sparse Arrays**, utilizing hash map frequency counting transformed an otherwise costly $O(N \times Q)$ nested search into an optimal $O(N + Q)$ lookup. Working with dynamic sequences in **Dynamic Array** reinforced efficient query processing and bitwise manipulation.

Across the additional challenges, such as **Number Line Jumps (Kangaroo)** and **Between Two Sets**, applying mathematical properties (relative velocity and GCD/LCM factoring) eliminated iterative simulation in favor of constant and sub-linear evaluation. Furthermore, sliding window logic in **Subarray Division** and min-max tracking in **Birthday Cake Candles** demonstrated clean linear-time sweeps.

Overall, this activity sharpened my ability to design scalable algorithms, account for corner cases, and maintain clean engineering standards. Earning the 3-Star Problem Solving badge on HackerRank validates this milestone and serves as a strong foundation for advanced data structures and technical interviews.