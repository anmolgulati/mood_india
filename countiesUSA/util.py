f = open('temp.txt','r')
countyFileLines = f.readlines()
countData = []
i = 0
while i < len(countyFileLines) - 1:
	countData.append((countyFileLines[i+1].replace('\n',''),countyFileLines[i].replace('\n','')))
	i+=2
# print len(countData)
for i in range(len(countData)):
	name = countData[i][0]
	nameList = name.splits(',')
	nameList1 = nameList[0].split(' ')
	actualName = ""
	for i in range(len(nameList1) -1):
		actualName = actualName + ' ' + nameList1[i]
	actualName.lstrip()
	

