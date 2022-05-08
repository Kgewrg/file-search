from tika import parser
from fileSearch import returnDir
import os


def retLabObjects(content):
    """ Βρισκει καποιον χαρακτηρα και επιστρεφει απο τον χαρακτηρα 
        εως το τελος
        param: content: (string) το string απο στο οποιο θα ψαξει
        return: labObjects: (πινακας) πινακσας στον οποιο τοποθετουτνται 
                οι γραμμες οι οποιες βρισκει"""
    labObjects=[]
    for i in range(len(content)):
        if (content[i]==''):
            j=i
            EOLcounter=0
            while(content[j]!='.'):
                EOLcounter+=1
                j+=1
            labObjects.append(content[i:i+EOLcounter])

    for i in range(len(labObjects)):
        labObjects[i]=labObjects[i].strip('')
    
    return labObjects


""" Το πρόγραμμα αυτο κάθεται σε ενα φακελο με αλλα pdf μεσα στον φακελο
    και ψαχνει σε κάθε pdf τους στοχους(σε αυτην την περιπτωση) και τους
    γραφει στο αρχειο Output.txt"""
outputFile=open('Output.txt','w', encoding='utf-8')
fileList=returnDir()
counter =0
for i in fileList:
    print(i.path)
    if ('.py' in i.name) or ('.txt' in i.name):
        continue

    parsedPdf = parser.from_file(i.path)
    content=parsedPdf['content']
    print (content)
    if counter > 1: break
    labObjectives=retLabObjects(content)
    

    outputFile.write(i.name)
    outputFile.write('\n')
    for objective in labObjectives:
        print("writing:",objective)
        outputFile.write(objective)
        outputFile.write('\n')
    outputFile.write('\n')
    counter+=1
outputFile.close()


    
    






