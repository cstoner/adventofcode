#!/usr/bin/env python

with open('day5_data.txt') as f_hdl:
    data = f_hdl.read()

# Part 1
def is_nice_string1(s):
    # Nice strings have 3 vowels
    def has_3_vowels():
        total = 0
        for vowel in ['a', 'e', 'i', 'o', 'u']:
            total += s.count(vowel)
        return total >= 3

    # Nice strings have at least 1 double-letter occurence (ie, aa bb cc)
    def has_double_letters():
        # Skip the last character to prevent an out of bounds error
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                return True
        # Default case is 
        return False

    # Nice strings are not on the 'naughty' list
    def has_naughty_substrings():
        for c in ['ab', 'cd', 'pq', 'xy']:
            if c in s:
                return True

        return False   

    return has_3_vowels() and \
           has_double_letters() and \
           not has_naughty_substrings()

assert(is_nice_string1('ugknbfddgicrmopn'))
assert(is_nice_string1('aaa'))
assert(not is_nice_string1('jchzalrnumimnmhp'))
assert(not is_nice_string1('haegwjzuvuyypxyu'))
assert(not is_nice_string1('dvszwmarrgswjxmb'))

# Part 2
def is_nice_string2(s):
    # True if any pair of letters occurs later in the string
    # (ie, 'xxyxx' would be true for 'xx', 'xyaxy' would be true for 'xy')
    def has_repeated_pair():
        for i in range(len(s)-1):
            possible_repeat = s[i:i+2]
            if possible_repeat in s[i+2:]:
                return True
        return False

    # True if a letter occurs with an extra in the middle
    # (ie, 'axa' for 'a', 'byb' for 'b')
    def has_repeat_with_middle_char():
        for i in range(len(s)-2):
            if s[i] == s[i+2]:
                return True
        return False

    return has_repeated_pair() and \
           has_repeat_with_middle_char()

assert(is_nice_string2('qjhvhtzxzqqjkmpb'))
assert(is_nice_string2('xxyxx'))
assert(not is_nice_string2('uurcxstgmygtbstg'))
assert(not is_nice_string2('ieodomkazucvgmuy'))

nice1_string_count = 0
nice2_string_count = 0
for line in data.split('\n'):
    if is_nice_string1(line):
        nice1_string_count += 1
    if is_nice_string2(line):
        nice2_string_count += 1

print str(nice1_string_count) + " nice strings on day 1"
print str(nice2_string_count) + " nice strings on day 2"