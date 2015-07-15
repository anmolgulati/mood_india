
def getCoordinateListForCounty(countyName):
	print countyName
	f = open(countyName,"r")
	coordinates = []
	lines = f.readlines()
	for i in range(len(lines) - 1):
		lines[i] = lines[i].replace(" ","")
		lines[i + 1] = lines[i+1].replace(" ","")
		cX = float(eval(lines[i]))
		cY = float(eval(lines[i+1]))
		coordinates.append((cX,cY))
	return coordinates

def checkPointInsidePolygon(x,y,polygon):
    n = len(polygon)
    inside =False

    p1x,p1y = polygon[0]
    for i in range(n+1):
        p2x,p2y = polygon[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside

def findCountyforCoordinates(x,y,countListFile):
	f = open(countListFile,'r')
	lines = f.readlines()
	for i in range(len(lines)):
		countyName = lines[i].rstrip()	
		filePath = "data/" + countyName
		if checkPointInsidePolygon(x,y,getCoordinateListForCounty(filePath)):
			return countyName

diction = {}
def temp():
	f = open('countyList','r')
	lines = f.readlines()
	lines1 = list(set(lines))
	print str(len(lines)) + " " + str(len(lines1))
	# for i in range(len(lines)):
	# 	countyName = lines[i].rstrip()
	# 	fileAddress = "data/" + countyName
	# 	crnts = getCoordinateListForCounty(fileAddress)
	# 	diction[countyName] = crnts

if __name__ == "__main__":
	temp()
	# print findCountyforCoordinates(18,66,'countyList')
	
