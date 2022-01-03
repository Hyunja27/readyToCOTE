Goal


=======

# mine

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

red_strength, red_toughness = [int(i) for i in input().split()]
blue_strength, blue_toughness = [int(i) for i in input().split()]



# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print(red_strength)
# print(red_toughness)

# print(blue_strength)
# print(blue_toughness)


for i in range(100000000):
    # print(blue_toughness - red_strength * i)
    # print(red_toughness - blue_strength * i)
    # print("=======")
    if blue_toughness - red_strength * i <= 0 and red_toughness - blue_strength * i <= 0:
        print("Draw")
        break
    elif blue_toughness - red_strength * i <= 0 or red_toughness - blue_strength * i <= 0:
        if blue_toughness - red_strength * i > red_toughness - blue_strength * i:
            print("Blue")
            break
        else:
            print("Red")
            break



# elif red_toughness - blue_strength > blue_toughness - red_strength:
#     print("Red")




==========

# answer