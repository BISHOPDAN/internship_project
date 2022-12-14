"""
strings = ["one", "two", "three"]

sources = ["onetwo", "one"]

for i in strings:
    if sources in strings or strings in sources:
        print("true")
        break
        
    else:
        print("false")
        break
"""

# Recursive Python program to check
# if a string is subsequence or prefix
# of another string
 
# Returns true if str1[] is a
# subsequence of str2[].
def isSubSequence(string1, string2, m, n):
    # Base Cases
    if m == 0:
        return True
    if n == 0:
        return False
 
    # If last characters of two
    # strings are matching
    if string1[m-1] == string2[n-1]:
        return isSubSequence(string1, string2, m-1, n-1)
 
    # If last characters are not matching
    return isSubSequence(string1, string2, m, n-1)
 
 
# Driver program to test the above function
string1 = ["one" "two" "three"]
string2 = ["onetwothree"]
 
if isSubSequence(string1, string2, len(string1), len(string2)):
    print (True)
else:
    print (False)



   
