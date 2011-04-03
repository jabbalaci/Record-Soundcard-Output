#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

import os
import sys
import shlex

from subprocess import Popen, PIPE
from termcolor import colored
from datetime import datetime

def color(text, color, attrs=[]):
    return colored(text, color, attrs=attrs)
    
def numberToPrettyString(n):
    """Converts a number to a nicely formatted string.
       Example: 6874 => '6,874'."""
    l = []
    for i, c in enumerate(str(n)[::-1]):
        if i%3==0 and i!=0:
            l += ','
        l += c
    return "".join(l[::-1])
    
def get_timestamp():
    now = datetime.now()
    date = datetime.date(now)
    time = datetime.time(now)
    return "%d%02d%02d_%02d%02d%02d" % (date.year, date.month, date.day, time.hour, time.minute, time.second)
    
def elapsed_time(end, start):
    elapsed = end - start
    minute = elapsed / 60.0
    return "Elapsed time: %d seconds, i.e. %.2f minutes." % (elapsed, minute)

def verify_output_dir(dir):
    if os.access(dir, os.W_OK) == False:
        sys.stderr.write( "%s: Error: cannot write to the specified temp. directory %s.\n" % (sys.argv[0], dir) )
        sys.stderr.write("Tip: verify if the directory exists and it's writable.\n")
        sys.exit(-1)

def verify_if_exists(program):
    if which(program) is None:
        sys.stderr.write( "%s: Error: the program %s is not found.\n" % (sys.argv[0], program) )
        sys.exit(-1)

def execute_command(command):
    """ execute an external command and return its output """
    args = shlex.split(command)
    verify_if_exists(args[0])
    return Popen(args, stdout=PIPE).communicate()[0]

def which(program):
    """ http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python """
    def is_exe(fpath):
        return os.path.exists(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

if __name__ == "__main__":
    pass
