import json
import pprint

### parser to parse the format we need the json in
def parser():
	with open('sampleJson.json') as f:
		data = json.load(f)
	counties = []
	for elements in data["var"]:
		counties.append((elements["code"],elements["name"]))
	return counties


### returns counties dict
def fomatter(counties):

	f = open('countyList','r')
	lines = f.readlines()
	f.close()
	f = open('temp.txt','r')
	countyFileLines = f.readlines()

	countData = []
	i = 0
	while i < len(countyFileLines) - 1:
		countData.append((countyFileLines[i].replace('\n',''),countyFileLines[i+1].replace('\n','')))
		i+=2
	countyDict = {}
	for i in range(len(lines)):
		for j in range(len(countData)):
			if lines[i].rstrip() in countData[j][1]:
				countyDict[lines[i].rstrip()] = countData[j]
				break
	
	for key,val in countyDict.items():
		print(key,val)

	# return countyDict

if __name__ == "__main__":
	countyDict = fomatter(parser())
