import os

#try and find the CLUSTER_PATH variable - this is where data will be stored
ModulePath = os.path.dirname(__file__)+'/'
try:
	DataPath = os.getenv('CLUSTER_PATH')+'/'
except:
	print('Please set CLUSTER_PATH environment variable')
	DataPath = ''

#cluster position
Pos1 = None
Pos2 = None
Pos3 = None
Pos4 = None

Vel = {}


#functions which will interpolate the positions/traces of each spacecraft
TraceFuncs = {}
