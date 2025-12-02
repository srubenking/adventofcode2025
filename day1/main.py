"""
Safe has a circular dial with numbers 0 through 99
With the dial at 11, an input of R8 would cause it to point to 19 (11 + 8)
With it at 19, an input of L20 would cause it to point to 99 (19 - 20 = -1 | -1 + 100 = 99)

Part 1: the password is equal to the number of times the dial is LEFT pointing at 0 after a rotation instruction
Part 2: the password is equal to the number of times the dial ever passes over OR lands on 0

"""

def main():
    f = open("input.txt")
    instructions = f.read().splitlines()

    dial = 50
    zeroes = 0

    print("Are you answering part 1 or part 2?")
    part = input()

    if part in ["one", "part one", "1", "part 1"]:
        for rotation in instructions:
            direction = rotation[0]
            clicks = int(rotation[1:])
            
            if direction == "L":
                # left
                dial -= clicks
            else:
                # right
                dial += clicks

            # account for negative numbers in general, and going < -100 with while loop
            while dial < 0:
                dial += 100

            # account for number > 99 in general, and going > 199 with while loop
            while dial > 99:
                dial -= 100

            if dial == 0:
                zeroes += 1

        print(f"Part 1: The dial has landed on zero {zeroes} times.")
    elif part in ["two", "part two", "2", "part two"]:
        for rotation in instructions:
            direction = rotation[0]
            clicks = int(rotation[1:])
            
            zero_times = get_zeroes(dial, clicks, direction)
            new_dial = set_dial(dial, clicks, direction)

            dial = new_dial
            zeroes += zero_times

        print(f"Part 2: The dial has landed on or passed by zero {zeroes} times.")
    else:
        print("invalid input")

def get_zeroes(dial, clicks, direction):
    if direction == "L":
        if dial - clicks <= 0:
            if dial == 0:
                return abs(int((dial - clicks) / 100))
            else:
                return 1 + abs(int((dial - clicks) / 100))
        else:
            return 0
    else:
        if dial + clicks >= 100:
            return abs(int((dial + clicks) / 100))
        else:
            return 0

def set_dial(dial, clicks, direction):
    if direction == "L":
        return (dial - clicks) % 100
    else:
        return (dial + clicks) % 100

main()