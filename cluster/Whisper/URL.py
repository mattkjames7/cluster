from .. import Globals 
import time
import os
import numpy as np
from ._Whisper import products

def URL(sc,Prod):
	'''
	Returns a function which works out the URLs for a given date
	
	Inputs
	======
	sc : int
		1,2,3,4
	Prod: str
		Product string (see below)

	Available data products
	=======================


	Prod	Description
	========================================================================
	Eint	Integrated power density (natural mode)
	Epass	Passive spectral power density (sounding mode)
	Enat	Spectral power density (natural mode)
	Esnd	Spectral power density (sounding mode)
	Density Electron density

	Returns
	=======
	urls
	'''
	
	def URLFunction(Date):
	

		prod = products[Prod.lower()]

		#get the year
		Year = Date//10000
		
		#get the URL for that year
		url0 = 'https://cdaweb.gsfc.nasa.gov/pub/data/cluster/c{:d}/whi/{:s}/{:04d}/'.format(sc,prod,Year)
		
		return url0
	
	return URLFunction

