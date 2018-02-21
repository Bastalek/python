#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Pedir el nombre apellidos y mostrar iniciales

def saludar(saludo):
	print saludo

def iniciales(nombre,ape1,ape2)
	import sys
	iniciales= nombre[0]+','+ape1[0]+','+ape2[0]+'.'
	print "Tus iniciales son " +iniciales.upper()

def iniciales2(nombre,ape1,*apellidos)
	iniciales=nombre[0]+'.'+ape1[0]
	for ape in apellidos:
		iniciales=iniciales+'.'+ape[0]
	return iniciales.upper()
