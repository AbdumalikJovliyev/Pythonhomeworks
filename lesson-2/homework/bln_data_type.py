# 1. Write a program that accepts a username and password and checks if both are not empty.
usr=input()
psw=input()
if usr and psw:
    print("They are not empty")
else: 
    print("They are empty")

# 2. Create a program that checks if two numbers are equal and outputs a message if they are.

a=int(input())
b=int(input())
if a == b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")

# 3. Write a program that checks if a number is positive and even.

n=int(input())
if n>0 and n%2==0:
    print("Yes")
else:
    print("No")

# 4. Write a program that takes three numbers and checks if all of them are different.

a,b,c=map(int,input().split())
if a != b and b != c and a != c:
    print("All numbers are different.")
else:
    print("Not all numbers are different.")

# 5. Create a program that accepts two strings and checks if they have the same length.

st1,st2=map(str,input().split())
if len(st1)==len(st2):
    print("They have sam length")
else:
    print("They have not same length")

# 6. Create a program that accepts a number and checks if it’s divisible by both 3 and 5.

n=int(input())
 if n % 3 == 0 and n % 5 == 0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

# 7. Write a program that checks if the sum of two numbers is greater than 50.

a=int(input())
b=int(input())
if a + b > 50:
    print("The sum is greater than 50.")
else:
    print("The sum is not greater than 50.")

# 8. Create a program that checks if a given number is between 10 and 20 (inclusive)

n=int(input())
if n>=10 and n<=20:
    print("YES")
else:
    print("NO")
    