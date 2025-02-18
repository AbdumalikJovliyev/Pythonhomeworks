# 1. Count Occurrences: Given a tuple and an element, find how many times the element appears in the tuple.

def count_occs(tup, elmt):
    return tup.count(elmt)

# 2. Max Element: From a given tuple, determine the largest element.

def find_max(tup):
    return max(tup)

# 3. Min Element: From a given tuple, determine the smallest element.

def find_min(tup):
    return min(tup)

# 4. Check Element: Given a tuple and an element, check if the element is present in the tuple.

def check(tup,elm):
    if elm in tup:
        print("Element is in the tuple")
    else:
        print("Element is not in the tuple")

# 5. First Element: Access the first element of a tuple, considering what to return if the tuple is empty.

def work(tup):
    if not tup:
        first=tup[0]
    else:
        print("The tuple is empty")

# 6. Last Element: Access the last element of a tuple, considering what to return if the tuple is empty.

def work(tup):
    if not tup:
        first=tup[-1]
    else:
        print("The tuple is empty")

# 7. Tuple Length: Determine the number of elements in the tuple.

def length(tup):
    return len(tup)

# 8. Slice Tuple: Create a new tuple that contains only the first three elements of the original tuple.

def work(tup):
    new_tup=tup[:3]
    return new_tup

# 9. Concatenate Tuples: Given two tuples, create a new tuple that combines both.

def conct(t1,t2):
    result = t1 + t2
    return result 

# 10. Check if Tuple is Empty: Determine if a tuple has any elements.

def work(tup):
    if tup:
        return True
    else:
        return False   

# 11. Get All Indices of Element: Given a tuple and an element, find all the indices of that element in the tuple.

def get_indices(tup, elmt):
    for i in range(len(tup)):
        if tup[i] == elmt:
            print(i)

# 12. Find Second Largest: From a given tuple, find the second largest element.

def sc_lgst(tup):
    tup=list(tup)
    tup.sort()
    return tup[-2]

# 13. Find Second Smallest: From a given tuple, find the second smallest element.

def sc_smlst(tup):
    tup=list(tup)
    tup.sort()
    return tup[1] 
 
# 14. Create a Single Element Tuple: Create a tuple that contains a single specified element.

tup=(1,)
print(tup, type(tup))

# 15. Convert List to Tuple: Given a list, create a tuple containing the same elements.

def convert(lst):
    tup=tuple(lst)
    return tup 

# 16. Check if Tuple is Sorted: Determine if the tuple is sorted in ascending order and return a boolean.

def is_sorted(tup):
    tup=list(tup)
    return tup == sorted(tup)

# 17. Find Maximum of Subtuple: Given a tuple, find the maximum element of a specified subtuple.

def max_sub(tup, start, end):
    return max(tup[start:end]) 

nums = (3, 7, 2, 9, 11, 4, 6)
start = int(input("Enter start index: ")) 
end = int(input("Enter end index: "))     

if 0 <= start < end <= len(nums): 
    print("Maximum element in subtuple:", max_sub(nums, start, end))
else:
    print("Invalid indices! Please enter a valid range.")

# 18. Find Minimum of Subtuple: Given a tuple, find the minimum element of a specified subtuple.

def min_sub(tup, start, end):
    return min(tup[start:end]) 

nums = (3, 7, 2, 9, 11, 4, 6)
start = int(input("Enter start index: ")) 
end = int(input("Enter end index: "))     

if 0 <= start < end <= len(nums): 
    print("Minimum element in subtuple:", max_sub(nums, start, end))
else:
    print("Invalid indices! Please enter a valid range.") 

# 19. Remove Element by Value: Given a tuple and an element, create a new tuple that removes the first occurrence of that element.

def rmv(tup,elm):
    new_tup=list(tup)
    new_tup.remove(elm) 
    return tuple(new_tup) 

# 20. Create Nested Tuple: Create a new tuple that contains subtuples, where each subtuple contains specified elements from the original tuple.

def create_nested(tup, start, end):
    return (tup[start:end], tup[end:]) 

# 21. Repeat Elements: Given a tuple and a number, create a new tuple where each element is repeated that number of times.

def rpt(tup,num):
    return tup*num

# 22. Create Range Tuple: Create a tuple of numbers in a specified range (e.g., from 1 to 10).

def create_tup(st,end):
    tup=tuple(range(st,end+1))
    return tup 

# 23. Reverse Tuple: Create a new tuple that contains the elements of the original tuple in reverse order.
tup=(1,2,3,4,5)
def reverse(tup):
    lst=list(tup)
    lst.reverse()
    return tuple(lst)
print(reverse(tup))

# 24. Check Palindrome: Given a tuple, check if the tuple is a palindrome (reads the same forwards and backwards).

def is_palindrome(tup):
    lst=list(tup) 
    return lst == list(reversed(lst))

# 25. Get Unique Elements: Given a tuple, create a new tuple that contains only the unique elements while maintaining the original order.

tup=(1,2,3,4,5,2,34,1,2,3,4,56,6)
def unique_els(tup):
    new_tup=[]
    for i in tup:
        if i not in new_tup:
            new_tup.append(i)
    new_tup=tuple(new_tup)
    return f"This is unique tuple: {new_tup}", f"This is original tuple: {tup}"
print(unique_els(tup))  
