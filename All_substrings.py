# Problem Statement

# For a given input string(str), write a function to print all the possible substrings.

# Substring
# A substring is a contiguous sequence of characters within a string.
# Example: "cod" is a substring of "coding". Whereas "cdng" is not as the characters taken are not contiguous

# Sample Input 1:
# abc

# Sample Output 1:
# a
# ab
# abc
# b
# bc
# c

def subString(s, n):
    # Pick starting point in outer loop
    # and lengths of different strings for
    # a given starting point
    for i in range(n):
        for len in range(i+1,n+1):
            print(s[i: len]);
 
# Driver program to test above function
s = input()
subString(s,len(s));
 