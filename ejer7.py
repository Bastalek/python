#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Visualiza todos los shell scripts
 
import os
directorio=raw_input('introduce un directorio:')
#if not os.access(directorio,0) 
#	print "El directorio existe"
#	exit()
ficheros=os.listdir(directorio)
for fichero in ficheros:
	if fichero[-3:]=='.sh':
		print fichero	

