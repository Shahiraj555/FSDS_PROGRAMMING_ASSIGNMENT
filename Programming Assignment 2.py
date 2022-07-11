# 1. Write a Python program to convert kilometers to miles?
# 2. Write a Python program to convert Celsius to Fahrenheit?
# 3. Write a Python program to display calendar?
# 4. Write a Python program to solve quadratic equation?
# 5. Write a Python program to swap two variables without temp variable?


k=float(input('Enter the kilometer'))  # 1. Write a Python program to convert kilometers to miles?
d=0.6213*k
print('The miles are',d)

c=float(input('Enter the temperature in celsius')) # 2. Write a Python program to convert Celsius to Fahrenheit?
d=c*1.8+32
print('The temperature in fahrenheit is ',d)

import calendar                 # 3. Write a Python program to display calendar?
yy = int(input("Enter year: "))
mm = int(input("Enter month: "))
print(calendar.month(yy,mm))

a=int(input('Enter the first number'))   # 5. Write a Python program to swap two variables without temp variable?
b=int(input('Enter the Second number'))
a,b = b,a
print('After swapping a and b are',a,b)



