import pandas as pd

print('Input any int number:')
AxieNum = input() ##Get the N
AxieNum = int(AxieNum)

test = [[0 for i in range(AxieNum)] for j in range(AxieNum)] ##init a two-dimension array

WhileLoopCon = AxieNum ##Loop control
XArrayPointer = 0 ##First row pointer in every loop
YArrayPointer = AxieNum - 1 ##Last column pointer in every loop
printnum = 0 ##Value for every item in array 'test'

while(WhileLoopCon>0):
    
    for i in range(WhileLoopCon - 1): ##Set up side (N - 1 items) value 
        test[XArrayPointer][XArrayPointer + i] = printnum
        printnum += 1

    for i in range(WhileLoopCon - 1): ##Set right side (N - 1 items) value
        test[XArrayPointer + i][YArrayPointer] = printnum
        printnum += 1

    for i in range(WhileLoopCon - 1): ####Set down side (N - 1 items) value
        test[YArrayPointer][YArrayPointer - i] = printnum
        printnum += 1

    for i in range(WhileLoopCon - 1): ##Set left side (N - 1 items) value
        test[YArrayPointer - i][XArrayPointer] = printnum
        printnum += 1
    ##print('WhileLoopCon:' + str(WhileLoopCon) + ' XArrayPointer:' + str(XArrayPointer) + ' YArrayPointer' + str(YArrayPointer))
    if(WhileLoopCon==1 or XArrayPointer==YArrayPointer): ##If N is odd number, fill center item (the last) value
        test[XArrayPointer][YArrayPointer] = printnum

    
    XArrayPointer = XArrayPointer + 1 ##Point to the first row in next loop
    YArrayPointer = YArrayPointer - 1 ##Point to the last column in next loop
    WhileLoopCon = WhileLoopCon - 2
#print(pd.DataFrame(test))
for i in range(len(test)):
    print(test[i])








        
