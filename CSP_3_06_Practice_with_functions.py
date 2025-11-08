#Herons Formula
import math

#returns the square root of the number n
def root(n):
    return math.sqrt(n)
def heron(a,b,c):
    s=(a+b+c)/2
    area=root(s*(s-a)*(s-b)*(s-c))
    return area

#Takes in the 3 side lengths of a triangle as arguments and returns half of
#the perimeter of a triangle.
def semiPerimeter(a,b,c):
    pass
    return (a+b+c)/2

#Modify the below function such that it takes in 4 arguments. multiply the first
#argument by the difference between itself and each individual argument. Reference herons formula for more context.
def multiplyDifferences(s,a,b,c):
    pass
    return s*(s-a)*(s-b)*(s-c)

#Given the 3 sides of a triangle return the area.
#use herons formula
#Use the functions above.
def herons(a,b,c):
    pass
    s=semiPerimeter(a,b,c)
    area_squared=multiplyDifferences(s,a,b,c)
    area=root(area_squared)
    return area

#quadratic equation

#takes in a number as an argument and returns that number multiplied by 2.
def denominator(a):
    pass
    return a * 2

#Takes in two arguments. multiply the first argument by negative 1. Then
#return the modified first argument added and subtracted by the second argument.
def plusMinus(b, value):
    pass
    b=b*-1
    add=b+value
    subtract=b-value
    return add,subtract

#takes in three numbers as arguments. The first and third multiplied together then
#multiplied by 4.Then subtract that result from the second argument squared.
#Return the overall result.
def mainCalc(a,b,c):
    pass
    return b**2-4*a*c

#The below function should take the inputs of the quadratic equation and return the result
#Make sure to use all the formulas from this section.
def quadratic(a,b,c):
    pass
    discriminant=mainCalc(a,b,c)
    if discriminant<0:
        return "Complex roots"
    sqrt_disc=root(discriminant)
    numerator_add,numerator_subtract=plusMinus(b,sqrt_disc)
    den=denominator(a)
    root1=numerator_add/den
    root2=numerator_subtract/den
    return root1,root2
