# Dictionary = key → value mapping
my_dict = {
    "name": "siva",
    "roll": "b5"
}

# Accessing
print(my_dict["name"]) # error if key missing
print(my_dict.get("name")) # safe (returns None if missing)

# Add/Update
my_dict["college"] = "sistk" # adding
my_dict["roll"] = "234e1a33b5" # updating
my_dict.update({"subject": "python"})
print(my_dict)

# Delete
del my_dict["college"] # error if not exists
my_dict.pop("address", None) # safe
print(my_dict)

# LOOPING
# looping through keys
for k in my_dict:
    print(k, end=", ")

# looping through values
for v in my_dict.values():
    print(v, end=", ")
print("\n")

# looping through keys and values
for k, v in my_dict.items():
    print(k, "-", v)

"""
NOTE:
my_dict.keys() - return keys[]
my_dict.values() - return values[]
my_dict.items() - return key, value pairs [(k, v)]
"""

# setdefault method - it returns the reference to original dict
d={}
d.setdefault("a", 0) # default value
print(d["a"])