#6. *Problem: List Modification*
   #Write a Python program that initializes a list with 5 integer values. Prompt the user to enter a new integer value and append this value to the list. Print the modified list.

list = [1,2,3,4,5]

new = int(input("enter integer value: "))

list.append(new)

print(list)