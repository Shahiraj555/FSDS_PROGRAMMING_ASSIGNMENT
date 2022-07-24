#1. Write a Python Program to find sum of array?

in_arr = eval(input("Enter the Array: "))

# Creating the function
def sum_of_array(l):
    l = list(l)
    result = 0
    for i in list(l):
        result += i
    return result
res = sum_of_array(in_arr)
print(f"The result of the entered array {list(in_arr)} is: {res}")


#2. Write a Python Program to find largest element in an array?
in_arr = eval(input("Enter the Array: "))

def largest_element(l):
    l = list(l)
    l.sort()
    n = l[-1]
    return n
res = largest_element(in_arr)
print(f"The largest element of the entered array {list(in_arr)} is: {res}")


#3. Write a Python Program for array rotation?
in_arr = eval(input("Enter the Array: "))
def rev_arr(l):
    l = list(l)
    l.reverse()
    return l
res = rev_arr(in_arr)
print(f"The rotated form of the entered array {list(in_arr)} is: {res}")

#4. Write a Python Program to Split the array and add the first part to the end?

arr = [10, 8, 7, 6, 34, 23, 56, 67]
n = len(arr)
position = 3
def splitArr(arr, n, k):
    for i in range(0, k):
        x = arr[0]
        for j in range(0, n - 1):
            arr[j] = arr[j + 1]

        arr[n - 1] = x
splitArr(arr, n, position)

for i in range(0, n):
    print(arr[i], end=' ')

#5. Write a Python Program to check if given array is Monotonic?
in_arr1 = eval(input("Enter the 1st Array: "))
in_arr2 = eval(input("Enter the 2nd Array: "))
def checkMonotonic(in_arr):
    if(all(in_arr[i]<=in_arr[i+1] for i in range(len(in_arr)-1)) or all(in_arr[i]>=in_arr[i+1] for i in range(len(in_arr)-1))):
        print(f'Array {in_arr} is Monotonic')
    else:
        print(f'Array {in_arr} is Not Monotonic')
checkMonotonic(in_arr1)
checkMonotonic(in_arr2)