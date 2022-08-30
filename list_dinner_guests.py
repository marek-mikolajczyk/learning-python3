#! /usr/bin/python3

friends_list = ['ola','ala','ela','ula']
initial_message = f"those are all guests invited: {friends_list}"
print(initial_message)
# lets invite zosia
friends_list.append('zosia')

# too many guests invited - remove 2 friends
popped_friend1 = friends_list.pop()
popped_friend2 = friends_list.pop()

# send message to removed friends
message1 = f"sorry {popped_friend1.title()} , not enough space!"
print(message1)
message2 = f"sorry {popped_friend2.title()} , not enough space!"
print(message2)

message = f"those are my confirmed guests now:  {friends_list}"
print(message)
# i dont like ola anymore
print("i just argued with ola")
dislike_friends = 'ola'
friends_list.remove(dislike_friends)
message = f"now my only friends are {friends_list}"
print(message)

# guests now allowed to invite animals
friends_list.append('kitty')
message = f"after allowing animals, this is my guest list: {friends_list}"
print(message)

# first guest will not come
del friends_list[0]
message = f"after guests who cancelled, this is my guest list: {friends_list}"
print(message)

# lets add doggy between guests
friends_list.insert(1, 'doggy')
message = f"after inserting doggy, this is my guest list: {friends_list}"
print(message)

guests_amount = len(friends_list)
message = f"number of guests: {guests_amount}"
print(message)