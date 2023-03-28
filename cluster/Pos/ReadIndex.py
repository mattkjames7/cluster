import numpy as np
from ..Tools.Downloading._ReadDataIndex import _ReadDataIndex
from . import _Pos

def ReadIndex(sc=1):
	'''
	Reads the index file for a given data product.
	
	Inputs
	======
	sc : str
		'a'|'b'|'c'|'d'|'e'

	
	Returns
	=======
	numpy.recarray
	
	'''
	return _ReadDataIndex(_Pos.idxfname.format(sc))
