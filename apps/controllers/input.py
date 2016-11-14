import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL
from apps.models.input import *

def ktp(uridt='null'):
	if isProfileExist(uridt):
		dt = {
		'%regform%':'hidden',
		'%recform%':'visible'
		}
	else:
		dt = {
		'%regform%':'visible',
		'%recform%':'hidden'
		}
	if uridt=='04123C72862B80':
		dt['%Name%']='Mila Anisa'
	elif uridt=='041C2E0A422A80':
		dt['%Name%']='Rolly Maulana Awangga'
	else:
		dt['%Name%']='Ieu lain KTP lur!'
	thisURI=urlEncode16(tokenuri+'%'+uridt)
	setTTL(thisURI)
	dt['%URI%']=thisURI
	dt['%UID%']=uridt
	return dt
	