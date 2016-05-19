#!/usr/bin/env python
# -*- coding: utf-8 -*- 
import random
import cairo
from PIL import Image
import operator
import os
import sys
sys.stdin.encoding
from readPKL import lista


chineseDic = {}
imagesDic = {}
GB = []

def save(symbol,matrixBits,nameValue):
    #print "FUNCTION 7"
    #print len(matrixBits)
    #print matrixBits
   # print len(matrixBits)
    global GB
    GB.append(matrixBits)
    imagesDic[symbol] = nameValue

def generatePixels(symbol,nameValue):
    #print "FUNCTION 6"
    value = 0
    if (symbol == "〈" or symbol == "、" or symbol == "。" or symbol == "〉" or symbol == "》" or symbol == "《" or symbol == "●" or symbol == "○" or symbol == "…" or symbol == "㈠" or symbol == "㈦" or symbol == "㈢" or symbol == "㈦" or symbol == "㈡" or symbol == "㈤"  or symbol == "㈨" or symbol == "㈩" or symbol == "㈧" or symbol == "㈥" or symbol == "㈣"):
        value = 1
        i = Image.open("./images/%d.png" % nameValue).convert('1')  
        
    else:
        i = Image.open("./images/%d.png" % nameValue).convert('1') 
    pixels = i.load() # this is not a list
    width, height = i.size
    L = []
    for x in range(width):
        for y in range(height):
            if (value == 0):
                cur_pixel = pixels[x, y]
                if (cur_pixel == 255):
                    cur_pixel = 0
                else:
                    cur_pixel = 1
            else: 
                cur_pixel = random.choice([1, 0])    
            L.append(cur_pixel)
    return L


def reducir(imagen, nuevaImagen, nuevoAncho):
        """ Reduce de tamaño una imagen.
                        imagen: Fichero de la imagen (ej. "foto.jpg")
                        nuevaImagen: Nombre de fichero de la nueva imagen (ej. "foto.jpg")
                        nuevoAncho: Nuevo ancho de la imagen, en píxeles (ej. 438)
        """
        # Abre la imagen
        img = Image.open(imagen)
        if (img == None):
                print "reducir\n\tNo se pudo abrir la imagen\n\n"
                return

        # Calcula el nuevo ancho de la imagen
        ancho = img.size[0]
        alto = img.size[1]
        nuevoAlto = int(round((nuevoAncho + 0.0) / ancho * alto))
        
        # Genera la nueva imagen con el nuevo tamaño
        nImg = img.resize((nuevoAncho, nuevoAlto))
        
        # Guarda la imagen
        nImg.save(nuevaImagen)

def createPNG(ctx,surface,symbol,nameValue):
    #print "FUNCTION 5"
    ctx.stroke() # commit to surface
   # print nameValue , "-----" , symbol
    surface.write_to_png('./images/%d.png' % nameValue)
    return surface
  
  
def initValues(ctx): 
    #print "FUNCTION 4"
    # paint background
    ctx.set_source_rgb(1, 1, 1)
    ctx.rectangle(0, 0, 1000, 200)
    ctx.fill()
    # draw text
    ctx.select_font_face("金文大篆体")
    ctx.set_font_size(200)
    ctx.move_to(0,200)
    ctx.set_source_rgb(0, 0, 0)
    return ctx


#Iteracion
def processCharacter(symbol,nameValue):
    #print "FUNCTION 3"
    # setup a place to draw
    surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, 1000, 200)
    ctx = cairo.Context (surface)
    ctx = initValues(ctx)
    #show text
    ctx.show_text(symbol) 
    surface = createPNG(ctx,surface,symbol,nameValue)
    
    reducir('./images/%d.png' % nameValue,'./images/%d.png' % nameValue,51)
    
    matrixBits = generatePixels(symbol,nameValue)
    save(symbol,matrixBits,nameValue)


def readDocument():
    #print "FUNCTION 2"    
    docOut = open('./matrixBits.txt','w')
    nameValue = 0
    for symbol, value in lista:
        processCharacter(symbol,nameValue)
        nameValue = nameValue + 1
    docOut.write(str(GB))

#print "FUNCTION 1"
readDocument()






