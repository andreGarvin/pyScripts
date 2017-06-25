import os

def clear_cache():

    clogs = open('tree', 'w')
    clogs.write('')
    clogs.close()

def log_cache( _path ):

    with open('tree', 'a+') as clogs:

        clogs.write('\n %s' % ( _path ))
        clogs.close()

def recursiveDirTree( root, paths ):
    root =  os.path.abspath(root)

    for i in paths:

        _path = os.path.abspath('%s/%s' % ( root, i ) )
        is_path_dir = os.path.isdir( _path )

        log_cache( _path )
        if is_path_dir and os.path.basename(_path) != '.git' and os.path.basename(_path) != 'node_modules' and os.path.basename(_path) != 'Heroku' and os.path.basename(_path) != 'MongoDB':

            recursiveDirTree( _path, os.listdir(_path) )


clear_cache()
recursiveDirTree( '../', os.listdir(os.path.abspath('../')) )
