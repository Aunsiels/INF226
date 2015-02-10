##############################################################################
# Telecom ParisTech                                    Jean-Louis Dessalles  #
#                     INF226: Algorithmes et Complexite                      #
# icc.enst.fr/ALG                                          www.dessalles.fr  #
##############################################################################
# 2012

"""	This program samples memory and measures its complexity by compressing the sample
"""

import sys
import random
import ctypes
import zlib
import bz2

compressor = zlib.compress		# compressor that is used in compression operations
# compressor = bz2.compress		# compressor that is used in compression operations

Bytes = [chr(i) for i in range(256)]		# 256 first chars


def BaseChange(Number, BaseSymbols):
	""" converts a number from base 10 to another base
	"""
	Base = len(BaseSymbols)
	result = ''
	while Number:
		result += BaseSymbols[Number % (Base)]
		Number //= Base
	return result

def Base4To16(DNA, Nucleotides='ATGC'):
	"""	converts DNA string with A,T,G,C into hexadecimal base
	"""
	Base = list(Nucleotides)
	HexaSequence = ''
	for locus in range(0, len(DNA), 4):
		Hexa = Base.index(DNA[locus])
		Hexa += Base.index(DNA[locus+1])*4
		Hexa += Base.index(DNA[locus+2])*16
		Hexa += Base.index(DNA[locus+3])*64
		HexaSequence += Bytes[Hexa]
	return HexaSequence
	
	
	
	
def compression(TextSample, TextName):
	"""	gets a string compressed and prints compression factor
	"""
	CompressedSize = len(compressor(TextSample))
	print("{0}: size {1} >> {2} (compression {3}%)".format(TextName, len(TextSample), 
		CompressedSize, 100-(100*CompressedSize)/len(TextSample)))
	return CompressedSize
	
def distText(Text1, Text2):
	#On commence par lire le contenu de Text1
	#Ficher d'environ 60k
	TextSample = open(Text1).read()
	#On calcule la taille du fichier compresse
	CompressedSize1 = compression(TextSample, Text1)
	#On concatene le contenu de Text2 au contenu precedent
	TextSample += open(Text2).read()
	#On calcule la taille du nouveau fichier compresse
	CompressedSize2 = compression(TextSample, Text1+" + "+Text2)
	#On compare les tailles
	print("Compression {1} avec {0} : {2}\n".format(Text1, Text2, CompressedSize2-CompressedSize1))
  
if __name__ == "__main__":	

	
	LArgs = len(sys.argv)	# number of arguments in the command line

	if LArgs == 1:
		#################################
		# Compressing a Random Number   #
		#################################
		print('\nCompressing a Random Number represented in bytes')
		i = 10000
		Num = random.randint(pow(10,i),pow(10,i+1)-1)
		StrNum = BaseChange(Num, Bytes)	# converts base 10 into 256
		CompressedSize = compression(StrNum, "Number")
		

		##############################
		# Compressing Pi             #
		##############################
		print('\nCompressing Pi represented in bytes')
		try:
			TextSample = open("Pi.txt").read()	
			TextSample = TextSample.replace('\n', '').replace('.','')
			CompressedSize = compression(TextSample, "Pi in base 10")
			Num = int(TextSample,base=10)
			StrNum = BaseChange(Num, Bytes)	# converts base 10 into 256
			CompressedSize = compression(StrNum, "Pi in base 256")
		except IOError:
			print("Please provide a text file 'Pi.txt' with decimal digits of Pi")

		######################################
		# Compressing pow(256,i) (base 256)  #
		######################################
		print('\nCompressing pow(256,i) base 256 represented in bytes')
		Num = pow(256,10000)
		StrNum = BaseChange(Num, Bytes)	# mostly null chars
		CompressedSize = compression(StrNum, "Number")


		##############################
		# Compressing pow(10,i) base 10  #
		##############################
		print('\nCompressing pow(10,i) base 10')
		Num = pow(10,10000)
		StrNum = str(Num)
		CompressedSize = compression(StrNum, "Number")

	elif LArgs == 2:
		try:
			CompressedSize = compression(open(sys.argv[1]).read(), sys.argv[1])
		except IOError:
			print('Unable to read %s' % sys.argv[1])
	elif LArgs == 3:
		try:
			distText(sys.argv[1], sys.argv[2])
		except IOError:
			print('Unable to read %s and %s' % sys.argv[1:])
	else:
		print('Usage: %s [<file1 to compress> [<file2 to compress and compare with file1]]' % sys.arv[0])
		
