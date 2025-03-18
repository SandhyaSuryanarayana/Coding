#Given a string, split the string(group the strings) based on numeric and alphabets. 
#Assume there are no special characters in the input

def split_string(s):
    l = 0
    r = 1

    lst = []

    while l<=r and r < len(s):
        #check if current and next string are of same datatype
        if s[l].isdigit() == s[r].isdigit() :
            r += 1
        else:
            lst.append(s[l:r])
            l = r
            r += 1

    if l < len(s):
        lst.append(s[l:r])

    return lst


s = '123what345is789python12345'

lst = split_string(s)

print("split string:",lst)

