# 1. Write a Python Program to Find LCM?
# 2. Write a Python Program to Find HCF?
# 3. Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?
# 4. Write a Python Program To Find ASCII value of a character?
# 5. Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?


a=int(input("Enter the first number:"))  # 1. Write a Python Program to Find LCM?
b=int(input("Enter the second number:"))
if(a>b):
    min1=a
else:
    min1=b
while(1):
    if(min1%a==0 and min1%b==0):
        print("LCM is:",min1)
        break
    min1=min1+1

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    def calculate_hcf(x, y):
        # selecting the smaller number
        if x > y:
            smaller = y
        else:
            smaller = x
        for i in range(1, smaller + 1):
            if ((x % i == 0) and (y % i == 0)):
                hcf = i
        return hcf

    print(calculate_hcf(10,40))


