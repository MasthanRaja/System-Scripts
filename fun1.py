def my_first_function(x, y):
    "this is our first function"
    print("Hello", x , y)

my_first_function("masthan", "Saji")

print("Hello Python")
print("I am already writing code and enjoying this course!")

# User input method - "input" Function
user_says = input("Please enter the string you want to print: ")
print (user_says)

# Variable 
progress = "I love writing python code!"

print(progress)

#DATA Types
#strings, Numbers and booleans, Lists ,sets, Tuples,Ranges, Dictionaries

#Format Method -1
"Cisco mode: %s, %d WAN slots, IOS %f" %("2600xm", 2, 12.4)

# Method-2
"Cisco mode: {}, {} WAN slots, IOS {}".format("2600xm", 2, 13.4)

#Method-3
model = '45000xm'
slots = 4
ios = 12.3
f"Cisco mode: {model}, {slots} WAN slots, IOS {ios}"

my_string = "I love programming in python more than Ruby or Perl"
print(my_string[-12])

my_string = "a0:12:90:00:80:43"
print(my_string[-11:-6])

my_string = "a0:12:90:00:80:43"
print(my_string.split(":"))

print(bool("Python 3") and not(23 == 23))


result = 0
     
x = bool(result) or (7 + 2) == (3 ** 2)
     
print(x)