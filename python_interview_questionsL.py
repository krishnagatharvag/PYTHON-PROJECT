      #swap two number
"""
a=5
b=10
a,b=b,a
print(a)
"""
      #odd even number
"""
num=eval(input("Enter number"))
if num%2==0:
    print("even number")
else:
    print("odd number")
"""
      #Palindrome
"""
inp=input("Enter number")
rev=inp[::-1]
if inp==rev:
    print("palindrome")
else:
    print("Not palindrome")
"""
    #cheking whether the given number is prime or not
"""
num=eval(input("Enter number"))

for i in range(2,num):
    if num%i ==0:
        print("not a prime number")
        break

else:
    print("prime number")
"""
     #prime number in given interval

"""
for num in range(10,20):
    if all(num%i for i in range(2,num)):
        print(num)
        

"""
   #fibonacci series
"""
def fib(n):
    a=0
    b=1
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)

fib(20)
"""
      # chenge the required charactor to uppr case latter
"""
str="krishna"
lenght=len(str)
out=""

for i in range(0,lenght,2):
    out+=str[i]
    if i<(lenght-1):
        out+=str[i+1].upper()

print(out)

str1="krishna"
lenght1=len(str1)
out1=""

for i in range(0,lenght1,2):
    out1+=str1[i].upper()
    if i<(lenght1-1):
        out1+=str1[i+1]

print(out1)
"""
   # input a4b3c2d1 output aaaabbbcca
"""
inp=input("Enter the value")
out=""

for ch in inp:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        out+=x*d

print(out)
"""
    # input d1c2b3a4 output aaaabbbcca(shorted order)
"""
inp=input("Enter the value")
out=""

for ch in inp:
    if ch.isalpha():
        x=ch
    else:
        d=int(ch)
        out+=x*d
        target = sorted(out)
        target1="".join(target)

print(target1)
"""
     #input aaaabbbccd outpot a4b3c2a1
"""
inp="aaaabbbcca"
char=inp[0]
counter=0
out=""

for ch in inp:
    if ch==char:
        counter=counter+1

    else:
        out+=char+str(counter)
        char=ch
        counter=1


out+=str(counter)+char
print(out)
"""
      # create a new list having unique values from a given list

"""
l=[10,20,30,10,40,50,20,50,70,30]
l1=[]
for i in l: 
    if i not in l1:
        l1.append(i)

print(l1)
"""

# create a new list having duplicate values from a given list
"""
l=[10,20,30,10,40,50,20,50,70,30]
l1=[]

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]==l[j] and l[i] not in l1:
            l1.append(l[i])

print(l1)
"""
     # create a new list having duplicate values from two list
"""
l1=[10,20,30,40,50]
l2=[1,2,3,10,20,30]
l=[]
for i in l1:
    for j in l2:
        if i==j and i not in l:
            l.append(i)
print(l)

"""
     #store the qube values of a list in list using for loop
"""
l=[1,2,3,4,5]
l1=[]

for i in l:
    l1.append(i**3)

print(l1)
"""

     # reverse the string
"""f
str="krishna"
print(str[::-1])
"""
        # reverse the words of the string
"""
str1="welcome to python programming"
str2=str1.split()
str3=str2[::-1]
out=" ".join(str3)

print(out)
"""
      # reverse the indivisual words of the string
"""
str1="welcome to python programming"
str2=str1.split()

for i in str2:
    print(i[::-1],end=" ")
"""
        # reverse the indivisual words of the string using list

"""
str1="welcome to python programming"
str2=str1.split()
l=[]
for i in str2:
    l.append(i[::-1])
    l1=" ".join(l)
    
print(l1)
"""
        #reverse the string withowt slicing
"""
str="krishna"
lenght=len(str)

for i in range(lenght-1,-1,-1):
    print(str[i],end="")
"""

   #reverse the string withowt slicing using list
"""
str="krishna"
lenght=len(str)
l=[]

for i in range(lenght-1,-1,-1):
    l.append(str[i])
    l1="".join(l)


print(l1)
"""
    # random and randit function
