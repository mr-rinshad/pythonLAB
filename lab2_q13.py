text=input("enter a string:")

for char in set(text):
    print(char,"=",text.count(char))
