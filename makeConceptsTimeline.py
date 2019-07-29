import os,json
from collections import defaultdict

path = 'data/recognition/'

#for filename in os.listdir(path):

with open(path+'Babylonad.json') as json_file:
    json_data = json.load(json_file)



# Create a set with every concept name
allConcepts = set()
for frame in json_data:
    for concept in frame['data']['concepts']:
        if concept['name'] not in allConcepts:
            allConcepts.add(concept['name']) 
        #print('%s %f' % (concept['name'], concept['value']))
print(allConcepts)



# Create a dict of lists. For each concept we have a dict of the size duration of the video
## 0 where the concept is not present and 1 where is present
conceptDict=defaultdict(list,{k:[] for k in allConcepts})


for key in conceptDict.keys():
    for frame in json_data:
        found = False
        for concept in frame['data']['concepts']:
            if key == concept['name'] and concept['value'] > 0.8:
                conceptDict[key].append(1)
                found = True
                break
        if not found:
            conceptDict[key].append(0)

print(len(conceptDict['cold']))
print(conceptDict['cold'])