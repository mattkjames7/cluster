import numpy as np
from ..Tools.Downloading._DeleteDate import _DeleteDate
from . import _Whisper

def DeleteDate(Date,sc,Prod,Confirm=True):
	'''
	delete all of the files from a given date
	
	'''
	prod = _Whisper.products[Prod.lower()]
	idxfname = _Whisper.idxfname.format(sc,prod)
	datapath = _Whisper.datapath.format(sc,prod)

	_DeleteDate(Date,idxfname,datapath,Confirm)
