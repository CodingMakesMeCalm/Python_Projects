import os
import time
import pandas as pd
import numpy as np

res = os.walk('D:\\InstallationMedium\\DB')
filescount = 0
filedf = pd.DataFrame(columns = ['path', 'file'])
 
for root, dirs, files in res:
    #sumdir = 0
    #print("Current path:", root)
    for file in files:
        if(file.find('') != -1):
            #print(root, os.path.splitext(file))
            #print(os.path.getsize(os.path.join(root, file))/1024/1024)
            #print(os.path.getatime(os.path.join(root, file)))
            #print(os.path.getctime(os.path.join(root, file)))
            #print(os.path.getmtime(os.path.join(root, file)))
            #print(dirs)
            #print(file)
            #print(file, 'size(MB)', os.path.getsize(os.path.join(root, file))/1024/1024)
            filedf.loc[filescount + 1] = [os.path.join(root,file), file]
            filescount = filescount + 1
        else:
            continue
#print(filedf['path'])
text = filedf.at[1, 'file']
print(text)
