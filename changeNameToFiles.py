import os

path = "C:\\Users\\idosh\\Desktop\\toolbox"

os.chdir(path)

for filename in os.listdir(os.getcwd()):
    save = filename
    x = filename.index('.')
    print(f"{x} x")
    typeFile = save[x:]
    print(f"{typeFile} typefile")
    save = save[:x]
    print(f"{save} filename")
    firstLetter = save[0]
    print(f"{firstLetter} fl")
    save = save[1:]
    print(f"{save} filename1")
    newfilename =  save+ firstLetter + typeFile
    os.rename(filename, newfilename, src_dir_fd=None, dst_dir_fd=None)

