#LISTS
"""
1. List is a non-primitive ds it means we can store multiple values under a single name.
2. to create a list we use square braces -> [].
3. lists are indexed so we can access the values using the index numbers.
"""

#characteristics
"""
1. Mutable
2. Ordered
3. Allows duplicates
4. Allows different types of data
5. Slicíng is possible
"""
# updating and accessing

list = [2, 3, 4]
print(list[0]) # accessing
list[0] = 1
print(list[0]) # updating

#methods
"""
1. append(val) : adds an elem at the end of the list.

2. insert(i, val) : adds 'val' at 'i' index.

3. remove(val) : removes 'val' from the list (only at the first occurance)

4. pop(i) : removes and returns the elemnt at index 'i' and removes last if no index value passed.

5. sort() : sorts the list in ascending order.

6. reverse() : reverses the list items.

7. count(val) : counts number of times 'val' repeated in the list.

8. index(val) : returns the index of val. (only first occurance)
"""
#example
list = [2, 3, 8, 6, 4, 31,1]
list.append(100) #[2,3,8,6,4,31,1,100]
list.insert(0, 200) #[200,2,3,8,6,4,31,1,100]
list.remove(4) # [200,2,3,8,6,31,1,100]
list.pop() # [200,2,3,8,6,31,1] & returns 100
list.sort() #[1,2,3,6,8,31,200]
list.reverse()#[200,31,8,6,3,2,1]
list.count(2) # returns 2
list.index(200)# returns 0

print(list) #output :[200,31,8,6,3,2,1]