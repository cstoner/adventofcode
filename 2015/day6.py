#!/usr/bin/env python
import numpy

with open('day6_data.txt') as f_hdl:
    data = f_hdl.read()

grid = numpy.zeros((1000,1000))

# We get coordinates as strings, and would like them
# to be integers.
# This function accepts input in "NNN,NNN" format
# and returns a 2-ple with the integers
def coord_to_ints(s):
    nums = s.split(',')
    return (int(nums[0]), int(nums[1]))

# Instructions come in the format:
#   <action> <start_range> through <end_range>
# where <action> can be one of
#  * turn on
#  * turn off
#  * toggle
# Part 2 changes the functions, but in practice only the toggle is different
def do_instruction(s):
    def turn_on(i):
        return i+1
    def turn_off(i):
        return max(0,i-1)

    # Day 1 toggle, not used in day 2
    def toggle1(i):
        if i == 0:
            return 1
        elif i == 1:
            return 0

    def toggle(i):
        return i+2

    def act_on_ranges(action, start, end):
        (x1, y1) = start
        (x2, y2) = end

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                grid[i][j] = action(grid[i][j])

    tokens = s.split(' ')
    if 'turn on' in s:
        act_on_ranges(turn_on, coord_to_ints(tokens[2]), coord_to_ints(tokens[4]))
    elif 'turn off' in s:
        act_on_ranges(turn_off, coord_to_ints(tokens[2]), coord_to_ints(tokens[4]))
    elif 'toggle' in s:
        act_on_ranges(toggle, coord_to_ints(tokens[1]), coord_to_ints(tokens[3]))

def count_grid():
    count = 0
    for row in grid:
        count += sum(row)   

    return int(count)

def clear_grid():
    for x in range(1000):
        for y in range(1000):
            grid[x][y] = 0

# Part 1 assertions
#do_instruction("turn on 0,0 through 999,999")
#assert(count_grid() == 1000000)
#clear_grid()
#assert(count_grid() == 0)

#do_instruction("toggle 0,0 through 999,0")
#assert(count_grid() == 1000)
#clear_grid()

#do_instruction("turn on 0,0 through 999,999")
#do_instruction("turn off 499,499 through 500,500")
#assert(count_grid() == 1000000 - 4)
#clear_grid()

for line in data.split('\n'):
    do_instruction(line)


print "Light count: {}".format(count_grid())