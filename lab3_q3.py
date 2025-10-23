# Program to find the sum of all items in a list using for loop

# Read list elements from user
n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)

# Initialize sum
total = 0

# Find sum using for loop
for num in numbers:
    total += num

print("The sum of all items in the list is:", total)