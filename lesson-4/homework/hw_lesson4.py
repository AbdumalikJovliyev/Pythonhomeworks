# 1. Return uncommon elements of lists. Order of elements does not matter.

# input:
#     list1 = [1, 1, 2]
#     list2 = [2, 3, 4]
# output: [1, 1, 3, 4]
# input:
#     list1 = [1, 2, 3]
#     list2 = [4, 5, 6]
# output: [1, 2, 3, 4, 5, 6]
# input:
#     list1 = [1, 1, 2, 3, 4, 2]
#     list2 = [1, 3, 4, 5]
# output: [2, 2, 5]

list1=[1,1,2]
list2=[2,3,4]
for i in list1:
    for j in list2:
        if i==j:
            list1.remove(i)
            list2.remove(j)
list1.extend(list2)
print(list1) 


# 2. Print the square of each number which is less than n on a separate line.

# input: n = 5
# output:
#     1
#     4
#     9
#     16

n=int(input("Enter the number "))
for i in range(1,n):
    print(5*" ", i**2)


# 3. txt nomli string saqlovchi o'zgaruvchi berilgan. txtdagi har uchinchi belgidan keyin pastgi chiziqcha (underscore) qo'yilsin.
# Agar belgi unli harf yoki orqasidan ostki chiziqcha qo'yilgan harf bo'lsa, ostki chiziqcha keyingi harfdan keyin qo'yilsin. 
# Agar belgi satrdagi oxirgi belgi bo'lsa chiziqcha qo'yilmasin.

# input: hello
# output: hel_lo
# input: assalom
# output: ass_alom
# input: abcabcdabcdeabcdefabcdefg
# output: abc_abcd_abcdeab_cdef_abcdefg

txt = str(input("Enter the string: "))
not_allowed = "aeiouAEIOU"
counter=0
result=''
for i in range(len(txt)):
    counter+=1
    result+=txt[i]
    if i!=len(txt)-1 and counter>=3 and txt[i] not in not_allowed:
        not_allowed+=txt[i]
        result+="_"
        counter=0
print(result) 


# 4. Number Guessing Game: Create a simple number guessing game.

# The computer randomly selects a number between 1 and 100.
# If the guess is high, print "Too high!".
# If the guess is low, print "Too low!".
# If they guess correctly, print "You guessed it right!" and exit the loop.
# The player has 10 attempts to guess it. If the player can not find the correct number in 10 attempts, print "You lost. Want to play again? ".
# If the player types one of 'Y', 'YES', 'y', 'yes', 'ok' then start the game from the beginning.
# Hint: Use Python’s random.randint() to generate the number.

import random 
while True:
    rand=random.randint(1,100)
    attempts=10
    print("\nTry to find the number (from 1 to 100)! You have 10 attempts.")

    while attempts>0:
        guess=int(input("Enter your guess: "))
        if guess>rand:
            print("Too high ")
        elif guess<rand:
            print("Too low ")
        else:
            print("You guessed it right!")
            exit()
        attempts-=1 

    if attempts == 0:
        print("You lost. Want to play again? ")
        ans = input().strip().lower()
        if ans not in ['y', 'yes', 'ok']:
            break 


# 5. Password Checker Task: Create a simple password checker.

# Ask the user to enter a password.
# If the password is shorter than 8 characters, print "Password is too short."
# If the password doesn’t contain at least one uppercase letter, print "Password must contain an uppercase letter.".
# If the password meets both criteria, print "Password is strong."

password=input("Enter the password: ")
counter=0
for i in password:
    if i==i.upper():
        counter+=1
if len(password)<8:
        print("Password is too short")
elif counter<1:
    print("Password must contain an uppercase letter.")
else:
    print("Password is strong")


# 6. Prime Numbers Task: Write a Python program that prints all prime numbers between 1 and 100.

# A prime number is a number greater than 1 that is not divisible by any number other than 1 and itself. Use nested loops to check divisibility.

prime_list=[]
for nums in range(1, 100):
    for j in range(2, int(nums/2)+1):
        if nums % j == 0:
            break
        else:
            prime_list.append(nums)
print(*set(prime_list)) 


# Bonus Challenge
# Task: Create a simple text-based Rock, Paper, Scissors game where the player plays against the computer.

# The computer randomly chooses rock, paper, or scissors using random.choice().
# The player enters their choice.
# Display the winner and keep track of scores for the player and the computer.
# First to 5 points wins the match.
import random

ply = 0
comp = 0

while ply < 5 and comp < 5:
    choice = random.choice(["rock", "paper", "scissors"])
    player = input("Enter your choice (rock, paper, or scissors): ").strip().lower()

    if player not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    if choice == player:
        print("It's a tie!")
    elif (choice == "rock" and player == "paper") or (choice == "paper" and player == "scissors") or (choice == "scissors" and player == "rock"):
        print("Player won this round!")
        ply += 1
    else:
        print("Computer won this round!")
        comp += 1

    print(f"Score - Player: {ply}, Computer: {comp}")

if ply == 5:
    print("Player won the game!")
else:
    print("Computer won the game!")