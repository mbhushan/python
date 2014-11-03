#!/usr/bin/python

import sys

def main():
    print "Hello there", sys.argv[1]
    
    #Command line args are there in sys.argv[1], sys.argv[2] etc
    #sys.argv[0] is the script name itself and can be ignored.

# Standard boiler plate to call the main program
if __name__ == '__main__':
    main()

 
