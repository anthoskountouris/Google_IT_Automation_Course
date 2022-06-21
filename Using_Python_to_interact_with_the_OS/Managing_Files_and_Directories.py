### Working with Files ###

## Remove ##

import os
os.remove("novel.txt")

## Rename ##

os.rename("first draft. txt", "Finished masterpiece.txt") # rename
os.path.exists("finished_masterpiece.txt") # check if it exists in that directory (T or F)

## Size of file ##
os.path.getsize("spider.txt")

# Get unix timestamp of the file (number of seconds since January 1st 1970)
os.path.getmtime("spider.txt") #12131243142.32131

# datetime
import datetime
timestamp = os.path.getmtime("spider.txt")
datetime.datetime.fromtimestamp(timestamp) #datetime.datetime(2020, 2, 6, 6, 2, 3 , 899999)

## Find the path of the file ##
os.path.abspath("spider.txt") #'/home/user/spider.txt'

### DIRECTORIES ###

## Get current working directory
print(os.getcwd()) # /home/user

## Make new directory
os.mkdir("new_dir")

## Change directories
os.chdir("new_dir") # You set as a parameter the directory you want to go

## Remove directory
os.rmdir("new_dir") #works only if the directory is empty

## List the files and directories of a directory
os.listdir("website") # ['images', 'index.html', 'favicon.ico']

## Creating the full paths of the files/directories in a directory

import os
os.listdir("website")
#[images",index.html',"favicon.ico"]
dir = "website"
for name in os.listdir(dir):
	fullname = os.path.join(dir, name)
	if os.path.isdir(fullname)
		print("{} is a directory".format(fullname))
	else:
		print("{} is a file".format(fullname))
# website/images is a directory
# website/index.html is a file
# website/favicon.ico is a file
