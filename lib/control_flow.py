#!/usr/bin/env python3

def admin_login(username, password):
    if (username.lower() == "admin" and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

result = admin_login("ADMIN", "12345")
print(result)


def hows_the_weather(temperature):
    # your code here
    if (temperature < 40):
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

result = hows_the_weather(75)
print(result)     
    


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

result = fizzbuzz(15)
print(result)        

def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None

result = calculator( "nope" , 90, 2)
print(result)

# def divide(num1, num2):
#     try:
#         quotient = num1 / num2
#         print(quotient)
#     except ZeroDivisionError:
#         print("Error: num2 cannot be equal to 0")
#     except TypeError:
#         print("Error: input must be of type int or float")
#     finally:
#         print("Isn't division fun?")

# divide (6,3)

# dog = "cuddly"

# dict_map = {
#     "hungry": "Refilling food bowl.",
#     "thirsty": "Refilling water bowl.",
#     "playful": "Playing tug-of-war.",
#     "cuddly": "Snuggling.",
# }

# # Remember that a dictionary's .get() method lets us set a default value!
# owner = dict_map.get(dog, "Reading newspaper.")