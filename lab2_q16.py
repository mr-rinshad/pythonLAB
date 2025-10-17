# a) Extract positive numbers
print("a)")
numbers = list(map(int, input("Enter integers: ").split()))
pos = [num for num in numbers if num > 0]
print("Positive numbers are:", pos)

# b) Generate squares
print("\nb)")
N = int(input("Enter N to generate squares: "))
sq = [i ** 2 for i in range(1, N + 1)]
print("Squares of numbers from 1 to", N, ":", sq)

# c) Extract vowels from string
print("\nc)")
word = input("Enter a string: ")
vowel = [ch for ch in word if ch.lower() in 'aeiou']
print("Vowels in the given word:", vowel)

# d) Get ordinal values of each character
print("\nd)")
word2 = input("Enter a string: ")
od = [ord(ch) for ch in word2]
print("Ordinal values of each letter in given word:", od)

