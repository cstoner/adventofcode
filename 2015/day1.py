#!/usr/bin/python

with open('day1_data.txt') as f_hdl:
    data = f_hdl.read()

curr_ident = 0
for (i,c) in enumerate(data):
    if c == '(':
        curr_ident += 1
    elif c == ')':
        curr_ident -= 1
    if curr_ident < 0:
        print("Unbalenced parens at char " + str(i+1))
        break

print(curr_ident)