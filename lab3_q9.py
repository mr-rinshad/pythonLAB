# Program to check whether a number is an Armstrong number or not

# Accept a number from the user
num = int(input("Enter a number: "))

# Store the original number for comparison
temp = num
sum = 0

# Find the number of digits
digits = len(str(num))

# Loop to calculate sum of digits raised to the power of number of digits
while num > 0:
    digit = num % 10
    sum += digit ** digits
    num //= 10

# Check if the sum is equal to the original number
if temp == sum:
    print(temp, "is an Armstrong number.")
else:
    print(temp, "is not an Armstrong number.")