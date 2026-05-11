# Count how many vowels are present in a given string.

def vowels_count(string):
    vowels = "aeiouAEIOU"
    count = 0

    for ch in string:
        if ch in vowels:
            count += 1 
    
    return count

print(vowels_count("siva"))
print(vowels_count("sivananda"))
print(vowels_count("sivananda reddy"))