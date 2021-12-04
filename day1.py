#!/usr/local/bin/python3
# import urllib.request
import re

## Part 1

# lost

## Part 2
window = [None, None, None]
prev_sum = None
cur_sum = None
count = 0

lines = open("day1_input.txt").readlines()
for line in lines:
  if not re.search("^\d+$", line):
    continue
  value = int(line.strip())

  window.pop(0)
  window.append(value)

  if all([w is not None for w in window]):
    cur_sum = window[0] + window[1] + window[2]

  if prev_sum and cur_sum and cur_sum > prev_sum:
    count += 1

  prev_sum = cur_sum

print(count)

