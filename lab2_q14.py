word=input("Enter a world:")

if len(word)>=3:
    if word.endswith("ing"):
        word +="iy"
    else:
        word +="ing"

print("Result:",word)
