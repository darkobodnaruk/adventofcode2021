#!/usr/local/bin/python3

input = open("day6_input.txt").read().split(",")
fish = [int(f) for f in input]
print(fish)

def simulate(fish, days):
    for d in range(days):
        print(f"day {d}")
        new_fish = []
        for idx, f in enumerate(fish):
            if f == 0:
                new_fish.append(8)
                fish[idx] = 6
            else:
                fish[idx] = f - 1
        fish += new_fish
        print(fish)
    print(len(fish))

# simulate(fish, 18)
# simulate(fish, 80)
simulate(fish, 256)