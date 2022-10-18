import sys
import os
import fileinput
from datetime import date
today = date.today()
print( "Enter user name:")
Name = input()

print( "Hello,", Name )

open( Name, 'a')
    
options = ['add', 'complete', 'edit' ,'remove', 'list', 'exit']
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

    if user_input == "remove":
        print ("Text to search for:")
        textToSearch = input( "> " )
        print ("Press Enter to confirm and delete the text.")
        textToReplace = input( "> " )
        print ("File to perform Search-Replace on:")
        fileToSearch  = (Name)
        tempFile = open( fileToSearch, 'r+' )
        for line in fileinput.input( fileToSearch ):
            if textToSearch in line :
                print('Match Found')
        else:
            print('Match Not Found!!')
            tempFile.write( line.replace( textToSearch, textToReplace ) )
            tempFile.close()
            input( '\n\n Press Enter to exit...' )


    if user_input == "complete":
           print ("Task to Complete:")
           from datetime import datetime
           now = datetime.now()
           dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
           taskToComplete= input( "> " )
           CompletedTask = "Done "
           fileToSearch  = Name
    #fileToSearch = 'D:\dummy1.txt
    tempFile = open( Name, 'r+' )
    for line in fileinput.input( fileToSearch ):
            if taskToComplete in line :
                tempFile.write(taskToComplete,_,CompletedTask, _, dt_string)
                
    tempFile.close()
  
    ##Needs to be fixed, requires two spaces to execute list command.##
    if user_input == "list":
        filepath = Name
        with open(filepath) as fp:
            line = fp.readline()
            cnt = 1
            while line:
                print("Line {}: {}".format(cnt, line.strip()))
                line = fp.readline()
                cnt += 1
        
    if user_input == "exit":
        quit()
        
