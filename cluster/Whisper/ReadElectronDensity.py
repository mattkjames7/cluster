import numpy as np
from .ReadCDF import ReadCDF
import DateTimeTools as TT

def ReadElectronDensity(date,sc):
    


	data,_ = ReadCDF(date,sc,Prod='Density')

	epoch = data['time_tags__C1_CP_WHI_ELECTRON_DENSITY']
	dens = data['Electron_Density__C1_CP_WHI_ELECTRON_DENSITY']

	dtype = [	('Date','int32'),
	  			('ut','float32'),
				('utc','float64'),
				('Density','float32')]
	
	n = epoch.size

	out = np.recarray(n,dtype=dtype)
	out.Date,out.ut = TT.CDFEpochtoDate(epoch)
	out.utc = TT.ContUT(out.Date,out.ut)
	out.Density = dens

	return out