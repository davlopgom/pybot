#!/usr/bin/env python
"""
 rael.py        Pesonal stuff.
 Author:        Rael Garcia <self@rael.io>
 Date:          06/2016
 Tested on:     Python 3 / OS X 10.11.5
"""
import re
import sys
import random

lve_welcome="Bienvenidos al la vieja escuela, un grupo de jugadores de PS4 de edad madurita, este grupo está creado con la intención de conocer gente madura con la que poder jugar y echar un buen rato, no olvides dejar tu id de PS4, que disfrutes de tu estancia aquí.\nPor cierto disponemos de comunidad en PS4, se llama la vieja escuela ESP, búscala y entra a nuestra comunidad para añadir a los demás miembros del grupo.\nUn saludo."

def salute(words):

    return lve_welcome
 
def farewell(words):

    return "talue"

def main(argv):
    if len(sys.argv)>1:
        print(salute(' '.join(sys.argv)))
        print(bye(' '.join(sys.argv)))
    else:
        print('I heard nothing.')

if __name__ == "__main__":
    main(sys.argv)
