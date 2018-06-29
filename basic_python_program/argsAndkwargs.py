#example for usage of *arg

#python program to illustrate
# *args

def testify(argl, *argv):
    print "first argument :", argl
    for arg in argv:
        print "Next argument through *argv :", arg
testify('Hello','Welcome','to','GeeksforGeeks')

print "=" * 100

#example for usage of **kwargs

def hello(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.iteritems():
            print "%s == %s" %(key, value)


#Using *args and **kwargs to call a function
def testify(arg1, arg2, arg3):
    print "arg1:", arg1
    print "arg2:", arg2
    print "arg3:", arg3
