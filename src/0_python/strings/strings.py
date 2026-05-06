"""
Strings:
    - Immutable
    - Indexed
"""

# String Methods
# strip (remove spaces)
s = "    hello"
print(s.strip())

# lower/upper
s = "HeLLo"
print(s.lower())  
print(s.upper())

# split (splits string into a list)
s = "hello world"
words = s.split()
print(words)   

# "separator".join(list)
words = ["hello", "world"]
print("-".join(words))   

# replace
s = "hello world"
print(s.replace("world", "python"))

# find/in
print("hello" in s)    
print(s.find("lo")) 

