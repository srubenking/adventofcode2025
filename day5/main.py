"""
3-5
10-14
16-20
12-18
10-22

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

    merged_ranges = (merge_ranges(ranges))
    total_items = 0

    for range in merged_ranges:
        total_items += range[1] - range[0]
    
    print(total_items)

    #answer is to low

    
def merge_ranges(ranges):
    ranges = sorted(ranges, key=order)
    reached_end = False
    index = 0

    # check index 0 against every other
    # track if any changes are made 
    # do it again if yes > repeat until no
    # check index 1 against every other
    # and so on

    while not reached_end:
        new_ranges = []
        range1 = ranges[index]
        
        
        for range2 in ranges:
            #print(f"comparing {range1} and {range2}")
            if range1[0] <= range2[0] and range1[1] >= range2[0]:
                if range1[1] >= range2[1]:
                    #print(f"{range2} is redundant as it is either equal to or contained within {range1}")
                    new_ranges.append(range1)
                elif range1[1] < range2[1]:
                    #print(f"new range should be {range1[0]}, {range2[1]}")
                    new_ranges.append((range1[0], range2[1]))                 
            #check if range 1 is contained within range2, or if there's overlap
            elif range1[0] > range2[0] and range1[0] <= range2[1]:
                if range1[1] < range2[1]:
                    #print(f"{range1} is redundant as it is contained within {range2}")
                    new_ranges.append(range2)
                elif range1[1] >= range2[1]:
                    #print(f"new range should be {range2[0]}, {range1[1]}")
                    new_ranges.append((range2[0], range1[1]))                  
            else:
                #print(f"no overlap, appending {range1} and {range2}")
                new_ranges.append(range1)
                new_ranges.append(range2)
       
        if sorted(list(set(new_ranges)), key=order) == ranges:
            #print("no changes")
            if index >= len(ranges) - 1:
                reached_end = True
                ranges = sorted(list(set(new_ranges)), key=order)
            else:
                index += 1
                ranges = sorted(list(set(new_ranges)), key=order)
                #print(f"no change, next is {index} in range length {len(ranges)}")       
        else:
            ranges = sorted(list(set(new_ranges)), key=order)
            index = 0
            #print(f"next is {index} in range length {len(ranges)}")

    return sorted(list(set(ranges)), key=order)

def order(item):
    return item[0]

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