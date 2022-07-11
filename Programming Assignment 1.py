# 1. Write a Python program to print 'Hello Python'?
# 2. Write a Python program to do arithmetical operations addition and division.?
# 3. Write a Python program to find the area of a triangle?
# 4. Write a Python program to swap two variables?
# 5. Write a Python program to generate a random number?


print('Hello Python')  # 1. Write a Python program to print 'Hello Python'?


a=int(input('Enter the first number'))   # 2. Write a Python program to do arithmetical operations addition and division.?
b=int(input('Enter Second number'))
c=a+b
d=a/b
print(c,d)


b=int(input('Enter the Base'))   # 3. Write a Python program to find the area of a triangle?
h=int(input('Enter the Height'))
c=0.5*b*h
print(c)


a=int(input('Enter the first number'))  # 4. Write a Python program to swap two variables?
b=int(input('Enter the Second number'))
a,b = b,a
print('After swapping a and b are',a,b)



print(random.randrange(1,20,2))   # 5. Write a Python program to generate a random number?
