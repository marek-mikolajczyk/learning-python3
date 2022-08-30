#!/usr/bin/python3

#with open('test123', 'r') as file_object:
#    contents = file_object.read()
#print(contents.rstrip())

with open('test123', 'r') as file_object:
    lines = file_object.readlines() 

pi_string = ''
for line in lines:
    pi_string += line.rstrip()
    print('my iteration')
    print(len(pi_string))
    print(pi_string)


