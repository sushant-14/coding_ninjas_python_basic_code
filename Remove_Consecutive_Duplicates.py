# Problem Statement

# For a given string (str), remove all the consecutive duplicate characters.

# Example:
# Input String: "aaaa" 
# Expected Output: "a"

# Input String: "aabbbcc"
# Expected Output: "abc"

def solve(s):
      seen = s[0]
      ans = s[0]
      for i in s[1:]:
         if i != seen:
            ans += i
            seen = i
      return ans
print(solve(input()))