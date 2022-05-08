import os



def returnDir(path='', fileList=[]):
    """ Returns a list with all files in the directory, seaches recusevly,
        filelist: (Array) List with the files of the direcotry in type of os.DirEntry 
        path: Custom directory path"""
    if path=='':
        path=os.getcwd()

    #print("Searching on directory:", path)
    dirIt=os.scandir(path)
    
    for i in dirIt:
        # avoid script it self
        if i.name == os.path.basename(__file__):
            continue

        # add files to fileList
        if i.is_file():
            #print("Appending file,", i.name, "from directory:", i.path)
            fileList.append(i)
        
        # Recurs to other directories
        if i.is_dir():
            #print("Recursing to:", i.path)
            returnDir(i.path, fileList)
    
    return fileList


def main():
    """ Τα αρχεια αποθυκευονται στον πινακα fileList, το script αυτο ειναι σαν template, 
        Κατω απο το fileList=returnDir() γραφεται ο κωδικας για εκεινη την περιπτωση 
        Ήδη γραμμενα κομμάτια κώδικα ειανι στο αρχειο codeDump.txt"""

    fileList=returnDir()
    print("Found the files: ")
    for i in fileList:
        print(i.name)
    


    # input("Enter a key to continiue")


    
    







if __name__=='__main__':
    main()