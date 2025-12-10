"""
Part 1: Read in input like shown below and calculate as obviously intended, then add the total together

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Expected output: 4277556

123 * 45 * 6 = 33210
328 + 64 + 98 = 490
51 * 387 * 215 = 4243455
64 + 23 + 314 = 401

Part 2: Calculate things cephalopod style, top down (longest string of digits is 4). Whitespace matters now as columns are read right to left.

123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  

Expected output: 3263827

4 + 431 + 623 = 1058
175 * 581 * 32 = 3253600
8 + 248 + 369 = 625
356 * 24 * 1 = 8544

"""
import time

def main():
    lines = read_file("input.txt")

    ## Part 1 ##
    total = 0
    split_lines = []
    for line in lines:
        split_lines.append(line.split())
    for i in range(0, len(split_lines[0])):
        total += do_math(i, split_lines)   
    print(f"Part 1 total: {total}")

    ## Part 2 ##
    total2 = 0
    ceph = get_cephalopod_numbers(lines)
    for num_list in ceph:
        total2 += do_cephalopod_math(num_list)

    print(f"Part 2 total: {total2}")

def get_cephalopod_numbers(lines):
    cephalopods = []
    
    for i in range(len(lines[0]) - 1, -1, -1):
        if lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i] != "    ":
            cephalopods.append(lines[0][i] + lines[1][i] + lines[2][i] + lines[3][i] + " ")
        else:
            cephalopods.append(" | ")
        if lines[4][i] != " ":
            cephalopods.append(lines[4][i])

    joined = "".join(cephalopods)
    split = joined.split("|")
    final = []
    for item in split:
        final.append(item.split())

    return final

def do_cephalopod_math(ceph_list):
    result = int(ceph_list[0])

    if ceph_list[-1] == "*":
        for num in ceph_list[1:-1]:
            result *= int(num)
    else:
        for num in ceph_list[1:-1]:
            result += int(num)

    return result

def do_math(index, lines):
    result = int(lines[0][index])
    if lines[-1][index] == "*":
        for line in lines[1:-1]:
            result *= int(line[index])
    else:
        for line in lines[1:-1]:
            result += int(line[index])

    return result

def read_file(file):
    f = open(file)
    lines = f.read().splitlines()

    return lines

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))