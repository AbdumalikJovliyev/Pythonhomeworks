# ### Task 1

# Write a script called temperature.py that defines two functions:

# 1. _convert_cel_to_far()_ which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:
#    _F = C \* 9/5 + 32_
# 2. _convert_far_to_cel()_ which take one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula:
#    _C = (F - 32) \* 5/9_

# The script should first prompt the user to enter a temperature in degrees Fahrenheit and then display the temperature converted to Celsius.
# Then prompt the user to enter a temperature in degrees Celsius and display the temperature converted to Fahrenheit. All converted temperatures should be rounded to 2 decimal places.

# Here’s a sample run of the program:

# ```
# Enter a temperature in degrees F: 72
# 72 degrees F = 22.22 degrees C

# Enter a temperature in degrees C: 37
# 37 degrees C = 98.60 degrees F

def convert_cel_to_far(Celsius):     
    Farenheit = Celsius * 9/5 + 32
    return round(Farenheit, 2)

def convert_far_to_cel(Farenheit):
    Celsius = (Farenheit - 32) * 5/9
    return round(Celsius, 2)

temp_farenheit = float(input("Enter a temperature in degrees F: "))
print(f"{temp_farenheit} degrees F = {convert_far_to_cel(temp_farenheit)} degrees C")
temp_celsius = float(input("Enter a temperature in degrees C: "))
print(f"{temp_celsius} degrees C = {convert_cel_to_far(temp_celsius)} degrees F")



# ### Task 2
# In this challenge, you will write a program called invest.py that tracks the growing amount of an investment over time.
# An initial deposit, called the principal amount, is made. Each year, the amount increases by a fixed percentage, called the annual rate of return.
# For example, a principal amount of \$100 with an annual rate of return of 5% increases the first year by \$5. The second year, the increase is 5% of the new amount \$105, which is \$5.25.
# Write a function called invest with three parameters: the principal amount, the annual rate of return, and the number of years to calculate. The function signature might look something like this:

# ```python
# def invest(amount, rate, years):
# ```
# The function then prints out the amount of the investment, rounded to 2 decimal places, at the end of each year for the specified number of years.

# For example, calling _invest(100, .05, 4)_ should print the following:
# year 1: $105.00
# year 2: $110.25
# year 3: $115.76
# year 4: $121.55
# To finish the program, prompt the user to enter an initial amount, an annual percentage rate, and a number of years. Then call invest() to display the calculations for the values entered by the user.

def invest(amount,rate,years): 
    for i in range(1,years+1):
        amount=round((amount+amount*rate),2)
        print(f"Year {i}: {amount}") 

init_amount=float(input("Enter the initial amount: ")) 
percent_rate=float(input("Enter annual percentage rate: "))
num_years=int(input("Enter the number of years: "))
invest(init_amount,percent_rate,num_years)


# ### Task 3
# A factor of a positive integer n is any positive integer less than or equal to n that divides n with no remainder.
# For example, 3 is a factor of 12 because 12 divided by 3 is 4, with no remainder. However, 5 is not a factor of 12 because 5 goes into 12 twice with a remainder of 2.
# Write a script factors.py that asks the user to input a positive integer and then prints out the factors of that number. Here’s a sample run of the program with output:

# ```
# Enter a positive integer: 12
# 1 is a factor of 12
# 2 is a factor of 12
# 3 is a factor of 12
# 4 is a factor of 12
# 6 is a factor of 12
# 12 is a factor of 12
# ```

def factors(num):
    integers=[]
    for i in range(1,num+1):
        if num%i==0:
            integers.append(i)
    for j in integers:
        print(f"{j} is a factor of {num}")
    
number=int(input("Enter the number: "))
factors(number)



# ### Task 4

# Write a program that contains the following lists of lists:
# universities = [
#     ['California Institute of Technology', 2175, 37704],
#     ['Harvard', 19627, 39849],
#     ['Massachusetts Institute of Technology', 10566, 40732],
#     ['Princeton', 7802, 37000],
#     ['Rice', 5879, 35551],
#     ['Stanford', 19535, 40569],
#     ['Yale', 11701, 40500]]

# Define a function, _enrollment_stats()_, that akes, as an input, a list of lists where each individual list contains three elements: (a) the name of a university, (b) the total number of enrolled students, and (c) the annual tuition fees.
# _enrollment_stats()_ should return two lists: the first containing all of the student enrollment values and the second containing all of the tuition fees.
# Next, define a _mean()_ and a _median()_ function. Both functions should take a single list as an argument and return the mean and median of the values in each list.
# Using universities, _enrollment_stats()_, _mean()_, and _median()_, calculate the total number of students, the total tuition, the mean and median of the number of students, and the mean and median tuition values.
# Finally, output all values, and format the output so that it looks like this:

# ```
# ******************************
# Total students: 77,285
# Total tuition: $ 271,905

# Student mean: 11,040.71
# Student median: 10,566

# Tuition mean: $ 38,843.57
# Tuition median: $ 39,849
# ******************************
# ```

nested_list =[]
total_students=[] 
tuition_fees=[]

def enrollment_status():
    num=int(input("Number of respondents to fill the list: ")) 

    for i in range(num):

        string_value = input(f"Enter a string for list {i+1}: ")
        int_value = int(input(f"Enter an integer for list {i+1}: "))
        float_value = float(input(f"Enter a float for list {i+1}: "))

        nested_list.append([string_value, int_value, float_value])
        total_students.append(int_value)
        tuition_fees.append(float_value)

    return total_students, tuition_fees 

#main code starts running: 
enrollment_status()

#other functions to find mean and median
def mean(lst):
    find_mean=sum(lst)/len(lst)
    return find_mean

# got some errors in median part, and got None for that part in the terminal section. 

def median(lst):
    lst.sort()
    if len(lst) % 2 == 0:
        mid1 = len(lst) // 2
        mid2 = mid1 - 1
        find_median = (lst[mid1] + lst[mid2]) / 2
    else:
        find_median = lst[len(lst) // 2]
    return find_median

def total(lst1, lst2):
    return f"Total students: {sum(lst1)}", f"Total tuition: {sum(lst2)}"

# Outputting the final values
total_students, total_tuition = total(total_students, tuition_fees)
print(total_students)
print(total_tuition)
print(f"Student mean: {round(mean(total_students), 2)}")
print(f"Student median: {round(median(total_students), 2)}")
print(f"Tuition mean: {round(mean(tuition_fees), 2)}")
print(f"Tuition median: {round(median(tuition_fees), 2)}")



# ### Task 5
# Define a function `is_prime(n)` which returns `True` if the given $n$ ($n$ > 0) is _prime number_, otherwise returns `False`.

import math
def is_prime(n):
    if n < 2:
        return False
    if n in (2, 3): 
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    end = int(math.sqrt(n))
    for i in range(5, end+ 1, 2):
        if n % i == 0:
            return False
    return True

number=int(input("Enter the number for checking: Is it prime or not: "))
print(is_prime(number))
