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
import time

def main():
    banks = read_file("input.txt")
    total_joltage = 0

    for bank in banks:
        twelve = get_batteries(bank, 12)
        total_joltage += get_joltage(twelve)

    print(total_joltage)

def get_joltage(bank):
    return int(bank)

def get_batteries(bank, total_batteries):
    batteries = []
    to_remove = len(bank) - total_batteries

    start = 0
    end = to_remove + 1

    while len(batteries) < total_batteries:
        battery, battery_position = find_largest(bank, start, end)
        batteries.append(battery)

        if battery_position != 0:
            to_remove -= battery_position - start

        start = battery_position + 1
        end = start + to_remove + 1

    return "".join(batteries)

def find_largest(bank, start, end):
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

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))