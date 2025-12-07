"""
Day 4

..@@.@@@@.    ..xx.xx@x.
@@@.@.@.@@    x@@.@.@.@@
@@@@@.@.@@    @@@@@.x.@@
@.@@@@..@.    @.@@@@..@.
@@.@@@@.@@    x@.@@@@.@x
.@@@@@@@.@    .@@@@@@@.@
.@.@.@.@@@    .@.@.@.@@@
@.@@@.@@@@    x.@@@.@@@@
.@@@@@@@@.    .@@@@@@@@.
@.@.@@@.@.    x.x.@@@.x.

13 rolls accessible

"""
import time

def main():
    floor_map = read_file("input.txt")
    total_forkliftable = 0

    for i in range(0, len(floor_map)):
        forkliftable, new_map = remove_rolls(floor_map)
        total_forkliftable += forkliftable
        for row in new_map:
            print("".join(row))
        
        floor_map = new_map.copy()

        print(f"{forkliftable} forkliftable rolls")    
        print(f"{total_forkliftable} total forkliftable rolls")

def remove_rolls(floor_map):
    forkliftable = 0
    new_map = []

    for row in range(0, len(floor_map)):
        row_list = floor_map[row].copy()
        for column in range(0, len(floor_map[row])):
            #print(f"checking row {row} column {column}")
            if floor_map[row][column] == "@":
                if find_neighbors(row, column, floor_map) < 4:
                    forkliftable += 1
                    row_list[column] = "x"
                    #print(f"{forkliftable} forkliftable so far")
            #input()
        new_map.append(row_list)

    return forkliftable, new_map

def find_neighbors(row, column, floor_map):
    total_rolls = 0
    nw, n, ne = "", "", ""
    w, e = "", ""
    sw, s, se = "", "", ""
    """
    pretend we're checking position Y where Y is a @ at (1, 2)
    ..@@.@@@@.
    @@Y.@.@.@@
    @@@@@.@.@@

    should have 6 neighbors
    str.count(sub, [start], [end])
    """
    if floor_map[row][column] == ".":
        return f"no roll found at row {row} column {column}"

    # check northwest, north, northeast
    if row > 0:
        if 0 < column <= len(floor_map[row]) - 1:
            nw = floor_map[row-1][column-1]
        if 0 <= column < len(floor_map[row]) - 1:
            ne = floor_map[row-1][column+1]
        n = floor_map[row-1][column]
    # check west, east
    if 0 < column <= len(floor_map[row]) - 1:
        w = floor_map[row][column-1]
    if 0 <= column < len(floor_map[row]) - 1:
        e = floor_map[row][column+1]
    # check southwest, south, southeast
    if row < len(floor_map) - 1:
        if 0 < column <= len(floor_map[row]) - 1:
            sw = floor_map[row+1][column-1]
        if 0 <= column < len(floor_map[row]) - 1:
            se = floor_map[row+1][column+1]
        s = floor_map[row+1][column]

    total_neighbors = "".join(nw + n + ne + w + e + sw + s + se)
    """
    print("checking:")
    print(nw + n + ne)
    print(w + "?" + e)
    print(sw + s + se)
    """
    total_rolls = total_neighbors.count("@")
    #print(f"{total_rolls} rolls found")
    return total_rolls

def read_file(file):
    f = open(file)
    string_list = f.read().splitlines()
    list_list = []

    for string in string_list:
        list_list.append(list(string))
    return list_list

start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))