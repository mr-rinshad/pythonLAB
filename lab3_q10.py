# Program to construct the pattern using nested loops

n = int(input("Enter the number of stars in upper"))

# Upper 
for i in range(1, n + 1):
    print("*" * i)

# Lower 
for i in range(n - 1, 0, -1):
    print("*" * i)
