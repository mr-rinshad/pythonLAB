n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    value = int(input("Enter number: "))
    numbers.append(value)


total = 0


for num in numbers:
    total += num

print("The sum of all items in the list is:", total)
