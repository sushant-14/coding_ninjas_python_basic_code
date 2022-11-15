# Reverse the given string word-wise. 
# The last word in the given string should come at 1st place, the last- second word at 2nd place, and so on. 
# Individual words should remain as it is.

# Sample Input 1:
# Welcome to Coding Ninjas

# Sample Output 1:
# Ninjas Coding to Welcome

# Sample Input 2:
# Always indent your code

# Sample Output 2:
# code your indent Always

string=[str(i) for i in input().split()]
string.reverse()
print(" ".join(string))
        
