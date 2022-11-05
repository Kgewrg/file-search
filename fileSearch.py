import os

def returnDir(path='', fileList=[]):
    """ Returns a list with all files in the directory, seaches recusevly,
        filelist: (Array) List with the files of the direcotry in type of os.DirEntry 
        path: Custom directory path, if left empty then execution path is taken as default """
    if path=='':
        path=os.getcwd()

    dirIt=os.scandir(path)
    
    for i in dirIt:
        # avoid script it self
        if i.name == os.path.basename(__file__):
            continue

        # add files to fileList
        if i.is_file():
            fileList.append(i)
        
        # Recurs to other directories
        if i.is_dir():
            returnDir(i.path, fileList)
    
    return fileList


def main():
    """ After you call the function returnDir() you have all the files of the directories current and below the 'path' parameter
        in an array.
        With this array you can create custom scripts to manipuate the files and their content, examples in the codeDump.txt file.    
    """
    fileList=returnDir()
    print("Found the files: ")
    for i in fileList:
        print(i.name)
    


    # input("Enter a key to continiue")

if __name__=='__main__':
    main()