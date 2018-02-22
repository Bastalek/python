import os

def grep(fichero,cadena):
	if not os.access(fichero,0):
		print 'El fichero no existe A'
		exit()
	if not os.path.isfile(fichero):
		print 'No es un fichero B'
		exit()
	f=open(fichero,'r')
	while True:
		linea=f.readline()
		if not linea:
			break
		if linea.count(cadena)>0:
			print linea[:-1]

def cp(fichero1,fichero2):
	if not os.access(fichero,0):
                print 'El fichero no existe A'
                exit()
        if not os.path.isfile(fichero):
                print 'No es un fichero B'
                exit()
	f1=open(fichero1,'r')	
	f2=open(fichero2,'w')
	lineas=f1.readlines()
	#f2.writelines(lineas)
	for linea in lineas:
		f2.write(linea)
	f1.close()
	f2.close()

def cpgrep(fichero1,fichero2,cadena):
	if not os.access(fichero,0):
                print 'El fichero no existe A'
                exit()
        if not os.path.isfile(fichero):
                print 'No es un fichero B'
                exit()
        f1=open(fichero1,'r')
        f2=open(fichero2,'w')
	while True:
                linea=f.readline()
                if not linea:
                        break
                if linea.count(cadena)>0:
			for linea in lineas:
               			 f2.write(linea)
        f1.close()
        f2.close()


while True:
