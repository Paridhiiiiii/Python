#SYNTAX -------------------------------------------------
print("Hello, World!")

#This is a comment.

#VARIABLES ----------------------------------------------
#variables are case sensitive(A will not overwrite a)
x=5
y="John"
print(x)
print(y)

#*Casting
x=str(3)
y=int(3)
z=float(3)
print(x,y,z)

#*Get the type
x=5
y="John"
print(type(x))
print(type(y))

#*Unpacking
fruits=["apple","banana","cherry"]
x,y,z=fruits
print(x)
print(y)
print(z)

#DATATYPES----------------------------------------------
x="Hello World"                   #str
x=20                              #int
x=20.5                            #float
x=1j                              #complex
x=["apple","cherry"]              #list
x=("apple","cherry")              #tuple
x=range(6)                        #range
x={"name":"John","age":36}        #dict
x={"apple","cherry"}              #set
x=frozenset{{"apple","cherry"}}   #frozenset
x=True                            #bool
x=b"Hello"                        #bytes
x=bytearry(5)                     #bytearray
x=memoryview(bytes(5))            #memoryview

#RANDOM NUMBER-------------------------------------------
import random
print(random.randrange(1,10))

#STRINGS-------------------------------------------------
print("Hello")
print('Hello')

#*Quotes inside quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#*Assign string to variable
a="Hello"
print(a)

#*Multiple strings
a="""Holla
Paridhi """
print(a)

#*String as array
a="Hello, world"
print(a[1])

#*Looping through a string
for x in "banana":
    print(x)

#*String length
a="Hello"
print(len(a)) 

#*check string
txt="The best things in life are free" 
print("free" in txt)

#*check if not
txt="The best things in life are free" 
print("expensive" not in txt)

#*Slicing - return a range of characters by using slice syntax
b="Hello, world!"
print(b[2:5])
print(b[:5]) #from start
print(b[2:]) #from end
print(b[-5:-2]) #negative indexing

#*Modify string
a=" Hello, world! "
print(a.upper())  #upper case
print(a.lower())  #lower case
print(a.strip())  #remove whitespace
print(a.replace("H","J"))   #replace string
print(a.split(","))   #split string

#*Concatenation
a="Hello"
b="World"
c=a+" "+b
print(c)

#*Format string - combine strings & numbers by using f-string or format() method
age=36
txt=f"My name is John, I am {age}"
print(txt)

quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

price=59 #Placeholder and modifier
txt=f"The price is{price:.2f} dollars" #fixed point no. with 2 decimals
print(txt)

txt=f"The price is {20*59} dollars"
print(txt)

#LISTS--------------------------------------------------- 
#to store muultiple items in a single variable
mylist=["apple","banana","cherry","kiwi","orange","mango"]

print(mylist)
print(len(mylist))  #length
print(type(mylist)) #datatype
print(mylist[-1]) #access items & negative indexing
print(mylist[-2:-5]) #range of negative indexes

#*check if item exists
if "apple" in mylist: 
    print("Yes, 'apple' is in the fruits list")

#*change item value
mylist[1]="strawberry"  
print(mylist)

#*change a range of item values
mylist[1:3]=["blackcurrent","watermelon"]

#*insert items
mylist.insert(2,"watermelon")
print(mylist)

#*append items
mylist.append("orange")
print(mylist)

#*extend items
tropical=["dragonfruit","avacado"]
mylist.extend(tropical)
print(mylist)

#*remove specific item
mylist.remove("banana")
print(mylist)

#*remove specific index
mylist.pop(1)
print(mylist)

#*delete entire list
del mylist

#*clear the list
mylist.clear()
print(mylist)

#*list comprehension - offers a shorter syntax when you want to create a anew list based on the values of an existing list.
fruits=["apple","banana","cherry","kiwi","mango"]
newlist=[x for x in fruits if "a" in x]
newlist=[x for x in fruits if x!="apple"]
newlist=[x for x in fruits]
newlist=[x for x in range(10) if x<5]
newlist=[x.upper( for x in fruits)]
newlist=[x if x!="banana" else "orange" for x in fruits] #return orange instead of banana
print(newlist)

#*constructor list-double round brackets
thislist=list(("apple","cherry"))  
print(thislist)

#*sort lists
thislist=["orange","mango","kiwi","pineapple","banana"] 
thislist.sort() #alphabetically sort
thislist.sort(reverse=True) #descending sort
thislist.reverse()   #reverse order
print(thislist)

def myfunc(n):   #customize sort function
    return abs(n - 50)
thislist=[100,50,65,82,23]
thislist.sort(key=myfunc)
print9thislist

