# Program to count occurrences of each word in a line of text

# Input a line of text
text = input("Enter a line of text: ")

# Split the text into words
words = text.split()

# Create an empty dictionary to store word counts
word_count = {}

# Count occurrences of each word
for word in words:
    word = word.lower()  # Optional: make counting case-insensitive
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Display the word counts
print("Word occurrences:")
print(word_count)