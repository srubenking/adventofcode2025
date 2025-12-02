"""
Safe has a circular dial with numbers 0 through 99
With the dial at 11, an input of R8 would cause it to point to 19 (11 + 8)
With it at 19, an input of L20 would cause it to point to 99 (19 - 20 = -1 | -1 + 100 = 99)

*** the password is equal to the number of times the dial is LEFT pointing at 0 after a rotation instruction ***

*** password method 0x434C49434B ***
need to count ANY CLICK that causes the dial to point to 0
not just those that happen at the end of a rotation

"""

def main():
    f = open("input.txt")
    instructions = f.read().splitlines()

    dial = 50
    zeroes = 0

    # test_instructions = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
    # dial points to 0 3 times DURING rotation, and 3 times at the END of a rotation - 6 times total
    print(f"The dial starts by pointing at {dial}")
    for rotation in instructions:
        direction = rotation[0]
        clicks = int(rotation[1:])
        
        zero_times = get_zeroes(dial, clicks, direction)
        new_dial = set_dial(dial, clicks, direction)

        # print(f"The dial is rotated {rotation} to point at {new_dial}; during this rotation, it points at zero {zero_times} times")

        dial = new_dial
        zeroes += zero_times

    print(f"The dial has pointed to or passed by 0 {zeroes} times")

def get_zeroes(dial, clicks, direction):
    if direction == "L":
        if dial - clicks <= 0:
            # less than OR equal to, to check both if it LANDS on zero and if it goes past - needs to return at least 1
            # also needs to check for how FAR past zero it goes - and the result needs to be positive
            # also have to account for when the dial STARTS at 0 - going L5 from 0 gets to 95, but does not add a zero as that zero has already been counted
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

def main_prototype():
    f = open("input.txt")
    instructions = f.read().splitlines()

    dial = 50
    zeroes = 0

    print("Enter the password:")
    password = input()

    if password == "password":
        for rotation in instructions:
            direction = rotation[0]
            clicks = int(rotation[1:])
            # print(f"dial is at {dial}, rotating {direction} for {clicks} clicks")

            # get how many times the dial passes zero by dividing by 100 and rounding down using int()
            if direction == "L":
                dial -= clicks
                new_zeroes = int(dial/100)
                if dial == 0:
                    new_zeroes += 1
            else:
                dial += clicks
                new_zeroes = int(dial/100)
            # set the dial to the correct position using modulo

            # print(f"expecting {new_zeroes} zeroes - press enter to continue")
            # next = input()

            dial = dial % 100
            zeroes += new_zeroes

            # print(f"dial is now at {dial}, and {zeroes} total zeroes - enter anything to continue")
            # next = input()

        print(f"Right password, {zeroes} zeroes")
    elif password == "test":
        test_instructions = ["L50", "R101", "L1", "R202", "L202"]
        for rotation in test_instructions:
            direction = rotation[0]
            clicks = int(rotation[1:])
            print(f"rotating from {dial} in {direction} for {clicks} clicks")
            # get how many times the dial passes zero by dividing by 100 and rounding down using int()
            
            if direction == "L":
                dial -= clicks
                if dial == 0:
                    new_zeroes = 1
                else:
                    new_zeroes = int(dial/100)
            else:
                dial += clicks
                new_zeroes = int(dial/100)
            # set the dial to the correct position using modulo

            # print(f"expecting {new_zeroes} zeroes - press enter to continue")
            # next = input()

            dial = dial % 100
            zeroes += new_zeroes

            print(f"dial now at {dial}, passing zero {zeroes} times")
        print(f"expected dial at 0, actual at {dial}, expected zeros at 7, actual at {zeroes}")
    elif password == "inc":
        for rotation in instructions:
            direction = rotation[0]
            clicks = int(rotation[1:])
            
            for click in range(clicks, 0):
                if direction == "L":
                    dial -= 1
                else:
                    dial += 1

                if dial == -1:
                    dial += 100
                if dial == 100:
                    dial -= 100

                if dial == 0:
                    zeroes += 1
            else:
                for click in range(0, clicks):
                    dial += 1
                    if dial == 0:
                        zeroes += 1

        print(f"Incrementing manually, found {zeroes} zeroes")
    else:
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

        print(f"Wrong password, {zeroes} zeroes")

main()