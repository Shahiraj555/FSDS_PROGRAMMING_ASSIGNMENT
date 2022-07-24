# 1. Write a Python Program to Display Fibonacci Sequence Using Recursion?

def fibo(n):
    if(n<=1):
        return n
    else:
        return fibo(n-1)+fibo(n-2)
a=int(input("Enter the no.of terms: "))
if(a<=0):
    print("Entered Number is Negative or Zero")
else:
    print("The Fibonacci Sequence is:")
    for i in range(a+1):
        print(fibo(i),end=' ')

#2. Write a Python Program to Find Factorial of Number Using Recursion?

def fact(n):
    return 1 if(n==0 or n==1) else n*fact(n-1)
n=int(input("Enter the value for n: "))
print("Factorial of {0} is {1}".format(n,fact(n)))


#3. Write a Python Program to calculate your Body Mass Index?
height=float(input("Enter height (in cm): "))
weight=float(input("Enter weight (in kg): "))
BMI=weight/((height/100)**2)
print("The BMI for the given height=%.2f and weight=%.2f is %.2f"%(height,weight,BMI))

#4. Write a Python Program to calculate the natural logarithm of any number?
import math
n=int(input("Enter the value for n: "))
print("Natural logarithm for the given number n={0} is {1}".format(n,math.log(n)))

#5. Write a Python Program for cube sum of first n natural numbers?
n=int(input("Enter the value for n: "))
Cube_Sum=0
for i in range(1,n+1):
    Cube_Sum+=i**3
print("The Cube Sum of the given number n={0} is {1}".format(n,Cube_Sum))