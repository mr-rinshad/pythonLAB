list1 = list(map(int, input("Enter the first list: ").split()))
list2 = list(map(int, input("Enter the second list: ").split()))

if len(list1) == len(list2):
    print("Both lists are of the same length")
else:
    print("Lists are not of the same length")

if sum(list1) == sum(list2):
    print("Both lists have the same sum")
else:
    print("Lists do not have the same sum")

common = set(list1) & set(list2)

if common:
    print("Common values are:", common)
else:
    print("No common values")



