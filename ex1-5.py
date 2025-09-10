
"""
Exercise 1:  Mailing Address
Create a program that displays your name and complete mailing 
address formatted in the manner that you would usually see it 
on the outside of an envelope.  Your program does not need to 
read any input from the user.  (9 lines)
"""

address = """Anna Bonn
8854 Roundhill Rd
Cincinnati OH 45236
"""
print(address)

"""
Exercise 2:  Hello
Write a program that asks the user to enter his or her name.  
The program should respond with a message that says hello to 
the user, using his or her name.  (9 lines)
"""

userName = input("What is your name? ")
print ("Hello " + userName)


"""
Exercise 3:  Area of a Room
Write a program that asks the user to enter the width and 
length or a room.  Once the values have been read, your 
program should compute and display the area of the room.  
The length and the width will be entered as floating point 
numbers.  Include units in your prompt and output message;  
either feet or meters, depending on which unit you are more 
comfortable working with.  (13 lines)
"""

roomLength = float(input("What is the length of the room? "))
roomWidth = float(input("What is the length of the room? "))

areaRoom = (roomLength*roomWidth)
print(areaRoom, " meters")

"""
Exercise 4:  Area of a Field
Create a program that reads the length and width of a 
farmer’s field from the user in feet.  Display the 
area of the field in acres.  
Hint: There are 43,560 square feet in an acre
"""

fieldLength = float(input("What is the length of the field? "))
fieldWidth = float(input("What is the width of the field? "))
areaField = fieldLength*fieldWidth
print (areaField, " square feet")

measureAcres = areaField / 43560
print (measureAcres, "acres")


"""
Exercise 5:  Bottle Deposits
In many jurisdictions a small deposit is added to drink 
containers to encourage people to recycle them.  In one 
particular jurisdiction, drink containers holding one liter 
or less have a $0.10 deposit, and drink containers holding 
more than one liter have $0.25 deposit.
Write a program that reads the number of containers of each 
size from the user.  Your program should continue by computing 
and displaying the refund that will be received for returning 
those containers.  Format the output so that it includes a dollar 
sign and always displays exactly two decimal places.  (15 lines)
"""

def bottleRefund ():
    numOneLiterBottle = int(input("How many bottles contain one liter or less? "))
    numMoreOneLiterBottle = int(input("How many bottles contain more than one liter? "))
    oneRefund = (numOneLiterBottle * 0.10)
    moreRefund = (numMoreOneLiterBottle * 0.25)
    totalRefund = (oneRefund + moreRefund)
    print(totalRefund)
    
bottleRefund()



def print_hi(name):
    print(f"Hi, {name}")


if __name__ == "__main__":
    print_hi("Netbeans")
