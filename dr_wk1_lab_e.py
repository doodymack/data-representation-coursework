#dr_wk1_lab.py

import requests
import csv
#To parse, in computer science, is where a string of commands – usually a program – is separated into more easily processed components,
# which are analyzed for correct syntax and then attached to tags that define each component
# parseString : Parsing String is the process of getting information that is needed in the String format

from xml.dom.minidom import parseString

# array of train positions are available in xml by Irish Rail here
url = "http://api.irishrail.ie/realtime/realtime.asmx/getCurrentTrainsXML"

# create a var called 'page' to store the data retrieved from get command and url 
page = requests.get(url)

# clean up the data as per parse definition above
doc = parseString(page.content)

# check it works
#print (doc.toprettyxml()) #output to console- comment this out once you know code works

# if I want to store the xml in a file. You can comment this out later
# with open ("trainxml.xml","w") as xmlfp:
    # doc.writexml(xmlfp)

# define a variable 'objTrainPositionsNodes' that saves the elemets in downloaded info from site 'doc' called "objTrainPositions"

#objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
#for objTrainPositionsNode in objTrainPositionsNodes:

# for each "objTrainPositions" now saved in var objTrainPositionsNodes, extract the 'traincode'. 
# 'item(0)': Return 1st item per element in case more than 1

    #traincodenode = objTrainPositionsNode.getElementsByTagName("TrainCode").item(0)
# extract the name of the node i.e. text as 'traincode'
    
    #traincode = traincodenode.firstChild.nodeValue.strip()
    #print (traincode)

# the code prints out each train code from the api


with  open('week03_train.csv', mode='w', newline='') as train_file:
    train_writer = csv.writer(train_file, delimiter='\t', quotechar='"', quoting=csv.QUOTE_MINIMAL)


    objTrainPositionsNodes = doc.getElementsByTagName("objTrainPositions")
    for objTrainPositionsNode in objTrainPositionsNodes:
    # for each "objTrainPositions" now saved in var objTrainPositionsNodes, extract the 'TrainLatitude'. 
    # 'item(0)': Return 1st item per element in case more than 1
        trainlatitudenode = objTrainPositionsNode.getElementsByTagName("TrainLatitude").item(0)
    # extract the name of the node i.e. text as 'traincode'
        trainLatitude = trainlatitudenode.firstChild.nodeValue.strip()
        dataList = []
        dataList.append(trainLatitude)
        train_writer.writerow(dataList)

        
print (trainLatitude)


    # other elements from API <objTrainPositions> that are retrievable:
    # <TrainStatus> <TrainLatitude> <TrainLongitude> <TrainCode> <TrainDate> <PublicMessage> <Direction>


    