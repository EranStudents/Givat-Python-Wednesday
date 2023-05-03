# Find all the even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)

# Find all the strings that start with a capital letter in a list
strings = ["apple", "Banana", "cat", "dog", "Elephant"]
capital_letter_strings = list(filter(lambda x: x[0].isupper(), strings))
print(capital_letter_strings)

# Find all the numbers that are greater than 10 in a list
numbers = [1, 29, 3, 42, 11, 6, 7, 8, 9, 10]
numbers_greater_than_10 = list(filter(lambda x: x > 10, numbers))
print(numbers_greater_than_10)
