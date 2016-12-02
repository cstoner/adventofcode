#!/usr/bin/env python

with open('day7_data.txt') as f_hdl:
    data = f_hdl.read()

# The testing dataset provided to test things
#data = """123 -> x
#456 -> y
#x AND y -> d
#x OR y -> e
#x LSHIFT 2 -> f
#y RSHIFT 2 -> g
#NOT x -> h
#NOT y -> i"""

def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

# gd - Gate Dict
# gate - Gate name
# This function needed to be memoized, or it is much too slow.
def evaluate_gates(gd, gate):
    if is_number(gate):
        return int(gate)

    gv = gd[gate]
    tok = gv.split(' ')

    if 'AND' in gv:
        val = evaluate_gates(gd, tok[0]) & evaluate_gates(gd, tok[2])
    elif 'OR' in gv:
        val = evaluate_gates(gd, tok[0]) | evaluate_gates(gd, tok[2])
    elif 'LSHIFT' in gv:
        val = evaluate_gates(gd, tok[0]) << int(tok[2])
    elif 'RSHIFT' in gv:
        val = evaluate_gates(gd, tok[0]) >> int(tok[2])
    elif 'NOT' in gv:
        # Since this is a 16-bit signal, the built-in python function won't work.
        str_val = '{0:016b}'.format(evaluate_gates(gd, tok[1]))
        str_val = str_val.replace('0', '3').replace('1', '0').replace('3', '1')
        val = int(str_val, 2)
    else:
        # In the event that none of the above match, try to check if it's 
        # a defined wire
        return evaluate_gates(gd, tok[0])

    # Shortcut the lookup in the future
    gd[gate] = str(val)
    return val

# This is the dict that holds the definition of each gate
# This is just a str->str map, and the actual processing is in the evaluate function
gate_map = {}

for line in data.split('\n'):
    tmp = line.split('->')
    if (len(tmp) > 1):
        gate_map[tmp[1].strip()] = tmp[0].strip()

# Only valid for the testing dataset
#assert(evaluate_gates(gate_map, 'x') == 123)
#assert(evaluate_gates(gate_map, 'y') == 456)
#assert(evaluate_gates(gate_map, 'd') == 72)
#assert(evaluate_gates(gate_map, 'e') == 507)
#assert(evaluate_gates(gate_map, 'f') == 492)
#assert(evaluate_gates(gate_map, 'g') == 114)
#assert(evaluate_gates(gate_map, 'h') == 65412)
#assert(evaluate_gates(gate_map, 'i') == 65079)

a_val = evaluate_gates(gate_map, 'a')
print "1st value of gate 'a' is {}".format(a_val)

# Part 2, reset the wires. Set value of gate a to wire b, and rerun everything
for line in data.split('\n'):
    tmp = line.split('->')
    if (len(tmp) > 1):
        gate_map[tmp[1].strip()] = tmp[0].strip()

gate_map['b'] = str(a_val)
a_val = evaluate_gates(gate_map, 'a')
print "2nd value of gate 'a' is {}".format(a_val)
