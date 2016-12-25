#!/usr/bin/env python3

# microsoft windows specific code
mswindows=False
try:
	import msvcrt
	mswindows=True
except ImportError:
	pass

if mswindows:
	import copy
	import sys

	class Console:
		def __init__(self):
			self.out=""
		def getLine(self):
			while True:
				if msvcrt.kbhit():
					got=msvcrt.getch()
					got=got.decode()
					if got!='\r':
						print(got, end="", sep="")
						sys.stdout.flush()
						self.out+=got
					else:
						ret=copy.copy(self.out)
						self.out=""
						print()
						return ret
				else:
					return None

def testGetLine():
	console=Console()
	while True:
		line = console.getLine()
		if line != None:
			print('line', line)
		else:
			pass
if __name__=='__main__':
	testGetLine()
