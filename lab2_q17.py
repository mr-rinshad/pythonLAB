n = int(input("Enter number of keys: "))
dict1 = {}

for _ in range(n):
    key = input("Enter the key: ")
    value = int(input("Enter value: "))
    dict1[key] = value

print("Original dictionary:", dict1)


asc = dict(sorted(dict1.items()))


desc = dict(sorted(dict1.items(), reverse=True))

print("Ascending order:", asc)
print("Descending order:", desc)


        
