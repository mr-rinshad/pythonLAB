def check_even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

n = int(input("Enter a number: "))
result = check_even_odd(n)
print("The number is", result)
