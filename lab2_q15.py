words=input("Enter words:").split()

longword=max(words,key=len)

print("The longest word is :",longword)
print("Length of the long word:",len(longword))
