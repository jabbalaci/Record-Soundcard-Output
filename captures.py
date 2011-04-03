#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

""" Common functions are collected here. """

import re
import sys
import string

import common
from common import execute_command

def get_captures():
    """ get the three Capture lines """
    cap_source = cap_switch = cap_volume = []
    
    output = execute_command("amixer contents")
    li = output.split("numid=")
    lines = []
    for e in li:
        e = e.rstrip("\n")
        if len(e) == 0:
            continue
        lines.append( ("numid=" + e).split("\n") )
        
    for e in lines:
        if "Capture Source" in e[0]:
            cap_source = e
        elif "Capture Switch" in e[0]:
            cap_switch = e
        elif "Capture Volume" in e[0]:
            cap_volume = e
    
    return (cap_source,  cap_switch,  cap_volume)
    
def set_cap_source(cap_source, option):
    """ Set the Caption Source. Option: 'Mic' (microphone) or 
        'Mix' (soundcard output). """
    def get_numid_str(s):
        """ extract the X value from numid=X,... """
        back = None
        result = re.search(r'numid=(\d+),', s)
        if result:
            back = result.group(1)
        return back
    
    if len(cap_source) == 0:
        return
    # else
    id_str = get_numid_str(cap_source[0])
    option_id_str = None
    if id_str:
        for e in cap_source:
            result = re.search(r'Item #(\d+) '+"'"+option+"'", e)
            if result:
                option_id_str = result.group(1)
                break
    if id_str and option_id_str:
        command = "amixer cset %s %s" % (cap_source[0], option_id_str)
        sys.stdout.write( execute_command(command) )

def set_cap_switch(cap_switch, option):
    """ set Caption Switch to 'on' or 'off' """
    if len(cap_switch) == 0:
        return
    # else
    command = "amixer cset %s %s" % (cap_switch[0], option)
    sys.stdout.write( execute_command(command) )
    
def set_cap_volume(cap_volume, option):
    """ Same as set_cap_switch(). Option is an integer. For recording
        soundcard output, this value should be low, otherwise the quality
        will be bad. """
    set_cap_switch(cap_volume, option)

if __name__ == "__main__":
    pass
