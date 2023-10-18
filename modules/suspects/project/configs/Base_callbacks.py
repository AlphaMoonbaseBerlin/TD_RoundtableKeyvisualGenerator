'''Info Header Start
Name : Base_callbacks
Author : Wieland@AMB-ZEPH15
Saveorigin : Project.toe
Saveversion : 2022.32660
Info Header End'''

def GetConfigSchema(CollectionValue, CollectionDict, CollectionList):

	Resolution = CollectionDict({
		"x" : CollectionValue(default = 1920, typecheck = (float, int), validator = lambda value : value > 0),
		"y" : CollectionValue(default = 1080, typecheck = (float, int), validator = lambda value : value > 0),})

	return {
    	"OutputResolution" : Resolution()
		}
		
		
#def GetConfigData():
#	return a jsonString. Can be used to fetch API data or similiar.
#	return ""