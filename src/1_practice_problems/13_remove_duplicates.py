# Remove duplicate values from a list while preserving the original order.

dups_list = [1, 3, 4, 5, 5, 5, 6, 7, 7]

# 1. using sets 
def remove_dups_1(li):
    return list(set(li))

print(remove_dups_1(dups_list))

# 2. using loop
def remove_dups_2(li):
    no_dups = []

    for i in li:
        if i not in no_dups:
            no_dups.append(i)
    
    return no_dups


print(remove_dups_2(dups_list))