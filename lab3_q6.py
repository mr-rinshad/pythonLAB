# Program to display a pyramid pattern based on user input

n = int(input("Enter number of steps: "))


for i in range(1, n + 1):
    
    for j in range(1, i + 1):
        print(i * j, end=" ")
    print()  #move to next row after
