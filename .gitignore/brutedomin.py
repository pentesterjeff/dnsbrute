import dns.resolver
import sys

try:
	domin = sys.argv[1]
	name_arq = sys.argv[2]
except:
	print 'Error'
	print 'Usage: dnsbrute.py <URL> <WORDLIST>'
	sys.exit(1)
try:
	arq = open(name_arq)
	lines = arq.read().splitlines()
except:
	print 'File Not Found'
	sys.exit(1)

for subdom in lines:
	try:
		domesub = subdom + '.' + domin
		r = dns.resolver.query(domesub, 'a')
		for result in r:
			print domesub, result
	except:
		pass
    
