#1. Create a program that takes a float number as input and rounds it to 2 decimal places.

t=float(input())
print(f"{t:.2f}")

#2. Write a Python file that asks for three numbers and outputs the largest and smallest.

a,b,c=map(float,input("Please enter three numbers: ").split())
largest=max(a,b,c)
smallest=min(a,b,c)
print(f"The largest number is {largest}")
print(f"The smallest number is {smallest}") 

#3. Create a program that converts kilometers to meters and centimeters.

km = float(input("Enter distance in kilometers: "))
met= km * 1000
cm = km * 100000 
print(f"{km} kilometers is equal to {met} meters or {cm} centimeters.")

#4. Write a program that takes two numbers and prints out the result of integer division and the remainder.

a,b=map(float,input("Enter two numbers: ").split())
div,r=divmod(a,b)
print(int(div),int(r))

#5. Make a program that converts a given Celsius temperature to Fahrenheit.

c=float(input("Temperature in Celsius: "))
print(f"{c} Celsius is equal to {c*(9/5)+32} Fahrenheit")

#6. Create a program that accepts a number and returns the last digit of that number.

num=float(input("Enter the number: "))
fn=num%10 
print(f"The last digit of {num} is {int(fn)}")

#7. Create a program that takes a number and checks if it’s even or not.

n=int(input("Number: "))
if n%2==0:
    print("It is even")
else: 
    print("It is not even")

