# Program to generate all factors of a number using while loop

num = int(input("Enter a number: "))


i = 1

print("Factors of", num, "are:")


while i <= num:
    if num % i == 0:
        print(i)
    i += 1
