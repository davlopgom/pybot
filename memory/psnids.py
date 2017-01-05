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
    'LVE - PSN ID List',
    '',
    '\U0001F47E Alucardd - alucardd79',
    '\U0001F47E BoLoLsD - BoLoLsD',
    '\U0001F47E DarkSieL - DarkSieL',
    '\U0001F47E Davs - SuPerDaVirL',
    '\U0001F47E Fo - Gahrall',
    '\U0001F47E Fran - kuaterps',
    '\U0001F47E Frank - FJRISH',
    '\U0001F47E Javi - mezORZ',
    '\U0001F47E Jordi - Jc80__',
    '\U0001F47E Jorge - tyryton',
    '\U0001F47E José - Kuwito',
    '\U0001F47E Ino - EddisV',
    '\U0001F47E Karmelo - karmeloguillen',
    '\U0001F47E Marcos - cyb_nai',
    '\U0001F47E Mateo - VIPTHC',
    '\U0001F47E Oscar - Heissentronik204',
    '\U0001F47E Ralph - Nessus7',
    '\U0001F47E Rael  - raelga',
    '\U0001F47E Ruben - el_morty',
    '\U0001F47E Sergio - Reynoldor',
    '\U0001F47E Xou - xou86',
    '\U0001F47E Yeray - yeray201103']

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
