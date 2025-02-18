# 1. Count Occurrences: Given a list and an element, find how many times the element appears in the list.

def count_occurrences(lst, element):
    num=lst.count(element)
    return num

# 2. Sum of Elements: Given a list of numbers, calculate the total of all the elements.

def sum_elm(lst):
    return sum(lst)

# 3. Max Element: From a given list, determine the largest element.

def lrgt(lst):
    return max(lst)

# 4. Min Element: From a given list, determine the smallest element.
def mnm(lst):
    return min(lst)

# 5. Check Element: Given a list and an element, check if the element is present in the list.

def lrgt(lst,elm):
    if elm in lst:
        print("Element is in the list")
    else:
        print("Element is not in the list")

# 6. First Element: Access the first element of a list, considering what to return if the list is empty.

def work(lst):
    if not lst:
        first=lst[0]
    else:
        print("The list is empty")

# 7. Last Element: Access the last element of a list, considering what to return if the list is empty.

def work(lst):
    if not lst:
        last=lst[-1]
    else:
        print("The list is empty")

# 8. Slice List: Create a new list that contains only the first three elements of the original list.

def work(lst):
    new_lst=lst[:3]
    return new_lst

# 9. Reverse List: Create a new list that contains the elements of the original list in reverse order.

def reverse_list(lst):
    return lst[::-1]

# 10. Sort List: Create a new list that contains the elements of the original list in sorted order.

def sort_list(lst):
    new_lst=lst.sort()
    return new_lst

# 11. Remove Duplicates: Given a list, create a new list that contains only unique elements from the original list.

def rmv_dups(lst): 
    new_lst = list(set(lst))
    return new_lst 


# 12. Insert Element: Given a list and an element, insert the element at a specified index.

index=int(input("Please, enter the index for inserting"))
def inserting(lst,lmnt):
    lst.insert(index,lmnt)
    return lst

# 13. Index of Element: Given a list and an element, find the index of the first occurrence of the element.

def work(lst,lmnt):
    return lst.index(lmnt,0)

# 14. Check for Empty List: Determine if a list is empty and return a boolean.

def work(lst):
    if lst:
        return True
    else:
        return False 

# 15. Count Even Numbers: Given a list of integers, count how many of them are even.

def work(lst):
    c=len(list(filter(lambda x: x%2==0,lst)))
    return c

# 16. Count Odd Numbers: Given a list of integers, count how many of them are odd.

def work(lst):
    c=len(list(filter(lambda x: x%2==1,lst)))
    return c

# 17. Concatenate Lists: Given two lists, create a new list that combines both lists.

def con_lists(lst1,lst2):
    lst1.extend(lst2)
    return lst1 

# 18. Find Sublist: Given a list and a sublist, check if the sublist exists within the list.

def sublist(lst,s_lst):
    if s_lst in lst:
        print("Yes, it exists")
    else:
        print("No, it does not exist")


# 19. Replace Element: Given a list, replace the first occurrence of a specified element with another element.

def rplct(lst, tgt, rpct):
    for i in range(len(lst)):  
        if lst[i] == tgt:
            lst[i] = rpct  
            break 
    return lst

lst = [1, 2.5, "hello", True, 5, "world", False]
while True:
    tgt = input("Enter the element to replace: ") 
    if tgt in lst:
        break 
    print("Element not found in the list. Try again.")

rpct = input("Enter the new element: ")
print("Updated list:", rplct(lst, tgt, rpct))


# 20. Find Second Largest: From a given list, find the second largest element.

lst=[1,21,2,3,34,4,5,3,4,24,23,4,134]
lst.sort()
print(lst[-2])


# 21. Find Second Smallest: From a given list, find the second smallest element.

lst=[1,21,2,3,34,4,5,3,4,24,23,4,134]
lst.sort()
print(lst[1])


# 22. Filter Even Numbers: Given a list of integers, create a new list that contains only the even numbers.

def filter(lst):
    even_nums=list(filter(lambda x: x % 2 == 0, lst))
    return even_nums


# 23. Filter Odd Numbers: Given a list of integers, create a new list that contains only the odd numbers.

def filter(lst):
    odd_nums=list(filter(lambda x: x % 2 == 1, lst))
    return odd_nums


