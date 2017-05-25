import os
import sys
import json
import time
import socket


cmds = {
    'ls': os.listdir('.'),
    'pwd': os.getcwd(),
    # '--d': download(),
    # '--s': send()
    # '--w': watch(  )
}


resp = {
    'data': False,
    'result': False
}



def OS_cmds( data ):
    
    
    for cmd in cmds:
        if cmd == data:
            resp['data'] = cmds[cmd]
            resp['result'] = True
            
            return True
        
    if data.split(' ')[0] == 'cd':
        path = os.getcwd().split('/')
        
        # if data.split(' ')[1] == '..':
        #     path.remove( path[len(path) - 1] )
            
        #     path = '/'.join( path )
            
        #     print path
            
        #     # os.chdir( '/'.join( path ) )
        
        #     resp['data'] = 'changed path: ' + str(cmds['pwd'])
        #     resp['result'] = True
        #     return True
        # else:
        
        os.chdir(data.split(' ')[1])
        print '/'.join( path )    
        resp['data'] = 'changed path: ' + str(cmds['pwd'])
        resp['result'] = True
        return True
        
    elif data.split(' ')[0] == 'cat' or data.split(' ')[0] == 'more':
            
        doc = ""
            
        # try:
        with open( data.split(' ')[1], 'r') as of:
            for l in of.read():
                doc += l
            of.close()
        
        resp['data'] = doc
        resp['result'] = True
        return True
    
        # except IOError as e:
        #     resp['data'] = '<ERROR: ' +  str( e ) + '>'
        #     resp['result'] = False
        #     return False
    
    else:
        resp['data'] = "unknown commend: '"+ data +"'."
        resp['result'] = 'null'
    

def Main():
    host = sys.argv[1]
    port = int( sys.argv[2] )
    max_size = 1024
    # 172.20.10.4
    
    sock = socket.socket() 
    sock.bind((host, port))
   
    # lieting up to 5 users
    sock.listen(5)

    # try:
    c, addr = sock.accept()
    print "<client [ "+str(addr)+" ] is connected>"
    # display starting up message
    
    while True:
        req = c.recv(max_size)
        
        if req.decode('utf-8') == 'q' or req.decode('utf-8') == 'kill':
            os.sytem('clear')
            sock.close()
            break
        
        else:
            try:
                OS_cmds( req )
                time.sleep( 1 )
            
                c.send( json.dumps( resp ) )
            except:
                
Main()

