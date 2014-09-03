import color_console as cons
	
def logInfo(message):
	default_colors = cons.getAttr()
	cons.setAttr(cons.FOREGROUND_BLUE | cons.FOREGROUND_INTENSITY)
	print("[*] " + message)
	cons.setAttr(default_colors)

def logOk(message):
	default_colors = cons.getAttr()
	cons.setAttr(cons.FOREGROUND_GREEN | cons.FOREGROUND_INTENSITY)
	print("[+] " + message)
	cons.setAttr(default_colors)
	
def logErr(message):
	default_colors = cons.getAttr()
	cons.setAttr(cons.FOREGROUND_RED | cons.FOREGROUND_INTENSITY)
	print("[-] " + message)
	cons.setAttr(default_colors)
	
def logHdr(message):
	default_colors = cons.getAttr()
	cons.setAttr(cons.FOREGROUND_YELLOW| cons.FOREGROUND_INTENSITY)
	print('[' + message + ']')
	cons.setAttr(default_colors)

def logHdr0(message):
	default_colors = cons.getAttr()
	cons.setAttr(cons.FOREGROUND_YELLOW| cons.FOREGROUND_INTENSITY)
	print('\n=== ' + message.upper() + ' ===\n')
	cons.setAttr(default_colors)	