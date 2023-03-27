from .. import Globals 
import time
import os
import numpy as np

def URL(sc):
	'''
	Returns a function which works out the URLs for a given date
	
	Inputs
	======
	sc : int
		1,2,3,4

	Returns
	=======
	urls
	'''
	
	def URLFunction(Date):
	

		prod = products[Prod.lower()]

		#get the year
		Year = Date//10000
		
		#get the URL for that year
		url0 = 'https://spdf.gsfc.nasa.gov/pub/data/cluster/c{:d}/jp/pse/{:04d}/'.format(sc,Year)
		
		return url0
	
	return URLFunction

