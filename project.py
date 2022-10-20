import fileinput
import os
import sys
from datetime import date

today = date.today()
print( "Enter user name:")
Name = input()

print( "Hello,", Name )

open( Name, 'a')
    
options = ['add' ,'complete', 'list', 'exit']
while True :
    user_input = ' '

    input_message = "pick an option:\n"

    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'
        
    input_message += "Your Choice: "

    while user_input.lower() not in options:
        user_input = input(input_message)
    user_input == input

    ## Complete requires more testing##
    if user_input == "add":
        print("Type task to be added")
        fd = open(Name,"a")
        fd.write(input())
        fd.write("\n")
        fd.close()
## In progress##
    if user_input == "complete":
        from datetime import date
        today = date.today()
        print ("Text to search for:")
        textToSearch = input( "> " )
        print ("Press Enter to complete the task and remove it from the list.")
        textToReplace = input( "" )

        fileToSearch  = (Name)

        tempFile = open( fileToSearch, 'r+' )
        for line in fileinput.input( fileToSearch ):
            if textToSearch in line :
                print('Task Completed')
            else:
                print('Task not found!!')
            tempFile.write( line.replace( textToSearch, textToReplace ) )
        tempFile.close()

    ##Needs to be fixed, requires two spaces to execute list command.##
    if user_input == "list":
        filepath = Name
        with open(filepath) as fp:
            num_lines = sum(1 for line in fp if line.rstrip())
            line = fp.readline()
            cnt = 1
            print('Total Tasks', num_lines)
        filepath = Name
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Task {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
                    
    if user_input == "exit":
                quit()
        
