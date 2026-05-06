# count frequency
nums = [1, 2, 2, 3, 3, 3]
# output: {1:1, 2:2, 3:3}
def count_freq(nums):
    freq_map = {}
    for i in nums:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1
    return freq_map


print(count_freq(nums))

# Count characters
s = "hello"
# Output: {'h':1, 'e':1, 'l':2, 'o':1}
print(count_freq(s))

# Word length map
words = ["apple", "banana"]
# output: {"apple":5, "banana":6}
def count_word_length(words):
    words_length = {}
    for i in words:
        if i not in words_length:
            words_length[i] = len(i)
    return words_length


print(count_word_length(words))

# Invert dictionary
d = {"a": 1, "b": 2}
# output: {1:"a", 2:"b"}
def invert_dict(dict):
    inv = {}
    for k, v in dict.items():
        inv[v] = k
    return inv

print(invert_dict(d))

# Group words by first letter
words = ["apple", "ant", "banana", "bat"]
"""
output:
{
 'a': ["apple", "ant"],
 'b': ["banana", "bat"]
}
"""
def group_words_by_first_letter(words):
    group = {}
    for word in words:
        if word[0] in group:
            group[word[0]].append(word)
        else:
            group[word[0]] = [word]
    return group

print(group_words_by_first_letter(words))

# Find max frequency element
nums = [1, 2, 2, 3, 3, 3]
# output: 3
def max_freq_elem(nums):
    freq_map = {}
    for i in nums:
        if i in freq_map:
            freq_map[i] += 1
        else:
            freq_map[i] = 1

    max_freq_eleme = max(freq_map, key=freq_map.get)
    return max_freq_eleme

print(max_freq_elem(nums))

# Merge two dicts
a = {"x": 1}
b = {"y": 2}
# output: {"x":1, "y":2}
merged_dict = a | b
print(merged_dict)

# Filter dict - Keep only values > 1
d = {"a": 1, "b": 2, "c": 3}
def filter_dict(dict, t=1):
    filtered = {}
    for k, v in dict.items():
        if v > t:
            filtered[k] = v
    return filtered

print(filter_dict(d))

# Count even/odd
nums = [1, 2, 3, 4]
# output: {"even":2, "odd":2}
def count_even_odd(nums):
    freq_map = {"even": 0, "odd": 0}
    for i in nums:
        if i % 2 == 0:
            freq_map["even"] += 1
        else:
            freq_map["odd"] += 1
    return freq_map

print(count_even_odd(nums))

#  Nested dict access
user = {"name": "Siva", "address": {"city": "Hyd"}}
# Get "Hyd"
print(user["address"]["city"])

# Store indices of the words
words = ["apple", "banana", "apple", "cherry", "banana"]
"""
output:
{
 "apple": [0, 2],
 "banana": [1, 4],
 "cherry": [3]
}
"""
def indices_map(words):
    freq_map = {}
    track_index = 0
    for word in words:
        if word in freq_map:
            freq_map[word].append(track_index)
        else: 
            freq_map[word] = [track_index]

        track_index+=1
    return freq_map
print(indices_map(words))

# Group by key (pattern)
words = ["apple", "banana", "apple", "cherry", "banana"]
"""
output:
{
 "apple": 2,
 "banana": 2,
 "cherry": 1
}
"""
def count_words(words):
    freq_map={}
    for word in words:
        freq_map[word] = freq_map.get(word, 0)+1
    return freq_map
print(count_words(words))

# Reverse grouping (Combine counting + grouping)
words = ["apple", "banana", "apple", "cherry", "banana"]
"""
{
 2: ["apple", "banana"],
 1: ["cherry"]
}
"""
def reverse_group(words):
    count_map={}
    inv_by_group={}
    for word in words:
        count_map[word] = count_map.get(word, 0)+1
    for k,v in count_map.items():
        inv_by_group.setdefault(v, []).append(k)
    return inv_by_group
print(reverse_group(words))