a=int(input("Enter the 1st number: "))
b=int(input("Enter the 2nd number: "))
c=int(input("Enter the 3rd number: "))

if a>=b and a>=c:
    big=a
elif b>=a and b>=c:
    big=b
else:
    big=c

print("The biggest number is: ",big)    

