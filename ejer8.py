#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Introduce una letra por teclado y busca los ficheros que la contengan en el nombre
import os
directorio=raw_input('introduce un directorio:')

letra=raw_input('introduce una letra:')
ficheros=os.listdir(directorio)
for fichero in ficheros:
	if fichero.count(letra)>0:
		print fichero	

