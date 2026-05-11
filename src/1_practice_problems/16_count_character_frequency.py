# Count how many times each character appears in a string.

def char_freq(string):
    freq_map = {}

    for ch in string:
        freq_map[ch] = freq_map.get(ch, 0) + 1
    
    return freq_map

print(char_freq("sivananda"))
