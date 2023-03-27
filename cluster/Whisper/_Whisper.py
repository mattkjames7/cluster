import numpy as np
from .. import Globals

#this just stores a few variables for this particular instrument

#data path and index file name: format(Prod,L,sc)
idxfname = Globals.DataPath + 'Whisper/{:d}.{:s}.dat'
datapath = Globals.DataPath + 'Whisper/{:d}/{:s}/'

#file version format
vfmt = 'v\d\d\d\d\d\d\d\d'

#dataproducts
products = {'eint':'efield_integratedpowerdensity_naturalmode',
			'epass':'efield_passivespectralpowerdensity_soundingmode',
			'enat':'efield_spectralpowerdensity_naturalmode',
			'esnd':'efield_spectralpowerdensity_soundingmode',
			'density':'electron_density'}