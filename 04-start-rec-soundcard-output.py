#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

import os
import os.path
import sys
import time

import captures
import common
from common import color

""" 
You will need a config file like this ( $HOME/.asoundrc ):
    
pcm.copy {
    type plug
    slave {
        pcm hw
    }
    route_policy copy
}

Record soundcard output in WAV format:
======================================
arecord -d 0 -c 2 -f S16_LE -r 44100 -t wav -D copy foobar.wav

Record soundcard output in OGG format:
======================================
arecord -d 0 -c 2 -f S16_LE -r 44100 -t wav -D copy | oggenc -o record.ogg -

In the 2nd case, the wav to ogg conversion is done on the fly. Notice the "-"
at the end which forces oggenc to read from the stdin.

The option "-d 0" means to use no time limit. Otherwise, for instance, "-d 10" 
would mean to stop recording after 10 seconds.

"""

TMP_DIR = './output'

def get_output_filename():
    print "Specify a %s where to save the soundcard output %s." % ( color('filename','green'), color('(without .ogg)','green') )
    print "You can also press %s to save the output %s." % ( color('ENTER','green'), color('to a temp. file','green') )
    filename = raw_input( color("Filename: ", 'yellow', ['bold']) )
    if len(filename) == 0:
        filename = os.path.join( TMP_DIR, "record_%s.ogg" % common.get_timestamp() )
    else:
        filename = os.path.join(TMP_DIR, filename + ".ogg")
        
    if os.path.exists(filename):
        sys.stderr.write( "%s: Error: the file %s already exists.\n" % (sys.argv[0], filename) )
        sys.exit(-2)

    return filename

def main():
    common.verify_output_dir(TMP_DIR)
    out = get_output_filename()
    command = "arecord -d 0 -c 2 -f S16_LE -r 44100 -t wav -D copy | oggenc -o %s -" % out
    print color(command, 'cyan')
    print color("Press CTRL+C to stop the recording process.", 'green')
    start = time.time()
    os.system(command)
    end = time.time()
    print color( common.elapsed_time(end, start), 'yellow' )
    print color("Size of the output file: %s bytes." % common.numberToPrettyString(os.path.getsize(out)), 'yellow')
    print color("If you want to listen to the recorded file, execute the following command:", 'green')
    print color("mplayer %s" % out, 'cyan')

if __name__ == "__main__":
    main()
