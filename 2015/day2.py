#!/usr/bin/python

def get_area(l,w,h):
    """The area we are of wrapping paper needed is given in the problem"""
    return 2*l*w + 2*w*h + 2*h*l + min([l*w,w*h,h*l])

assert(get_area(2,3,4) == 58)
assert(get_area(1,1,10) == 43)

def get_ribbon(l,w,h):
    sides = [l,w,h]
    side1 = min(sides)
    sides.remove(side1)
    side2 = min(sides)

    return 2*side1 + 2*side2 + l*w*h

assert(get_ribbon(2,3,4) == 34)
assert(get_ribbon(1,1,10) == 14)

with open('day2_data.txt') as f_hdl:
    data = f_hdl.read()

total_area = 0
total_ribbon = 0
for line in data.split('\n'):
    (l, h, w) = (int(num) for num in line.split('x'))
    total_area += get_area(l, h, w)
    total_ribbon += get_ribbon(l, h, w)

print "Total area needed: {}".format(total_area)
print "Total ribbon needed: {}".format(total_ribbon)