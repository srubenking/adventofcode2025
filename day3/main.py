"""
Each line in the puzzle input represents a battery bank. Each digit represents a battery.
Joltage is equal to the number formed by the digits on the batteries you switch on, and the order of the batteries in the bank cannot be changed.

The goal is to find the largest joltage possible for each bank, and add up the total output for all banks when using this highest possible joltage for each.

Test set:
In 987654321111111, you can make the largest joltage possible, 98, by turning on batteries 1 and 2.
In 811111111111119, you can make the largest joltage possible, 89, by turning on batteries 1 and 15.
In 234234234234278, you can make the largest joltage possible, 78, by turning on batteries 14 and 15.
In 818181911112111, you can make the largest joltage possible, 92, by turning on batteries 7 and 12.

Total output joltage is 357
"""

def main():
    banks = read_file("input.txt")
    total_joltage = 0

    for bank in banks:
        battery1, battery1_index = find_largest(bank, 0, len(bank) - 1)
        battery2, battery2_index = find_largest(bank, battery1_index + 1, len(bank))

        joltage = int(str(battery1) + str(battery2))
        # yes I am leaving the above as is, it's 3am and apparently my brain couldn't conceive of "multiply the first digit by 10 to put it in the correct place"

        # print(f"In {bank}, you can make the largest joltage possible, {joltage}, by turning on batteries {battery1_index + 1} and {battery2_index + 1}.")
        total_joltage += joltage
    
    print(f"Total output joltage is {total_joltage}")
    return

def find_largest(bank, start, end):
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