
"""
def is the variable
whatType is the name of the function 
userInput is the parameter of the function and the variable that the user inputs
type is a built in function that labels the datatype 

"""

def whatType(userInput):
    print(type(userInput))

whatType(3)
whatType(3.0)
whatType("anna")
whatType(True)
whatType('a')

#why do i have to do everything for you???  =)

#8/25/25

message = """this is a
multilined message
to my bestie
"""

print(message)

print (42000)
print(42,000)
print(42.000)

name = "anna"
newName = "annie"
name = newName
newName = name

print (name)
print (newName)

classOf2026 = ["Student 1", "Student 2"]

print (2+2)
print ("hello")
print (len("hello"))

#8/25/25 

myName = "anna"
print (myName * 5)
#str is casting the integer data type to a string
#so you can concatenate two strings together
print(myName + str(5))

"""
addition to numbers and strings
subtraction to numbers only
division
/ typical division - the answer is always a float
// floor division - to the largest whole integer, answer is an int
% modulus operator - finds the remainder of the division, answer is an int
mulitiplication to number and strings
* multiplies only
** exponential 
"""

#8/28/25

age = 48
print (type(age))
age = (float(age))
print (type(age))

#create a list of new emails

studentNames = ["Poly", "ana", "chris", "tommy"]
emailAddress = "@ursulineacademy.org"

for student in studentNames:
    email = student+emailAddress
    print(email)

aList = ["poly", "anna"]
print(aList)

userName = input("What is your name? ")
userAddress = input("What is your address? ")

print(userName, userAddress)

#calculate the area of a circle
radius = float(input("What is the radius? "))

areaCircle = 3.14*(radius**2)

print(areaCircle)


principal = 10000
n = 12
r = 0.08
t = float(input("What is the number of years the money will be compounded for? " ))

finalAmount = principal*(1+(r/n))**(n*t)

print(finalAmount)