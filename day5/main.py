"""
3-5
10-14
16-20
12-18

1
5
8
11
17
32

The Elves are trying to determine which of the available ingredient IDs are fresh. In this example, this is done as follows:

Ingredient ID 1 is spoiled because it does not fall into any range.
Ingredient ID 5 is fresh because it falls into range 3-5.
Ingredient ID 8 is spoiled.
Ingredient ID 11 is fresh because it falls into range 10-14.
Ingredient ID 17 is fresh because it falls into range 16-20 as well as range 12-18.
Ingredient ID 32 is spoiled.

So, in this example, 3 of the available ingredient IDs are fresh.

Process the database file from the new inventory management system. How many of the available ingredient IDs are fresh?

"""
import time

def main():
    ranges, items = read_file("input.txt")
    

    return

def get_all_IDs(ranges, items):
    return

def get_fresh(ranges, items):
    fresh_items = 0

    for item in items:
        for r in ranges:
            if r[0] <= item <= r[1]:
                fresh_items += 1
                break

    return f"{fresh_items} fresh items"

def read_file(file):
    f = open(file)
    lines = f.read().splitlines()

    ranges = lines[:lines.index("")]
    int_ranges = []
    for r in ranges:
        pair = (int(r[:r.index("-")]), int(r[r.index("-") + 1:]))
        int_ranges.append(pair)

    items = lines[lines.index("") + 1:]
    int_items = list(map(int, items))

    return int_ranges, int_items

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))