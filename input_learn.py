#! /usr/bin/python3
'''
x = input('give your answer:\t')
print(f"you choose {x}")


prompt = "give me your name\n"
prompt += "what is your shoe size?"

print(prompt)


x = input('how old are you?:\t')
x = int(x)

print(x)


available_cars = ['honda','mazda']
x = input('what car you want?:\t')

if x in available_cars:
    print('yeah we have it')
else:
    print('we dont have it currently')


#pizza_toppings = ['cheese', 'pepperoni', 'avocado']

prompt = "enter your topping\n"
prompt += "type 'quit' when done\n"


pizza_toppings = []
while True:
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        pizza_toppings.append(topping)

message = f"Your selected toppings: {pizza_toppings}"
print(message)
'''

prompt = "enter your topping\n"
prompt += "type 'quit' when done\n"

pizza_toppings = []
active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
    else:
        pizza_toppings.append(message)

message = f"Your selected toppings: {pizza_toppings}"
print(message)