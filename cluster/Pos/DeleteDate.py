import numpy as np
from ..Tools.Downloading._DeleteDate import _DeleteDate
from . import _Pos

def DeleteDate(Date,sc,Confirm=True):
	'''
	delete all of the files from a given date
	
	'''
	idxfname = _Pos.idxfname.format(sc)
	datapath = _Pos.datapath.format(sc)

	_DeleteDate(Date,idxfname,datapath,Confirm)
