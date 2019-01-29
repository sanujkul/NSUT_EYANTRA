#OurNodes:
def findLeftRight(prev, curr, nex):
    currSlope = (ourNodesDict[curr][0]-ourNodesDict[prev][0])/(ourNodesDict[curr][1]-ourNodesDict[prev][1])   #slope of current path
    nextSlope = (ourNodesDict[nex][0]-ourNodesDict[curr][0])/(ourNodesDict[nex][1]-ourNodesDict[curr][1])     #slope of path to be taken
    if currSlope==nextSlope:
        return "U"
    if currSlope==0:
        #currDirection = (ourNodesDict[curr][0]-ourNodesDict[prev][0])                      #if +: current going right, - current goint left
        #if currDirection == -1:
        if nextSlope==1:
           return "R"
        else:
            return "L"
        
    if currSlope==1:
        if nextSlope==0:
            return "L"
        else:
            return "R"
        
    if currSlope==-1:
        if nextSlope==0:
            return "R"
        else:
            return "L"

def findStartLeftRight(stSlope, curr, nex):
    currSlope = stSlope  #slope of current path
    nextSlope = (ourNodesDict[nex][0]-ourNodesDict[curr][0])/(ourNodesDict[nex][1]-ourNodesDict[curr][1])     #slope of path to be taken

    if currSlope==nextSlope:
        return "U"
    
    if currSlope==0:
        #currDirection = (ourNodesDict[curr][0]-ourNodesDict[prev][0])                      #if +: current going right, - current goint left
        #if currDirection == -1:
        if nextSlope==1:
           return "R"
        else:
            return "L"
        
    if currSlope==1:
        if nextSlope==0:
            return "L"
        else:
            return "R"
        
    if currSlope==-1:
        if nextSlope==0:
            return "R"
        else:
            return "L"


ourNodes = [[0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0],
           [0,0,0,0,0,0,0,0,0,0,0,0,0]]

ourNodes[1][6] = [1,[(1,3)]]
ourNodes[1][7] = [2,[(1,1)]]

ourNodes[2][4] = [3,[(2,3)]]
ourNodes[2][5] = [4,[(1,2),(2,1)]]
ourNodes[2][8] = [5,[(4,3),(1,2)]]
ourNodes[2][9] = [6,[(1,3)]]

ourNodes[3][2] = [7,[(5,3)]]
ourNodes[3][3] = [8,[(2,2),(5,1)]]
ourNodes[3][6] = [9,[(3,3),(2,2),(1,1)]]
ourNodes[3][7] = [10,[(4,2),(3,1),(1,3)]]
ourNodes[3][10] = [11,[(9,3),(4,2)]]
ourNodes[3][11] = [12,[(9,1)]]

ourNodes[4][1] = [13,[(5,2)]]
ourNodes[4][4] = [14,[(6,3),(5,2),(2,1)]]
ourNodes[4][5] = [15,[(3,2),(6,1),(2,3)]]
ourNodes[4][8] = [16,[(8,3),(3,2),(4,1)]]
ourNodes[4][9] = [17,[(9,2),(8,1),(4,3)]]
ourNodes[4][12] = [18,[(9,2)]]

ourNodes[5][2] = [19,[(5,1),(10,3)]]
ourNodes[5][3] = [20,[(6,2),(10,1),(5,3)]]
ourNodes[5][6] = [21,[(7,3),(6,2),(3,1)]]
ourNodes[5][7] = [22,[(8,2),(7,1),(3,3)]]
ourNodes[5][10] = [23,[(14,3),(8,2),(9,1)]]
ourNodes[5][11] = [24,[(14,1),(9,3)]]

ourNodes[6][1] = [25,[(10,2)]]
ourNodes[6][4] = [26,[(11,3),(10,2),(6,1)]]
ourNodes[6][5] = [27,[(7,2),(11,1),(6,3)]]
ourNodes[6][8] = [28,[(13,3),(7,2),(8,1)]]
ourNodes[6][9] = [29,[(14,2),(13,1),(8,3)]]
ourNodes[6][12] = [30,[(14,2)]]

ourNodes[7][2] = [31,[(10,1),(15,3)]]
ourNodes[7][3] = [32,[(11,2),(15,1),(10,3)]]
ourNodes[7][6] = [33,[(12,3),(11,2),(7,1)]]
ourNodes[7][7] = [34,[(13,2),(12,1),(7,3)]]
ourNodes[7][10] = [35,[(19,3),(13,2),(14,1)]]
ourNodes[7][11] = [36,[(19,1),(14,3)]]

