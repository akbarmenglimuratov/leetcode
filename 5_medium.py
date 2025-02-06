'''
Given a string s, return the longest palindromicsubstring in s.
'''

import array

def first_substring(s):
    n = len(s)
    high = 1
    start = 0

    for i in range(n/2):
        if s[i] == s[n - i]:
            longest += s[i]
        else:
            pass



# s = input()
s = 'babas'
print(first_substring(s))
