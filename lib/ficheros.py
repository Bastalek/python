import os 

def crea_dir(directorio):

	if os.access(directorio,0):
		return 1
	else:
			os.mkdir(directorio)	
			return 0
def fich(directorio):
	if not os.access(directorio,0):
		print 'No es un directorio'
		exit()
	lista=os.listdir(directorio)
		for cosa in lista: 
			f1=directorio+'/'+cosa
			if os.path.isfile(f1):
				print cosa+'---->'+str(os.path.getsize(f1))

def fich2(directorio,tamano):
        if not os.access(directorio,0):
                print 'No es un directorio'
                exit()
	if tamano[-1].upper() not in ('K','M','G'):
		print 'No es un valo valido, KMG'
		exit()

	t=int(tam[:-1])
	print 'TAMAÑO'+t

	if tamano[-1]=='K': 
		t=t*1024
	elif tam[-1]=='M':
		t=t*1024*1024
	else:	
		t=t*1024*1024*1024
      	
	lista=os.listdir(directorio)
        	for cosa in lista:
                	f1=directorio+'/'+cosa
                	if os.path.isfile(f1):
				if os.path.getsize(f1)>t:
                        	print fichero+'---->'+str(os.path.getsize(f1))
		else:
			print 'no es un parametro valido'

def cat(fichero):
	if not os.access(fichero,0):
		print 'El fichero no existe'
		exit()
	if not os.path.isfile(fichero):
		print 'No es un fichero'
		exit()
	f=open(fichero,'r')
	contenido=f.read()
	print contenido
	f.close()

def grep(fichero,texto)
		




