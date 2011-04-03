#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

import captures

def main():
    """ When finished recording the soundcard output, don't forget
        to restore recording to microphone. Otherwise applications
        like Skype won't handle your microphone. """
    (cap_source,  cap_switch,  cap_volume) = captures.get_captures()
    captures.set_cap_source(cap_source, 'Mic')
    captures.set_cap_switch(cap_switch, 'on')
    captures.set_cap_volume(cap_volume, 10)

if __name__ == "__main__":
    main()
