# Program to construct the pattern using nested loops

n = 5  # Number of rows for the upper half

# Upper half of the pattern
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# Lower half of the pattern
for i in range(n - 1, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()