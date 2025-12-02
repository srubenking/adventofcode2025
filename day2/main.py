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
"""

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
        if is_repeat(i):
            total_in_range += i
    return total_in_range

def is_repeat(num):
    # this is where the meat goes - need to check for redundancy
    # return True if repeat, like 11 or 22 - return False otherwise
    # ironically, after having converted them to integers I believe treating them as strings would be the easiest way to check for this
    check_num = str(num)
    result = False
    length = len(check_num)
    # check if number is odd by getting remainder from length % 2 - no odd number would be invalid, so only proceed if remainder is 0
    if length % 2 == 0:
        middle = int(length / 2)
        first_half = check_num[:middle]
        second_half = check_num[middle:]
        if first_half == second_half:
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