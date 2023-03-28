import numpy as np
from .ReadIndex import ReadIndex

def DataAvailability(sc=1):
	'''
	Provide a list of dates for which there are data.

	Inputs
	======
	sc : int
		1,2,3,4

	
	'''
	idx = ReadIndex(sc)
	return np.unique(idx.Date)
