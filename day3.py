#!/usr/local/bin/python3

import re

## Part 1
line_count = 0
zero_bit_counts = []
lines = open("day3_input.txt").readlines()
for line in lines:
    for idx, bit in enumerate(line):
        if bit == "0":
            if len(zero_bit_counts) < idx + 1:
                zero_bit_counts.append(1)
            else:
                zero_bit_counts[idx] += 1
    line_count += 1

print(zero_bit_counts)

gamma_rate = ""
epsilon_rate = ""
for count in zero_bit_counts:
    if count > line_count/2:
        gamma_rate += "0"
        epsilon_rate += "1"
    else:
        gamma_rate += "1"
        epsilon_rate += "0"

print(gamma_rate)
print(int(gamma_rate , 2))
print(epsilon_rate)
print(int(epsilon_rate, 2))

print(int(gamma_rate , 2) * int(epsilon_rate, 2))

print("---")

## Part 2

def load_input():
    lines = list(map(lambda l: l.strip(), open("day3_input.txt").readlines()))
    # lines = list(map(lambda l: l.strip(), open("day3_input_test.txt").readlines()))
    return lines

def calc_zero_bit_counts(lines):
    zero_bit_counts = []
    for line in lines:
        for idx, bit in enumerate(line):
            if len(zero_bit_counts) < idx + 1:
                zero_bit_counts.append(0)
            if bit == "0":
                zero_bit_counts[idx] += 1
    return zero_bit_counts

def calc_rating(mode):
    lines = load_input()
    bitlength = len(lines[0])
    rating = None

    for idx in range(bitlength):
        zero_bit_counts = calc_zero_bit_counts(lines)
        zcount = zero_bit_counts[idx]

        if rating == None:
            if mode == "oxygen_generator":
                if zcount <= len(lines)/2:
                    lines = list(filter(lambda l: l[idx] == "1", lines))
                else:
                    lines = list(filter(lambda l: l[idx] == "0", lines))
            elif mode == "co2_scrubber":
                if zcount <= len(lines)/2:
                    lines = list(filter(lambda l: l[idx] == "0", lines))
                else:
                    lines = list(filter(lambda l: l[idx] == "1", lines))

        if len(lines) == 1:
            rating = lines[0]

    return rating

oxy_rating = int(calc_rating("oxygen_generator"), 2)
co2_rating = int(calc_rating("co2_scrubber"), 2)

print(oxy_rating)
print(co2_rating)

result = oxy_rating * co2_rating
print(result)

