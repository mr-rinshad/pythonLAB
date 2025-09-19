number=input("Enter intergrs seperated by spaces: ").split()
result=[]

for n in number:
    num=int(n)
    if num >100:
        result.append("over")
    else:
        result.append(num)

print("Result: ",result)        
