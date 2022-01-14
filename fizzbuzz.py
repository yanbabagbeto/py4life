def fizz_buzz(input):
    if input % 5 == 0 and input % 3 == 0:
        return "FizzBuzz"
    elif input % 3 == 0:
        return "Fizz"
    elif input % 5 == 0:
        return "Buzz"
    else:
        return input


print(f"{fizz_buzz(30)}: 30")
print(f"{fizz_buzz(20)}: 20")
print(f"{fizz_buzz(90)}: 90")
print(f"{fizz_buzz(9)}: 9")
print(f"{fizz_buzz(45)}: 45")
print(f"{fizz_buzz(17)}: 17")
