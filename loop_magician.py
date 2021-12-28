#! /usr/bin/python3
'''
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
  print(f"{magician.title()}, that was a great trick!")
  print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")



pizzas = ['texas', 'hawai', '4cheese']
for pizza in pizzas:
    print(f"i like {pizza} pizza")

print("i like all of those pizzas!")



for myvalue in range(1,6):
    print(myvalue)


squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
	
print(squares)



➊ squares = []
➋ for value in range(1, 11):
➌     square = value ** 2
➍     squares.append(square)
➎ print(squares)
  squares = []
   for value in range(1,11):
➊     squares.append(value**2)

   print(squares)



# list comprehension
message = []
message = [ value*10 for value in range(1,7,2) ]
print(message)
print(len(message))
'''

players = ['charles', 'martina', 'michael', 'florence', 'eli']
message = [ print(f"{player.title()} is the best") for player in players[:3]]
