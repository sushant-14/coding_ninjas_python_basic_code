# Problem Statement

# Aadil has been provided with a sentence in the form of a string as a function parameter.
# The task is to implement a function so as to print the sentence such that each word in the sentence is reversed.

# Example:
# Input Sentence: "Hello, I am Aadil!" The expected output will print, ",olleH I ma !lidaA".

a=[str(i[::-1]) for i in input().split()]
print(" ".join(a))