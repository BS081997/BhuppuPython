#__File operations using OS module

from os.path import abspath,curdir
a=curdir
print("Current Directory is represented by - ", "'",a,"'")



#__For absolute path of current directory

b=abspath(curdir)
print(b)


#__Remove and Rename file

'''from os import remove,rename
remove("foo/second.txt")
rename("foo/third.txt","foo/second.txt") '''


#__

'''from os import remove,rename
from os.path import join
remove(join("foo","one.txt"))
rename(join("foo","one.txt"),join("foo","three.txt")) '''


#__For list all the files and folders in a particular directory

from os import listdir
print(listdir("foo"))


#__For remove the directory if the directory is empty

'''from os import rmdir
rmdir("bar") '''


#__For Make cross-platform function

from os.path import join
def show_foobar_here(path):
    print(join(path,"dir-1"))





