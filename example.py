


# def converter(celsius):
#     result = (celsius * 9/5) + 32 
#     return  str(celsius) + ' degrees Celsius are ' + str(result) + ' degrees Farenheit.'



# print(converter(21.5))
# print(converter(-7))
# print(converter(11))
# print(converter(0))

# 18.5 degrees Celsius are 65.3 degrees Farenheit.


# def currConverter(usd):
#     egp = usd * 50
#     return str(egp) + " EGP equal to " + str(usd) + " USD."


# print(currConverter(50))



# print("Please enter your name:")

# name = input()

# print("Your name is " + name)

# name = input("Please enter your name: ")
# print("Your name is " + name)


# x = input("Enter a number: ")
# y = input("Enter a second number: ")
# result = int(x) + int(y)

# message = "The result of " + x + " plus " + y + " is " + str(result)

# print(message)

# def converter():
#     celsius = input("Enter a temperature in degrees Celsius: ")
#     result = (int(celsius) * 9/5) + 32 
#     return  celsius + ' degrees Celsius are ' + str(result) + ' degrees Farenheit.'


# print(converter())



# secret_word = "kiwi"
# guess = input("write secret word: ")
# print(secret_word==guess)

# res = 7
# cal = input("What is the result of 5+2?: ")

# if res == int(cal):
#     print("Congratulations! You found the correct result.")

# print("The program terminated successfuly")


# def currConverter(usd):
#     egp = usd * 50
#     if egp >= 100000:
#         print("this is a lot of money")
#     return str(egp) + " EGP equal to " + str(usd) + " USD."


# print(currConverter(100000))


# secret_word = "kiwi"
# guess = input("write secret word: ")
# if secret_word != guess:
#     print("Ooops! You didn't guess the secret word!")
# else:
#     print(secret_word==guess)


# first_no = input("write first number: ")
# second_no = input("write second number: ")

# subtract = int(first_no) - int(second_no)

# if subtract > 10:
#     print("The result is greater than 10.")
# elif subtract > 0:
#     print("The result is greater than 0 but not than 10.")
# elif subtract == 0:
#     print("The result is zero")
# else:
#     print("The result is a negative number.")


# no1 = input("write first number: ")
# no2 = input("write second number: ")

# if float(no1) > 10 and float(no2) > 10:
#     print("Both numbers are greater than 10.")
# else:
#     print("At least one of the numbers you entered is not greater than 10.")





# def guess_game(secret_number , secret_color):
#     number = input("write number between 1 to 20: ")
#     color = input("Choose a color: ")   


#     if float(number) == secret_number and color == secret_color:
#         print("You've found both the secret number and the secret color!")
#     elif float(number) == secret_number or color == secret_color:
#         print("You found at least one of the secrets!")
#     else:
#         print("You didn't find any of the secrets!")
#         print("Better luck next time!")
#     print("Try again!")


# guess_game(5, "green")



# def greet(name, age):
#     message = "Your name is " + name + " and you are " + age + " years old."
#     return message

# name = input("Enter your name: ")
# age = input("Enter your age: ")

# print(greet(name, age))



# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# num_one = input("Enter a number: ")
# num_two = input("Enter another number: ")

# message = "The result of " + num_one + " + " + num_two + " is " + str(add(float(num_one), float(num_two)))
# print(message)

# message = "The result of " + num_two + " - " + num_one + " is " + str(subtract(float(num_one), float(num_two)))
# print(message)


# def get_result(answer):
#     if answer == 'a':
#         return True
#     else:
#         return False

# print("Do you like programing?")
# print("a. Yes")
# print("b. No")
# result = input("Enter a or b: ")

# if get_result(result):
#     print("Awesome! Programming is really fun!")
# else:
#     print("Hang in there! It's an acquired taste!")


# commit converter function

