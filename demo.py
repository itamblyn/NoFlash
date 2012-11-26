#!/usr/bin/env python

import os, sys
import commands

def check_wifi():

    wifi_detected = int(commands.getoutput('/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s | grep Ithaca_n | wc -l'))
    return wifi_detected

def take_picture(wifi_detected):

    if wifi_detected == 1:

        print 'Flash deactivated, taking photograph'
        commands.getoutput('open ./graphics/flashFalse.jpeg')
    else:
        print 'Flash active, taking photograph'
        commands.getoutput('open ./graphics/flashTrue.jpeg')

    commands.getoutput('./wacaw-04/wacaw test')
    commands.getoutput('open ./test.jpeg')
def main():
    """
    This is the main function.
    """
    # A clean way to ask for user input
    try:
        # Attempt to retrieve required input from user
        prog = sys.argv[0]
    #    a = float(sys.argv[1])
    #    b = float(sys.argv[2])
    except IndexError:
        # Tell the user what they need to give
        print '\nusage: '+prog+' a b    (where a & b are numbers)\n'
        # Exit the program cleanly
        sys.exit(0)

    # Execute the function defined above

    wifi_detected = check_wifi()

    take_picture(wifi_detected)

# This executes main() only if executed from shell
if __name__ == '__main__':
    main()
