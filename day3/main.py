"""
Each line in the puzzle input represents a battery bank. Each digit represents a battery.
Joltage is equal to the number formed by the digits on the batteries you switch on, and the order of the batteries in the bank cannot be changed.

Part 1:
The goal is to find the largest joltage possible using 2 batteries for each bank, and add up the total output for all banks.

Test set:
In 987654321111111, you can make the largest joltage possible, 98, by turning on batteries 1 and 2.
In 811111111111119, you can make the largest joltage possible, 89, by turning on batteries 1 and 15.
In 234234234234278, you can make the largest joltage possible, 78, by turning on batteries 14 and 15.
In 818181911112111, you can make the largest joltage possible, 92, by turning on batteries 7 and 12.

Total output joltage is 357

Part 2:
Now the goal is the same but with 12 batteries instead of 2.

Test set:
In 987654321111111, you can make the largest joltage possible, 987654321111, by turning on all but batteries 13, 14, 15.
In 811111111111119, you can make the largest joltage possible, 811111111119, by turning on all but batteries 12, 13, 14.
In 234234234234278, you can make the largest joltage possible, 434234234278, by turning on all but batteries 1, 2, 4.
In 818181911112111, you can make the largest joltage possible, 888911112111, by turning on all but batteries 2, 4, 6.

Total output joltage is 3121910778619
"""
from collections import OrderedDict

def main():
    banks = read_file("input.txt")
    total_joltage = 0

    for bank in banks:
        twelve = get_batteries(bank, 12)
        total_joltage += get_joltage(twelve)

    print(total_joltage)

def get_joltage(bank):
    return int(bank)

def freq_analysis(bank):
    freq = {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0,
    }
    for battery in bank:
        freq[battery] += 1

    return freq

def remove_smallest(bank, total_batteries):
    freq_ind = 0
    check = freq_analysis(bank)
    new_bank = bank
    to_remove = len(bank) - total_batteries
    removed = 0

    for key, value in check.items():
        if removed < to_remove:
            if value == 0:
                continue
            for batt in bank:
                if batt == key and removed < to_remove:
                    new_bank = new_bank.replace(key, "", 1)
                    removed += 1
    
    return new_bank

def remove_smallest_debug(bank, total_batteries):
    freq_ind = 0
    check = freq_analysis(bank)
    new_bank = bank
    to_remove = len(bank) - total_batteries
    removed = 0

    print(f"to remove {to_remove} batteries")

    for key, value in check.items():
        print(f"{value} {key}s found in bank")
        input()
        if removed < to_remove:
            if value == 0:
                print("checking next number")
                input()
                continue
            for batt in bank:
                if batt == key and removed < to_remove:
                    new_bank = new_bank.replace(key, "", 1)
                    removed += 1
                    print(f"{batt} found, {removed} total removed")
                    input()
    
    return new_bank

def get_batteries(bank, total_batteries):
    batteries = []
    to_remove = len(bank) - total_batteries

    start = 0
    end = to_remove + 1

    # actually we just want to iterate over the whole bank checking len(bank) - 12 numbers at a time and incrementing the start by 1?
    while len(batteries) < total_batteries:
        #print(f"there are {to_remove} batteries to remove - checking from index {start}-{end}: {bank[start:end]}")
        #input()
        battery, battery_position = find_largest_p2(bank, start, end)
        #print(f"found largest battery: battery at index {battery_position} with {battery} joltage")
        batteries.append(battery)
        #print(f"{"".join(batteries)}")
        #input()
        if battery_position != 0:
            to_remove -= battery_position - start

        start = battery_position + 1
        end = start + to_remove + 1
        # need to keep checking pairs until the end in case the last one is the largest
    #print(f"final twelve found: {"".join(batteries)}")
    """
    while removed < to_remove:
        print(f"there are {to_remove - removed} batteries to remove - checking from index {start}-{end}")
        battery, battery_position = find_largest_p2(bank, start, end)
        print(f"found largest battery: battery at index {battery_position} with {battery} joltage")
        batteries.append(battery)

        start = battery_position + 1
        removed += len(bank[:start]) -1
        print(f"{removed} batteries removed so far")

        if len(batteries) == 12:
            break

        start = battery_position + 1
        end = start + to_remove - removed
        # need to keep checking pairs until the end in case the last one is the largest
    """

    return "".join(batteries)

def find_largest_p2(bank, start, end):
    largest = 0
    largest_index = int()

    for i in range(start, end):
        if int(bank[i]) > largest:
            largest = int(bank[i])
            largest_index = i
    
    return str(largest), largest_index

def read_file(file):
    f = open(file)
    return f.read().splitlines()

main()