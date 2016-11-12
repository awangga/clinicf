import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL

def ktp(uridt='null'):
	thisURI=urlEncode16(tokenuri+'%'+uridt)
	setTTL(thisURI)
	dt = {
	'%UID%':uridt, 
	'%Nama%':'Rolly Maulana Awangga',
	'%URI%':thisURI
	}
	return dt
	