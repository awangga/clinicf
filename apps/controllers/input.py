import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL
from apps.models.input import *

def ktp(uridt='null'):
	if isProfileExist(uridt):
		dt = {
		'%regform%':'none',
		'%recform%':'block'
		}
	else:
		dt = {
		'%regform%':'none',
		'%recform%':'block'
		}
	thisURI=urlEncode16(tokenuri+'%'+'input%postReg'+'%'+uridt)
	setTTL(thisURI)
	dt['%URI%']=thisURI
	dt['%UID%']=uridt
	return dt
	
def postReg(getdt,postdt):
	nama = postdt.get('nama', [''])[0]
	tanggal_lahir = postdt.get('tanggal_lahir', [''])[0]
	alamat = postdt.get('alamat', [''])[0]
	pekerjaan = postdt.get('pekerjaan', [''])[0]
	telepon = postdt.get('telepon', [''])[0]
	gender = postdt.get('gender', [''])[0]
	agama = postdt.get('agama', [''])[0]
	uid = getdt
	insertProfile(uid,nama,tanggal_lahir,alamat,pekerjaan,telepon,gender,agama)
	return nama