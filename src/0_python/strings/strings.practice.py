# reverse string
s = "python"
print(s[::-1])

# count words → output: 2
s = "hello world"
print(len(s.split()))

# remove duplicates
s = "programming"
def remove_dups(string):
    no_dups = ""
    for s in string:
        if s not in no_dups: 
            no_dups+=s
    
    return no_dups
print(remove_dups(s))

# replace space with -
s = "hello world"
# print("-".join(s.split()))
print(s.replace(" ", "-"))

# check palindrome → True
s = "madam"
def isPalindrome(string):
    return string == string[::-1]
print(isPalindrome(s))