"""
import random
print(random.randrange(9))

from random import randint
print(randint(0,9))

from random import randint
print(randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),randint(0,9),sep='')
"""
      #count function
"""
str="kaarishnaa"
print(str.count("a"))
"""
 # counter librery
"""
from collections import Counter
str="krkkishna"
tar=Counter(str)
print(tar)
"""
     #find the occarence of an element in a list or string
"""
l=[1,2,3,4,5,1,7,8,1]
x=1
counter=0

for i in l:
    if i==x:
        counter=counter+1

print(counter)

str="karaishnaa"
y="a"
counter1=0
for j in str:
    if j==y:
        counter1=counter1+1

print(counter1)
"""
     #swap first and last element of string
"""
str="welcome to python programming"
str1=str.split()
str1[-1],str1[0]=str1[0],str1[-1]
tar=" ".join(str1)
print(tar)
"""
     #swap any two elements of list
"""
l=[10,20,30,40,50,60,70,80,90]
l[2],l[6]=l[6],l[2]
print(l)
"""
  #deleting element from a list
"""
l=[10,20,30,40,50,60,70,80,90]
del l[5]
print(l)
"""
     #slicing for avoiding number
"""
l=[10,20,30,40,50,60,70,80,90]
print(l[:-1])#-90
print(l[:-2])#-80,90
"""
    #list comprehension
"""
l=[10,20,30,40,50,60,70,80,90]
x= [num%2==0 for num in l]
print(x)

x= all([num%2==0 for num in l])
print(x)

y=[y for y in range(11) if y%2==0]
print(y)

y=[y+5 for y in range(11) if y%2==0]
print(y)
"""
     # squre of a given list
"""
nums=[1,2,3,4]
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)

x=[x*x for x in nums  ]
print(x)
"""

      #convert list into string
"""
a = [1, 2, 3, 4, 5, 6, 7, 8]
tar="".join(str(i) for i in a)
print(tar)
"""
    #table of two
"""
for i in range(1,11):
    print(2,"*",i,"=",2*i)
    
"""
    #search an element in a list
"""
l=[1,4,2,6,8]
x=4

for i in l:
    if x==i:
        print("element found")
        break

else:
    print("element not found")


ele=4  #7
flag=0
for i in l:
    if ele==i:
        print("element found")
        flag=1
        break

if(flag==0):
    print("element not found")
    
"""
   #tuple packing unpaking
"""
tup=(1,2,3,4,5)
a,b,c,d,e=tup
print(d)
"""
     # reverse the number using while loop
"""
i=20
while i>=0:
    print(i)
    i=i-1
"""
#string with no duplicate value
"""
str="welcome to automation"
str1=""
for i in str:
    if i not in str1:
        str1+=i

print(str1)
"""
     #replace function
"""
str="krishna kant goswami"
print(str.replace("a","A"))
"""

"""
l=[10,20,30,20,10,50,60,70,80,90,50,70]
l1=max(l)
print(l1)
"""

    #sorting
"""
l=[30,20,10,60,40,80,90,50,70]
l.sort()
print(l)

print(l[-1])#bigest element

l.sort(reverse=True)
print(l)


l2=sorted(l)
print(l2)
"""
   #membership operator
"""
l=[2,89,10,76,"krishna",33,54,1,200,45]

print("krishna" in l)#membership operator
print("corry" not in l)
"""

"""
l1=[1,2,3,4,5]
l2=[1,2,3,4,5,6,7]
l=list((set(l1+l2)))
print(l)
"""
#create a dictonary from two given lists
"""
l1=["name","company","city","salary"]
l2=["krishna","ust","pune",10000000]
dic={}
for i in range(len(l1)):
    dic[l1[i]]=l2[i]

print(dic)
"""
"""
# dic={"name":"krishna","company":"ust","city":"pune"}
# dic["name"]="goswami"
# print(dic)
dic={"name":"krishna","company":"ust","city":"pune"}
dic["surname"]="goswami"


print(dic)
"""

