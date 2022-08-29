from dog import Dog

my_dog = Dog('Willie', 6)

print(f"my dog name is {my_dog.name}")
print(f"my dog age is {my_dog.age}")

input = input("give command to doggie (sit/roll_over): ")

if input == "sit":
        my_dog.sit()
elif input == "roll_over":
        my_dog.roll_over()