def compare(s1, s2, n):
    if s1[:n] == s2[:n]:
        return True
    else:
        return False

# Main program
s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
n = int(input("Enter number of characters to compare: "))

result = compare(s1, s2, n)
print("Result:", result)