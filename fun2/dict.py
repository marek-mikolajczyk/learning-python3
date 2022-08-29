alien_0 = {'color': 'green', 'speed': 'slow'}

# this does not work 
#print(alien_0['points'])

print(alien_0.get('points', 'NIE MA'))


# loop all key-value pairs

user_0 = {
       'username': 'efermi',
       'first': 'enrico',
       'last': 'fermi',
       }

for k, v in user_0.items():
    print(f"k is {k} and v is {v}")


# loop all keys - skip keys' values

favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for n in favorite_languages.keys():
    print(n.title())

# sorted way
for n in sorted(favorite_languages.keys()):
    print(n.title())

# loop over values
for v in favorite_languages.values():
    print(v.title())

# make unique value - use set

print('make unique value - use set')
for v in set(favorite_languages.values()):
    print(v.title())

# list []
# tupple ()
# set {}