# print("saurabh")  #name print 

#print("munna","raju") # same line 
#print(34) 

# print(23+12) #add  


##  DATATYPES 

# intergers :     +ve , -ve , 0 
# String :         any name 
# Float :          7.8
# Boolean :        True or False 
# None    :        when you not give any value 



# name = "raju"
# age = 23 
# price = 45.3 

# print("my name is : ", name) 
# print("my age is : ", age) 
# print("my price is : ",  price) 



# print(type(name))  #check type anything datatype

# print(type(age))   #check type anything datatype

# print(type(price)) #check type anything datatype 

# String 

# its work anytypes 
# name1 = "raju"
# name2 = 'raju'
# name3 = '''raju'''

# print(name1)
# print(name2)
# print(name3)



 # ***********************************************
 # 
 # keyboard 
  #  :-  keyboard are reserved words in python  

# case sensitive 
  # its case senstive language , apple Apple both are different 

# print sum 

# a = 2 
# b = 4 
# sum = a+b
# print(sum) 

# Comments in python :=  use # for cmnt 

# Types of operators 
# an operator is a symbol that performs a certain operation .  

# Airthmetic Operators 

# (+,-,*,%,**) 


# a = 5 
# b = 3 

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)    # its output falue is float  
# print(a % b)    #  find reminder value 
# print(a ** b)   # work like power value (5)3


## relational operators  ( )

# a = 7 
# b = 8 

# print (a == b ) #false 
# print( a != b ) #true 
# print(a >= b )   #false
# print(a < b )   #true  


## Assignment operator  

# ( = ,+= ,-= ,*= ,/= ,%= ,<=) 

# num = 10 
# # num += 10     # (num = num + 10  # 10+10 => 20 )
# num **= 10     # num = num - 10

# print(num)


##  Logical operator 

#  not , and , or its result in boolean 

# print(not False ) #True 

# a = 45 
# b = 23 

# print(not (a>b)) #false 

# a = 45 
# b = 90 

# and 

# a = 40  
# b = 39 

# val1 = False
# val2 = True 
# print(val1 and val2 )  #output is true 
# print("or operator:", (a == b) or (a > b)) 


# Type Conversion .............. 

# a = ( 2 )
# b = 3.23

# sum = a + b 
# print ( sum)

# ================================== 
# a = 3.45
# a = str(a)  check data type 

# print(type(a))


# Input in python ********************************* 

# input() statement is used to accept values ( using keyboard) from user 

# * input () #result for input () is always a str  
# :- 
# name = input("enter your age: ")
# print("you entered", name) 

#* int ( input ()) #int # a = int(input("it is first number"))
# b = int(input("it is second number")) 

# print( a >= b )  #check the boolean  
#*float (input())  #float 


# name = input ("enter your name: ") 
# print ("welcome ", name )  


# name = input("your name: ")
# age = int(input("your age: ") ) 
# marks = float(input("your marks: ") )

# print("welcome" , name) 
# print("age=" , age)
# print("marks" , marks)  
 
# [practise question]
 
# write a program to input 2 numbers & print their sum. 

# val1 = int(input("enter 1st : ")) 
# val2 = int(input("enter 2nd : "))

# print( "sum = ", val1 + val2 )  




# WAP to input side of a square & print its area.   

# :-
# side = float(input("enter square side " )) 
# print("area =", side ** 2) 
 

# wap to input 2 floating point numbers & print their average.

# a = float(input("first number "))
# b = float(input("second number"))
 
# print ("avg=", (a+b)/2) 


# wap to input 2 int number, a and b. print true if a is greater than 
# or equal to b. if not print false .  
# :- 
# a = int(input("it is first number"))
# b = int(input("it is second number")) 

# print( a >= b )  #check the boolean  

# =================================================================
# =================================================================
# =================================================================
# =================================================================

# ********** Strings & Conditional Statement ****************** 

# Strings 
# :- String is data type that stores a sequence of characters.

# str1 = "hello"
# str2 = 'hello'   #  it's string type 
# str3 = """ hello"""  

# str1 = "hello everyone .\n  it is my first day "
# print(str1)     # \n is use for change the line 

# concatenation :- it is use for add two value or two word 

# str1 ="hello"
# str2 = "world" 

# print(str1+str2) # output:  helloworld 



# length of str 

# str1 = "okmydear" 
# print(len(str1)) # len used for count value of string 




# indexing :-  index - position write 

# str = "hellomy friend"
# ch = str[6]  # it is denoted whom number you know by indexing 
# print (ch)  #output :- y 

#Slicing :-   Accessing parts of a string  

# str[ starting_idx : ending _idx]   #ending idx is not included 

# str = "munna bhai "
# print(str[6:11])    #output :- unn 
 
# Negative index :- backward count -3: -4  

# str ="hello guys"
# print(str[-8:-1])     #output :- llo guy  


## String Functions 

# endswith("er")          #return true if string end with substr

# str = "Hello to all of you"
# print(str.endswith("you"))


# str.replace(old,new)  #replace all occurrence of old  

# str = "hello everyone what are you doing " 
# print(str.replace("what","kya"))   # its use for replace any word 


# find(word) :-  return 1st index of 1st occurrer 

# str = "hello everyone what are you doing"
# print(str.find("w"))    #output is 15 . 

# count("word")  :- how many came 

# str = "hello everyone what are you doing"
# print(str.count("o"))     # output is 4 


# #  to input user's first name & print its length. 

# name = input(" enter your name : ")
# print("length of your name is", len(name))

# firstName = "raju bhai"
# print(len(firstName))

# wap to find the occurrence of '$' in a String. 

# str = "hello everyone what $ are you doing  $99.09" 
# print(str.count("$"))   #output is  2 


## Conditional Statements 

# if-elif-else (syntax)   

# age = 45

# if(age >= 45): 
#   print("he is big") 

# light = "yellow"

# if(light == "red"):
#   print("stop")
# elif(light == "green"):
#   print("go")
# elif(light == "yellow"):
#    print("look")
# else :
#     print("light is broken") 

# print("end of code") 

# ************************************************************************************** 

# age = 23

# if(age >= 18): 
#   print("teen")
# else:
#   print("small") 

# ***************************************************************************************

# marks = int(input("enter student marks : "))

# if(marks >= 90):
#     grade = "A" 
# elif(marks >= 80 and marks < 90 ):
#     grade = "B"
# elif(marks >= 70 and marks < 80 ):
#     grade = "C"
# else:
#     grade = "D"

# print("grade of the student ->",grade) 

# *************************************************************************************** 


# nesting 

# WAP to check if a number entered by the user is odd or even. 

# str = int(input("entered a number : ")) 
# num = 12 

# if( num % 2 == 0 ):
#   print("even")
# else:
#   print("odd")

# **********************************************************************

## print name by user and its length 

# name = input("enter your name : ")
# print("length of your name is", len(name))



## wap to find occurrence of '$' in a string 

# str = "hi, $Iam sjfl fajie dj $ djfjds $$89.0" 
# print(str.count("$")) 


# str = "saurabh"
# print(str[4])  #output :- a


# str = "hello world"
# print(str[1:8])   #output:- ello wo 
















