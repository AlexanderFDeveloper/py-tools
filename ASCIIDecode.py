import sys

ASCIIValues = [int(arg) for arg in sys.argv[1:]]
ASCIIString = "".join([chr(value) for value in ASCIIValues])

print 'Ascii Decoded:', ASCIIString
