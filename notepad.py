import os
from datetime import *

# Imports time stamp 
now = datetime.now()

current_day = now.day
current_month = now.month
current_year = now.year

current_hour = now.hour
current_minute = now.minute

# formats the current date in a sting
current_date = "%s/%s/%s" % ( current_month, current_day, current_year )

# formats the current time into a string
current_time = "%s:%s" % (current_hour, current_minute)

#  this exits the notepad program
def exitNotePad():
    
    # prompts again to end the notepad program
    exit = raw_input("Would you like to exit notepad? ( Y or N ): ")
    
    # reprompts weather the codiiotns we not true
    while exit != "Y" or exit != "N" or len(exit) == 0:
        exit = raw_input("Would you like to exit notepad? ( Y or N ): ")
    
    # the program will continue and start over
    # and clear the screen
    if exit == "N":
        os.system('clear')
        notePad()


    # if the input was 'N' the program exit
    # and change back to the pervious directory
    elif exit =="Y":
        
        os.chidr('..')
        print "GOODBYE"

def getNotepadName():
    '''
        this promst the user for a name
    '''
    name = raw_input('name: ')
    
    while len( name ) == 0:
        name = raw_input('name: ')
    
    return name

def notePad():
    
    # gets the file name
    file_name = getNotepadName()
    
    note = raw_input("<write> ")
    
    if len( note ) > 0:
        
        # note.split(' ')
        os.chdir('notepad')
        
        # reading and writing permission
        openFile = open(file_name, "wr+")
        
        # writes the note into the file
        openFile.write('%s\t%s\n%s' % ( current_date, current_time, note ) )
        
        print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
        print '( %s )\n' % note 
        print "%d bytes has been saved into the file." % ( len( note ) ) # tells how many bytes of memory was saved on to the file
        print "=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-="
        
        os.chdir('..')
        
        # closes the file
        openFile.close()
    
    # if the user never wrote anthing or doesnt type anything it asks him it asks to continue of not
    if note == 'exit' or len( note ) == 0:
        exitNotePad()

notePad()