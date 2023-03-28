import numpy as np
from .. import Globals

#this just stores a few variables for this particular instrument

#data path and index file name: format(Prod,L,sc)
idxfname = Globals.DataPath + 'Pos/pos-{:1d}.dat'
datapath = Globals.DataPath + 'Pos/{:1d}/'

#file version format
vfmt = 'v\d\d'

dtype = [	('Date','int32'),
  			('ut','float32'),
			('utc','float64'),
			('xgse','float64'),
			('ygse','float64'),
			('zgse','float64'),
			('xgsm','float64'),
			('ygsm','float64'),
			('zgsm','float64'),]

pos = {1:None,2:None,3:None,4:None}
obj = {1:None,2:None,3:None,4:None}