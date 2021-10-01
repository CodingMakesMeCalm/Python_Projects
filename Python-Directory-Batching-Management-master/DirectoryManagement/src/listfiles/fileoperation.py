'''
Created on Jan 13, 2020

@author: K
'''
import os
import time
import zipfile
import shutil
import listfiles.filter as fi

class foperate:
    def __init__(self):
        self.CurDir = os.getcwd()
    
    def RenameFile(self, cond):  ##cond name has to be filename.suffix, the filename is the name seed, the suffix is for function using to filter files 
#         print("\nPlease type the file name and file type with filename.filetype",
#               "\nFor example, if you need files like text01.txt,text02.txt,text03...., please type text.txt"
#               "\nThe new file name will start with filename01.")
        nameseed = os.path.splitext(cond)[0]  ##get new file name
        suffixfilter = os.path.splitext(cond)[1]  ##get file suffix
        funcfilter = fi.ffilter()
        df = funcfilter.FileFilter(self.CurDir, 'filetype', 'equal', suffixfilter, False)
        rowidx = 0
        for file in df['file']:
            newname = nameseed + '0' + str(rowidx) + suffixfilter
            if (newname == file):  ##if newfile name is existing already, return. Will not rollback.
                return 'Name is existing'
            else:
                os.renames(os.path.join(df.at[rowidx + 1, 'path'], file), os.path.join(df.at[rowidx + 1, 'path'], newname))
                rowidx = rowidx + 1
        return 'finish'
    
    ##filefilter format 'filetype=.suffix' or 'filename=name'
    def CopyFile(self, newpath, filefilter):  ##
        if (newpath == ''):
            return 'new path can not be empty'
        funcfilter = fi.ffilter()
        
        filtercond = funcfilter.FFParaPreprocess(filefilter)
        df = funcfilter.FileFilter(self.CurDir, filtercond[0], filtercond[1], filtercond[2], False)  ##input True will copy all matched files in recursive current folder
        rowidx = 0
        for file in df['file']:
            if(os.path.exists(os.path.join(newpath, file))):
                return 'file is existing in the new path'
            else:
                shutil.copy(os.path.join(df.at[rowidx + 1, 'path'], file), os.path.join(newpath, file))
                rowidx = rowidx + 1
        return 'finish'    


    def RemoveFile(self, path, filtercondition):
        pass
    
    
    def ZipFile(self, destipath, filefilter):  ##input destipath format 'filepath\zipfilename.zip
        
#         while True:
#             print("\nPlease type the destination path with zip file name. Using fullpath.zip.", 
#                   "\nPreass Enter with empty will use current directory and current date (%Y%m%d%H%M%S) as zip file name.",
#                   "\nType '0' will return previous.")
#             destipath = input()
#             if (destipath == '0'):
#                 return False
#             elif (os.path.exists(os.path.split(destipath)[0]) == False):
#                 print("Path is not available, please retype.")
#                 continue
#             elif (destipath == ''):
#                 zipname = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.zip'
#                 destipath = os.path.join(self.CurDir,zipname)
#                 break
#             else:
#                 break
        if (destipath == ''):
            destipath = os.path.join(self.CurDir, (time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.zip'))
        funcfilter = fi.ffilter()
        
        filtercond = funcfilter.FFParaPreprocess(filefilter)
        df = funcfilter.FileFilter(self.CurDir, filtercond[0], filtercond[1], filtercond[2], False)  ##input True will zip all matched files in recursive current folder
        rowidx = 0
        with zipfile.ZipFile(destipath, 'w') as z:
            for file in df['file']:
                z.write(os.path.join(df.at[rowidx + 1, 'path'], file))
                
        return 'finish'
            
        
            
                
            