import sys
import argparse

parser = argparse.ArgumentParser(prog="Double it")

parser.add_argument("numbers", type=int, nargs="*",
                    help="The numbers to be doubled")
parser.add_argument("-d", "--debug",
                    help="Enable verbose debugging", action="store_true")

args = parser.parse_args()

for number in args.numbers:
    if args.debug:
        print("Current value", number)
    print(number * 2)


# python doubleit 12 13 14
# expected output
# 24
# 26
# 28

# if len(sys.argv) < 2:
#     print("No arguments")
#     sys.exit(1)  # quit the program

# for arg in sys.argv[1:]:
#     number = int(arg)
#     print(number * 2)
