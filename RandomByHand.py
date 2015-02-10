#*-------------------------------------------------------*#
#* Elementary randomness tests for short sequences       *#
#*                       J-L Dessalles September 2012    *#
#*-------------------------------------------------------*#

"   Elementary randomness tests for short sequences"

import random
import os.path

InputFileName = 'BinaryString.txt'

Test1 = '00101001011101101011010001011010110110100010110010111010'
Test2 = '0001101110011010111111100101000001101111100101001100011010101010101111000'

def RandomBinString(Length):
	" returns a random binary string of given length "
	return bin(random.getrandbits(Length))[2:]	 # ignoring first two characters '0b'

def SimplePatterns(MaxLength, mode='short'):
	""" returns a list of 'simple' patterns
		'Simple' correspond to the following modes:
		short, repetitive or uniform   """
	if mode == 'short':
		Patterns = range(1 << MaxLength, 2 << MaxLength)  # all patterns with 1 plus up to MaxLength bits
		Patterns = map(bin, Patterns)
		Patterns = map(lambda x: x[3:], Patterns)   # getting rid of leading '0b1'
	else:
		Patterns = []
		if mode == 'repetitive':
			models = SimplePatterns(2,mode='short')	# oops, recursive call, just for fun
		elif mode == 'uniform':
			models = ['0', '1']
		for P in models:
			for Length in range(1, 1 + MaxLength // len(P)):
				Patterns.append(P * Length)	
	return sorted(Patterns)

def OverlappingFind(Sequence, Pattern):
	" search for overlapping pattern in a sequence "
	if not Pattern: return 0
	# FirstPosition = Sequence.find(Pattern)
	# if FirstPosition >= 0:
		# return 1 + OverlappingFind(Sequence[FirstPosition+1 : ], Pattern)   # recursive call
	NbPatterns = 0
	for Pos in range(len(Sequence)):
		if Sequence[Pos:].startswith(Pattern):
			NbPatterns += 1
	return NbPatterns

def Scan(Sequence, MaxLength=5, mode='repetitive'):
	" Scans for simple patterns "
	Histogram = dict()  # empty dictionary
	Patterns = SimplePatterns(MaxLength, mode=mode)
	for P in Patterns:
		Histogram[P] = OverlappingFind(Sequence, P)
	return Histogram

def HistogramDisplay(Histogram, Reduction=1):
	" displays histogram with text "
	DisplayString = '\n'
	DisplayLength = max(map(len,Histogram.keys()))
	for P in sorted(sorted(Histogram.keys()), key=len):
		DisplayString += '%s\t%s\n' % (P.rjust(DisplayLength), '#' * int(Histogram[P]/max(1,Reduction)))
	return DisplayString + '\n'
	
	
def Sequences(S):
	" Converts binary string into decimal string that counts identical bits "
	DecimalList = []
	Length = len(S)
	while S:
		Tested = int(S, 2)   # Takes advantage of the fact that int() deletes leading zeros
		NewLength = len(bin(Tested)) - 2
		DecimalList.append(Length - NewLength)
		Length = NewLength
		Inverting = int('1' * Length, 2)   # used to complemet (as ~ does not seem to work)
		S = bin(Tested ^ Inverting)[2:]
		if S == '0':
			DecimalList.append(Length)
			break
##        print TestedString
##        if raw_input('? '):
##            break
	return DecimalList

if __name__ == '__main__':
	print __doc__

	if os.path.exists(InputFileName):
		TestString = open(InputFileName).read().strip()
	else:
		TestString = Test2
	RandomString = RandomBinString(len(TestString))
	
##    Length = 2*(len(TestString)//2) # closest even length
##    TestString = TestString[:Length]   # truncating the string to even length
##    TestNumber = int(TestString, 2) # reading the string as a binary number
##    AlternatingString = '01' * (Length//2) # Alternating list of same length
##    AlternatingNumber = int(AlternatingString, 2)
##    Tested = TestNumber ^ AlternatingNumber
##    TestedString = bin(Tested)[2:].rjust(Length,'0')     # ignoring first two characters '0b'
##    #print bin(TestNumber)[2:].rjust(Length,'0')
##    #print bin(AlternatingNumber)[2:].rjust(Length,'0')
##    #print TestedString
##    #print bin(Tested ^ AlternatingNumber)[2:].rjust(Length,'0')
##    print ' '.join(map(str, Sequences(TestString)))
##    print ' '.join(map(str, Sequences(TestedString)))

	for T in (TestString, RandomString): 
		print
		print T
		print HistogramDisplay(Scan(T, MaxLength=6, mode='uniform'), Reduction=len(T)/160.0)
	
	
