##############################################################################
# Telecom ParisTech                                    Jean-Louis Dessalles  #
#                     INF226: Algorithmes et Complexite                      #
# icc.enst.fr/ALG                                          www.dessalles.fr  #
##############################################################################
# 2012

"""	This program samples memory and measures its complexity by compressing the sample
"""

import sys
import os
import random
import ctypes
import binascii
import zlib
import bz2
import urllib
import re

MaxTry = 1

def getRandomMemoryContent(Size):
	for Try in range(MaxTry):
		try:
			if os.name == 'nt':	# We are on Windows
				Address = random.randint(0,2**29)
				#print Address
				# return	binascii.hexlify(ctypes.string_at(Address, Size))
				return	ctypes.string_at(Address, Size)
			else:	# probably on unix
				libc = ctypes.CDLL('libc.so.6')
				Address = libc.malloc(Size)
				#print Address
				return(ctypes.string_at(Address, Size))
		except Exception as E:
			print E
			pass
	return None
	
def getTextInHexa(Text):
	return binascii.hexlify(Text)


def cleanhtml(raw_html):
  return re.sub(re.compile('<[^>]*>'),'', raw_html)	# substitutes html tags by nothing

  
if __name__ == "__main__":	

	MaxTry = 128	# number of attempts to read memory at random location
	Size = 10 * 2**10	# Size of memory sample
	compressor = zlib.compress

	##############################
	# Compressing memory samples #
	##############################
	for sample in range(10):
		MemorySample = getRandomMemoryContent(Size)
		print list(MemorySample[:20])
		if MemorySample:
			CompressedSize = len(compressor(MemorySample))
			print("Memory sample of size {0} is compressed down to {1} bytes ({2}%)".format(len(MemorySample), 
				CompressedSize,100-(100*CompressedSize)/len(MemorySample)))

	print('')	
	print('. . .')

	##############################
	# Compressing Text samples   #
	##############################
	# TextSample = open('../ComplexitySimplicity.html').read(Size)
	# Getting text sample from wikipedia
	WordsToSearch = ['Complexity', 'Andrey%20Kolmogorov', 'Gregory%20Chaitin', 'Constitution']
	print('Comparison with Wikipedia pages about \n\t- {0}'.format('\n\t- '.join(WordsToSearch)))
	for WordToSearch in WordsToSearch:
		TextSample = urllib.urlopen("http://en.wikipedia.org/w/index.php?action=raw&title=" + WordToSearch).read(Size)
		TextSample = cleanhtml(TextSample)
		TextSample = getTextInHexa(TextSample)	# to be fair with the case of memoy samples
		CompressedSize = len(compressor(TextSample))
		print("Text   sample of size {0} is compressed down to {1} bytes ({2}%)".format(len(TextSample), 
			CompressedSize, 100-(100*CompressedSize)/len(TextSample)))
	
	
	
	