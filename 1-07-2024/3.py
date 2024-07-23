#3. *Problem: List Operations*
#   Write a Python program that creates an empty list, prompts the user to enter 5 numbers, adds these numbers to the list, and then prints the list.

x = []

for i in range(5):

    y = int(input(f"Enter number {i+1}: "))
    x.append(y)

print(y)

print("The entered numbers are:", x)
