#!/usr/bin/env python
from sets import Set

with open('day9_data.txt') as f_hdl:
    data = f_hdl.read()

#data = """London to Dublin = 464
#London to Belfast = 518
#Dublin to Belfast = 141"""

cities = Set()
dist_map = {}
for line in data.split('\n'):
    tokens = line.split(' ')

    city1 = tokens[0]
    city2 = tokens[2]
    dist = int(tokens[4])

    cities.add(city1)
    cities.add(city2)

    dist_map[(city1, city2)] = dist
    dist_map[(city2, city1)] = dist

cities = list(cities)

def get_unvisited_cities(path, all_cities):
    cities_copy = list(all_cities)

#    print "Path: {}".format(path)
#    print "All Cities: {}".format(all_cities)

    for city in path:
        cities_copy.remove(city)

    return cities_copy

assert(get_unvisited_cities(['a'], ['a', 'b', 'c']) == ['b', 'c'])
assert(get_unvisited_cities(['a', 'b'], ['a', 'b', 'c']) == ['c'])

def expand_travel_list(paths, all_cities):
    ret = []
    for path in paths:
        remaining_cities = get_unvisited_cities(path, list(all_cities))
        for city in remaining_cities:
            new_path = list(path)
            new_path.append(city)
            ret.append(new_path)
    return ret

assert(expand_travel_list([['a']], ['a', 'b']) == [['a', 'b']])
assert(expand_travel_list([['a']], ['a', 'b', 'c']) == [['a', 'b'], ['a', 'c']])

def score_trip(p):
    trips_list = [(p[i], p[i+1]) for i in range(len(p)-1)]

    score = 0
    for trip in trips_list:
        score += dist_map[trip]
    return score

start_paths = [[city] for city in cities]
curr_paths = expand_travel_list(start_paths, cities)
while ( len(get_unvisited_cities(curr_paths[0], cities)) > 0):
    curr_paths = expand_travel_list(curr_paths, cities)

print "Number of paths calculated: {}".format(len(curr_paths))
scores = [score_trip(p) for p in curr_paths]
print "The Shortest trip has a lenght: {}".format(min(scores))
print "The Longest trip has a length: {}".format(max(scores))