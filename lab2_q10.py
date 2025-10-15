color_list1=input("Enter color for list 1: ").split()
color_list2=input("Enter color for list 2: ").split()

set1=set(color_list1)
set2=set(color_list2)

result=set1-set2

print("Result:",result)


