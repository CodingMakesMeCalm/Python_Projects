'''
Created on Jan 13, 2020

@author: K
'''
import os
import pandas as pd
import time

class flist:
    
    def __init__(self):
        self.CurDir = os.getcwd()
        
        #orderby = ['FileName', 'FileSize(KB)', 'IsFolder', 'LastAccess', 'Create', 'LastModify']
    def ListObjects(self, orderby):  ##return all objects in current folder
        if (orderby not in ['FileName', 'FileSize(KB)', 'IsFolder', 'LastAccess', 'Create', 'LastModify']):
            return 'Wrong orderby name'
        
        outlist = pd.DataFrame(columns = ['FileName', 'FileSize(KB)', 'IsFolder', 'LastAccess', 'Create', 'LastModify'])
        rowidx = 1
        
        for obj in os.scandir(self.CurDir):
            objprep = obj.stat()
            
            filename = obj.name
            filesize = objprep.st_size/1024
            isfolder = obj.is_dir()
            lastacc = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(objprep.st_atime))
            createtime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(objprep.st_ctime))
            lastmodi = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(objprep.st_mtime))
            
            outlist.loc[rowidx] = [filename, filesize, isfolder, lastacc, createtime, lastmodi]
            rowidx = rowidx + 1
        
        outlist.sort_values(by = ['IsFolder', orderby], ascending = (False, False), inplace = True)  ##
        ##set print option
        pd.set_option('display.width', 5000)
        pd.set_option('display.max_columns', 500)
        pd.set_option('display.max_rows', 500)
        pd.set_option('display.max_colwidth', 1000)
        
        #print(outlist.shape[0])
        #print(outlist.reset_index(drop = True))
        return outlist
    
        
    def RecursiveListAll(self):  ##print recursive list start with current path 
        dirscount = 0
        filescount = 0
        totalsize = 0

        for root, dirs, files in os.walk(self.CurDir):  ##get a triple array by Recursion
            sumdir = 0
            print("Current path:", root)
            for file in files:
                filepath = os.path.join(root, file)
                print("\t", filepath, "\tSize(KB):", os.path.getsize(filepath)/1024)
                sumdir = sumdir + os.path.getsize(filepath)/1024
                filescount = filescount + 1
            print("files total size(MB) in this directory:", sumdir/1024)
            totalsize = totalsize + sumdir/1024
            dirscount = dirscount + 1

        print("\nTotal sub-directories:", dirscount - 1, "\nTotal files:", filescount, "\nTotal size(MB):", totalsize)


    def RecursiveListFileCond(self, cond = ''):  ##list files by recursion and return a dataframe
        rowidx = 0
        filedf = pd.DataFrame(columns = ['path', 'file', 'size(KB)'])

        for root, dirs, files in os.walk(self.CurDir):  ##get a triple array by Recursion
            for file in files:
                if (file.find(cond) != -1):
                    filesize = os.path.getsize(os.path.join(root, file))/1024
                    filedf.loc[rowidx + 1] = [root, file, filesize]                    
                else:
                    continue
                rowidx = rowidx + 1
                
        return filedf    
