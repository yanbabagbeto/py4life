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


###### Looping over list and Enumerate #########

# letters = ["a", "b", "c"]
# for index, letter in enumerate(letters):
#     print(f"(index:{index}, {letter})")


######### Add item to list#########

# letters = ["a", "b", "c"]
# # Add at the end
# letters.append("d")
# print(letters)

# # Add at the beginning
# letters.insert(1, "-")
# print(letters)

# # Add after the nth item
# letters.insert(2, "b'")
# print(letters)

# # Remove at the end of the list
# letters.pop(0)
# print(letters)
# letters.remove("b")
# print(letters)
# del letters[1:]
# print(letters)
# letters.clear()
# print(letters)


######### Finding items #########
# letters = ["a", "b", "c"]
# print(letters.count("d"))

# if "d" in letters:
#     print(letters.index("d"))

######### Sorting lists #########
# numbers = [3, 51, 2, 8, 6]
# numbers.sort()
# print(numbers)
# numbers.sort(reverse=True)
# print(numbers)
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))

########## Sorting list with tuples #############

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]


# def sort_item(item):
#     return item[1]


# items.sort(key=sort_item)
# print(items)

########## Lambda expresion or Anonoymous function #############

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# items.sort(key=lambda item: item[1])
# print(items)

# items.sort(key=lambda item: item[1], reverse=True)
# print(items)


######## Map function ############

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# prices = list(map(lambda item: item[1], items))
# print(prices)

######## Filter function ############

# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# filtered_list = list(filter(lambda item: item[1] >= 10, items))
# print(filtered_list)

######## List Comprehension ############
# items = [
#     ("Product1", 10),
#     ("Product2", 9),
#     ("Product3", 12),
# ]

# # variable = [expression for item in items ]
# prices = [item[1] for item in items]
# print(f"Prices : {prices}")
# filtered_list = [item for item in items if item[1] >= 10]

# filtered_list.sort(key=lambda item: item[1], reverse=True)
# print(f"Filtered list: {filtered_list}")
