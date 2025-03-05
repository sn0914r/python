#String methods
"""
1. .lower() : converts all characters to lowercase and returns a new string
2. .upper() : converts all characters to uppercase and returns a new string
3. .title() : converts the first letter of every word to uppercase and returns a new string
4. .capitalize() : converts the first character to uppercase and returns a new string
5. .swapcase() : conevrts the uppercase to lowercase letters and vice versa and returns a new string

6. .isalpha() : returns true if every character in the string is an alphabet
7. .isdigit() : returns true if every character in the string is an integer
8. .isalnum() : returns true if every character in the string is an alphabet or an integer
9. .isspace() : returns true if the entire string is a whitespace
10. .islower() : returns true if every character is alphabet and is in lowercase
11. .isupper() : returns true if every character is alphabet and is in uppercase
12. .istitle() : returns true if every character is alphabet and each word starts with uppercase letter.

13. .startswith(s) : returns true if the string starts with given substring argument (s)
14. .endswith(s) : returns true if the string ends with given substring argument (s)
15. .find(s) : returns starting index if the given substring exists in the main string if substring doesn't exit then it returns -1
16.  .rfind(s) : returns the starting index of the given substring in the last occurance
17. .count(s) : retuns the count of number of time the substring appeared in the string.

18. .strip() : removes the white spaces at beginning and ending of the string and returns a new string.
19. .lstrip() : removes the white spaces at beginning of the string and returns a new string.
20. .rstrip() : removes the white spaces at ending of the string and returns a new string.
21. replace(s1, s2) : replaces the s1 with s2 and returns a new string

22. .split(e) : splits the string at "e" in the string and returns a list
23. .join(listname) : makes the list into string
"""

string = "pYthoN pythON "

print(f"Lower case : {string.lower()}")
print(f"Upper case : {string.upper()}")
print(f"Capitalise : {string.capitalize()}")
print(f"title : {string.title()}")
print(f"Swapcase : {string.swapcase()}", end="\n\n")

print(f"isalpha : {string.isalpha()}")
print(f"isdigit : {string.isdigit()}")
print(f"isalnum : {string.isalnum()}")
print(f"isspace : {string.isspace()}")
print(f"islower : {string.islower()}")
print(f"isupper : {string.isupper()}")
print(f"istitle : {string.istitle()}", end="\n\n")

print(f"startswith(\"py\") : {string.startswith("py")}")
print(f"endswith(\"ON\") : {string.endswith("ON")}")
print(f"find(\"o\") : {string.find("o")}")
print(f"rfind(\"o\") : {string.rfind("o")}")
print(f"count(\"t\") : {string.count("t")}", end="\n\n")

print(f"lstrip : {string.lstrip()}")
print(f"rstrip : {string.rstrip()}")
print(f"replace(\" \",\"-\") : {string.replace(" ","-")}", end="\n\n")

print(f"split(\" \") : {string.split(" ")}")
print(f"join(list) : {"-".join(["python","language"])}")

"""
output : 

Lower case : python python 
Upper case : PYTHON PYTHON
Capitalise : Python python
title : Python Python
Swapcase : PyTHOn PYTHon

isalpha : False
isdigit : False
isalnum : False
isspace : False
islower : False
isupper : False
istitle : False

startswith("py") : False
endswith("ON") : False
find("o") : 4
rfind("o") : 4
count("t") : 2

lstrip : pYthoN pythON
rstrip : pYthoN pythON
replace(" ","-") : pYthoN-pythON-

split(" ") : ['pYthoN', 'pythON', '']
join(list) : python-language

"""