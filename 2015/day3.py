#!/usr/bin/python
with open("day3_data.txt") as f_hdl:
    data = f_hdl.read()

def get_plot(data):
    curr_x = 0
    curr_y = 0
    plot = {}

    plot[(0, 0)] = 1
    for c in data:
        if c == '>':
            curr_x += 1
        elif c == '<':
            curr_x -= 1
        elif c == '^':
            curr_y += 1
        elif c == 'v':
            curr_y -= 1

        if (curr_x, curr_y) in plot:
            plot[(curr_x, curr_y)] += 1
        else:
            plot[(curr_x, curr_y)] = 1

    return plot

assert(len(get_plot('>')) == 2)
assert(len(get_plot('^>v<')) == 4)
assert(len(get_plot('^v^v^v^v^v')) == 2)

def split_route(data):
    route1 = ""
    route2 = ""
    for i in range(len(data)):
        if i % 2 == 0:
            route1 += data[i]
        else:
            route2 += data[i]

    route1_plot = get_plot(route1)
    route2_plot = get_plot(route2)

    route1_plot.update(route2_plot)

    return route1_plot

assert(len(split_route('^v')) == 3)
assert(len(split_route('^>v<')) == 3)
assert(len(split_route('^v^v^v^v^v')) == 11)

print str(len(get_plot(data))) + " houses visisted"
print str(len(split_route(data))) + " split houses visited"
