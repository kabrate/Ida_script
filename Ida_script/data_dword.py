import struct
import binascii
start = AskAddr(0x14028E330 , "start address:")
print ("start address:%08x"%(start))
length = AskLong(0x400 , "length:")
print ("length:%d"%(length))
fn = AskStr("c:\\table.dump" ,"save as:" )
with open(fn,"wb+") as f:
    for addr in range(start , start+length,8):
        f.write( '0x'+binascii.b2a_hex(struct.pack("I",Byte(addr)))+',')#Dword
print ("success to save as ",fn)
