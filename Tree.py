import sys

size=11
sys.stdout.write('          *')
for y in range (0, size):
    for x in range (0, size - y):
        sys.stdout.write(" ")
    for star in range (0, y+y):
        sys.stdout.write("b")
    print('')
for y in range (0, 2):
    for x in range (0, size/2+3):
        sys.stdout.write(" ")
    sys.stdout.write(" aaa")
    print('')
