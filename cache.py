from time import gmtime, strftime
import os, sys

"""
cache.py, by Andre Garvin, 6-25-2017

    A cli tool built in pytho used to cache tree paths
    in current directories or anyother directories.
    You can cache paths and contents of those paths
    to see if any new files, folders, and sub folders were
    added to the. Saving the in formation to a folder called
    'tree' of all the paths of each path given to this program.

    This tool can also check for any new files or folders,
    upated the cache, clean the cache entire cache storage.
"""
# global varivbles used by the program
cache_str_data, log_message = '', ''
current_time = strftime("%m-%d-%Y", gmtime())

def display_help( action ):

    commands = {
        "logs": {
            "info": """This shows the logs of all or a crertina cache docment/s.""",
            "snippet": [
                "cache logs",
                "cache logs < cache name >"
            ]
        },
        "stat": {
            "info": """Thuis gives a status report of any differnece
                between the cache data from last time the user
                ached it verse the currnet state if the the
                directory. Also gives the last tie used cached
                that folder, the len of the items in it, and
                the amount of paths in the folder.""",
                "snippet": [
                    "cache stat < cache_name >"
                ]
        },
        "checkout": {
            "info": """this dissmises or skips a creatin item from a cahce
                dignosies. Such as any sub folders, dot files, or any
                other items you want to dismiss.\ncreate a cache-checkout file, and list all the files
                or directories to ignore.""",
                "snippet": [
                    "cache checkout"
                ]
        },
        "update": {
            "info": """This literally means what it says, it updates the cache
                of given folder you want it to cache. This as well updates
                the logs on the cache and time stamp it.""",
                "snippet": [
                    "cache update --all",
                    "cache update < cache name >"
                ]
        },
        "clear": {
            "info": """This either deletes a certain cache or clears the whole entire cache foler 'tree' including the logs.""",
                "snippet": [
                    "cache clear < cache name >",
                    "cache clear tree *( deletes the whole cache folder )"
                ]
        },
        "cache": {
            "info": """This is self explanitory, it caches a foler and creates and
                new cache doc for you compresses the data not casuing and memeory
                usage issues.""",
                "snippet": [
                    "cache < cache name >",
                    "cache *( shows the help manual )"
                ]
        },
        "help": {
            "info": "Shows all the commands and how to use them.",
            "snippet": [
                "cache --help"
            ]
        }
    }

    if action != None and action in list( commands ):
        print('\n# %s\n> %s' % ( action, commands[action]['info'] ))

        for i in commands[action]['snippet']:
            print('\t- %s' % ( i ))
        return

    for command in commands:
        print('\n# %s\n> %s' % ( command, commands[command]['info'] ))
        for i in commands[command]['snippet']:
            print('\t- %s' % ( i ))
    return


def handle_error( err_msg ):

    print( err_msg )
    return


def slice_path( _path ):
    _path = os.path.split( _path.strip(' ') )

    paths = []
    _path_len = len( _path ) - 1

    while _path[ _path_len ] != '':
        paths.append( _path[ _path_len ] )
        _path = os.path.split( _path[0] )

    return paths
# with open('tree', 'r') as clogs:
#     _path = clogs.read().split('\n')


def write_to_log( log_data ):

    with open('./tree/.log', 'a+') as lf:
        if log_message != '':
            lf.write('%s# log-message: %s\n' % ( log_data, log_message ) )

        else:
            lf.write('%s' %  ( log_data ) )

        lf.close()


def recursiveDirTree( root, paths ):
    root =  os.path.abspath(root)

    global cache_str_data

    for i in paths:

        _path = os.path.abspath('%s/%s' % ( root, i ) )
        is_path_dir = os.path.isdir( _path )

        cache_str_data += '%s\n' % ( _path )
        if is_path_dir and os.path.basename(_path) != '.git' and os.path.basename(_path) != 'node_modules' and os.path.basename(_path) != 'Heroku' and os.path.basename(_path) != 'MongoDB':

            recursiveDirTree( _path, os.listdir(_path) )

def log_cache( file_name, cache_str_data ):
    global current_time

    with open('./tree/%s' % ( file_name ), 'w') as clogs:
        clogs.write( cache_str_data )
        clogs.close()


def clear_cache( cache_name ):

    if cache_name == 'tree':

        ans = input('Are you sure wyou want to delete main tree cache(Y/n): ')
        if ans == 'Y':
            os.rmdir('tree')
            return 'tree=null'

        return 'tree=0'

    else:
        os.remove('./tree/%s' % ( cache_name ))
        return '%s=null'


def create_cache( _path ):

    if os.path.exists('./tree') and os.path.isdir('./tree'):
        try:
            recursiveDirTree( _path, os.listdir(os.path.abspath(_path)) )
            log_cache( os.path.basename( _path ), cache_str_data )

        except:
            create_cache( os.path.abspath('../%s' % ( _path )) )
    else:
        os.mkdir('tree')
        create_cache( _path )


def argParser( args ):

    obj = {
        'action': '',
        'args': [],
        'payload': []
    }

    if args[0][:2] == '--':
       obj['action'] = args[0][2:]


    for i in args:
        if i[0] == '-' and i[1] != '-':
            obj['args'] = list( i )[1:]
        elif i[0] != '-':
            obj['payload'].append( i )

    return obj


def excute_command( action, args, payload ):

    if len( payload ) != 0:

        if action == 'help' or args[0] == 'h':

            if len( payload ) != 0:
                display_help( payload[0] )

            display_help( None )

        elif action == '':

            noncacheables, cacheables = [], []
            for i in payload:
                if os.path.exists( i ):
                    cachables.append( i )
                    create_cache( i )

                else:
                    noncacheables.append( i )

                    if len( cacheables ) == 0:

                        if len( args ) != 0:
                            exArgs( args )

                            write_to_log('# [ %s ]: %s\n' % ( str( cachables ), current_time ) )
                        else:
                            handle_error('*error: Nothing was cached, exit.')

        # elif action == 'stat':
        # elif action == 'logs':
        elif action == 'clear':

            clear_cache()

        # elif action == 'update':
        # elif action == 'checkout':

        return

    handle_error('*error: This porgram needs the required payload to proceed.')

# main fucntion of program
def main():

    # calls the fucntion argParser to parser the
    # arguements given throuht the command line
    args = argParser( sys.argv[1:] )

    # excute the commands after the arguements have been parsered
    excute_command( args['action'], args['args'], args['payload'] )

if __name__ == '__main__':
    main()
