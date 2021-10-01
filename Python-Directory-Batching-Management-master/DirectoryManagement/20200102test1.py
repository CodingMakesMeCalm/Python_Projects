import os
import time
import pandas as pd
import numpy as np
import listfiles.filter as fi
import listfiles.listfile as lf
import listfiles.fileoperation as fo

#df = pd.DataFrame(columns = ['path','name'])

#t = lf.FileFilter(os.getcwd(), 'filetype', 'equal', '.py', True)
t = fo.foperate()
t.CurDir = 'D:\\PersonalDoc\\PythonProjects\\DirectoryManagement'
print(t.ZipFile('D:\\text.zip', 'filetype=.txt'))
# for ent in os.scandir(os.getcwd()):
#     #t = ent.stat()
#     
#     #print(ent.name)
#     #print(ent.inode())
#     #print("isdir: ", ent.is_dir())
#     #print("isfile: ", ent.is_file())
#     #print(ent.is_symlink())
#     #print(ent.path)
    #filesurf = (os.path.splitext(ent.path))[1]
#     print("\n" , os.path.split(ent.path)[0],
#           "\n" , os.path.split(ent.path)[1],
#           "\n" , os.path.splitext(ent.path)[1])
#     if ((filesurf == '') or (ent.is_dir() == True) or (filesurf != '.py')):
#         #print('nothing')
#         print("cond1:------->", ent.stat().st_size)
#     else:
#         print(ent.path)

#     print(t.st_mode)
#     print(t.st_file_attributes)
#     print(t.st_dev)
# 
#     print("\ncontent of t\n")
#     print(t.st_atime)
#     if (t.st_atime < time.time()):
#         print("less than")
#     else:
#         print("big than")
#     print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t.st_atime)))
# 
#     print(t.st_ctime)
#     print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t.st_ctime)))
#     
#     print(t.st_mtime)
#     print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t.st_mtime)))
#     
#     print(t.st_size/1024, 'KB')
    #print(t.uid)
#     print("end of t")
#     print("-----------------------\n")
   
##print('\n')
##filepath = input()
##print(os.path.exists(filepath))
##if (filepath[-1] == '\\'):
##    print(filepath[-1])
##else:
##    print(filepath[-1])

##df=pd.DataFrame(np.arange(16).reshape((4,4)),index=['a','b','c','d'],columns=['one','two','three','four'])
##df.loc['5'] = [1,2,3,4]

##res = os.walk('D:\\InstallationMedium\\DB')
##dirscount = 0
##filescount = 0
##totalsize = 0
##
##for root, dirs, files in res:
##    sumdir = 0
##    print("Current path:", root)
##    for file in files:
##        filepath = os.path.join(root, file)
##        print("\t", filepath, "\tSize(KB):", os.path.getsize(filepath)/1024)
##        sumdir = sumdir + os.path.getsize(filepath)/1024
##        filescount = filescount + 1
##    print("files total size(MB) in this directory:", sumdir/1024)
##    totalsize = totalsize + sumdir/1024
##    dirscount = dirscount + 1
##
##print("total sub-directories:", dirscount - 1, "\ntotal files:", filescount, "\ntotal size(MB):", totalsize)


# res = os.walk('D:\\InstallationMedium\\DB')
# filescount = 0
# filedf = pd.DataFrame(columns = ['path', 'file'])
#  
# for root, dirs, files in res:
#     #sumdir = 0
#     #print("Current path:", root)
#     for file in files:
#         if(file.find('') != -1):
#             #print(root, os.path.splitext(file))
#             #print(os.path.getsize(os.path.join(root, file))/1024/1024)
#             #print(os.path.getatime(os.path.join(root, file)))
#             #print(os.path.getctime(os.path.join(root, file)))
#             #print(os.path.getmtime(os.path.join(root, file)))
#             #print(dirs)
#             #print(file)
#             #print(file, 'size(MB)', os.path.getsize(os.path.join(root, file))/1024/1024)
#             filedf.loc[filescount + 1] = [os.path.join(root,file), file]
#             filescount = filescount + 1
#             print(os.path.(os.path.join(root,file)))
#         else:
#             continue
#print(filedf['path'])
# text = filedf.at[1, 'file']
# print(text)
# print(os.path.splitext("vi_cheat_sheet.pdf"))
# print(os.path.isfile("D:\\FanshaweLearning\\INFO5111\\vi_cheat_sheet.pdf"))
        #filedf.loc[filescount + 1] = [root, file]
        #filepath = os.path.join(root, file)
        #print("\t", filepath, "\tSize(KB):", os.path.getsize(filepath)/1024)
        #sumdir = sumdir + os.path.getsize(filepath)/1024
        #filescount = filescount + 1
        #print(fileser)
    #print("files total size(MB) in this directory:", sumdir/1024)
    #totalsize = totalsize + sumdir/1024
    #dirscount = dirscount + 1
# 
# #print(filedf.loc[filedf.file.str.contains('iso')])
# 
# #print("total sub-directories:", dirscount - 1, "\ntotal files:", filescount, "\ntotal size(MB):", totalsize)