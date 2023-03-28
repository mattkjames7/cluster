import numpy as np
from .ReadIndex import ReadIndex
from .ReadCDF import ReadCDF
import RecarrayTools as RT
import DateTimeTools as TT
from .. import Globals
import os
import PyGeopack as gp

def _ConvertCDF(date,sc):
	
	#define some strings
	st = 'Epoch__C{:1d}_JP_PSE'.format(sc)
	sp = 'sc_r{:1d}_xyz_gse__C{:1d}_JP_PSE'.format(sc,sc)

	#read cdf
	data,meta = ReadCDF(date,sc)
	#print(list(meta.keys()))
	
	n = data[st].size


	#create output array
	dtype = [	('Date','int32'),
	  			('ut','float32'),
				('utc','float64'),
				('xgse','float64'),
				('ygse','float64'),
				('zgse','float64'),
				('xgsm','float64'),
				('ygsm','float64'),
				('zgsm','float64'),]
	out = np.recarray(n,dtype=dtype)


	#convert time
	out.Date,out.ut = TT.CDFEpochtoDate(data[st])
	out.utc = TT.ContUT(out.Date,out.ut)

	#fill in gse
	out.xgse = data[sp][:,0]/6381.0
	out.ygse = data[sp][:,1]/6381.0
	out.zgse = data[sp][:,2]/6381.0

	#remove anything outside of 20 Re
	goodx = (out.xgse >= -20.0) & (out.xgse <= 20.0)
	goody = (out.ygse >= -20.0) & (out.ygse <= 20.0)
	goodz = (out.zgse >= -20.0) & (out.zgse <= 20.0)
	good = np.where(goodx & goody & goodz)
	out = out[good]

	#calcualte gsm
	out.xgsm,out.ygsm,out.zgsm = gp.Coords.GSEtoGSM(out.xgse,out.ygse,out.zgse,out.Date,out.ut,V=[-429.877,29.78,0.0])

	return out



def Combine(sc):
	'''
	Combine all of the position files for one spacecraft.
	
	Inputs
	======
	sc : int
		1,2,3,4
	'''
	
	#read the data index
	idx = ReadIndex(sc)
	n = idx.size
	srt = np.argsort(idx.Date)
	idx = idx[srt]

	#read it all in together
	data = []
	s = 0
	for i in range(0,n):
		print('\rReading file {:d} of {:d}'.format(i+1,n),end='')
		tmp = _ConvertCDF(idx.Date[i],sc)
		data.append(tmp)
		s += tmp.size

	print()
	
	#create the output array
	out = np.recarray(s,dtype=data[0].dtype)

	#fill it
	p = 0
	for i in range(0,n):
		print('\rCombining {:d} of {:d}'.format(i+1,n),end='')
		out[p:p+data[i].size] = data[i]
		p += data[i].size
	print()

	#make sure we only keep unique times
	_,ui = np.unique(out.utc,return_index=True)
	out = out[ui]



	path = Globals.DataPath + 'Pos/'
	if not os.path.isdir(path):
		os.makedirs(path)
	fname = path + '{:d}.bin'.format(sc)
	RT.SaveRecarray(out,fname,StoreDtype=True)