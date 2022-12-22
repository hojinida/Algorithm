import sys

printer = {"12345678": "ascending", "87654321": "descending"}

s = input()
s = s.replace(' ', '')

if s in printer:
    sys.stdout.write(printer[s])
else:
    sys.stdout.write("mixed")
