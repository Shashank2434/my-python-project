#variable is a reusable container for storing values
#Variable behaves as if it were the value it contains

#example
# age = 29
# print(age)

#String concatenation , we only use when we want to print exact message
# print("Shashank is " + str(age) + " old ") # here we type cast age which is 29 to string as we can only concatenate str (not "int") to str
# print("Shashank is",age,"Years old") # we can also do concatenation like this adding (,) will add a space
# print(f"Shashank is {age} year old") # Other and popular way to print it as fstring here we dont have to worry about spaces


# Tips
# x,y,z =(1,2,3)
# print(x,y,z)

# Set multiple variable to single value
# x=y=z=6
# print(x,y,z)
# A=x,y,z
# print(A)

#Ways to Declare variable
# MyName="Shashank" #pascal case
# myName="Shashank" # camel case
# myname="Shashank" #flat case
# my_name="Shashank" #Snake Case

# Rules to declare variable
# 1. Start with _ or letter
# 2.It only contain : letter , name ,Underscore(_)
# 3. Variables are case sensitive
# 4. Variables cant be reserved words
# for =20 #for is a reserve word