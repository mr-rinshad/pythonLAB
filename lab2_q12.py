
numbers = list(map(int, input("Enter integers separated by space: ").split()))


odd_numbers = [num for num in numbers if num % 2 != 0]

print("List after removing even numbers:", odd_numbers)

