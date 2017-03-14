import sys
import webbrowser
import argparse
import validators
import os

welcomeMsg = """
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+
 |C|l|i|c|k|j|a|c|k|i|n|g| |T|e|s|t| |T|o|o|l| |v|1|.|7| 
 +-+-+-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+ +-+-+-+-+ +-+-+-+-+
"""
finishMsg = "The file was created, opening the web browser..."

print welcomeMsg

#parse
parser = argparse.ArgumentParser(description="", version="1.7")
parser.add_argument('-u',action="store", dest="url", help="frame Url", required=True)
parser.add_argument('-l', action="store", dest="label", help="message upside the frame", required=True)
parser.add_argument('-o', action="store", dest="output", help="path and file name destination", required=True)
results = parser.parse_args()

#validate url
if not validators.url(results.url):
	print "The argument -u is invalid"
	sys.exit();

#validate output
folder = os.path.dirname(results.output)
if not os.path.isdir(folder):
	print "The argument -o is invalid"
	sys.exit();

#save file
file = open(results.output,'w')
file.write('<html><span>'+ results.label +'</span><br/><iframe src="'+ results.url +'" width="90%" height="100%"></iframe></html>')
file.close()

print finishMsg

#open browser
webbrowser.open(results.output, 2)