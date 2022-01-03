Goal
A turtle and a Rabbit are trying to find out who is faster. They are running on a rectangular stadium. After certain amount of time wins the one who is closer(in either direction) to the finish line.
Here is an example of 5x4 stadium:
#####
#.......#
#.......#
#####
One lap is 14 cells. Finish line is always in the same cell as start line.

Your goal is to find out who is closer to finish line after duration seconds
Input
stadiumLength - length of the stadium (cells)
stadiumWidth - width of the stadium (cells)
turtleSpeed - speed of the turtle (cells per second)
rabbitSpeed - speed of the rabbit (cells per second)
duration - duration of the run (seconds)
Output
Print out "TURTLE" if the turtle is closer to finish line, "RABBIT" if rabbit is closer or "DRAW" if the distance is the same.
Constraints
stadiumLength >= 2
stadiumWidth >= 2
Example
Input
5 4 1 5 1
Output
TURTLE



=======

# mine 
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

stadium_length, stadium_width, turtle_speed, rabbit_speed, duration = [int(i) for i in input().split()]

# Write an answer using print
# # To debug: print("Debug messages...", file=sys.stderr, flush=True)

# print(stadium_length)
# print(stadium_width)
# print(turtle_speed)
# print(rabbit_speed)
# print(duration)


lap_total = 2 * stadium_length + 2 * (stadium_width - 2)
turtle_total = turtle_speed * duration
rabbit_total = rabbit_speed * duration


if lap_total - turtle_total == 0 or lap_total - rabbit_total == 0:
    if lap_total - turtle_total == 0:
        print("TURTLE")
    elif lap_total - rabbit_total == 0:
        print("RABBIT")
else:
    if abs(lap_total - turtle_total) > abs(lap_total - rabbit_total):
        print("TURTLE")
    elif abs(lap_total - turtle_total) == abs(lap_total - rabbit_total):    
        print("DRAW")
    else:
        print("RABBIT")



==========

# answer

import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l, w, t, r, d = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

t=t*d%14
r=r*d%14
t=min(t,14-t)
r=min(r,14-r)
print('TURTLE'if t<r else 'RABBIT' if r<t else 'DRAW')
