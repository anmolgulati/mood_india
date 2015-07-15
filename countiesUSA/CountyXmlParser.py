from xml.dom import minidom
from django.utils.encoding import smart_str, smart_unicode

global counter
def writeCountyDataToFile(fileAddress,data):
	global counter
	try:
		f = open(fileAddress,'w')
		f.write(data)
		f.close()
	except:
		print "file could not open"

def createFileOfCountyNames(filename,name):
	f = open(filename,'w + t')
	f.write(name + "\n")
	f.close()


def parseXML(filename):
	doc = minidom.parse(filename)

	placeMarks = doc.getElementsByTagName("Placemark")
	f = open('countyList',"w")

	for placeMark in placeMarks:
		_id = placeMark.getAttribute("id")
		_name = placeMark.getElementsByTagName("name")[0]
		_polygon = placeMark.getElementsByTagName("Polygon")[0]
		_outerBoundary = _polygon.getElementsByTagName("outerBoundaryIs")[0]
		_linearRing = _outerBoundary.getElementsByTagName("LinearRing")[0]
		_coordinates = _linearRing.getElementsByTagName("coordinates")[0]
		crdnts = _coordinates.firstChild.data.replace(',','\n')
		filename = unicode(str(_name.firstChild.data),errors ='replace')
		filename = unicode(str(filename),errors = 'ignore')
		fileAddress = "data/" + str(filename)
		data = crdnts
		# print filename + " " + _name.firstChild.data
		writeCountyDataToFile(fileAddress,data)
		f.write(str(filename) + '\n')

	f.close()
	print "counter = " + str(counter)

if __name__ == "__main__" :
	global counter
	counter = 0
	parseXML('cb_2014_us_county_500k.kml')