#extended function
"""
l1=[1,2,3,4]
l2=[5,6,7,8]
print(l1+l2)
l1.extend(l2)
print(l1)
"""

print("krishna is\n good boy \tatharva")

"""
#sorting by alphabet
str1="welcome to python programming"
st2=str1.split()
#st=sorted(st2)
#print(st)
st2.sort()
print(st2)
"""
"""

str2="krishnaaahh"
lenght=len(str1)
l=[1,2,3,4,5,6,7,8,1,2,3,4,5,6]

from collections import Counter
out=Counter(str2)
out1=list(out.items())
out1.sort()
print(out1)
"""
# l=["kk","ram","ashok","nitin","sanjeev","mukesh","krishna","sonam","ramesh","atul","vaibhav","kamal","rahul","kumar"]
# x="k"
# l1=[]
#
# for ele in l:
#     if ele[0]==x:
#         l1.append(ele)
#
# print(l1)


# str1="krishnakantgoswami"
# lenght=len(str1)
# str2=""
# for i in range(0,lenght,3):
#     str2+=str1[i]
#     if i<(lenght-1):
#         str2+=str1[i+1]
#     if i<(lenght-2):
#         str2+=str1[i+2].upper()
#
# print(str2)

"""
str1="welcometopythonprogramming"
lenght=len(str1)
str2=""
for i in range(0,lenght,3):
    str2+=str1[i]
    if i<(lenght-1):
        str2+=str1[i+1]
    if i<(lenght-2):
        str2+=str1[i+2]
    if i<(lenght-3):
        str2+=str1[i+3].upper()

print(str2)

########################
str1="welcometopythonprogramming"
lenght=len(str1)
str2=""
for i in range(0,lenght,3):
    str2+=str1[i].upper()
    if i<(lenght-1):
        str2+=str1[i+1]
    if i<(lenght-2):
        str2+=str1[i+2]


print(str2)

"""

    # adding elements of two list
# l=[1,2,3,4,5,6]
# l1=[1,2,3,4,5,6]
# l2=[]
#
# for i in range(len(l)):
#     l2.append(l[i]+l1[i])
# print(l2)
print("##############################")
# l1=[1,2,3,4,5]
# l2=[1,2,3,4,5,6,7]
# addi=0
# for i in l1:
#     addi+=i
# for j in l2:
#     addi+=j
#
# print(addi)


#adding elements of list

# list = [5,7,4,3,9,8,19,21]
# out=0
# for i in list:
#     out+=i
#
#
# print(out)


#print 1 to 100 except 50 to 60
l=[]
# for i in range(1,101):
#     if i==50 or i==51 or i==52 or i==53 or i==54 or i==55 or i==56 or i==57 or i==58 or i==59 or i==60  :
#
#         continue
#     print(i)


# for num in range(1, 101):
#     if 50 <= num <= 60:
#         continue
#     print(num)

#find out common letters in between two strings
"""
def common_letters():
    str1=input("enter first word : ")
    str2=input("enter second word : ")
    s1=set(str1)
    s2=set(str2)
    l=s1&s2
    print(l)


common_letters()
print("############################################")
str1="welcome"
str2="common"
s=""
for i in str1:
    for j in str2:
        if i==j and i not in s:
            s+=i
print(s)
"""

#find the missing numbers of array
lst=[1,3,5,6,7,8,20]
def missing_no(lst):
    list1=[]
    for i in range(1,lst[-1]):
        if i not in lst:
            list1.append(i)
    return (list1)

print(missing_no(lst))


#Find Out Pairs with given sum in an array in python

# list = [5,7,4,3,9,8,19,21]
# n = len(list)
# k=17
# for i in range(n):
#     for j in range(i+1,n):
#         if list[i]+list[j] == k:
#             print(list[i],list[j])


#to find total number of positive and negative number in list
# l=[-11,33,44,-66,-88,22,33]
# positive=0
# negative=0
# for i in l:
#     if (i>0):
#         positive=positive+1
#     else:
#         negative=negative+1
# print("positive number is:",positive)
# print(("negative number is:",negative))

