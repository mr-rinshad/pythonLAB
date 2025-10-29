# Program to generate all factors of a number using while loop

# Accept a number from the user
num = int(input("Enter a number: "))

# Initialize variable
i = 1

print("Factors of", num, "are:")

# Loop to find factors
while i <= num:
    if num % i == 0:
        print(i)
    i += 1