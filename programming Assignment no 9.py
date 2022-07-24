#1. Write a Python program to check if the given number is a Disarium Number?

num = input('Enter a Number: ')
def DisariumNumber(num):
    sum = 0
    for item in range(len(num)):
        sum = sum + int(num[item]) ** (item + 1)
    return sum
result = DisariumNumber(num)
if result == int(num):
    print(f'{num} is a Disarium Number')
else:
    print(f'{num} is a Not Disarium Number')



#2. Write a Python program to print all disarium numbers between 1 to 100?
def DisariumNumbers(start=0, end=100):
    output_num = []
    for number in range(start, end + 1):
        sum = 0
        for item in range(len(str(number))):
            sum = sum + int(str(number)[item]) ** (item + 1)
        if sum == number:
            output_num.append(number)
    return output_num
output = DisariumNumbers(1, 100)
print("All disarium numbers between 1 to 100 are: ", output)

#5. Write a Python program to determine whether the given number is a Harshad Number?
def HarshadNumber():
    num = input('Enter a Number: ')
    sum = 0
    for item in range(len(num)):
        sum = sum + int(num[item])
    if int(num) % sum == 0:
        print(f'{num} is a Harshad Number')
    else:
        print(f'{num} is a Not Harshad Number')


HarshadNumber()
HarshadNumber()