# original_string = "   Hello,   World!   "
# no_spaces = original_string.replace(" ", "")
# print(no_spaces)
"""
l=[6,9,89,9,1,3,2,44,56,34,7,1,3,4,55,6,100,90]
l.sort()
print(l[-1])
print(l[0])
l1=l[:6]
l2=[]
for i in l1:
    if i not in l2:
        l2.append(i)

print(l2)
"""
#flatten the three list into one
"""
l1=[[1,2,3],[4,5,6],[7,8,9]]
l2=l1[0]
l3=l1[1]
l4=l1[2]
x=l2+l3+l4
print(x)
"""
"""
#elements from last
l=[1,2,3,4,5,6,7,8,9]
lenght=len(l)

print(list(range(l[-1],l[-7],-1)))
print(list(range(21,4,-1)))# this is strightforword
l=[1,2,3,4,5,6,7,8,9]
print(l[-1:4:-1])

"""
"""
# should only accept  first 4 charactor then 3 number then 2 charactor
val=input("Enter value")
if val[0:3].isalpha() and val[4:6].isdigit() and val[7:8].isalpha():
    print("True")
else:
    print("False")
"""
"""
# input "abc" output "bcd"

val=input("Enter value")
l=[]
for i in val:
    l.append(ord(i)+1)#we can replace 1 by any number to get required string

for j in l:
    print(chr(j),end="")
"""
"""
    
l = [1, 2, 3, 11, 22, 33, 4, 5, 11, 22, 33, 7, 8, 9, 11, 22, 33]


values_to_remove = [11,22,33]

l1=[]
for i in l:
    if i not in values_to_remove:
        l1.append(i)

print(l1)

#or 
l=[1,2,3,11,22,33,4,5,11,22,33]
l1=[x for x in l if x not in(11,22,33)]
print(l1)

"""

#Angle for 3hours 15 min
"""
def angle(H,M):
    print(30*H-11/2*M)


angle(3,15)
"""
# str1="welcome to python programming"
# l=[]
# str2=str1.split()
#
# from collections import Counter
# out=Counter(str1)
# out1=list(out.items())
# out1.sort()
# out2=dict((x,y) for x,y in out1)#tuple to dictionary
#
# print(out2)

"""
#remove common elements from list
l1=[1,2,3,4,5,5,7,8,8,8,9,9,9,9]
l2=[5,8,11,22,33,12,34]
l=[]
lenght=len(l1)

for i in range(lenght):
    for j in range(i+1,lenght):
        if l1[i]==l1[j]:
            l.append(l1[i])
            
y=[x for x in l1 if x not in l]
print(y)
"""


#to mathch username and password
import getpass
users={'sonam':'pass1',
       'kk':'pass2',
       'atharva':'pass3'}
username=input('enter username:')
password=input('enter password:')
if username in users and users[username]==password:
       print("access garented")
else:
       print("access denied")

#username and password inputs with 3 attempt in python
# attempts=0
# while attempts<3:
#     username=input("enter username:")
#     password=input("enter password:")
#     if username=="user123" and password=="pass123":
#         print("you have successfully log in")
#         break
#     else:
#         print("incorrect credentiel")
#         attempts=attempts+1
#         continue

l1=[1,2,3,4,5,1,2]
l2=[1,2,3,4,5,6,7,3,4]
l=[]
lenght=len(l1)
for i in range(lenght):
    for j in range(i+1,lenght):
        if l1[i]==l1[j]:
            l.append(l1[i])



lenght1=len(l2)

for i in range(lenght1):
    for j in range(i+1,lenght1):
        if l2[i]==l2[j]:
            l.append(l2[i])

x=[y for y in l1+l2 if y not in l]
print(x)


# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# # from webdriver_manager.chrome import ChromeDriverManager
# # driver=webdriver.Chrome(ChromeDriverManager().install())
# driver=webdriver.Chrome("C:\\Users\\KK\\.wdm\\drivers\\chromedriver\\win64\\116.0.5845.111\\chromedriver-win32\\chromedriver.exe")
# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC




