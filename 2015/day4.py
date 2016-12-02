#!/usr/bin/env python
import md5

data="yzbqklnj"

def matches_five_zeroes(s):
    return s[0] == s[1] == s[2] == s[3] == s[4] == '0'

assert matches_five_zeroes(md5.md5('abcdef609043').hexdigest())

def matches_six_zeroes(s):
    return s[0] == s[1] == s[2] == s[3] == s[4] == s[5] == '0'

i = 0
md5_val = md5.md5(data + '0').hexdigest()
while not (matches_five_zeroes(md5_val)):
    i += 1    
    md5_val = md5.md5(data + str(i)).hexdigest()

print "Matches 5 zeroes: " + str(i)

i = 0
md5_val = md5.md5(data + '0').hexdigest()
while not (matches_six_zeroes(md5_val)):
    i += 1    
    md5_val = md5.md5(data + str(i)).hexdigest()

print "Matches 6 zeroes: " + str(i)
