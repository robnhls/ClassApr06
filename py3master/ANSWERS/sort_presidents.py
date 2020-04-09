#!/usr/bin/env python

# list to hold all presidents (will be list of lists)
all_pres = []
FIRST_NAME = 2
LAST_NAME = 1
STATE_OF_BIRTH = 6

with open("../DATA/presidents.txt", "r") as PRES:

    for line in PRES:
        fields = line.rstrip('\n\r').split(":")
        all_pres.append(fields) # add list of fields

# sort by lname, fname
for fields in sorted(all_pres, key=lambda e: (e[LAST_NAME], e[FIRST_NAME])):
    print(fields[FIRST_NAME], fields[LAST_NAME], fields[STATE_OF_BIRTH])

