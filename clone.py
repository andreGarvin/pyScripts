import sys
import os

def readFile( file_name ):
    with open(file_name, 'r') as of:
	 return of.read()


'''
def clone( obj ):

    if len(obj['payload']) == 2:
        
    elif len(obj['payload']) > 2:
'''

def argParser( args ):

    obj = {
        'action': '',
        'args': [],
        'payload': []
    }

    if args[0][:2] == '--':
       obj['action']=args[0][2:]
    
    
    for i in args:
        if i[0] == '-' and i[1] != '-':
            obj['args']=list(i)[1:]
        elif i[0] != '-':
            obj['payload'].append(i)
    
    return obj
    

if '__main__' == __name__:
    args=sys.argv[1:]
    
    if len(args) < 1:
        print "*error: This program requires two or more payload arguements this recvied '%d'" % (len(args))
    else:
        argParser(args)