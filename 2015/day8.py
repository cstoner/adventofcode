#!/usr/bin/env python
import re

def length_of_code(s):
    return len(s)

assert(length_of_code(r'""') == 2)
assert(length_of_code(r'"abc"') == 5)
assert(length_of_code(r'"aaa\"aaa"') == 10)
assert(length_of_code(r'"\x27"') == 6)

def unescape_string(s):
    # Each string is surrounded by double-quotes
    m = re.findall(r'"(.*)"', s)
    if len(m) < 1:
        return ""
    unquoted_s = m[0]

    unescaped_string = ""
    remainder = unquoted_s    

    while len(remainder) > 0:
        # Read until the first '\'
        slash_idx = remainder.find('\\')
        if slash_idx < 0:
            unescaped_string += remainder
            break

        # Add all the stuff before the slash to the unescaped string
        unescaped_string += remainder[:slash_idx]

        if remainder[slash_idx+1] == 'x':
            # This might be a hex escaped sequence
            try:
                c_val = int(remainder[slash_idx+2:slash_idx+4], 16)
                unescaped_string += chr(c_val)
                remainder = remainder[slash_idx+4:]
            except ValueError:
                unescaped_string += remainder[slash_idx+1]
                remainder = remainder[slash_idx+2:]
        else:
            # This is just a character literal
            unescaped_string += remainder[slash_idx+1]
            remainder = remainder[slash_idx+2:]

    return unescaped_string

def length_of_data(s):
    return len(unescape_string(s))

assert(length_of_data(r'""') == 0)
assert(length_of_data(r'"abc"') == 3)
assert(length_of_data(r'"aaa\"aaa"') == 7)
assert(length_of_data(r'"\x27"') == 1)


def data_savings(s):
    return length_of_code(s) - length_of_data(s)

assert(data_savings(r'""') == 2)
assert(data_savings(r'"abc"') == 2)
assert(data_savings(r'"aaa\"aaa"') == 3)
assert(data_savings(r'"\x27"') == 5)

# Shamelessly stolen from someone else's solution
# It revealed that I was not converting '\x' characters from hex
def escaped_char_count(s):
    count = 0
    i = 1
    while i < len(s) - 1:
        if s[i] == "\\":
            i += 4 if s[i+1] == "x" else 2
        else:
            i += 1
        count += 1
    return count
def alt_data_savings(s):
    return len(s) - escaped_char_count(s)

assert(data_savings(r'""') == alt_data_savings(r'""'))
assert(data_savings(r'"abc"') == alt_data_savings(r'"abc"'))
assert(data_savings(r'"aaa\"aaa"') == alt_data_savings(r'"aaa\"aaa"'))
assert(data_savings(r'"\x27"') == alt_data_savings(r'"\x27"'))

# Part 2
def escape_string(s):
    chars_to_escape = ['"', '\\']
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

assert(escape_string(r'""') == r'"\"\""')
assert(escape_string(r'"abc"') == r'"\"abc\""')
assert(escape_string(r'"aaa\"aaa"') == r'"\"aaa\\\"aaa\""')
assert(escape_string(r'"\x27"') == r'"\"\\x27\""')

def data_loss(s):
    return len(escape_string(s)) - len(s)

with open('day8_data.txt') as f_hdl:
    data = f_hdl.read()

data_saved = 0
data_lost = 0
for line in data.split('\n'):
    assert(data_savings(line) == alt_data_savings(line))

    data_saved += data_savings(line)
    data_lost += data_loss(line)

print "(Part 1) The difference in length between code and data is {}".format(data_saved)
print "(Part 2) The number of characters increased by {}".format(data_lost)