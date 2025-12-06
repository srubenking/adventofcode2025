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
    banks = read_file("test.txt")
    total_joltage = 0
    
    print("input:    987654321111111")
    print("expected: 987654321111")
    print(f"actual:   {remove_smallest('987654321111111')}")

    print("input:    811111111111119")
    print("expected: 811111111119")
    print(f"actual:   {remove_smallest('811111111111119')}")

    print("input:    234234234234278")
    print("expected: 434234234278")
    print(f"actual:   {remove_smallest('234234234234278')}")

    print("input:    818181911112111")
    print("expected: 888911112111")
    print(f"actual:   {remove_smallest('818181911112111')}")
"""
    for bank in banks:
        # part 1:
        # battery1_index, battery2_index, joltage = get_pair(bank)
        # print(f"In {bank}, you can make the largest joltage possible, {joltage}, by turning on batteries {battery1_index + 1} and {battery2_index + 1}.")

        # iterate over whole battery bank, check if each number is larger than the smallest current candidate and boot that one if so
        # dict.pop("key", None) to remove a key regardless of if it exists? probably not relevant
        print(bank)
        print(get_twelve(bank))
        # total_joltage += joltage
        
    
    print(f"Total output joltage is {total_joltage}")
"""

def get_joltage(list):
    return

def freq_analysis(bank):
    # going back to this, I have an idea
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

    # now put them in ascending order by key

    return freq

def join_list(list):
    string = ""

    for item in list:
        string += str(item)

    return string

def remove_smallest(bank):
    freq_ind = 0
    check = freq_analysis(bank)
    new_bank = bank
    to_remove = len(bank) - 12
    print(f"going to remove {to_remove}")
    removed = 0

    for key, value in check.items():
        if removed < to_remove:
            # print(f"checking for {key}s")
            if value == 0:
                # print(f"no {key}s, moving on")
                continue
            for batt in bank:
                if batt == key and removed < to_remove:
                    # print(f"found {key} and removed")
                    new_bank = new_bank.replace(key, "", 1)
                    removed += 1
                    # print(f"now removed {removed}")
    
    return new_bank

def get_twelve(bank):
    batteries = []
    to_remove = len(bank) - 12
    removed = 0

    start = 0
    end = to_remove + 1

    # actually we just want to iterate over the whole bank checking len(bank) - 12 numbers at a time and incrementing the start by 1?

    while removed < to_remove:
        print(f"there are {to_remove - removed} batteries to remove - checking from battery at index {start} to battery at index {end}")
        battery, battery_position = find_largest_p2(bank, start, end)
        print(f"found largest battery: battery at index {battery_position} with {battery} joltage")
        batteries.append(battery)

        removed += len(bank[start:])
        print(f"{removed} batteries removed so far")

        if len(batteries) == 12:
            break

        start = battery_position + 1
        end = start + to_remove - removed
        # need to keep checking pairs until the end in case the last one is the largest


    twelve = "" # empty string to add batteries onto
    return batteries

def get_pair(bank):
    battery1, battery1_index = find_largest_p1(bank, 0, len(bank) - 1)
    battery2, battery2_index = find_largest_p1(bank, battery1_index + 1, len(bank))

    joltage = battery1 * 10 + battery2
    
    return battery1_index, battery2_index, joltage

def find_largest_p2(bank, start, end):
    bank_numbers = list(map(int, bank))
    largest = max(bank_numbers[start:end])
    largest_index = bank_numbers.index(largest)
    return largest, largest_index

def find_largest_p1(bank, start, end):
    largest = 0
    largest_index = int()

    for i in range(start, end):
        if int(bank[i]) > largest:
            largest = int(bank[i])
            largest_index = i
    
    return largest, largest_index

def read_file(file):
    f = open(file)
    return f.read().splitlines()

main()