thislist=["banana","Orange","Kiwi","cherry"]  #case insensitive sort
thislist.sort()  
print(thislist)

#*copy lists
thislist=["apple","cherry"]
mylist=thislist.copy()
mylist=list(thislist) #another way
print(mylist)

#*join lists
list1=["a","b","c"]
list2=[1,2,3]
list3=list1+list2

for x in list2: #another way
    list1.append(x)
print(list1)

list1.extend(list2) #another way
print(list1)

#TUPLE---------------------------------------------------
thistuple=("apple","banana","cherry")
print(thistuple)

#*Update tuple- to change,add,remove values convert into list then convert it back to tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#*unpacking a tuple
fruits=("apple","banana","cherry")
(green,yellow,red)=fruits
print(green)
print(yellow)
print(red)

fruits=("apple","banana","cherry","strawberry","raspberry") #using asterisk*
(green,yellow,*red)=fruits
print(green)
print(yellow)
print(red)

#*join tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)

#*multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)

#SETS----------------------------------------------------
myset={"apple","banana","cherry"}

#*add sets
thisset={"apple","banana","cherry"}
thisset.add("orange")
print(thisset)

tropical={"pineapple","mango","papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kiwi", "orange"] #update method does not have to be a set, it can be tuples,lists,dict etc.
thisset.update(mylist)
print(thisset)

#*remove set items
thisset.remove("banana") 
thisset.discard("banana") #another way
thisset.pop() #another way
thisset.clear() #another way
del thisset
print(thisset)

#*join sets
set1 = {"a", "b", "c"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.union(set2) #union
set3 = set1 | set2 #another way
print(set3)

set3 = set1.intersection(set2) #intersection
set3 = set1 & set2#another way
print(set3)

set1.intersection_update(set2) 
print(set1)

set3 = set1.difference(set2) #difference
set3 = set1 - set2 #another way
print(set3)

set1.difference_update(set2)
print(set1)

set3 = set1.symmetric_difference(set2)
set3 = set1 ^ set2 #another way
print(set3)

#DICTIONARIES---------------------------------------------
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#*accessing items
x = thisdict["model"]  #Get the value of the "model" key:
x = thisdict.get("model")
x = thisdict.keys()  # list of the keys:
x = thisdict.values() #list of the values:
x = thisdict.items()  #list of the key:value pairs
 
if "model" in thisdict:  #check if key exists
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

#*change dictionary items
thisdict["year"] = 2018  #Change the "year" to 2018:
thisdict.update({"year": 2020})  #Update the "year" of the car
thisdict["color"] = "red"  #Adding an item

#*removing item
thisdict.pop("model") 
thisdict.popitem()  #removes the last inserted item
del thisdict["model"]
thisdict.clear()

#*copying dict
mydict = thisdict.copy()
mydict = dict(thisdict) #another way

#*nested dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  }
}
print(myfamily["child2"]["name"]) #access items

for x, obj in myfamily.items():  #loop through nested dict
  print(x)

  for y in obj:
    print(y + ':', obj[y])

#NUMPY---------------------------------------------------
import numpy as np
arr=np.array(42) #0-D array
arr=np.array([1,2,3,4,5])  #1-D array
arr=np.array([[1,2,3],[4,5,6]])  #2-D array
arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])  #3-D array
print(arr)

#*check no. of dimension
a=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(a.ndim)

#*define no. of dimensions
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)

#*Accessing elements
arr = np.array([1, 2, 3, 4]) 
print(arr[0])  #1-D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1]) #2-D array

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print('3rd element on 2nd row: ',arr[0, 1, 2])  #3-D array

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', arr[1, -1]) #negative indexing

#*Slicing array
import numpy as np 
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])  #slice index 1 to index 5
print(arr[1:5:2]) #Return every other element from index 1 to index 5
print(arr[::2])  #Return every other element from the entire array

import numpy as np
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #From the second element, slice elements from index 1 to index 4 (not included)
print(arr[0:2, 2]) #From both elements, return index 2
print(arr[0:2, 1:4]) #*DOUBT* From both elements, slice index 1 to index 4 (not included)

#*Datatype
import numpy as np
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

#*Copy & View
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
arr[0] = 42
print(arr)
print(x)
print(y)
print(x.base)
print(y.base)

#*shape
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
arr1 = np.array([1, 2, 3, 4], ndmin=5) #DOUBT
print(arr.shape)
print('shape of array :', arr1.shape) 

#*reshape
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
newarr1 = arr.reshape(2, 3, 2)
print(newarr)
print(newarr1)