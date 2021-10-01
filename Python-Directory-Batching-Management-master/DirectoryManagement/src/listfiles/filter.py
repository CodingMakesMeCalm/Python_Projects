'''
Created on Jan 10, 2020

@author: K
'''

import pandas as pd
import os
import re
import time
import datetime


class ffilter:
    
    def __init__(self):
        self.dicfilterleft = ['filetype', 'filename', 'filesize', 'access', 'create', 'modify']
    
    # parameter diction of filterleft = [filetype, filename, filesize, access, create, modify]
    # parameter diction of filterm = [equal, lessthan, morethan]
    # parameter filterright is the condition. 
    # For example, to search file size more than 2M, parameters will be filterleft=filesize, fileter=morethan, filterright=2
    def FileFilter(self, curdir, filterleft, filterm, filterright, issubincluded=False):
        outputlist = pd.DataFrame(columns=['path', 'file'])
        if (issubincluded == False):  # #searching do not include sub directory, no recursive
            if (filterm == 'equal'):
                if (filterleft == 'filetype'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        filesuff = (os.path.splitext(file.name))[1]  # #get file suffix
                        if ((file.is_dir() == True) or (filesuff == '') or (filesuff != filterright)):
                            continue
                        else:
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]  # #save by [path of file(no including file name), file name]
                            rowidx = rowidx + 1
                            continue
                    return outputlist
                elif (filterleft == 'filename'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        filename = (os.path.splitext(file.name))[0]  # #get file name
                        if ((file.is_dir() == True) or (filename.find(filterright) == -1)):
                            continue
                        else:
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                    return outputlist                    
                else:
                    return False
            elif (filterm == 'lessthan'):
                if (filterleft == 'filesize'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_size / 1024 / 1024 < filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist                    
                elif (filterleft == 'access'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_atime < filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                elif (filterleft == 'create'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_ctime < filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                elif (filterleft == 'modify'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_mtime < filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                else:
                    return False
            elif (filterm == 'morethan'):
                if (filterleft == 'filesize'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and ((file.stat().st_size / 1024 / 1024) > filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist 
                elif (filterleft == 'access'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_atime > filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                elif (filterleft == 'create'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_ctime > filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                elif (filterleft == 'modify'):
                    rowidx = 0
                    for file in os.scandir(curdir):
                        if ((file.is_dir() == False) and (file.stat().st_mtime > filterright)):
                            outputlist.loc[rowidx + 1] = [os.path.split(file.path)[0], file.name]
                            rowidx = rowidx + 1
                            continue
                        else:
                            continue
                    return outputlist
                else:
                    return False
        else:  # #searching include sub directory, recursive
            if (filterm == 'equal'):
                if (filterleft == 'filetype'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            filesuff = (os.path.splitext(file))[1]
                            if ((filesuff == '') or (filesuff != filterright)):
                                continue
                            else:
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                    return outputlist
                elif (filterleft == 'filename'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            filename = (os.path.splitext(file))[0]
                            if (filename.find(filterright) == -1):
                                continue
                            else:
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                    return outputlist        
                else:
                    return False
            elif (filterm == 'lessthan'):
                if (filterleft == 'filesize'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getsize(os.path.join(root, file)) / 1024 / 1024 < filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist                    
                elif (filterleft == 'access'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getatime(os.path.join(root, file)) < filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                elif (filterleft == 'create'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getctime(os.path.join(root, file)) < filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                elif (filterleft == 'modify'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getmtime(os.path.join(root, file)) < filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                else:
                    return False
            elif (filterm == 'morethan'):
                if (filterleft == 'filesize'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getsize(os.path.join(root, file)) / 1024 / 1024 > filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist                    
                elif (filterleft == 'access'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getatime(os.path.join(root, file)) > filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                elif (filterleft == 'create'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getctime(os.path.join(root, file)) > filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                elif (filterleft == 'modify'):
                    rowidx = 0
                    for root, dirs, files in os.walk(curdir):
                        for file in files:
                            if (os.path.getmtime(os.path.join(root, file)) > filterright):
                                outputlist.loc[rowidx + 1] = [root, file]
                                rowidx = rowidx + 1
                                continue
                            else:
                                continue
                    return outputlist
                else:
                    return False
            else:
                return False
    
    #if using date filter, the input has to be 'yyyymmdd' format
    def FFParaPreprocess(self, parastr):  ##Analyze and split parameter from string        
        filterleft, filterright = re.split('[<,>,=]', parastr)
        filterm = ''
        
        if (filterleft not in self.dicfilterleft):
            return 'Wrong file attribute'
        
        if ('<' in parastr):
            filterm = 'lessthan'
        elif ('>' in parastr):
            filterm = 'morethan'
        elif ('=' in parastr):
            filterm = 'equal'
        else:
            return 'Wrong operate symbol'
        
        if ((filterleft in ['filesize', 'access', 'create', 'modify']) and filterright.isdigit() == False):
            return 'Wrong digital value'
        elif ((filterleft in ['filetype', 'filename']) and (filterm != 'equal')):
            return 'Wrong equal value'
        elif ((filterleft == 'filetype') and (filterright[0] != '.')):
            return 'Wrong filetype suffix'
        else:
            if ((filterleft in ['access', 'create', 'modify']) and filterright.isdigit() == True):
                filterright = int(time.mktime(datetime.datetime.strptime(filterright, '%Y%m%d').timetuple()))
            elif (filterleft == 'filesize'):
                filterright = int(filterright)            
            return (filterleft, filterm, filterright)    
    