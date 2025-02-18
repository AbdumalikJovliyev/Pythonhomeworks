# 1. Union of Sets: Given two sets, create a new set that contains all unique elements from both sets.
s1={1,2,3,4}
s2={3,2,4,2,6}
s1.union(s2)

# 2. Intersection of Sets: Given two sets, create a new set that contains elements common to both sets.
s1={1,2,3,4}
s2={3,2,4,2,6}
s1.intersection(s2)

# 3. Difference of Sets: Given two sets, create a new set with elements from the first set that are not in the second.
s1={1,2,3,4}
s2={3,2,4,2,6}
new_set=s1.difference(s2)

# 4. Check Subset: Given two sets, check if one set is a subset of the other.
s1={1,2,3,4}
s2={3,2,4,2,1,6}
if s1.issubset(s2) or s2.issubset(s1):
    print("YES")
else:
    print("NO")

# 5. Check Element: Given a set and an element, check if the element exists in the set.
st={3,2,4,2,1,6}
elmt=input("Enter the element: ")
if elmt in st:
    print("YES, It exists in the set")
else:
    print("NO, It does not exist in the set")

# 6. Set Length: Determine the number of unique elements in a set.
st={'a','b','d','c'}
length=len(st)
print(length)

# 7. Convert List to Set: Given a list, create a new set that contains only the unique elements from that list.

lst=[2,3,4,5,3,2,4]
st=set(lst)
print(st,lst)

# 8. Remove Element: Given a set and an element, remove the element if it exists.

st = {'fd', 2, 4, "world", True, 2.3}
elmt = input("Enter the element: ")
try:
    elmt = eval(elmt)
except:
    pass 

if elmt in st:
    st.remove(elmt)
print(st)

# 9. Clear Set: Create a new empty set from an existing set.

st={1,2,3,4,5}
new_st=st.clear()
print(new_st)

# 10. Check if Set is Empty: Determine if a set has any elements.

st={}
if st:
    print("Set is not empty")
else:
    print("Set is empty")


# 11. Symmetric Difference: Given two sets, create a new set that contains elements that are in either set but not in both.

s1={2,3,5,7,11,13}
s2={3,5,7,9,11}
new_set=s1.symmetric_difference(s2)
print(new_set) 


# 12. Add Element: Given a set and an element, add the element to the set if it is not already present.

st={2,3,4,5,6,7}
elmt=int(input("Enter the element: "))
if elmt not in st:
    st.add(elmt)
print(st)


# 13. Pop Element: Given a set, remove and return an arbitrary element from the set.

st={2,3,4,5,6,7}
popped_el=st.pop()
print(popped_el)
print(st)

# 14. Find Maximum: From a given set of numbers, find the maximum element.

st={2,3,4,5,6,7}
print(max(st))

# 15. Find Minimum: From a given set of numbers, find the minimum element.
st={2,3,4,5,6,7}
print(min(st))

# 16. Filter Even Numbers: Given a set of integers, create a new set that contains only the even numbers.
st={2,3,4,5,6,7,8,9,10,11}
even_nums=set(filter(lambda x: x%2==0, st))
print(even_nums)

# 17. Filter Odd Numbers: Given a set of integers, create a new set that contains only the odd numbers.

st={1,2,3,4,5,6,7,8,9,10,11}
odd_nums=set(filter(lambda x: x%2==1, st))
print(odd_nums)

# 18. Create a Set of a Range: Create a set of numbers in a specified range (e.g., from 1 to 10).

start=int(input("Enter the starting value "))
end=int(input("Enter the ending value "))
nums=set(range(start,end+1))
print(nums)

# 19. Merge and Deduplicate: Given two lists, create a new set that merges both lists and removes duplicates.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
merged_set = set(list1).union(set(list2))
print(merged_set)

# 20. Check Disjoint Sets: Given two sets, check if they have no elements in common.

st1={1,3,5,7,9}
st2={2,4,6,8,10}
if st1.isdisjoint(st2):
    print("NO elements in common")
else:
    print("They have elements in common")
 
# 21. Remove Duplicates from a List: Given a list, create a set from it to remove duplicates, then convert back to a list.

lst=[1,2,3,2,1,3,4,5,6,2,34,5,3,2,3,2]
lst=list(set(lst))
print(lst) 
 
# 22. Count Unique Elements: Given a list, determine the count of unique elements using a set.

lst=[1,2,3,2,1,3,4,5,6,2,34,5,3,2,3,2]
lst=set(lst)
print(len(lst))

# 23. Generate Random Set: Create a set with a specified number of random integers within a certain range.

import random

def generate_rn_set(size, start, end):
    return set(random.randint(start, end) for _ in range(size))

size = int(input("Enter the number of elements: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

random_set = generate_rn_set(size, start, end)
print("Generated Random Set:", random_set)
