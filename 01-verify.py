#!/usr/bin/env python

# Recording soundcard output
# https://ubuntuincident.wordpress.com/2011/03/26/recording-soundcard-output/
# Laszlo Szathmary, 2011 (jabba.laci@gmail.com)

import captures

def main():
    """ get the three Capture lines and print them to the stdout """
    (cap_source,  cap_switch,  cap_volume) = captures.get_captures()
    print "\n".join(cap_source)
    print "\n".join(cap_switch)
    print "\n".join(cap_volume)

if __name__ == "__main__":
    main()
