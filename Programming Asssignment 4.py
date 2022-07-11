# 1. Write a Python Program to Find the Factorial of a Number?
# 2. Write a Python Program to Display the multiplication Table?
# 3. Write a Python Program to Print the Fibonacci sequence?
# 4. Write a Python Program to Check Armstrong Number?
# 5. Write a Python Program to Find Armstrong Number in an Interval?
# 6. Write a Python Program to Find the Sum of Natural Numbers?

num=5  # 1. Write a Python Program to Find the Factorial of a Number?
factorial=1
for i in range(1,num + 1):
       factorial = factorial*i
print("The factorial of",num,"is",factorial)

a=int(input('enter the number for which you want multiplication'))    # 2. Write a Python Program to Display the multiplication Table?
for i in range(1,11):
    print(a,'*',i,'=',a*i)

n = int(input("Enter the value of 'n': "))  # 3. Write a Python Program to Print the Fibonacci sequence?
a = 0
b = 1
sum = 0
count = 1
print("Fibonacci Series: ", end=" ")
while(count <= n):
  print(sum, end=" ")
  count += 1
  a = b
  b = sum
  sum = a + b