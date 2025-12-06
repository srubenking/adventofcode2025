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
        print(bank)
        twelve = remove_smallest(bank, 12)
        print(twelve)
        input()
        total_joltage += get_joltage(twelve)

    # too low apparently
    
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

def read_file(file):
    f = open(file)
    return f.read().splitlines()

main()