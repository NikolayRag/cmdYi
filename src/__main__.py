import argparse, sys

import cmdyi
import Yi4kAPI

import kiLog
kiLog.names(('',))


if __name__ == '__main__':
	cParser= argparse.ArgumentParser(description= 'Yi 4k remote control.')

	for cmd in Yi4kAPI.commands:
		if cmd.variable:
			if cmd.values:
				limitZip= list(zip(range(0,len(cmd.values)), cmd.values))
				cParser.add_argument(('-%s' % cmd.commandName),
					choices=list(str(a) for a,b in limitZip),
					help=str(dict(limitZip))
				)
			else:
				cParser.add_argument(('-%s' % cmd.commandName))
		else:
			cParser.add_argument(('-%s' % cmd.commandName), action='store_true', help='')

	
	try:
		args= vars(cParser.parse_args())
	except:
		sys.exit(0)


	setAny= False
	argsA= {}
	for argn,argv in args.items():
		if argv:
			setAny= True
			break

	if not setAny:
		cParser.print_help()
		sys.exit(0)



	cmdyi.execute(args)
