#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

import captures

def main():
    """ set captures for recording the soundcard output """
    (cap_source,  cap_switch,  cap_volume) = captures.get_captures()
    captures.set_cap_source(cap_source, 'Mix')
    captures.set_cap_switch(cap_switch, 'on')
    captures.set_cap_volume(cap_volume, 3)

if __name__ == "__main__":
    main()
