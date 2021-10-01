##import xlrd as xl
##
##with xl.open_workbook('D:\\PersonalDoc\\PythonPrac\\ChargeBackDiffTracing\\exportdata.xlsx') as sourcedata:
##    worksheet = sourcedata.sheet_by_name('Data1')
##    for i in range(worksheet.nrows):
##        for j in range(worksheet.ncols):
##            print(worksheet.cell_value(i,j), end = ' ' )
##        print('\n')

import pandas as pd
import datetime as dte
import time

def LoadExcel(excelpath = '', excelsheet = ''): ##Return dataframe, rows# and columns#
    
    if(excelpath=='' or excelsheet==''):
        return
    else:
        df = pd.read_excel(excelpath, sheet_name = excelsheet)
        return [df, len(df), df.shape[1]]

def DropDuplicated(df, col = ''): ##Return a  distinct Series of specific column(col)
    
    if(df.empty==True or col==''):
        return
    else:
        distinctlist = (df.drop_duplicates(col, keep='first'))[col]        
        return distinctlist

def GetSpecificDataset(df, querycode = 0, querycol = '', datecol = '', startdate = dte.datetime.now(), enddate = dte.datetime.now() + dte.timedelta(-30)):
##Use date condition(on column datecol) to select specific values(querycode) from one column(querycol)
    if(df.empty==True or querycode==0 or querycol=='' or datecol=='' ):
        return
    else:
        segdt = df[df[querycol]==querycode]
        #resdt = segdt[(segdt[datecol].values.astype('datetime[D]')>= startdate) & segdt[datecol].values.astype('datetime[D]')<= enddate]
        resdt = segdt[(segdt[datecol]>= startdate) & (segdt[datecol]<= enddate)]
        return resdt

def GetGroupDataset(df, groupcol='', groupbycol=''): ##Use one column(groupcol) to group other column(groupbycol) data
    if(df.empty==True or groupcol=='' or groupbycol==''):
        return
    else:
        resofgroup = df.groupby(by=[groupcol])[groupbycol].sum()
        return resofgroup
    
excel_path = '.\\exportdata.xlsx' ##输入excel文件所在路径
sheet_name = 'Data1' ##excel数据sheet名
company_col = 'Company' ##excel中公司代码列
claim_date_col='ClaimCreateTime' ##excel中时间列1
pre_date_col='PretreatmentTime' ##excel中时间列2
prequerydate=pd.to_datetime(['07-01-2019', '08-01-2019']) ##查询时间列1条件
claimquerydate=pd.to_datetime(['07-01-2019', '08-01-2019']) ##查询时间列2条件
groupcol='ProfitCenter' ##分组列
groupby1='PreCount' ##分组目标列1
groupby2='RealPaid' ##分组目标列2

outputexcelpath = 'output.xlsx' ##输出文件路径，默认与python脚本所在路径相同
sheetheader = ['RealPaid', 'PreCount', 'Diff'] ## 输出文件数据列名

ds = LoadExcel(excel_path, sheet_name) ##
sourceDF = ds[0]

companylist = DropDuplicated(sourceDF, company_col)

excelwriter = pd.ExcelWriter(outputexcelpath)

for i in range(len(companylist)):

    predataset = GetSpecificDataset(sourceDF, companylist[companylist.index[i]], company_col, pre_date_col, prequerydate[0], prequerydate[1])
    pregroup = GetGroupDataset(predataset, groupcol, groupby1)

    claimdataset = GetSpecificDataset(sourceDF, companylist[companylist.index[i]], company_col, claim_date_col, claimquerydate[0], claimquerydate[1])
    claimgroup = GetGroupDataset(claimdataset, groupcol, groupby2)

    if(i==0):
        res0 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res0.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==1):
        res1 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res1.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==2):
        res2 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res2.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==3):
        res3 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res3.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==4):
        res4 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res4.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==5):
        res5 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res5.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==6):
        res6 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res6.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==7):
        res7 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res7.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==8):
        res8 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res8.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==9):
        res9 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res9.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==10):
        res10 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res10.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==11):
        res11 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res11.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==12):
        res12 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res12.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==13):
        res13 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res13.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==14):
        res14 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res14.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==15):
        res15 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res15.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==16):
        res16 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res16.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==17):
        res17 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res17.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==18):
        res18 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res18.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==19):
        res19 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res19.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==20):
        res20 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res20.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==21):
        res21 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res21.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==22):
        res22 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res22.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==23):
        res23 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res23.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==24):
        res24 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res24.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==25):
        res25 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res25.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==26):
        res26 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res26.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==27):
        res27 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res27.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==28):
        res28 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res28.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i==29):
        res29 = pd.concat([claimgroup, pregroup, claimgroup.sub(pregroup, axis=0)], axis=1)
        sheetname = str(companylist[companylist.index[i]].astype(object))
        res29.to_excel(excelwriter, sheet_name = sheetname, header = sheetheader)
    elif(i>=30):
        print('More than 30 companys, press s to save, press any key to quit without saveing')
        a = input()
        if(a=='s'):
            pass
        else:
            exit(0)
        
excelwriter.save()
print('Complete successfully! Press enter to close')
input()

