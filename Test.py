import sys
import os

import random
import zlib
import bz2

from NumberCompression import compression

compressor = zlib.compress              # compressor that is used in compression operations

def distText(Text1, Text2):
	#On commence par lire le contenu de Text1
	#Ficher d'environ 60k
	TextSample = open(Text1).read()
	#On calcule la taille du fichier compresse
	CompressedSize1 = compression(TextSample, Text1)
	#On concatene le contenu de  Text2 au contenu precedent
	TextSample += open(Text2).read()
	#On calcule la taille du nouveau fichier compresse
	CompressedSize2 = compression(TextSample, Text1+"+"+Text2)
	#On compare les tailles
	print("Compression {1} avec {0} : {2}\n".format(Text1, Text2, CompressedSize2-CompressedSize1))

def run (Text1): 
	TextSample = open(Text1).read()
	length = len(TextSample)
	Text_temp = compressor(TextSample)
	CompressedSize1 = len(Text_temp)
	I = 0
	print("A l'etape {0}, la difference est {1}\n".format(I,length - CompressedSize1))
	while I < 1000:
		I = I+1
		Text_temp = compressor(Text_temp)
		CompressedSize1 = len(Text_temp)
		print("A l'etape {0}, la difference est {1}\n".format(I,length - CompressedSize1))

if __name__ == "__main__":


	LArgs = len(sys.argv)   # number of arguments in the command line

	if LArgs == 3:
		try:
			distText(sys.argv[1],
			sys.argv[2])
			run(sys.argv[1])
		except IOError:
			print('Unable to read %s and %s' % sys.argv[1:])
	else:
		print('Usage:\n %s <file1 to compress> <file2 to compress and compare with file1>' % os.path.basename(sys.argv[0]))

									  

