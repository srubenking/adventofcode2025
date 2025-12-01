"""
Safe has a circular dial with numbers 0 through 99
With the dial at 11, an input of R8 would cause it to point to 19 (11 + 8)
With it at 19, an input of L20 would cause it to point to 99 (19 - 20 = -1 | -1 + 100 = 99)

*** the password is equal to the number of times the dial is LEFT pointing at 0 after a rotation instruction ***

"""

def main():
    f = open("input.txt")
    instructions = f.read().splitlines()

    dial = 50
    zeroes = 0

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

    print(zeroes)

main()