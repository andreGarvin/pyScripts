import sys
import os

def readFile( file_name ):
    with open(file_name, 'r') as of:
        return of.read()


def clone( obj ):

    if len(obj['payload']) == 2:
        trg=obj['payload'][0]
        dest=obj['payload'][1]
        
        data=readFile(trg)
        with open(dest, 'w') as df:
            df.write(data)
            
            df.close()
        
        print 'Cloning complete.'
        print "Transferred %d bytes from '%s' file to '%s' file" % ( len(data), trg, dest )
        
        return True
    
    elif len(obj['payload']) > 2:
        
        if len(obj['args']) == 0:
            print '*error: This is program was two or more files but recieved 0 arguments'
            return False
        else:
            
            args=obj['args']
            if 'd' in args:
                
                directory=[ f for f in os.listdir('.') if os.path.isdir(f) ]
                payload=obj['payload'][:len(obj['payload'])-1]
                trg_dir=obj['payload'][len(obj['payload'])-1]
                
                if not(trg_dir in directory):
                    os.mkdir(trg_dir)
                    os.system('cp %s %s' % (' '.join(payload), trg_dir))
                    
                    print 'Cloning complete.'
                    print "Transferred %s files to directory '%s'" % (' '.join(payload), trg_dir)
                    return True
            
            elif 'f' in args:
                dest=obj['payload'][len(obj['payload'])-1]
                size=0
                
                for i in obj['payload'][:len(obj['payload'])-1]:
                    
                    data='\n\n\n%s: \n %s'%(i, readFile(i))
                    
                    size+=len(data)
                    with open(dest,'a+') as df:
                        
                        df.write(data)
                        df.close()
                
                print 'Cloning complete.'
                print "Transferred %d bytes to '%s' file" % (size, dest)




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
        clone(argParser(args))