ourNodes[8][1] = [37,[(15,2)]]
ourNodes[8][4] = [38,[(16,3),(15,2),(11,1)]]
ourNodes[8][5] = [39,[(12,2),(16,1),(11,3)]]
ourNodes[8][8] = [40,[(18,1),(12,2),(13,1)]]
ourNodes[8][9] = [41,[(19,2),(18,1),(13,3)]]
ourNodes[8][12] = [42,[(19,2)]]

ourNodes[9][2] = [43,[(15,1)]]
ourNodes[9][3] = [44,[(15,3),(16,2)]]
ourNodes[9][6] = [45,[(17,3),(16,2),(12,1)]]
ourNodes[9][7] = [46,[(18,2),(17,1),(12,3)]]
ourNodes[9][10] = [47,[(18,2),(19,1)]]
ourNodes[9][11] = [48,[(19,3)]]

ourNodes[10][4] = [49,[(16,1)]]
ourNodes[10][5] = [50,[(16,3),(17,2)]]
ourNodes[10][8] = [51,[(17,2),(18,3)]]
ourNodes[10][9] = [52,[(18,3)]]

ourNodes[11][6] = [53,[(17,1)]]
ourNodes[11][7] = [54,[(17,3)]]

#Following line will make a dict from ourNodes:
ourNodesDict = {}
for i in range(1,12):              #Counter will go till 11
    for j in range(1,13):          #Counter will go till 12
        if ourNodes[i][j] != 0:
            ourNodesDict[ourNodes[i][j][0]] = [i,j]
    
print(ourNodesDict)
print("=================================")

prevNode = -1
lastSlope = 0
#====================================================================================
def findPath(path):
    global prevNode
    global lastSlope
    directions = []
    for i in range(0,len(path)-1):
        #print(i)\
        if i==0:
            directions.append(findStartLeftRight(lastSlope,path[0],path[1]))
        else:
            if i > 0:
                prevNode  = path[i-1]
            #Checking for start node

            currNode = path[i]
            nextNode = path[i+1]
    
            if currNode==25 and prevNode==-1:
                if ourNodesDict[nextNode][1]>ourNodesDict[currNode][1]:
                    directions.append("L")
                else:
                    path.append("R")
            elif currNode==30 and prevNode==-1:
                if ourNodesDict[nextNode][1]>ourNodesDict[currNode][1]:
                    directions.append("R")
                else:
                    directions.append("L")
            else:
                #print(prevNode)
                #print(currNode)
                directions.append(findLeftRight(prevNode, currNode, nextNode))

    print(directions)  
#====================================MAIN CODE================================================
#====================================Orientation Detector================================================
def findOrientation(lastSlope,reqSlope):
    commands = []
    if(lastSlope == reqSlope):
        commands.append("PICK")
    elif(lastSlope == 0):
        if(reqSlope==-1):
            commands.append("r")
            commands.append("r")
            commands.append("PICK")
            commands.append("l")
            commands.append("l")
        elif(reqSlope==1):
            commands.append("l")
            commands.append("l")
            commands.append("PICK")
            commands.append("r")
            commands.append("r")
    elif(lastSlope == 1):
        if(reqSlope==0):
            commands.append("r")
            commands.append("r")
            commands.append("PICK")
            commands.append("l")
            commands.append("l")
        elif(reqSlope==-1):
            commands.append("l")
            commands.append("l")
            commands.append("PICK")
            commands.append("r")
            commands.append("r")
    elif(lastSlope == -1):
        if(reqSlope==1):
            commands.append("r")
            commands.append("r")
            commands.append("PICK")
            commands.append("l")
            commands.append("l")
        elif(reqSlope==0):
            commands.append("l")
            commands.append("l")
            commands.append("PICK")
            commands.append("r")
            commands.append("r")
    print(commands)
            
#====================================update Last Slope================================================
def updateLastSlope(path):
    global lastSlope
    n = len(path)-1
    lastSlope = (ourNodesDict[path[n]][0]-ourNodesDict[path[n-1]][0])/(ourNodesDict[path[n]][1]-ourNodesDict[path[n-1]][1])

#====================================MAIN CODE=================================
#1===========================
path = [25,19,20,14,15]
findPath(path)
updateLastSlope(path)
facePebble = 3
faceAxis = 1 # 1 ----> slope = 0
reqSlope = 0
findOrientation(lastSlope,reqSlope)

#2===========================
path = [15,14,20]
#Update prevNode before going to next:
findPath(path)
updateLastSlope(path)
facePebble = 5
faceAxis = 3 # 3 ----> slope = 1
reqSlope = 1
findOrientation(lastSlope,reqSlope)

#2===========================
path = [20,26,27]
findPath(path)
updateLastSlope(path)
reqSlope = -1
findOrientation(lastSlope,reqSlope)
