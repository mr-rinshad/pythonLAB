num = int(input("Enter a number: "))
limit = int(input("Enter the limit of the table: "))

print("Multipilication Table of ", num)
for i in range(1, limit+1):
    print(f'{num}x{i}={num*i}')