# 24. List Length: Determine the number of elements in the list.

def length(lst):
    return len(lst)
   
# 25. Create a Copy: Create a new list that is a copy of the original list.

def cpy(lst):
    new_l=lst.copy()
    return new_l


# 26. Get Middle Element: Given a list, find the middle element. If the list has an even number of elements, return the two middle elements.

def middle(lst):
    if len(lst)%2==0:
        return lst[len(lst)//2-1], lst[len(lst)//2]
    else:
        return lst[len(lst)//2]


# 27. Find Maximum of Sublist: Given a list, find the maximum element of a specified sublist.

def max_sub(lst, start, end):
    return max(lst[start:end]) 

nums = [3, 7, 2, 9, 11, 4, 6]
start = int(input("Enter start index: ")) 
end = int(input("Enter end index: "))     

if 0 <= start < end <= len(nums): 
    print("Maximum element in sublist:", max_sub(nums, start, end))
else:
    print("Invalid indices! Please enter a valid range.")


# 28. Find Minimum of Sublist: Given a list, find the minimum element of a specified sublist.

def min_sub(lst, start, end):
    return min(lst[start:end]) 

nums = [3, 7, 2, 9, 11, 4, 6]
start = int(input("Enter start index: ")) 
end = int(input("Enter end index: "))     

if 0 <= start < end <= len(nums): 
    print("Maximum element in sublist:", min_sub(nums, start, end))
else:
    print("Invalid indices! Please enter a valid range.")


# 29. Remove Element by Index: Given a list and an index, remove the element at that index if it exists.

lst=[2,4,3,2,1,3,4]
def rmv(lst,index):
    lst.remove(lst[index])
    return lst

index=int(input("enter the index of the element: "))
if index<=len(lst)-1:
    print(rmv(lst,index))
else:
    print("It does not exist in the list")

# 30. Check if List is Sorted: Determine if the list is sorted in ascending order and return a boolean.

def is_sorted(lst):
    return lst == sorted(lst)


# 31. Repeat Elements: Given a list and a number, create a new list where each element is repeated that number of times.

def rpt(lst,num):
    return lst*num


# 32. Merge and Sort: Given two lists, create a new sorted list that merges both lists.

lst1=[2,1,32,3,5,4]
lst2=[2,3,6,2,3,5,45]
def merge_sort(lst1,lst2):
    lst1.extend(lst2)
    lst1.sort()
    return lst1
print(merge_sort(lst1,lst2))


# 33. Find All Indices: Given a list and an element, find all the indices of that element in the list.

def find_inds(lst,elmt):
    return list(filter(lambda i: lst[i] == elmt, range(len(lst))))
   
# 34. Rotate List: Given a list, create a new list that is a rotated version of the original list (shift elements to the right).

def reverse(lst):
    lst.reverse()
    return lst 
 
# 35. Create Range List: Create a list of numbers in a specified range (e.g., from 1 to 10).

st=1
end=10
def create_lst(st,end):
    new=list(range(st,end+1))
    return new 
print(create_lst(st,end))


# 36. Sum of Positive Numbers: Given a list of numbers, calculate the sum of all positive numbers.

def sum_pos(lst):
    return sum(list(filter(lambda x: x>0, lst)))


# 37. Sum of Negative Numbers: Given a list of numbers, calculate the sum of all negative numbers.

def sum_neg(lst):
    return sum(list(filter(lambda x: x<0, lst)))

# 38. Check Palindrome: Given a list, check if the list is a palindrome (reads the same forwards and backwards).

def is_palindrome(lst):
    return lst == list(reversed(lst)) 


# 39. Create Nested List: Create a new list that contains sublists, where each sublist contains a specified number of elements from the original list.

def create_nstd(lst, size):
    new=[]
    for i in range(0,len(lst),size):
        new.append(lst[i:i+size])
    return new
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = 3
print(create_nstd(numbers, size)) 

# 40. Get Unique Elements in Order: Given a list, create a new list that contains unique elements while maintaining the original order.

def unique_order(lst):
    new_lst=[]
    for i in lst:
        if i not in new_lst:
            new_lst.append(i)
    return new_lst 