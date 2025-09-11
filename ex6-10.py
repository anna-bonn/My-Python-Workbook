"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
def ex6():
    mealCost = float(input("How much was your meal? "))
    mealTax = mealCost * 1.0575
    mealTip = mealCost * 0.18
    totalCost = mealTax + mealTip

    print(totalCost)
    


"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
def ex7():
    n =float(input("Input a positive integer. "))
    sum = (n*(n+1))/2



"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""

def weight():
    widget = 75
    gizmo = 112
    orderGizmo = float(input("How many gizmos did you order? "))
    orderWidget = float(input("How many widgets did you order? "))
    widgetWeight = (orderWidget * widget)
    gizmoWeight = (orderGizmo * gizmo)
    totalWeight = (widgetWeight + gizmoWeight,  "grams")
    print (totalWeight)
    
#weight()



"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
def interest():
    p = float(input("How much money are you entering? "))
    n = 1
    r = 0.04
    t = [1,2,3]
    
    for i in t:
        a = p*(1+(r/n))**(n*i)
        #print(i, type(i))
        print(a)

#interest()
    
"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
import math

def arithmetic():
    a = float(input("What is the value of a?"))
    b = float(input("What is the value of b?"))
    sum = (a+b)
    diff = (a-b)
    quot = (a/b)
    remain = (a%b)
    log10 = math.log(a)
    expo = a**b
    print(sum, diff, quot, remain, log10, expo)
    
arithmetic()  


if __name__ == "__main__":
    print("Hi there!")
