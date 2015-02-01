n = 0
x= 0

def ispalindrome(n):
    s = str(n)
    reversestring = ""

    for i in range (len(s) -1, -1, -1): #print it out backwards
        reversestring += s[i]   

    return reversestring == s
               

def findlargestpalindrome():
    palindrome = -1

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):

            if ispalindrome(i * j) and i * j > palindrome:
                palindrome = i * j

    return palindrome;

print(findlargestpalindrome())

#do it with a word first... see if you can then do it with numbers.
    
            
