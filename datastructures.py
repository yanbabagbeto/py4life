# zeros = [0] * 5
# letters = ["a", "b", "c"]
# combined = zeros + letters
# numbers = list(range(20))
# print(list("Welcome Home"))

###### Unpacking list #########


# three_numbers = [8, 2, 3]
# first, second, third = three_numbers

# print(first)
# print(third)

# print(f"First and third have been printed")
# numbers = [1, 2, 4, 4, 5, 6, 8, 8, 7, 4, 2, 1]

# alpha, beta, *other = numbers

# print(alpha)
# print(beta)
# print(other)

# thefirst, *in_between, last = numbers
# print(numbers)
# print(in_between)

###### Enumerate #########

letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
