from sys import argv

def readFile( file_name ):
    with open(file_name, 'r') as of:
        return of.readlines()


def diff( obj ):
    f1=readFile(obj['payload'][0])
    f2=readFile(obj['payload'][1])
    
    if obj['payload'][0] == obj['payload'][1]:
        
        print "*error: same file '%s' was given." % ( obj['payload'][0] )
        return False
    
    else:
        
        for i, j in zip(f1, f2):
            
            if i != '\n' and j != '\n':
                
                if i != j:
                    print '(%s) - %s ' % ( obj['payload'][0], i )
                    print '(%s) - %s ' % ( obj['payload'][1], j )
                
                if i == j:
                    print '(%s) + %s ' % ( obj['payload'][0], i )
                    print '(%s) + %s ' % ( obj['payload'][1], j )




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
    args=argParser(argv[1:])

    diff(args)