#! /usr/bin/python3
'''

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for name in favorite_languages.keys():
    print(name.title())

'''

users = {
       'aeinstein': {
           'first': 'albert',
           'last': 'einstein',
           'location': 'princeton',
           },

       'mcurie': {
           'first': 'marie',
           'last': 'curie',
           'location': 'paris',
           },
       }

for username,user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")