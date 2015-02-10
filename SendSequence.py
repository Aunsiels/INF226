##############################################################################
# Telecom ParisTech                                    Jean-Louis Dessalles  #
#                     INF226: Algorithmes et Complexite                      #
# icc.enst.fr/ALG                                          www.dessalles.fr  #
##############################################################################
# 2012

"""	This program reads a binary sequence and sends it to the server
"""

import sys
import os
import os.path
import string
import random
import time

Location = '~icc/public_html/Temp'

if __name__ == "__main__":	

	Sequence = raw_input("Please enter a binary sequence: ")
	Sequence = Sequence.translate(None, string.printable[2:])
	if not set(list(Sequence)) <= set(['0','1']):
		print('Incorrect sequence')
		time.sleep(2)
	else:
		Answer = raw_input('Do you want to send this string?\n%s\n' % Sequence)
		if Answer.lower().startswith('y'):
			User = str(random.randint(0,9999))
			try:	User = os.environ['USER']
			except KeyError:
				try:	User = os.environ['USERNAME']
				except KeyError:	pass
			# print User, Sequence
			try:
				Filout = os.path.expanduser(os.path.join(Location, 'Sequence_%s_%d' % (User, random.randint(1,999))))
				# print Filout
				open(Filout,'w').write(Sequence+'\n')
				print('sequence sent')
			except IOError:
				print('sequence not sent')
			time.sleep(2)
			
		



