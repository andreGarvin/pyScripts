from time import gmtime, strftime
import os, sys

# def insert( _str_, insert_str ):
#     return '%s\n%s' % ( _str_, insert_str )
"""
cache.py, by Andre Garvin, 6-25-2017

    A cli tool built in python used to cache tree paths
    in current directories or anyother directories.
    You can cache paths and contents of those paths
    to see if any new files, folders, and sub folders were
    added to the. Saving the in formation to a folder called
    'tree' of all the paths of each path given to this program.

    This tool can also check for any new files or folders,
    upated the cache, clean the cache entire cache storage.
"""
# global varivbles used by the program
destory_cacahe_True = False
cache_str_data, log_message = '', ''
current_time = strftime("%m-%d-%Y", gmtime())

def display_help( action ):
    # This display a specfic command or all the commands
    # descriptions and command snippets

    # all the commands along with their description and command snippets
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


    if command_exist( action ):

        # checks weather the fucntion was given a specfic command to read
        if action != None:
            # if so ddisplay the command name, description
            print('\n# %s\n> %s' % ( action, commands[action]['info'] ))

            # and the command snippets
            for i in commands[action]['snippet']:
                print('\t- %s' % ( i ))
            return

        # else show all the coammands, their descriptions, and snippets
        for command in commands:
            print('\n# %s\n> %s' % ( command, commands[command]['info'] ))
            for i in commands[command]['snippet']:
                print('\t- %s' % ( i ))
        return

    handle_error("*error: Unknown command '%s', ecute `cache --help` to see all commands.")
    return


def command_exist( action ):
    # retruns true if the command exist else false
    commands = ['help', 'clear', 'cache', 'checkout', 'logs', 'update', 'stat']

    if action in commands:
        return True
    return False

def readFile( file_name ):
    # reads a file and returns the file content
    with open( file_name, 'r') as of:
        data = of.read()
        of.close()
        return data

def handle_error( err_msg ):
    # prints the error message to the treminal
    print( err_msg )
    return


def slice_path( _path ):
    """
        Returns back a list of gets all the paths
        sliced from the '_path' string
    """
    # striping the string of whitespace & getting the
    # paths from the string truning it into a tuple
    #   ( 'C:\\Users\\andre\\projects', 'pyScripts' )
    _path = os.path.split( _path.strip(' ') )

    paths = []
    _path_len = len( _path ) - 1

    # while last item in the '_path' tuple does not euwal a empty string
    while _path[ _path_len ] != '':
        # using the current length of the '_path' tuple to get the last item of the tulple
        # append the strng to the 'paths' list
        paths.append( _path[ _path_len ] )

        # then set the first item of the tuple and split paths then assign back to '_path'
        _path = os.path.split( _path[0] )

    # return the 'paths' list
    return paths


# def insert( _str_, insert_str ):
#     return '%s\n%s' % ( _str_, insert_str )

def diff( arr_1, arr_2 ):
    """
        Prints the differnece between two
        list and poin the to that index;
        vice versa for strings
    """

    print('runn')
    print( '\n'.join( arr_1 ) )
    print()
    print( '\n'.join( arr_2 ) )
    print()

    diffs = []
    for i in arr_2:
        if i not in arr_1:
            diffs.append( os.path.basename( i ) )

    return diffs

# def get_log( pointer ):

def write_to_log( log_data ):
    """
        Making a logger for the data
        being cached.
    """
    # open a file to write to called '.log'
    with open('./tree/.log', 'a+') as lf:
        # write the formatted dataa to the log file
        if log_message != '':
            lf.write('%s# log-message: %s\n' % ( log_data, log_message ) )

        else:
            lf.write('%s' %  ( log_data ) )

        lf.close()


def recursive_dir_tree( root, paths ):
    """
        This function recursivley goes
        through all directories and sub
        dictrectories getting all paths
        to all files and sub diretory.
    """
    # make the 'root' path given a absolute path
    root =  os.path.abspath(root)

    # import 'cache_str_data'
    global cache_str_data

    # iterate over each item in the 'paths' list
    for i in paths:

        # make a new path based by concactenating the 'root' path and the new path 'i'
        # reslove the absoulte path of the new formatted path
        _path = os.path.abspath('%s/%s' % ( root, i ) )
        is_path_dir = os.path.isdir( _path )

        # concactenate the str of the paths over each recurison
        cache_str_data += '%s\n' % ( _path )
        if is_path_dir and os.path.basename(_path) != '.git' and os.path.basename(_path) != 'node_modules' and os.path.basename(_path) != 'Heroku' and os.path.basename(_path) != 'MongoDB':

            # if the '_path' is a directory then call the fucntion passing
            # in the 'root' path which was the new path ( '_path' ) and the a
            # list of all the files or sub folders of that new path
            recursive_dir_tree( _path, os.listdir(_path) )


