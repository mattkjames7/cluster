from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _Pos
from .URL import URL

def DownloadData(sc=1,Date=[20010203,20221231],Overwrite=False,Verbose=True):
	'''
	Downloads EFI data.

	Inputs
	======
	sc : int
		1,2,3,4

	'''
	URLF = URL(sc)

	_DownloadData(URLF,_Pos.idxfname.format(sc),_Pos.datapath.format(sc),
			Date,_Pos.vfmt,None,Overwrite,Verbose)
	
	
