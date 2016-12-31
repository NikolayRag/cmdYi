import argparse, sys

from cmdyi import *
from kiLog import *


if __name__ == '__main__':
	cParser= argparse.ArgumentParser(description= 'Yi 4k remote control.')

	cParser.add_argument('-arg', type=bool, nargs='?', const=True, help='')
	
	try:
		args= cParser.parse_args()
	except:
		sys.exit(0)


	kiLog.states(False, ok=False, warn=False)
#	kiLog.states('', ok=True)

	print(args)

#	cmdyi.execute(args)
