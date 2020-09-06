# To write a program to remove the duplicates in a list.
list1 = [3, 5, 5, 9, 2, 0, 4, 7, 9, 3, 4]
uniques = []
for number in list1:
    if number not in uniques:
        uniques.append(number)
print(uniques)
