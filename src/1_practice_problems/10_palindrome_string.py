# Check whether a given string is a palindrome.

def is_palindrome(string):
    return string == string[::-1]

print(is_palindrome("siva"))
print(is_palindrome("sms"))