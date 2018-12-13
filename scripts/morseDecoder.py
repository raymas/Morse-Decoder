#! /usr/bin/python
# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:         morseDecoder.py
# Purpose:      Morse decoder using
#
# Author:       RedEye
#
# Created:      07/04/2018
# Copyright:    (c) Authors, 2018
# About:
#
# Sources :
#-------------------------------------------------------------------------------
import random
import numpy as np
import matplotlib.pyplot as plt


ALPHABET = [x for x in "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789"]
MORSE_ALPHABET = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.','---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.', '-----']

MORSE = dict(zip(ALPHABET, MORSE_ALPHABET))

print(MORSE)
