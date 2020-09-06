# Program to find the largest number in the list.
list1 = [2, 7, 23, 67, 99, 34, 109, 5, 265, 34, 23, 642, 56, 764, 435, 753, 345]
max = list1[0]
for i in list1:
    if i > max:
        max = i
print(max)

