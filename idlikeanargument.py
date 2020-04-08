
import sys
# idlikeanargument.py 5 5 False

quality = 0
quantity = 1
contrary = False

filename = sys.argv[0]

if len(sys.argv) > 1:
    quality = int(sys.argv[1])

if len(sys.argv) > 2:
    quantity = int(sys.argv[2])

if len(sys.argv) > 3:
    contrary = bool(sys.argv[3])

print(filename, quality, quantity, contrary)
