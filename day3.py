#!/usr/local/bin/python3

import re

## Part 1
# line_count = 0
# zero_bit_counts = []
# lines = open("day3_input.txt").readlines()
# for line in lines:
#     for idx, bit in enumerate(line):
#         if bit == "0":
#             if len(zero_bit_counts) < idx + 1:
#                 zero_bit_counts.append(1)
#             else:
#                 zero_bit_counts[idx] += 1
#     line_count += 1

# print(zero_bit_counts)

# gamma_rate = ""
# epsilon_rate = ""
# for count in zero_bit_counts:
#     if count > line_count/2:
#         gamma_rate += "0"
#         epsilon_rate += "1"
#     else:
#         gamma_rate += "1"
#         epsilon_rate += "0"

# print(gamma_rate)
# print(int(gamma_rate , 2))
# print(epsilon_rate)
# print(int(epsilon_rate, 2))

# print(int(gamma_rate , 2) * int(epsilon_rate, 2))

# print("---")

## Part 2
line_count = 0
zero_bit_counts = []
# lines = open("day3_input.txt").readlines()
lines = """00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010""".split("\n")
for line in lines:
    for idx, bit in enumerate(line):
        if bit == "0":
            if len(zero_bit_counts) < idx + 1:
                zero_bit_counts.append(1)
            else:
                zero_bit_counts[idx] += 1
    line_count += 1

oxygen_generator_lines = lines
oxygen_generator_rating = None
co2_scrubber_lines = lines
co2_scrubber_rating = None

print(zero_bit_counts)

for idx, zcount in enumerate(zero_bit_counts):
    print(idx)
    if oxygen_generator_rating == None:
        if zcount <= line_count/2:
            # zero bit is less common, one bit is more common, keep numbers with one bit
            print("zero bit is less common")
            oxygen_generator_lines = list(filter(lambda l: l[idx] == "1", oxygen_generator_lines))

        else:
            print("zero bit is more common")
            oxygen_generator_lines = list(filter(lambda l: l[idx] == "0", oxygen_generator_lines))

    if co2_scrubber_rating == None:
        if zcount < line_count/2:
            # zero bit is least common, keep numbers with zero bit
            co2_scrubber_lines = list(filter(lambda l: l[idx] == "0", co2_scrubber_lines))
        else:
            co2_scrubber_lines = list(filter(lambda l: l[idx] == "1", co2_scrubber_lines))

    if len(oxygen_generator_lines) == 1:
        oxygen_generator_rating = oxygen_generator_lines[0]
    if len(co2_scrubber_lines) == 1:
        co2_scrubber_rating = co2_scrubber_lines[0]

    if idx >= 6:
        print(oxygen_generator_lines)
        print(co2_scrubber_lines)
        print()

print(oxygen_generator_rating, co2_scrubber_rating)
