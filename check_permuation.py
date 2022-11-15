# Check Permutation
# Problem Statement

# For a given two strings, 'str1' and 'str2', check whether they are a permutation of each other or not.

# Permutations Of Each Other
# Two strings are said to be a permutation of each other when either of the string's characters can be rearranged
# so that it becomes identical to the other one.

# Example:

# str1= "sinrtg"
# str2="string"

# The character of the first string (str1) can be rearranged to form str2 and
# hence we can say that the given strings are a permutation of each other.

from os import *
from sys import *
from collections import *
from math import *

def isPermutation(string1, string2) :
    if sorted(string1)==sorted(string2):
        return True
    #Your code goes here

#main
string1 = input()
string2 = input()
ans = isPermutation(string1, string2)
if ans :
    print('true')
else :
    print('false')

