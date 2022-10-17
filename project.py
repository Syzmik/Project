import sys
import os
import fileinput
print( "Enter user name:")
Name = input()

print( "Hello,", Name )
try:
    open( Name, 'x')
except FileExistsError:
        pass
        
options = ['add', 'complete', 'edit' ,'remove', 'list', 'exit']

user_input = ' '

input_message = "pick an option:\n"

for index, item in enumerate(options):
    input_message += f'{index+1}) {item}\n'
    
input_message += "Your Choice: "

while user_input.lower() not in options:
    user_input = input(input_message)
user_input == input

if user_input == "add":
    print("Type task to be added")
fd = open(Name,"a")
fd.write(input())
fd.write("\n")

if user_input == "list":
    filepath = Name
with open(filepath) as fp:
   line = fp.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = fp.readline()
       cnt += 1
    

