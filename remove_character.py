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