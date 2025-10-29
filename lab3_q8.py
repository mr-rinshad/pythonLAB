# Program to print the reverse of a number using while loop

# Accept a number from the user
num = int(input("Enter a number: "))

rev = 0   # Variable to store the reversed number

# Loop until the number becomes 0
while num > 0:
    digit = num % 10        # Get the last digit
    rev = (rev * 10) + digit  # Add it to the reversed number
    num = num // 10         # Remove the last digit

print("Reversed number:", rev)