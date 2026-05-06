# First non-repeating character
s = "aabbcde"
# Output: c
def fist_non_repeating_char(string):
    no_dups = {}
    for ch in string:
        no_dups[ch] = no_dups.get(ch, 0)+1

    for ch in s:
        if no_dups[ch] == 1:
            return ch

print(fist_non_repeating_char(s))

# Most frequent character
s = "programming"
def most_freq_char(string):
    freq_map = {}
    for ch in string:
        freq_map[ch] = freq_map.get(ch, 0)+1
    return max(freq_map, key=freq_map.get)
print(most_freq_char(s))

# Anagram check
s1 = "listen"
s2 = "silent"
def is_anagram(string1, string2):
    return sorted(string1) == sorted(string2)
print(is_anagram(s1, s2))
        

# Remove all vowels
s = "hello world"
def remove_vowels(string):
    no_vowels = [ch for ch in string if ch.lower() not in "aeiou"]
    return "".join(no_vowels)
print(remove_vowels(s))

# Longest word
s = "I love programming in python"
def get_longest_word(string):
    long_word = ""
    for segment in string.split():
        if len(long_word) < len(segment):
            long_word = segment
    return long_word
print(get_longest_word(s))