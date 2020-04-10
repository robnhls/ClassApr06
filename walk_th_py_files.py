import os.path


# print the py files in this directory


for dirpath, directories, files in os.walk("c:\\class"):
    if ".git" in dirpath:
        continue
    for filename in files:
        if filename.endswith(".txt"):
            print(filename)
        # print("dirpath", dirpath)
        # print("files", files)
        # print("directories", directories)
        # print("-------------------------------")
