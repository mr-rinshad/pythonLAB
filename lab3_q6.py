# Program to display a pyramid pattern based on user input

# Accept number of steps from the user
n = int(input("Enter number of steps: "))

# Outer loop for rows
for i in range(1, n + 1):
    # Inner loop for columns
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()  # Move to next line after each row