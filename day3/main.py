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

def main():
    banks = read_file("test.txt")
    total_joltage = 0
    
    for bank in banks:
        # part 1:
        # battery1_index, battery2_index, joltage = get_pair(bank)
        # print(f"In {bank}, you can make the largest joltage possible, {joltage}, by turning on batteries {battery1_index + 1} and {battery2_index + 1}.")

        # iterate over whole battery bank, check if each number is larger than the smallest current candidate and boot that one if so
        # dict.pop("key", None) to remove a key regardless of if it exists? probably not relevant
        print(get_twelve(bank))
        # total_joltage += joltage
    
    print(f"Total output joltage is {total_joltage}")
    return

def get_joltage(list):
    return

def get_twelve(bank):
    largest, smallest = 0, 9
    smallest_index = int()
    batteries = [] 
    # thought would be dictionary of the chosen batteries' index in the bank (unique) : the number it corresponds to (not unique)
    # going to try a list instead

    for i in range(0, len(bank)):
        battery = int(bank[i])
        
        # NEXT IDEA: need to somehow track more than simply the oldest smallest index

        if battery > largest:
            largest = battery
            batteries.append(largest)
            if i >= 12:
                print(f"popping battery {battery} at index {smallest_index}")
                batteries.pop(smallest_index)
        elif battery < smallest:
            # this could be a problem - being small and EARLY matters more than being small in general, maybe?
            if i < 12:
                print(f"{battery} is smaller than {smallest}")
                smallest = battery
                smallest_index = i
                print(f"smallest battery index set to {smallest_index}")
                batteries.append(smallest)
        elif battery == smallest:
            if i < 12:
                batteries.append(smallest)
            elif i >= 12:
                print(f"popping battery {battery} at index {smallest_index}")
                batteries.pop(smallest_index)
                smallest = battery
                smallest_index = i
        elif battery >= smallest:
            batteries.append(battery)
            if i >= 12:
                print(f"popping battery {battery} at index {smallest_index}")
                batteries.pop(smallest_index)
                smallest = battery
        
    return batteries

def get_pair(bank):
    battery1, battery1_index = find_largest_p1(bank, 0, len(bank) - 1)
    battery2, battery2_index = find_largest_p1(bank, battery1_index + 1, len(bank))

    joltage = battery1 * 10 + battery2
    
    return battery1_index, battery2_index, joltage

def find_largest_p2(bank, start, end):
    largest = 0
    largest_index = int()

    for i in range(start, end):
        if int(bank[i]) > largest:
            largest = int(bank[i])
            largest_index = i
    
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