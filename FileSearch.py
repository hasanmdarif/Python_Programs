import fnmatch
import os

#Searches File for different extensions
rootPath = '/'
while 1:
    pattern = "*." + input("Enter Extension for which you want to search files for. (Example : png, mp3)\n")
    for root, dirs, files in os.walk(rootPath):
        for filename in fnmatch.filter(files, pattern):
            print(os.path.join(root, filename))
    print("End of List")
