import sys
print( "Enter user name:")
Name = input()

print( "Hello,", Name )
try:
    open( Name, 'x')
except FileExistsError:
        pass
        
print( "What would you like to do ? add, delete, view or edit")
input() == Choice)
if Choice == add :
    print( "Write what the next task is, then press enter.")
    
