import numpy as np
from .GetPos import GetPos
from scipy.interpolate import interp1d,InterpolatedUnivariateSpline
from . import _Pos
import DateTimeTools as TT

def GetPosInterpolator(sc,Reload=False):
    
	if _Pos.obj[sc] is None or Reload:

		#get the pos data
		pos = GetPos(sc)

		#create interpolator objects for each coordinate
		fields = ['xgse','ygse','zgse','xgsm','ygsm','zgsm']
		objs = {}
		for f in fields:
			use = np.where(np.isfinite(pos[f]))
			objs[f] = interp1d(pos.utc[use],pos[f][use],kind='linear',bounds_error=False,fill_value=np.nan)
			#objs[f] = InterpolatedUnivariateSpline(pos.utc[use],pos[f][use])

		_Pos.obj[sc] = objs

	def PosInterpolator(*args):

		if len(args) == 2:
			#date and time
			Date,ut = args
			if np.size(Date) == 1 and np.size(ut) > 1:
				Date = np.zeros(np.size(ut),dtype='int32') + Date
			utc = TT.ContUT(Date,ut)
		else:
			utc = args
			Date,ut = TT.ContUTtoDate(utc)
		
		#create the output object
		n = utc.size
		out = np.recarray(n,dtype=_Pos.dtype)

		#fill Date time etc
		out.Date = Date
		out.ut = ut
		out.utc = utc

		#interpolate the other fields
		fields = ['xgse','ygse','zgse','xgsm','ygsm','zgsm']
		for f in fields:
			out[f] = _Pos.obj[sc][f](out.utc)

		return out

	return PosInterpolator
