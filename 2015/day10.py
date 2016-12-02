#!/usr/bin/env python

actual_input = "3113322113"

def expand_input(i):
    output = ""
    counter = 0
    curr_char = i[0]
    for char in i:
        if char == curr_char:
            counter += 1
        else:
            output += str(counter) + curr_char
            curr_char = char
            counter = 1

    output += str(counter) + curr_char
    return output

assert(expand_input("1") == '11')
assert(expand_input("11") == '21')
assert(expand_input("21") == '1211')
assert(expand_input("1211") == '111221')
assert(expand_input("111221") == '312211')
assert(expand_input("312211") == '13112221')

for x in range(40):
    actual_input = expand_input(actual_input)

print "After 40 iterations, length of result is {}".format(len(actual_input))

for x in range(10):
    actual_input = expand_input(actual_input)

print "After 50 iterations, length of result is {}".format(len(actual_input))
