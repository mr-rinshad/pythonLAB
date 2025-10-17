n1=int(input("Enter no.of key for dict 1:"))
dict1={}

for _ in range(n1):
    key=input("Enter key:")
    value=input("Enter value:")
    dict1[key]=value

n2=int(input("Enter no.of key for dict 2:"))
dict2={}

for _ in range(n2):
    key=input("Enter key:")
    value=input("Enter value:")
    dict2[key]=value
   

merged = dict1.copy()
merged.update(dict2)

print("Merged dictionary:", merged)
