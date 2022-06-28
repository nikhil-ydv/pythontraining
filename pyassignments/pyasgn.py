#1

str1 = "Nikhil"
ch = input("Enter character to remove  \n")
str2 = str1.replace(ch,"")
print (str2)

#2

str1 = "Nikhil"
ch = input("Enter character to count  \n")
count = 0
for i in range(len(str1)):
    if(ch==str1[i]):
        count+=1
print(count)

#3 

str1 = "Nikhil"
str2 = "iinlkh"
str1 = str1.lower()
str2 = str2.lower()

if(len(str1) == len(str2)):

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if(sorted_str1 == sorted_str2): #checking if sorted arrays are equal
        print(str1 + " and " + str2 + " are anagram.")
    else:
        print(str1 + " and " + str2 + " are not anagram.")

else:
    print(str1 + " and " + str2 + " are not anagram.")

#4

str1 = "war"
str2 = "raw"
str3 = ""
for i in range(len(str1)):
    str3=str1[i]+str3
if(str2==str3):
    print("Palindrome true")
else:
    print("not a palindrome")

#5

vowel=['a','e','i','o','u']
ch = input("Enter character to check \n")
ch = ch.lower()
if ch in vowel:
    print("Character is a vowel")
else:
    print("character is a consonant")

#6

num = input("Your Input\n")
if ord(num) in range(48,58):
    print("Digit")
else:
    print("not a digit")

#7

num = input("Your Input\n")
def isdigit(num):
    return "It's a digit" if ord(num)>=48 and ord(num) <=57 else "Not a digit"
print(isdigit(num))

#8

str1 = input("Your string\n")
chr = input("Enter character to be used for replacing\n")
list1 = list(str1.split(" "))
str1=""
for s in list1:
    if list1.index(s) is not len(list1)-1:
        print(list1.index(s))
        str1 =  str1 + s + chr
    else:
        str1 = str1 + s
print(str1)

#9

str1 = input("Your string\n")
chr = input("Enter character to be used for replacing\n")
str1 = str1.replace(" ",chr)
print(str1)

#10

from curses.ascii import isupper

str1 ="Nikhil"
list1=[]
list1[:0]=str1    
str1=""  
for i in range(len(list1)):
    if list1[i].isupper() == True:
        list1[i] = list1[i].lower()
    str1 = str1 + list1[i]
print(str1)

#11

from curses.ascii import islower

str1 ="Nikhil"
list1=[]
list1[:0]=str1
vowel=['a','e','i','o','u','A','E','I','O','U']    
str1=""  
for i in range(len(list1)):
    if list1[i] in vowel and list1[i].islower() == True:
        list1[i] = list1[i].upper()
    str1 = str1 + list1[i]
print(str1)

#12

arr = [1,2,3,4,5,6,7,8,10]
for i in range(1,11):
    if i not in arr:
        print(i)

#13

from collections import Counter

li=[1, 3, 2, 6, 2, 3, 5, 6, 4, 5, 7, 9 , 11, 11]
d = Counter(li)

repeated_list = list([num for num in d if d[num]>1])
print("Duplicate integers: ",repeated_list)

#14

def sum_pair(arr,n):
    count=0 
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j]==n:
                count=count+1
                print(arr[i],arr[j])
    return count 
arr=[1, 5, 7, -1, 3, 3] 
n=6 
sum_pair(arr,n)

#15

def arrEqual(arr1,arr2):
    if(len(arr1)==len(arr2)):
        return "Equal" 
    else: 
        return "Not equal"
arr1=[1,2,3,4] 
arr2=[5,6,7,8] 
print(arrEqual(arr1,arr2))

#16

arr=[1,9,8,2,4,5,105,17,0]
arr.sort()
print("Smallest and Largest in array:\n")
print(arr[0])
print(arr[len(arr)-1])

#17

arr=[1,9,8,2,4,5,105,17,0]
arr.sort()
print("Second Largest in array:\n")
print(arr[len(arr)-2])

#18

arr=[1,9,8,2,4,5,105,17,0]
arr.sort(reverse = True)
print("Top 2 in array:\n")
print(arr[0],arr[1])

#19 Remove Duplicates

li = [11,1,4,5,2,6,7,9,3,5,3,5,9,8,11]
unique = set(li)
print(unique)

#20

arr=[1,9,8,2,4,5,105,17,0]
arr.sort(reverse = True)
print("Top 2 in array:\n")
print(arr[0],arr[1])

#21 reverse array

arr=[1,9,8,2,4,5,105,17,0]
rev=arr[::-1]
print(rev)

#22 reverse array using two ways

arr=[1,9,8,2,4,5,105,17,0]
rev=arr[::-1]
print("using slicing")
print(rev)
arr.reverse()
print("using reverse()")
print(arr)

#23 length of array

arrpy = [1,2,3,4]
print(len(arrpy))

#24 Insert at end in array

arrpy = [1,2,3,4]
arrpy.append(19)
print(arrpy)








