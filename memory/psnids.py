#!/usr/bin/env python
"""
 psnids.py  Battlenet user list.
 Author:        Rael Garcia <self@rael.io>
 Date:          0692016
 Tested on:     Python 3 / OS X 10.11.5
"""
import re
import sys
import random

psnids = [
    'LVE - PSN ID list',
    '----------------------------',
    'DarkSieL - DarkSieL',
    'Frank - FJRISH',
    'Oscar - Heissentronik204',
    'Ralph - Nessus7',
    'Javi - mezORZ',
    'BoLoLsD - BoLoLsD',
    'Yeray - yeray201103',
    'Xou -  xou86',
    'Ino - EddisV',
    'Karmelo - karmeloguillen',
    'Sergio - Reynoldor']

def hear(words):

    if re.search( r'^\/psnids.*', words, re.I|re.M):
        return ("\n".join(psnids))


def main(argv):
    if len(sys.argv)>1:
        print(hear(' '.join(sys.argv)))
    else:
        print('I heard nothing.')

if __name__ == "__main__":
    main(sys.argv)
