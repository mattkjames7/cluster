import numpy as np
from .ReadIndex import ReadIndex
from ..Tools.ReadCDF import ReadCDF as RCDF
from . import _Pos
import os


def ReadCDF(Date,sc=1):
	'''
	Inputs
	======
	sc : int
		1,2,3,4


	
	'''
	#we should only accept dates at the start of a month
	if Date % 100 > 1:
		Date = (Date//100) * 100 + 1

	#read the data index
	idx = ReadIndex(sc)
	
	#check the index for the appropriate date
	use = np.where(idx.Date == Date)[0]
	if use.size == 0:
		print('Date not found, run cluster.Pos.DownloadData() to check for updates.')
		return None,None
	idx = idx[use]
	mx = np.where(idx.Version  == np.max(idx.Version))[0]
	mx = mx[0]
	
	#get the file name
	fname = _Pos.datapath.format(sc) + idx[mx].FileName


	#check file exists
	if not os.path.isfile(fname):
		print('Index is broken: Update the data index')
		return None,None
		
	#read the file
	return RCDF(fname)
