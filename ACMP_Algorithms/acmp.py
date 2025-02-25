'''
a=input()
d=''
for i in range(len(a)):
    if a[i]=="1" and a[i] not in a[-1::] and a[i+1]=="3":
        d="omadsiz chipta"
        break
    else:
        d="omadli chipta"
print(d) 


#Robolandiya(ro'yhatga olish)
# Masala 1068
a,b=map(str,input().split())
if a[-1].lower()=="v":
    print(b,a)
else:
    print(a,b) 
    


for n in range(1, 4):
    for j in range(4, 7):
        print(f"n = {n} and j = {j}")



n=int(input())
c=[0]
d=0   # it is for index of the exact input
for i in range(n):
    i=tuple(map(int,input().split()))
    d+=1
    if i[1]==1 and i[0]>max(c):
        c.append(i[0])
        c.append(d)    # this is inside of the if because it is added if its value before is added to the list, it saves some memory
pointer=-1          # it is for printing the answer 
for i in range(len(c)):
    if len(c)>1 and c[i]==max(c):
        pointer=c[i+1]
print(pointer)  

# I have one issue: what if there are several males who shares similar score


# Read number of residents
n = int(input())

max_age = -1
oldest_index = -1  # Store the index of the oldest male

for i in range(1, n + 1):  # Start from 1 to match 1-based index
    age, gender = map(int, input().split())
    
    if gender == 1:  # Only consider males
        if age > max_age:
            max_age = age
            oldest_index = i  # Store 1-based index of the oldest male

# Print the result
print(oldest_index if oldest_index != -1 else -1)

'''

def fib(limit):
  a,b=0,1
  lst=[] 
  c=0
  while c!=limit:
    lst.append(b)
    a,b=b,a+b
    c+=1
  return lst

lim=int(input())
summa=0
for i in fib(lim):
  summa+=i**2
if lim!=1:
   print(summa)
else:
  print(1)