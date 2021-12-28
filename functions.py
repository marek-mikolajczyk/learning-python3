#! /usr/bin/python3
'''
usernames = ['Marek', 'Tomek']
def greet_user():
    print(message)

weathertext = "what weather is today?"
weathertoday = input(weathertext)

for username in usernames:
    message = f"hello {username}, what a {weathertoday.title()} we have today"
    greet_user()
'''

def greet_user(username, dayofweek):
    """Display a simple greeting."""
    print(f"Hello, {username.title()}! at {dayofweek}")

greet_user('jesse', 'Tuesday')