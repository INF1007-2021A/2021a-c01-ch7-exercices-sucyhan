#!/usr/bin/env python
# -*- coding: utf-8 -*-

# TODO: Importez vos modules ici
import math
import _exercice_version_prof
import sys
import sys

sys.path.insert(0, "\\Users\\sucyh\\Documents\\GitHub\2021a-c01-ch6-1-exercices-sucyhan\\_exercice_version_prof6.py")
from _exercice_version_prof6 import frequence
from turtle import *

# TODO: Définissez vos fonction ici
# Exercice1
def ellipsoide(a, b, c, p):
    Volume = 4 / 3 * math.pi * a * b * c
    masse = p * Volume
    return Volume, masse


def draw_tree():
    setheading(90)
    color("green")


    #appeler fct recursive
    draw_branch(70,7,35)
    done()

def draw_branch(branch_len, pen_size, angle):
    if branch_len > 0:
        pensize(pen_size)
        forward(branch_len)
        right(angle)
        draw_branch(branch_len - 10, pen_size -1, angle - 5)
        left(2 * angle)
        draw_branch(branch_len - 10, pen_size - 1, angle - 5)
        right(angle)
        backward(branch_len)

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    Volume, masse = (ellipsoide(1, 2, 3, 4))
    print(Volume, masse)

    print((lambda sentence: sorted(frequence(sentence).items(), key=lambda x: x[1])("je suis une phrase")))

    draw_tree()