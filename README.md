# file-search
A recursive function that returns all files in of the lower file tree 

(Some comments of this repo may still be in Greek that's because i forgot to change them)

The core part out of this repo is the function returnDir in the fileSearch.py file.
  This function returns all the file of a file tree in a list (a queue with the "deepest" files first)
  The items of the list are of type: nt.DirEntry so you can get the name of the file with .name na the path with .path
  
The usefull thing about this is what you can do with this list, for example, the 3rd "code block" in the codeDump.txt, travers this list and copies the cotents
of all .c and .sh file into one .txt output file.

