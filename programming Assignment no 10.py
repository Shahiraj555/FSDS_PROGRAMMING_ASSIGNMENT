#1. Write a Python program to find sum of elements in list?

lst = [1,2,3,4,5,6,7,8,9]
def sum_list(l):
    sum = 0
    for i in l:
        sum += i
    return sum
result = sum_list(lst)
print("The sum of elements in the list is: ", result)

#2. Write a Python program to Multiply all numbers in the list?
lst = [1,2,3,4,5,6,7]
def mult_list(l):
    mult = 1
    for i in l:
        mult *= i
    return mult

result = mult_list(lst)
print("The multiplication of elements in the list is: ", result)

#3. Write a Python program to find smallest number in a list?
lst = [21,32,13,478,5,66,87]
def sml_list(l):
    r = len(l)
    for i in range(r):
        sml_l = sorted(l)[0]
    return sml_l
result = sml_list(lst)
print(f"The smallest number in the list {lst} is {result}")

#5. Write a Python program to find second largest number in a list?

lst = [21,32,13,478,5,66,87]
def lar_list(l):
    r = len(l)
    for i in range(r):
        lar_l = sorted(l)[-2]
    return lar_l
result = lar_list(lst)
print(f"The second largest number in the list {lst} is {result}")

#7. Write a Python program to print even numbers in a list?
lst = [21,32,13,478,5,66,87,65,23,435,7,91]
def lar_list(l):
    lar_l = [i for i in l if i%2 == 0]
    return lar_l
result = lar_list(lst)
print(f"The even numbers in the list {lst} are {result}")