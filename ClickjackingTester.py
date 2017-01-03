import sys
import webbrowser

mensajeBienvenida = """
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+
 |C|l|i|c|k|j|a|c|k|i|n|g| |T|e|s|t| |T|o|o|l| |v|1|.|0| 
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+
"""
version = "v1.0"
name = 'ClickjackingTest.html'

print mensajeBienvenida
print version

if len(sys.argv) != 3:
	print "Invalid amount of parameters please read the help in README.md file"
	sys.exit(1)
	
url = sys.argv[1]
spanLabel = sys.argv[2]

file = open(name,'w')
file.write('<html><span>'+spanLabel+'</span><br/><iframe src="'+url+'" width="90%" height="100%"></iframe></html>')
file.close()

webbrowser.open(name,2)
