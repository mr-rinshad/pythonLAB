# List of first names
names = ["Rinshad", "Aisha", "Rahul", "Ananya", "Aman", "Sara"]

# Count occurrences of 'a' (case-insensitive)
count = sum(name.lower().count('a') for name in names)

print("Total occurrences of 'a':", count)