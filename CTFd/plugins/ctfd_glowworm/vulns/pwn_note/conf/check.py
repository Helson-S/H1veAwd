from pwn import *
from sys import *
import time

host = argv[1]
port = int(argv[2])
timeout = 30

context.log_level = 'critical'


def getIO():
    return remote(host, port, timeout=timeout)

#normal I/O check
def check1():
	try:
		p = getIO()
		info = p.recvuntil(b"choice>", drop=True, timeout=0.5)
		if info[-1] != 10:
			raise Exception("Service is nothing")
		p.close()
	except Exception as e:
		p.close()
		raise Exception("check1 error, "+str(e))
	return True



def checker():
	try:
		# add your check function name
		if check1():
			pass
		else:
			print("team" + str(port)[1:3])
	except Exception as e:
		print("team" + str(port)[1:3])


if __name__ == '__main__':
    checker()

