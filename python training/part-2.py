
###################

#String Merging

name="aziz"
surname="simsek"
age="24"

print(name +" "+surname)

text="My name is " + name +" and my surname is "+surname+".i am "+ age +" years old."
print(text)

###################

#selecting the basic index

password="abc12345"
print(password[0])
print(password[2])
print(password[-1])
print(password[-3])

###################

#String Slicing

userName="blackCat001"

print(userName[0])
print(userName[1])
print(userName[-2])

print(userName[2:6])#from the 2nd index to the 6th,but not including the 6th
print(userName[0:])#from beginning to end
print(userName[1:4])
print(userName[:3])#form the 0th index to the 2nd index
print(userName[-10:-5])#reverse from the 9th index to the 5th index

print(userName[0:11:2])#increasing by twos from start to finish
print(userName[::2])#jumping two by two from start to finish
print(userName[::-1])#the process of reading backwards

###################

#String Formatting

name="aziz"
surname="simsek"
age=24

print("my name is {} {}".format(name, surname))
print("my name is {1} {0}".format(name,surname))
print("my name is {s} {n}".format(n=name,s=surname))
print("my name is {n} {s}".format(n=name,s=surname))
print("my name is {} {}.i am {} years old.".format(name,surname,age))
#new formatting method
print(f"my name is {name} {surname} and I'am {age} years old")
print("my name is",name,"and my surname is ",surname," I'am ",age," years old.")

number=5/3
print(number)
print("the result is {n:1.3}".format(n=number))#show the decimal part as only 3 digits
print("the result is {n:1.6}".format(n=number))

###################

#String Methods

words=" The sea is near the Hotel."
print(words)
result=words.upper()
print(result)
result=words.lower()
print(result)
result=words.title()#it makes the initial of every word big
print(result)
result=words.capitalize()# it just makes the initial of the sentence big
print(result)
result=words.islower()
print(result)
result=words.isupper()
print(result)
result=words.strip() #eliminates spaces at the beginning and end of sentences
print(result)

words="The sea is near the Hotel . Hotel has got a small beach."
result=words.split() #creates an array after splitting
print(result)
newResult=words.split(".")#after dividing by point,it creates an array
print(result)

newResult="-".join(words)#if we want to add a symbol between the letters,dec
print(newResult)

newResult=words.index("Hotel")#index query process
print(newResult)

newResult=words.startswith("t")#the first letter inquiry process.Attention!.It has a letter sensitivity
print(newResult)
newResult=words.startswith("T")
print(newResult)
newResult=words.startswith("d")
print(newResult)
newResult=words.endswith(".")#last letter inquiry process.Attention!.It has a letter sensitivity
print(newResult)

sentence="I live in Izmir "

result=sentence.replace("Izmir","Istanbul")#the process of changing words
print(result)
result=sentence.replace("i","K").replace("l","A")
print(result)

#you can see more examples on the "w3schools.com" site.

"""


#########################################
#Lists
#########################################

#-can be changed
#-it is inclusive
#-it is ordered and index operations can be performed

notes=[1,2,3,4]
type(notes)

names=["a","b","v","d"]

not_nam=[1,2,3,"a","b",True,[1,2,3]]


not_nam[0]
not_nam[5]
not_nam[6]
not_nam[6][1]  # getting elements from the lists within the list

type(not_nam[6])
type(not_nam[6][1])

not_nam[0]=101
not_nam

not_nam[0:4]


###############################
#List Methods
###############################

dir(notes)

########################
#len:size information
########################

len(notes)
len(not_nam)

###################################
# append: adding elements to lists
##################################

notes
notes.append(100)
notes


##########################
# pop:performs the deletion of the element acccording to the index in the list
################################

notes.pop(3)
notes

##########################
# insert:adds elements in the list according to a specific index
##########################

notes.insert(3,564)
notes

"""
