# 1. Create a program to ask name and year of birth from user and tell them their age.

name=input("Enter your name: ")
year=int(input("Enter your birth year: "))
print(f"{name} you are {2025-year} years old")


# 2. Extract car names from this text:

txt = 'LMaasleitbtui'
car1=txt[::2]
car2=txt[1::2]
print(car1, car2)
 
# 3. Write a Python program to:
#    - Take a string input from the user.
#    - Print the length of the string.
#    - Convert the string to uppercase and lowercase.

ln=str(input())
print(len(ln))
upp=ln.upper()
low=ln.lower()
print(upp, low)


# 4. Write a Python program to check if a given string is palindrome or not.
# > What is a Palindrome String? A string is called a palindrome if the reverse of the string is the same as the original one. Example: “madam”, “racecar”, “12321”.
pln=str(input())
if pln==pln[::-1]:
    print(f"Yes, {pln} is palindrome")
else: 
    print(f"No, {pln} is not palindrome")


# 5. Write a program that counts the number of vowels and consonants in a given string.

vr=str(input())
vowels=0
cnsts=0
for i in range(len(vr)):
    if vr[i].lower()=="a" or vr[i].lower()=="u" or vr[i].lower()=="e" or vr[i].lower()=="o" or vr[i].lower()=="i":
        vowels+=1
print(f"Number of vowels in {vr} is {vowels} \nNumber of consonants in {vr} is {len(vr)-vowels}")


# 6. Write a Python program to check if one string contains another.

str1=str(input())
str2=str(input())
if str1 in str2 or str2 in str1:
    print("YES")
else: 
    print("NO")


# 7. Ask the user to input a sentence and a word to replace. Replace that word with another word provided by the user.  
# Example:  
#    - Input sentence: "I love apples."  
#    - Replace: "apples"  
#    - With: "oranges"  
#    - Output: "I love oranges."

snt=str(input("Enter the sentence: "))
rpl=str(input("Which word do you want to replace: "))
nt=str(input("Enter the word for replacing: "))
print("This is the sentence after replacement", snt.replace(rpl,nt))

# 8. Write a program that asks the user for a string and prints the first and last characters of the string.  

str=str(input("Enter the string: "))
print(str[0], str[-1])


# 9. Ask the user for a string and print the reversed version of it.

st=str(input("Enter the string: "))
print("The reversed verison of entered string is:", st[::-1])

# 10. Write a program that asks the user for a sentence and prints the number of words in it.  

snt=str(input("Enter the sentence: "))
print(len(snt.split()))

# 11. Write a program to check if a string contains any digits.  

st=str(input())
c=0
for i in range(len(st)):
    if st[i].isdigit():
        c+=1
if c:
    print("Yes it contains digits: ")
else:
    print("No, it does not contain digits: ")


# 12. Write a program that takes a list of words and joins them into a single string, separated by a character (e.g., - or ,).  

w1,w2,w3,w4=map(str,input("Enter the words: ").split())
d=''
d+=w1+","+w2+","+w3+","+w4
print(d)


# 13. Ask the user for a string and remove all spaces from it.  

st=str(input("Enter the string "))
print(st.strip())

# 14. Write a program to ask for two strings and check if they are equal or not.  

st1=str(input("Enter the first string "))
st2=str(input("Enter the second string "))
if st1 == st2:
    print("They are equal")
else: 
    print("They are not equal")


# 15. Ask the user for a sentence and create an acronym from the first letters of each word.  
    # Example:  
    # - Input: "World Health Organization"  
    # - Output: "WHO"  

st=str(input("Enter the sentence: "))
c=''
for i in st:
    if i==i.upper():
        c+=i
print(c.strip())


# 16. Write a program that asks the user for a string and a character, then removes all occurrences of that character from the string.  

st=str(input("Enter the string: "))
ch=str(input("Enter the character: "))
st=st.replace(ch,"")
print(st)

# 17. Ask the user for a string and replace all the vowels with a symbol (e.g., *).  

st=str(input("Enter the string "))
for i in st:
    if i.lower()=="a" or i.lower()=="u" or i.lower()=="e" or i.lower()=="o" or i.lower()=="i":
        st=st.replace(i,"*")
print(st)


# 18. Write a program that checks if a string starts with one word and ends with another.  
    # Example:  
    # - Input: "Python is fun!"  
    # - Starts with: "Python"  
    # - Ends with: "fun!"  

st=str(input("String: "))
start=str(input("Starts with "))
end=str(input("Ends with "))
if st.startswith(start) and st.endswith(end):
    print(f"Yes, {st} starts with {start} and ends with {end}")
else:
    print("No, it does not")