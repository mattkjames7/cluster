import numpy as np
from ..Tools.Downloading._RebuildDataIndex import _RebuildDataIndex
from . import _Pos

def RebuildDataIndex(sc):
	'''
	Rebuilds the data index for a data product.

	Inputs
	======
	sc : int
		1,2,3,4
	
	'''		
	idxfname = _Pos.idxfname.format(sc)
	datapath = _Pos.datapath.format(sc)

	vfmt = _Pos.vfmt

	
	_RebuildDataIndex(datapath,idxfname,vfmt)