def log_cache( file_name, cache_str_data ):
    """
        This fucntion wites all the paths
        of the concactenated string 'cache_str_data'
        in the tree folder.
    """
    # import current_time
    global current_time

    # write the data to the file
    with open('./tree/%s' % ( file_name ), 'w') as clogs:
        clogs.write( cache_str_data )
        clogs.close()


def clear_cache( cache_name ):
    """
        Clears the cache data of
        a given cache file or the
        entire cache folder. However
        not including the .logs file
    """
    if cache_name == 'tree':

        ans = input('Are you sure wyou want to delete main tree cache(Y/n): ')
        if ans == 'Y':
            os.rmdir('tree')
            return 'tree=null'

        # returns this status report
        return 'tree=0'

    else:
        os.remove('./tree/%s' % ( cache_name ))
        return '%s=null'


def create_cache( _path ):
    """
        creates a cache document in the tree folder
    """
    # first checks to see that the tree folder exist and is a folder
    if os.path.exists('./tree') and os.path.isdir('./tree'):
        try:
            # call the recursiveDirTree() passing in the '_patgh" and the items in that path
            recursive_dir_tree( _path, os.listdir(os.path.abspath(_path)) )
            # call the log_cache()
            log_cache( os.path.basename( _path ), cache_str_data )

        except:
            # if any erros occur such as the '_path' given not being abslotue path
            create_cache( os.path.abspath('../%s' % ( _path )) )
    else:
        # creates the folder called 'tree' and calls create_cache() passing back the original given '_path'
        os.mkdir('tree')
        create_cache( _path )


def stat( _path ):
    """
        Gives a status report of the cached document
        such as:
            - new files
            - deleted files
            ? files being moved
            - number of paths
            - the last log made saved
                to the .log file realted
                to cache doument
    """
    stat_report = {
        'diffs': [],
        'paths': [],
        'mia': [],
        'log': get_log( _path )
    }
    # importing the 'cache_str_data'
    global cache_str_data

    cache_file = './tree/%s' % ( _path )

    if os.path.exists(cache_file):
        cached_paths = readFile(cache_file).split('\n')


        try:
            recursive_dir_tree( _path, os.listdir(os.path.abspath(_path)) )
        except:
            _path = os.path.abspath('../%s' % ( _path ))
            recursive_dir_tree( _path, os.listdir( _path ) )

        cache_str_data = cache_str_data.split('\n')

        stat_report['diffs'] = diff( cached_paths, cache_str_data )
        stat_report['mia'] = diff( cache_str_data, cached_paths )
        print( stat_report )
        # display_report(diffs)



def ex_args( args, data ):
    """
        Excutes any args ( flags ) passed in by
        the command line
    """
    # iterates over each command arg in the list args
    # and excutes them, along with the data passed in
    # the function exArgs()
    for i in args:
        if i == 'm':
            log_message = ' '.join( data )
        elif i == 'all':
            destory_cacahe_True = True
    return


def excute_command( action, args, payload ):

    if len( payload ) != 0:
        if action == 'help' or 'h' in args:

            if len( payload ) != 0:
                display_help( payload[0] )
            else:
                display_help( None )

        elif action == 'create':
            noncacheables, cachables = [], []

            for i in payload:
                if os.path.exists( i ):
                    cachables.append( i )
                    create_cache( i )

                else:
                    noncacheables.append( i )

                    if len( cachables ) == 0:
                        if len( args ) != 0:
                            ex_args( args, noncachables )

                            write_to_log('# [ %s ]: %s\n' % ( str( cachables ), current_time ) )

                    else:
                        handle_error('*error: Nothing was cached, excute `cache --help < command name >` for help on command usage; exit.')

        elif action == 'clear':
            clear_cache( payload )

        elif action == 'stat':
            stat( payload[0] )

        # elif action == 'logs':
        # elif action == 'update':
        # elif action == 'checkout':
        return

    # else:
    #     if not command_exist( action ):
    #         handle_error("*error: Unknown command '%s', excute `cache --help < command name >` for the commands and usage." % ( action ))
    handle_error('*error: This program needs the required payload to proceed.')


def arg_parser( args ):
    """
        This parsers the arguements
        passed down from the command
        line.
    """
    obj = {
        'action': '',
        'args': [],
        'payload': []
    }

    # assigns any argument with a '--' to the 'action' key
    if args[0][:2] == '--':
       obj['action'] = args[0][2:]

    # iterates over all the arguments
    for i in args:
        # if the command only has '-' then append to the 'args' key list
        if i[0] == '-' and i[1] != '-':
            obj['args'] = list( i )[1:]
        # else append it to the 'payload' key list
        elif i[0] != '-':
            if args.index( i ) == 0:
                obj['action'] = i
            else:
                obj['payload'].append( i )

    # return the object once itis parsed
    return obj


# main fucntion of program
def main():

    # calls the fucntion argParser to parser the
    # arguements given throuht the command line
    args = arg_parser( sys.argv[1:] )

    # excute the commands after the arguements have been parsered
    excute_command( args['action'], args['args'], args['payload'] )


if __name__ == '__main__':
    main()
