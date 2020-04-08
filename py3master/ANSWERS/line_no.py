#!/usr/bin/env python

import sys

for file_name in sys.argv[1:]:
    with open(file_name) as file_in:
        for line_number, line in enumerate(file_in, 1):
            # print("{:4d}: {}".format(line_number, line), end='\n')
            print(f"{line_number:4d}: {line}")





