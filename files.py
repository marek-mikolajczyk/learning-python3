#! /usr/bin/python3

with open('/etc/hosts', "r") as file_object:
    contents = file_object.read()
print(contents)