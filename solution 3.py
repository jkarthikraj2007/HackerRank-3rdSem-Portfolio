#!/bin/python3
"""
HackerRank: Time Conversion
Topic: Strings & Logic

Problem:
Convert a 12-hour AM/PM time string ("hh:mm:ssAM"/"hh:mm:ssPM") into
24-hour (military) time format "HH:mm:ss".

Approach:
Split off the last 2 characters (AM/PM marker) and parse hours,
minutes, seconds from the rest. Apply the standard 12-hour rule:
  - 12:xx:xx AM -> 00:xx:xx
  - hh:xx:xx AM (hh != 12) -> unchanged
  - 12:xx:xx PM -> unchanged (stays 12)
  - hh:xx:xx PM (hh != 12) -> hh + 12

Complexity:
Time:  O(1) -> fixed-length string, constant work
Space: O(1) -> no extra structures beyond the output string
"""


def timeConversion(s):
    period = s[-2:]
    hh = int(s[0:2])
    rest = s[2:8]  # ":mm:ss"

    if period == "AM":
        if hh == 12:
            hh = 0
    else:  # PM
        if hh != 12:
            hh += 12

    return f"{hh:02d}{rest}"


if __name__ == "__main__":
    s = input().strip()
    result = timeConversion(s)
    print(result)
