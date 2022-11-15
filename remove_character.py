# For a given string (str) and a character X, 
# write a function to remove all the occurrences of X from the given string and return it. 
# The input string will remain unchanged if the given character(X) doesn't exist in the input string.

def removeAllOccurrencesOfChar(string,c):
    for i in string[:]:
        if i==c:
            string.remove(i)
        else:
            i=+1
    return "".join(string)
string =[*input()]
c = input()
output = removeAllOccurrencesOfChar(string,c)
print(output)