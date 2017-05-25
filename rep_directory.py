import os
import sys
import json
import platform
'''
REP_directory = {
    '__data__': {
        'OS': platform.system(),
        'time': '11-27-2016'
    }
}

def rep( N, Type ):
    
    
    
        file_name : {
            'content': '',
            'size': 0
        }
        
        dir_name: [
            {
                'file_name': '',
                'content': '',
                'size': 0
            }
        ] 
    
    
    try:
        if Type == 'f':
            # os.system('chmod u+rw '+ N)
            REP_directory[ N ] = {}
            
            with open( N, 'r' ) as f:
                REP_directory[ N ]['content'] = f.read()
                REP_directory[ N ]['size'] = len( f.read() )
            print("[ ** downloaded: "+ N +" ** ]")
            
        elif Type == 'dir':
            if N != 'data' and N != '.c9' and N != '.git':
                REP_directory[ N ] = ''
            
                os.chdir( N )
            
                main()
                # REP_directory[ N ] = os.listdir('.')

                os.chdir('..')
            else:                  

                REP_directory[ N ] = ''
        
                os.chdir( N )

                REP_directory[ N ] = os.listdir('.')

                os.chdir('..')

            print("< *** "+ N +" *** >")
    except:
        print "<ERROR: failed to rep.>"
        
        with open('save.json', 'w') as JS:
            JS.write( json.dumps( REP_directory ) )
            JS.close()
        

    with open('save.json', 'w') as JS:
        JS.write( json.dumps( REP_directory ) )
        JS.close()

def main():
    
    directory = [ f for f in os.listdir('.') ]
    
    for i in directory:
        if i != 'collect.py' and i != 'save.json':
            if os.path.isfile( i ):
            
                print("[ downloading ~> "+ i +" ]")
                rep( i, 'f' )
    
            elif os.path.isdir( i ) :
                print("{ REP: '"+ i + "' }")
                rep( i, 'dir' )
main()
'''

def cloneDir(lvl,dirpath,dest_file):
    
    if os.path.isdir(dirpath):
       cur_dir=os.listdir(dirpath)
       
       
       obj = {
           'type': 'root',
           'dirpath': '',
	   'contents': {}
       }
       for i in cur_dir:
           if os.path.isfile(i):
	      data=readFile(i)
              obj['contents'][i]={
                 'type': 'file',
		 'data': data,
		 'size': len(data)
	      }
           elif os.path.isdir("%s/%s"%(dir_path,i)):
                obj['contents'][i]={
                   'type': 'dir',
		   'contents': {},
                   'len': len(os.listdir("%s/%s"%(dir_path,i)))
		}
       if lvl == 0:
          return obj
       else:
            


if '__main__' == __name__:
   args=sys.argv[1:]
   cloneDir(1,args[0],args[1])
