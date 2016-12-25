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

	out=""
	def getLine():
		global out
		while True:
			if msvcrt.kbhit():
				got=msvcrt.getch()
				got=got.decode()
				if got!='\r':
					print(got, end="", sep="")
					sys.stdout.flush()
					out+=got
				else:
					ret=copy.copy(out)
					out=""
					return ret
			else:
				return None
