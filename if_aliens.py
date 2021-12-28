#! /usr/bin/python3
'''
alien_color = 'blue'

print('exercise1')
if alien_color == 'green':
      print("you get 5 points!")
else:
      print("you dont get 5 points")


print('exercise2a')
alien_color = 'blue'
if alien_color == 'green':
      print("you get 5 points!")
if alien_color != 'green':
      print("you get 10 points!")

print('exercise2b')
alien_color = 'green'
if alien_color == 'green':
      print("you get 5 points!")    
else:
      print("you dont get 5 points")




print('exercise3')
alien_color = 'yellow'
if alien_color == 'green':
      print("you get 5 points!")    
elif alien_color == 'yellow':
      print("you get 10 points!")  
elif alien_color == 'yellow':
      print("you get 15 points!")  
else:
      print("you dont get any points")



print('exercise4')
person_age = 33
if person_age < 2:
      print("baby")
if person_age >= 2 and person_age < 4:
      print("toddler")
if person_age >= 4 and person_age < 13:
      print("kid")
if person_age >= 13 and person_age < 20:
      print("teenager")
if person_age >= 20 and person_age < 65:
      print("adult")
if person_age >= 65:
      print("elder")



requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
      if requested_topping == 'green peppers':
            print(f"we dont have {requested_topping}")
      else: 
            print(f"we have {requested_topping}")


#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
requested_toppings = []
if len(requested_toppings) == 0:
      print("list of ingredients is empty")
else:
      print("list not empty")


available_toppings = ['mushrooms', 'olives', 'green peppers',
      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
           print(f"Adding {requested_topping}.")
    else:
           print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")


print('exercise5-8')

#my_usernames = ['ola', 'ala', 'ela', 'admin', 'ula']
my_usernames = []
login_user = 'admin'
if login_user == 'admin':
      print("hello master")
else:
      print("hello humble user")

if len(my_usernames) == 0:
      print("We need to find some users!")

'''

current_users = ['ola', 'ala', 'ela', 'admin', 'ula']
new_users = ['ola', 'ala', 'zosia', 'tomek']

for new_user in new_users:
      if new_user in current_users:
            print(f" {new_user} this username was already used")
      else:
            print(f" {new_user} this username is available")