#assignment03-cso.py

# import required libraries
from ast import Pass
import requests
import json

# when inspect the URL each dataset is listed in dataset url i.e.
# https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/FP001/JSON-stat/2.0/en"
# Therefore if split the url into urlBegining + dataset + urlEnd can then
# allow the url in request be modified for each requested dataset
# i.e. dataset here 'FP001' becomes a var 'dataset' that can be called for in the script when executed
# e.g. getFormattedAsFile("FP001") where 'FP001' becomes 'dataset' when main script is run

urlBegining = "https://ws.cso.ie/public/api.restful/PxStat.Data.Cube_API.ReadDataset/"
urlEnd = "/JSON-stat/2.0/en"

# returns unformatted raw json file from cao of 'dataset'
def getAll(dataset):   
    url = urlBegining + dataset + urlEnd
    response = requests.get(url)
    return response.json()
    
# create file and upload raw version of dataset
def getAllAsFile(dataset):
    with open("cso.json", "wt") as fp:
        print(json.dumps(getAll(dataset)), file=fp)


if __name__ == "__main__":
    getAllAsFile("FIQ02")
    #getFormattedAsFile("FP001")