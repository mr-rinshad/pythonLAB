names=list(input("enter the names:").split())

count=sum(name.lower().count('a') for name in names)

print("Total occurence of 'a':",count)

