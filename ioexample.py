import os

with os.popen("ipconfig") as ip_info:
    for line in ip_info:
        if "IPv4 Address" in line:
            print(line[:-1])
