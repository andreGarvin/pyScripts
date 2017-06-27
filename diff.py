from sys import argv

def readFile( file_name ):
    with open(file_name, 'r') as of:
        return of.readlines()


def diff( f1, f2 ):

    if f1 == f2:

        print("*error: same file name '%s' was given." % ( f1 ) )
        return False

    else:

        fn1, fn2 = f1, f2
        f1=readFile( f1 )
        f2=readFile( f2 )
        for i, j in zip(f1, f2):

            if i != '\n' and j != '\n':

                if i != j:
                    print( '(%s) - %s ' % ( fn1, i ) )
                    print( '(%s) - %s ' % ( fn2, j ) )

                # if i == j:
                #     print( '(%s) + %s ' % ( fn1, i ) )
                #     print( '(%s) + %s ' % ( fn2, j ) )




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

    diff(args['payload'][0], args['payload'][1])
