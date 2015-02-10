##############################################################################
# Telecom ParisTech                                    Jean-Louis Dessalles  #
#                     INF226: Algorithmes et Complexite                      #
# icc.enst.fr/ALG                                          www.dessalles.fr  #
##############################################################################
# 2012

"""	This program retrieves a binary sequence from the server
"""

import sys
import os
import os.path
import string
import time
import glob


Location = '~icc/public_html/Temp'
StorageFile = 'BinaryString.txt'

if __name__ == "__main__":	

	Files = glob.glob(os.path.join(os.path.expanduser(Location), 'Sequence_*_*'))
	print Files
	BString = ''.join([open(F).read() for F in Files])
	BString = BString.translate(None, '\n')
	BString = BString.translate(None, string.printable[2:])
	print('\n%d binary strings concatenated' % len(Files))
	print('Final string:\n%s\n' % BString)
	print('Storing binary string into %s' % StorageFile)
	open(StorageFile, 'w').write(BString)
	time.sleep(2)
			
		



