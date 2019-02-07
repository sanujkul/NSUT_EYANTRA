################################__Make Route Efficient Code begins____####################
"""
Function : replace 
Parameters: string1 to edit, string2 to find, string3 to replace
return:    Make the input route more efficient
Logic : replaces all occurances of string2 in string1 with string3
""" 
def replace(tRoute, searchString,toReplaceString):
    splitStrings = tRoute.split(searchString)
    length = len(splitStrings)
    processedString = ""
    for i in range(0,length):
        processedString = processedString + splitStrings[i]
        if i != length-1:
            processedString = processedString + toReplaceString
    return processedString

"""
Function : processChar
Parameters: route that has to be send to XBEE, character to be replaced
return:    Make the input route more efficient
Logic : 5 consecutive 'r'  replace with 1 'l'
        5 consecutive 'l'  replace with 1 'r'
        4 consecutive 'r'  replace with 2 'l'
        4 consecutive 'l'  replace with 2 'r'
""" 
def processChar(tRoute,char,howMany):
    toReplace = '0'
    toAdd = 6 - howMany
    if char=='r':
        toReplace = 'l'
    elif char=='l':
        toReplace = 'r'

    toReplaceString = ''
    for i in range(0,toAdd):
        toReplaceString = toReplaceString + toReplace
        
    searchString = ''
    for i in range(0,howMany):
        searchString = searchString + char

    return  replace(tRoute, searchString,toReplaceString)   

"""
Function : makeRouuteEfficient
Parameters: route that has to be send to XBEE
return:    MAke the input route more efficient
Logic : 5 consecutive 'r'  replace with 1 'l'
        5 consecutive 'l'  replace with 1 'r'
        4 consecutive 'r'  replace with 2 'l'
        4 consecutive 'l'  replace with 2 'r'
        all 'rl'  and 'lr' to be ommitted
"""        
def makeRouuteEfficient(tRoute):
    print(tRoute)
    tRoute = processChar(tRoute,'r',5)
    print(tRoute)
    tRoute = processChar(tRoute,'l',5)
    print(tRoute)
    tRoute = processChar(tRoute,'r',4)
    print(tRoute)
    tRoute = processChar(tRoute,'l',4)
    print(tRoute)
    while tRoute.find('rl') != -1:
        tRoute = replace(tRoute, 'rl','')
    print(tRoute)
    while tRoute.find('lr') != -1:
        tRoute = replace(tRoute, 'lr','')
    print(tRoute)

    return tRoute

################################__Make Route Efficient Code ends____####################
TravelRoute = 'lfrfllsrrrrrfrfrsrrrrllfsrrlllfsllll'

print(makeRouuteEfficient(TravelRoute))

#def makeRouteEfficient(tRoute):
    
