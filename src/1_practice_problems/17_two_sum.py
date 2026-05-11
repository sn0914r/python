"""
Given a list of integers and a target number, find two numbers in the list that add up to the target and return
their indices.
"""
nums = [2, 7, 11, 15]
target = 22

def two_sum(li, target):
    for ind, elem in enumerate(li):
        ind_in = ind + 1
        for elem_in in li[ind_in:]:
            total = elem_in + elem
            if total == target:
                return ind, ind_in
            ind_in += 1
    
    return "Not found"

print(two_sum(nums, target))