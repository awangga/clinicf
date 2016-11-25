import sys
sys.path.append('../../')
from lib.cilok import urlEncode16,tokenuri,setTTL
from apps.models import profile
profile = profile.Model()

class Controller(object):
	def ktp(self,uridt='null'):
		if profile.isExist(uridt):
			dt = {
			'%regform%':'none',
			'%recform%':'block',
			'%Name%':'anu'
			}
		else:
			dt = {
			'%regform%':'block',
			'%recform%':'none'
			}
		thisURI=urlEncode16(tokenuri+'%'+'input%postReg'+'%'+uridt)
		setTTL(thisURI)
		dt['%URI%']=thisURI
		dt['%UID%']=uridt
		return dt
	
	def postReg(self,getdt,postdt):
		nama = postdt.get('nama', [''])[0]
		tanggal_lahir = postdt.get('tanggal_lahir', [''])[0]
		alamat = postdt.get('alamat', [''])[0]
		pekerjaan = postdt.get('pekerjaan', [''])[0]
		telepon = postdt.get('telepon', [''])[0]
		gender = postdt.get('gender', [''])[0]
		agama = postdt.get('agama', [''])[0]
		uid = getdt
		profile.create(uid,nama,tanggal_lahir,alamat,pekerjaan,telepon,gender,agama)
		return nama
		