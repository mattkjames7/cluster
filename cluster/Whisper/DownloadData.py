from .. import Globals
import numpy as np
from ..Tools.Downloading._DownloadData import _DownloadData
from . import _Whisper
from .URL import URL

def DownloadData(sc=1,Prod='Density',Date=[20010203,20221231],Overwrite=False,Verbose=True):
	'''
	Downloads EFI data.

	Inputs
	======
	sc : str
		'a'|'b'|'c'|'d'|'e'
	Prod: str
		Product string (see below)
	L : str or int
		Level of data to download (0,1,2)

	Available data products
	=======================

	Prod L	Description
	========================================================================
	EFI  2	Electric Field Instrument Level 2 CDF

	VAF  1	EFI Sensor Voltages A Fast Survey Level 1 CDF
	VAP  1	EFI Sensor Voltages A Particle Burst Level 1 CDF
	VAW  1	EFI Sensor Voltages A Wave Burst Level 1 CDF
	VBF  1	EFI Sensor Voltages B Fast Survey Level 1 CDF
	VBP  1	EFI Sensor Voltages B Particle Burst Level 1 CDF
	VBW  1	EFI Sensor Voltages B Wave Burst Level 1 CDF
	EFF  1	EFI Fast Survey Level 1 CDF
	EFP  1	EFI Particle Burst Level 1 CDF
	EFW  1	EFI Wave Burst Level 1 CDF

	VAF  0	EFI Sensor Voltages A Fast Survey Level 0 Packets
	VAP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
	VAW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
	VBF  0	EFI Sensor Voltages B Fast Survey Level 0 Packets
	VBP  0	EFI Sensor Voltages A Particle Burst Level 0 Packets
	VBW  0	EFI Sensor Voltages A Wave Burst Level 0 Packets
	EFF  0	EFI E-field Fast Survey Level 0 Packets
	EFP  0	EFI E-field Particle Burst Level 0 Packets
	EFW  0	EFI E-field Wave Burst Level 0 Packets

	(Level 0 data might not work)

	'''
	URLF = URL(sc,Prod)
	prod = _Whisper.products[Prod.lower()]
	_DownloadData(URLF,_Whisper.idxfname.format(sc,prod),_Whisper.datapath.format(sc,prod),
			Date,_Whisper.vfmt,None,Overwrite,Verbose)
	
	
