def hello_user(username, day):
    greeting = (f"hello {username}, {day} is a nice day of the week!")
    return greeting

username = input("Give me your username: ")
day = input("Give me day of the week: ")

hello_user(username='zosia', day='wtorek')

print 