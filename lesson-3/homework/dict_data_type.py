# 1. Get Value: Given a dictionary and a key, retrieve the associated value, considering what to return if the key doesn’t exist.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key: ")
value = my_dict.get(key, "Key not found")
print(value) 

# 2. Check Key: Given a dictionary and a key, check if the key is present in the dictionary.
my_dict = {'a': 1, 'b': 2, 'c': 3}
key = 'c'
if key in my_dict:
    print("The key is in the dictionary")
else:
    print("The key is not in the dictionary")

# 3. Count Keys: Determine the number of keys in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
num=len(my_dict.keys()) 
print(num)

# 4. Get All Keys: Create a list that contains all the keys in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3, 'd':4}
keys_list = list(my_dict.keys())
print(keys_list) 


# 5. Get All Values: Create a list that contains all the values in the dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
keys_list = list(my_dict.values())
print(keys_list)


# 6. Merge Dictionaries: Given two dictionaries, create a new dictionary that combines both.

my_dict = {'a': 1, 'b': 2, 'c': 3}
dict_2={'d':4,'f':5,'g':6}
my_dict.update(dict_2)
new_dict=my_dict
print(new_dict)

# 7. Remove Key: Given a dictionary and a key, remove the key if it exists, handling the case if it doesn’t.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key='c'
mess=my_dict.get(key,False)
if not mess:
    print("The key does not exist")
else:
    my_dict.pop(key) 
    print(my_dict)

# 8. Clear Dictionary: Create a new empty dictionary.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.clear()
print(my_dict)


# 9. Check if Dictionary is Empty: Determine if a dictionary has any elements.

my_dict = {'a': 1, 'b': 2, 'c': 3}
if len(my_dict)>0:
    print("It is not empty")
else:
    print("It is emoty")

# 10. Get Key-Value Pair: Given a dictionary and a key, retrieve the key-value pair if the key exists.

my_dict = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key: ")

if key in my_dict:
    print(f"The key-value pair is: ({key}, {my_dict[key]})")
else:
    print("The key does not exist in the dictionary")

# 11. Update Value: Given a dictionary, update the value for a specified key.

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.update({'b':4})
print(my_dict)


# 12. Count Value Occurrences: Given a dictionary, count how many times a specific value appears across the keys.

my_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': 3}
value = 3
count = list(my_dict.values()).count(value)
print(count)


# 13. Invert Dictionary: Given a dictionary, create a new dictionary that swaps keys and values.
dict1={'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': 3,'f':5}
new_dict={value:key for key,value in dict1.items()}
print(new_dict)  

# 14. Find Keys with Value: Given a dictionary and a value, create a list of all keys that have that value.

dict1={'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': 3,'f':5}
val=2
lst=list(key for key,value in dict1.items() if value==val) 
print(lst)


# 15. Create a Dictionary from Lists: Given two lists (one of keys and one of values), create a dictionary that pairs them.

lst1=['a','b','c']
lst2=[1,2,3]

new_dic=dict(zip(lst1,lst2))
print(new_dic)

# 16. Check for Nested Dictionaries: Given a dictionary, check if any values are also dictionaries.

my_dict = {'a': 3, 'b': 2, 'c': 3, 'd': 2, 'e': {2:4}}
lst=list(filter(lambda x: type(x)==dict, my_dict.values()))
if lst:
    print("Yes")
else:
    print("No")

# 17. Get Nested Value: Given a nested dictionary, retrieve a value from within one of the inner dictionaries.

d={'s':3,'r':4,'t':5}
keys=['s','r','t']
current = d
for key in keys:
    if isinstance(current, dict) and key in current:
        current = current[key] 
print(current)  

# 18. Create Default Dictionary: Create a dictionary that provides a default value for missing keys.

from collections import defaultdict
default_dict = defaultdict(lambda: 0)

default_dict["a"] = 10  
print(default_dict["a"])
print(default_dict["b"]) 

# 19. Count Unique Values: Given a dictionary, determine the number of unique values it contains.

dict1={'s':3,'r':4,'t':5}
print(len(set(dict1.values())))


# 20. Sort Dictionary by Key: Create a new dictionary sorted by keys.

old_dict={'s':3,'r':4,'t':5,'a':4,'f':6}
new_dict=dict(sorted(old_dict.items()))
print(new_dict) 

# 21. Sort Dictionary by Value: Create a new dictionary sorted by values.

my_dict={'s':3,'r':4,'t':5,'a':4,'f':6}
new_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print(new_dict) 

# 22. Filter by Value: Given a dictionary, create a new dictionary that only includes items with values that meet a certain condition.

my_dict={'s':3,'r':4,'t':5,'a':4,'f':6}
new_dct=dict(filter(lambda x: x[1]%2==0, my_dict.items(),))
print(new_dct)

# 23. Check for Common Keys: Given two dictionaries, check if they have any keys in common.
dict1={'s':3,'r':4,'t':5,'a':4,'f':6}
dict2={'d':3,'r':4,'g':5,'a':4,'f':6}
if dict1.keys() in dict2.keys() or dict2.keys() in dict1.keys():
    print("Yes, they have common keys")
else:
    print("No they don't have common keys")

# 24. Create Dictionary from Tuple: Given a tuple of key-value pairs, create a dictionary from it.

tup = (('a', 1), ('b', 2), ('c', 3))
dct=dict(tup)
print(dct)


# 25. Get the First Key-Value Pair: Retrieve the first key-value pair from a dictionary.
dict2={'d':3,'r':4,'g':5,'a':4,'f':6}
lst=list(dict2.items())
print(lst[0]) 