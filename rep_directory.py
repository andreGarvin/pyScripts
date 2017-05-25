import os
import sys
import json
import time
import platform

REP_directory = {
    '__data__': {
        'OS': platform.system(),
        'time': '11-27-2016'
    }
}

def rep( N, Type ):
    
    
    """
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
    
    """
    
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
        """
        with open('save.json', 'w') as JS:
            JS.write( json.dumps( REP_directory ) )
            JS.close()
        """

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
