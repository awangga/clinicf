import sys
import pymongo
import time
sys.path.append('../../')
from lib import config


conn = pymongo.MongoClient(config.mongohost, config.mongoport)
db = conn.klinik


def getProfile(UID):
	db.profile
	return db.profile.find_one({"uid":UID})

def isProfileExist(UID):
	if getProfile(UID)== None:
		return False
	else:
		return True
	
def getAllRec(NIK):
	db.rec
	return db.profile.find({"UID":NPM},{ "waktu": 1, "Nilai": 1, "Topik": 1,"_id": 0 })

def getLastRec(NIK):
	db.rec
	return db.rec.find_one({"NPM":NPM})

def getToday(NIK):
	db.rec
	return db.rec.find({"NPM":NPM,"waktu":time.strftime("%d/%m/%Y")})

def isIndexExist(cursor):
	try:
		cursor[0]
		return True
	except IndexError:
   			return False  

def insertTodayOnly(NPM,Nilai,Pembimbing,Topik):
	cur = getToday(NPM)
	if isIndexExist(cur):
		return "exist"
	else:
		insertRec(NPM,Nilai,Pembimbing,Topik)
		return "done"

def insertRec(NPM,Nilai,Pembimbing,Topik):
	db.rec
	doc = {"NPM":NPM,"Nilai":int(Nilai),"waktu":time.strftime("%d/%m/%Y"),"Pembimbing":Pembimbing,"Topik":Topik}
	idProcess = db.rec.insert_one(doc).inserted_id
	return str(doc)

def insertProfile(uid,nama,tanggal_lahir,alamat,pekerjaan,telepon,gender,agama):
	db.profile
	doc = {"uid":uid,"nama":nama,"waktu_pendaftaran":time.strftime("%d/%m/%Y"),"tanggal_lahir":tanggal_lahir,"alamat":alamat,"pekerjaan":pekerjaan,"telepon":telepon,"gender":gender,"agama":agama}
	idProcess = db.profile.insert_one(doc).inserted_id
	return str(doc)
	