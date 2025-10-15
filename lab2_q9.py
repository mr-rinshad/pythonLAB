str1=input("Enter string 1:")
str2=input("Enter string 2:")

newstr1=str1[0]+str2[1]+str1[2:]
newstr2=str2[0]+str1[1]+str2[2:]

str3=newstr1+" "+newstr2
print("Result:",str3)


