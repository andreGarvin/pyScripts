import sys
import os

def readFile( file_name ):
    with open(file_name,'r') as of:
	 return of.read()

def clone( obj ):
    
    if len(obj['payload']) == 2:
       trg=obj['payload'][0]
       dest=obj['payload'][1]

       with open(trg,'r') as of:
            data=of.read()

	    with open(dest,'w') as df:
		 
		 df.write(data)
		 df.close()

	    of.close()
	    print 'cloning complete'
	    print "Transferred %d bytes from '%s' file to '%s' file." % (len(data), trg, dest)

       return True

    elif len(obj['payload']) > 2:

	 if len(obj['args']) == 0:
            print "*error: this program was given two or more files but recived 0 arguements."
            return False		 

	 args=obj['args']
         if 'd' in args:
	    
            dir=[ f for f in os.listdir('.') if os.path.isdir(f) ]
            payload=obj['payload'][:len(obj['payload'])-1]
            trg_dir=obj['payload'][len(obj['payload']-1)]
            
	    if not(trg_dir in dir):
	       os.mkdir(trg_dir)
	       os.system('cp %s %s' % (' '.join(payload), trg_dir))
               print 'cloning complete.'
	       print "transfered files '%s' to directory '%s'." % (' '.join(payload), trg_dir)
               return True

            print "*error: could not make directory '%s' directory already exist." % (trg_dir)
       
         elif 'f' in args:
              dest=obj['payload'][len(obj['payload'])-1]
              size=0
              for i in obj['payload'][0:len(obj['payload'])-1]:
	          
                  with open(i,'r') as of:
                       data="\n\n\n%s: \n %s"%(i,of.read())
		       
		       size+=len(data)
		       with open(dest,'a+') as df:
                            
			    df.write(data)
			    df.close()
	      print 'cloning complete'
	      print "transferred %d bytes to '%s' file"%(size,dest)

def argParser( args ):
    obj={
	'action': '',
	'args': [],
	'payload': []
    }

    if args[0][0:2] == '--':
       obj['action']=args[0][2:]

    for i in args:
        if i[0] == '-' and i[1] != '-':
           obj['args']=list(i)[1:]
        elif i[0] !=  '-':
             obj['payload'].append(i)

    return obj


if '__main__' == __name__:
   args=sys.argv[1:]

   if len(args) <  1:
      print "*error: this program requires two or more payload arguemts this was given '%d'" % (len(args))


   clone(argParser(args))
   print readFile('../git.txt')
