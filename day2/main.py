"""
Input is a list of ranges (min-max) separated by commas.

Part 1: Any ID made of ONLY a sequence of digits repeated TWICE (e.g. 55, 6464, 123123, but not 112 or 1122 or 121212) is invalid.

Part 2: Any ID made of only a sequence of digits repeated ANY NUMBER OF TIMES (e.g. 12341234, 123123123, 1212121212, 1111111) is now invalid as well.

What do you get if you add up all of the invalid IDs?
"""
import math
import time

def main():
    ranges = ranges_from_file("input.txt")
    invalid_total = 0
    
    # check all ranges for invalid IDs, add the sum of the IDs themselves to the invalid_total
    for r in ranges:
        invalid_total += check_range(r)
    
    print(f"{invalid_total} total repeats")

def check_range(pair):
    # take pair, a two item list of integers, and check for invalid IDs for all integers between those two
    start = pair[0]
    end = pair[1] + 1
    total_in_range = 0

    for i in range(start, end):
        if is_repeat_two(i):
            total_in_range += i
    return total_in_range

def get_digits(num):
    # gets the number of digits in num - have to add 1 to get the right number, result otherwise is x where 10^x = num
    return int(math.log10(num)) + 1

def get_factors(num):
    # clumsily iterate over all integers up to num and check if num is divisable by each, add them to list
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return factors

def is_repeat_one(num):
    # repeat check for part 1 - ignores odd length IDs as they're valid by default
    # any even length ID with two repeating sequences should be divisible by 1...1 where the length of that number is the length of the ID / 2
    # and the space between is empty or filled with 0s
    digits = get_digits(num)

    if digits % 2 == 0:
        check = int(10 ** (digits / 2) + 1)
        if num % check == 0:
            return True
    return False

def is_repeat_two(num):
    # accounts for any repeating sequences of any length occurring any amount of times
    digits = get_digits(num)
 
    # start with digits, then iterate over its factors to produce the new check number
    factors_list = get_factors(digits)
    for factor in factors_list:
        check = 0
        range_end = int(digits / factor)
        for i in range(0, range_end):
            check += 10 ** (i * factor) 
        if num % check == 0:
            return True
    return False

def ranges_from_file(file):
    # take input file string, split on commas to create a list of strings consisting of two numbers separated by hyphens
    with open(file, "r") as file:
        file_content = file.read()
    ranges = file_content.split(",")
    int_ranges = []

    # take that new list, split on hyphens to create a list of lists containing the individual pairs of numbers, then turn those strings into integers
    for pair in ranges:
        str_pair = pair.split("-")
        int_pair = []
        for num in str_pair:
            int_pair.append(int(num))
        int_ranges.append(int_pair)
    
    return int_ranges

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))