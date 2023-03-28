import numpy as np
from . import _Pos
import RecarrayTools as RT
from .. import Globals

def _ReadSCFile(sc):

	path = Globals.DataPath + 'Pos/'
	fname = path + '{:d}.bin'.format(sc)
	
	return RT.ReadRecarray(fname)


def GetPos(sc,Reload=False):
	'''
	Get the position file for one of the cluster spacecraft

	Inputs
	======
	sc : int
		1,2,3,4

	'''

	out = _Pos.pos[sc]

	if out is None or Reload:
		_Pos.pos[sc] = _ReadSCFile(sc)
		out = _Pos.pos[sc]

	return out

