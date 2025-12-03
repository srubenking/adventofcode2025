"""
Example input: 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
Input is a list of ranges (min-max) separated by commas.

Any ID made of ONLY a sequence of digits repeated TWICE (55, 6464, 123123, but not 112 or 1122 or 121212) is invalid. No ID valid or invalid will have leading 0s.

Your job is to find all of the invalid IDs that appear in the given ranges. In the above example:

11-22 has two invalid IDs, 11 and 22.
95-115 has one invalid ID, 99.
998-1012 has one invalid ID, 1010.
1188511880-1188511890 has one invalid ID, 1188511885.
222220-222224 has one invalid ID, 222222.
1698522-1698528 contains no invalid IDs.
446443-446449 has one invalid ID, 446446.
38593856-38593862 has one invalid ID, 38593859.
The rest of the ranges contain no invalid IDs.
Adding up all the invalid IDs in this example produces 1227775554.

What do you get if you add up all of the invalid IDs?

Part 2:

Any ID made of only a sequence of digits repeated ANY NUMBER OF TIMES (12341234, 123123123, 1212121212, 1111111) is now invalid
"""
import math

def main():
    ranges = ranges_from_file("input.txt")
    # run check_range() on ranges, a list of pairs of integers
    invalid_total = 0
    for r in ranges:
        invalid_total += check_range(r)
    
    print(f"{invalid_total} total repeats")

def check_range(pair):
    # take pair, a two item list of integers, and check for invalid IDs between those two numbers
    start = pair[0]
    end = pair[1] + 1
    total_in_range = 0

    for i in range(start, end):
        # first pair from example should add 2 to the count, with 11 and 22 being the trigger
        # print(f"{i} is a repeat: {is_repeat(i)}")
        if is_repeat_two(i):
            total_in_range += i
    return total_in_range

def get_digits(num):
    # gets the number of digits in num - have to add 1 to get total, result otherwise is x where 10^x = num
    return int(math.log10(num)) + 1

def get_factors(num):
    factors = []
    for i in range(1, num):
        if num % i == 0:
            factors.append(i)

    return factors

def is_repeat_two(num):
    # result is too high
    
    # same as before but adding an else statement for odd numbers
    digits = get_digits(num)
    # don't need explicit even/odd check - just need to iterate over all possibilities
 
    # start with digits, then iterate over its factors - for example 15 digits, then 5 then 3 then 1
    factors_list = get_factors(digits) # [1, 3, 5]
    for factor in factors_list:
        check = 0
        range_end = int(digits / factor)
        for i in range(0, range_end):
            check += 10 ** (i * factor) 
        if num % check == 0:
            return True
    return False

def is_repeat_one(num):
    # try implementing Zeb's method - get number of digits with log10 and round up (or round down and add 1)
    # then divide the number by a sequence 1...1 with 0s (or nothing) filling the space - length is the number of digits / 2 + 1
    # 2 : 2, 4 : 3, 6 : 4, 8: 5
    # for example 123123 is 6 digits, so 123123/1001 = 123, 55/11 = 5, 1010/101 = 10, 12341234/10001 = 1234
    digits = get_digits(num)
    result = False
    # check if even
    if digits % 2 == 0:
        # do even things
        divide_by = int(10 ** (digits / 2) + 1)
        if num % divide_by == 0:
            result = True
    return result

def ranges_from_file(file):
    # take input file string, split on commas to create a list of digit pairs separated by hyphens
    with open(file, "r") as file:
        file_content = file.read()
    ranges = file_content.split(",")
    # take that list, split on hyphens to return a new list of lists and turn strings into integer pairs
    int_ranges = []

    for pair in ranges:
        str_pair = pair.split("-")
        int_pair = []
        for num in str_pair:
            int_pair.append(int(num))
        int_ranges.append(int_pair)
    
    return int_ranges

main()