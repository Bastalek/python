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
	for cosa in lista 
		f1=directorio+'/'+cosa
		if os.path.isfile(f1)
			print fichero+'---->'+str(os.path.getsize(f1))
