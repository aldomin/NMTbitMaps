#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cPickle as pkl
import cairo
from PIL import Image
import operator
import os
import sys
sys.stdin.encoding

dictionary = {}
lista = []

def RetrivePKL():
    i = 0
    with open('./vocab.zh.pkl', 'rb') as f:
            dictionary = pkl.load(f)
    outText = open('./dictionary3.txt','w')
    global lista
    lista = dictionary.items()
    lista.sort(key=lambda x: x[1])
    
    print len(lista)
    for ch, b in lista:
        strLine = ch + " : " + str(b)
        outText.write(str(strLine))
        outText.write("\n")
    outText.close()




    
RetrivePKL()