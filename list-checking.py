# Program to compare two lists of integers

# Prompt the user to enter two lists of integers
list1 = list(map(int, input("Enter the first list of integers (separated by spaces): ").split()))
list2 = list(map(int, input("Enter the second list of integers (separated by spaces): ").split()))

# Check whether lists are of the same length
if len(list1) == len(list2):
    print("Both lists are of the same length.")
else:
    print("The lists are of different lengths.")

# Check whether the lists sum to the same value
if sum(list1) == sum(list2):
    print("Both lists sum to the same value.")
else:
    print("The lists do not sum to the same value.")

# Check whether any value occurs in both lists
common_values = set(list1) & set(list2)
if common_values:
    print("Common values found in both lists:", common_values)
else:
    print("No common values found between the lists.")