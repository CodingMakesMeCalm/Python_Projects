import os
import pandas as pd




class DirectoryManament(object):

    def __init__(self):
        self.CurUser = os.getlogin()  ##get current user name
        self.CurDir = os.getcwd()  ##get current directory which this .py file is in
        
        #self.Objects = os.listdir()

       
    def ChangeDirectory(self, path):
        if (os.path.exists(path)):  ##if new path is existing, change current path to the new
            os.chdir(path)
            self.CurDir = os.getcwd()
            return True
        else:
            print("The given path is not existing, type 'C' to create it, other key will return without any change.")
            ifcreate = input()
            if (ifcreate == 'C'):
                os.makedirs(path)
                os.chdir(path)
                self.CurDir = os.getcwd()
                return True
            else:
                return False


#     def FFParaPreprocessInteraction(self):  ##Input parameter by interactive. Preprocess parameter of function FileFilter.
#         leftfileter = ''
#         fileter = ''
#         rightfileter = ''        
#         while True:
#             print("\nPlease choose file attribute, type '0' to return previous. Other key will repeat.",
#                   "\n1.use file type to filter.",
#                   "\n2.use file name to filter, support fuzzy searching.",
#                   "\n3.a range of file size to filter.",
#                   "\n4.a range of access time to filter.",
#                   "\n5.a range of create time to filter.",
#                   "\n6.a range of modify time to filter.")
#             leftfileter = input()
#             if (leftfileter == '0'):
#                 return False
#             elif (leftfileter == '1'):
#                 leftfileter = 'filetype'
#                 fileter = 'equal'
#                 break
#             elif (leftfileter == '2'):
#                 leftfileter = 'filename'
#                 fileter = 'equal'
#                 break
#             elif (leftfileter == '3'):
#                 leftfileter = 'filesize'
#                 break
#             elif (leftfileter == '4'):
#                 leftfileter = 'access'
#                 break
#             elif (leftfileter == '5'):
#                 leftfileter = 'create'
#                 break
#             elif (leftfileter == '6'):
#                 leftfileter = 'modif'
#                 break
#             else:
#                 continue
#         if (fileter != 'equal'):
#             while True:
#                 print("\nPlease choose filter, type '0' to return previous. Other key will repeat.",
#                       "\n1.lessthan, only available on file size, access time, create time and modify time filter",
#                       "\n2.morethan, only available on file size, access time, create time and modify time filter")
#                 fileter = input()
#                 if (fileter == '0'):
#                     return False
#                 elif (fileter == '1'):
#                     fileter = 'lessthan'
#                     break
#                 elif (fileter == '2'):
#                     fileter = 'morethan'
#                     break
#                 else:
#                     continue        
#         while True:    
#             print("\nPlease type condition to filter, type '0' to return previous. Other key will repeat.",
#                   "\nIf the content of type is not match with filter, will repeat to type.")
#             rightfileter = input()
#             if (rightfileter == '0'):
#                 return False
#             elif (leftfileter == 'filetype' and rightfileter[0] == '.'):
#                 break
#             elif (leftfileter == 'filename' and rightfileter.isalnum() == True):
#                 break
#             elif ((leftfileter == 'filesize' or leftfileter == 'access' or leftfileter == 'create' or leftfileter == 'modif') and rightfileter.isdigit() == True):
#                 break
#             else:
#                 continue            
#         return (leftfileter, fileter, rightfileter)

    def NetworkFileServerLogin(self, username, password):
        pass


        
    def NetworkFileCopy(self, path, netdestination):
        pass
        #scp
        #ftp
        #other
        #login


if (__name__ == "__main__"):

    DM = DirectoryManament()
    
    print("Hi,", DM.CurUser, "welcome to Directory Batch Management System.")

    while True:
        print("\nCurrent directory is:", DM.CurDir)
        print("=================================")
        print("Choose an option(type the number): \n",
              "1.Change current directory.\n",
              "2.List detail objects of current directory.\n",
              "3.Traversing all files by recursive under current directory.\n",
              "4.Batching rename\copy\\remove specific file type.\n",
              "5.Batching zip specific files.\n",
              "6.Batching copy network files.\n",
              "7.Exit\n",
              "Other key will repeat this menu.\n",
              "==================================")
        firstlev = input()
    
        if (firstlev == '1'):
            while True:
                print("\nThis is in option 1:")
                print("Current directory is:", DM.CurDir)
                print("Type new directory, must be full path. Type '0' to return previous menu.")
                newpath = input()
                if (newpath == '0'):
                    break
                else:
                    if (DM.ChangeDirectory(newpath)):
                        print("Current directory is: ", DM.CurDir)
                        print("Change new directory successfully. Type '0' to return previous menu. Other key will stay.\n")
                        seclev = input()
                        if (seclev == '0'):
                            break
                        else:
                            continue
                    else:
                        break
        elif (firstlev == '2'):
            while True:
                print("\nThis is in option 2:")
                print("Current directory is:", DM.CurDir)
                print("Choose item of order by Descending. Type '0' to return previous menu. Other key will stay\n",
                      "1.Order by name\n",
                      "2.Order by size(KB)\n",
                      "3.Order by last access time\n",
                      "4.Order by create time\n",
                      "5.Order by last modify time\n")
                orderoption = input()
                if (orderoption == '0'):
                    break
                elif (orderoption == '1'):
                    print(DM.ListObjects('FileName').reset_index(drop = True))
                elif (orderoption == '2'):
                    print(DM.ListObjects('FileSize(KB)').reset_index(drop = True))
                elif (orderoption == '3'):
                    print(DM.ListObjects('LastAccess').reset_index(drop = True))
                elif (orderoption == '4'):
                    print(DM.ListObjects('Create').reset_index(drop = True))
                elif (orderoption == '5'):
                    print(DM.ListObjects('LastModify').reset_index(drop = True))
                else:
                    continue
        elif (firstlev == '3'):
            while True:
                print("\nThis is in option 3:\n")
                print("Current directory is:", DM.CurDir)
                print("Choose type of Traversing. Type '0' to return without any operation\n", 
                      "Type '1' to Traversing all items of current directory\n",
                      "For condition searching, type key word(s) directly.")
                cond = input()
                if (cond == '0'):
                    break
                elif (cond == '1'):
                    DM.RecursiveListAll()
                    print("\nPress Enter to return precious.")
                    input()
                    continue
                else:
                    print(DM.RecursiveListFileCond(cond))
                    print("\nPress Enter to return precious.")
                    input()
                    continue
        elif (firstlev == '4'):
            DM.RenameFile()
        elif (firstlev == '5'):
            pass
        elif (firstlev == '6'):
            pass
        elif (firstlev == '7'):
            exit(0)
        else:
            continue


