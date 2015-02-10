##############################################################################
# Telecom ParisTech                                    Jean-Louis Dessalles  #
#                     INF226: Algorithmes et Complexite                      #
# icc.enst.fr/ALG                                          www.dessalles.fr  #
##############################################################################
# 2014

"""	This program samples memory and measures its complexity by compressing the sample
"""

import random
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
	return result	# returned as a string

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
	
	
	
	
def compression(TextSample, TextName, Verbose=True):
	"""	gets a string compressed and prints compression factor
	"""
	CompressedSize = len(compressor(TextSample))
	if Verbose:
		print("{0}: size {1} >> {2} (compression {3}%)".format(TextName, len(TextSample), 
			CompressedSize, 100-(100*CompressedSize)/len(TextSample)))
	return CompressedSize
	
  
if __name__ == "__main__":	
	
	##############################
	# Compressing pow(10,i) base 10  #
	##############################
	i = 10000
	print('\nCompressing pow(10,%d) base 10' % i)
	Num = pow(10,i)
	StrNum = str(Num)
	compression(StrNum, "Number")

	######################################
	# Compressing pow(256,i) (base 256)  #
	######################################
	i = 10000
	print('\nCompressing pow(256,%d) base 256 represented in bytes' % i)
	Num = pow(256,i)
	StrNum = BaseChange(Num, Bytes)	# mostly null chars
	compression(StrNum, "Number")


	#################################
	# Compressing a Random Number   #
	#################################
	i = 10000
	print('\nCompressing a pseudo-Random Number larger than 10^%d represented in bytes' % i)
	Num = random.randint(pow(10,i),pow(10,i+1)-1)
	StrNum = BaseChange(Num, Bytes)	# converts base 10 into 256
	compression(StrNum, "Number")
	

	##############################
	# Compressing Pi             #
	##############################
	print('\nCompressing Pi represented in bytes')
	try:
		TextSample = open("Pi.txt").read()	
		TextSample = TextSample.replace('\n', '').replace('.','')
		compression(TextSample, "Pi in base 10")
		print("Strange: Pi's decimals seem to be compressible !!")
		Num = int(TextSample,base=10)
	except IOError:
		print("Please provide a text file 'Pi.txt' with decimal digits of Pi")


