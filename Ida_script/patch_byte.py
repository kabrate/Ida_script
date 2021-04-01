def patch(start):
	fileName=AskFile(0,"*.dump",'ImportFile')
	buffer = open(fileName, "rb").read()#记得把hex转为ascii码
	begin = start;
	for index, byte in enumerate(buffer):
		PatchByte(begin+index, ord(byte))
start = AskAddr(0x1299a0 , "start address:")	
patch(start)