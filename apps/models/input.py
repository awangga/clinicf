import sys
import pymongo
sys.path.append('../../')
from lib import config


conn = pymongo.MongoClient(config.mongohost, config.mongoport)
db = conn.klinik


def getProfile(UID):
	db.profile
	return db.sign.find_one({"UID":UID})

def isProfileExist(UID):
	if getProfile(UID)== None:
		return False
	else:
		return True
	
def getAllRec(NIK):
	db.rec
	return db.sign.find({"UID":NPM},{ "waktu": 1, "Nilai": 1, "Topik": 1,"_id": 0 })

def getLastRec(NIK):
	db.rec
	return db.sign.find_one({"NPM":NPM})

def getToday(NIK):
	db.rec
	return db.sign.find({"NPM":NPM,"waktu":time.strftime("%d/%m/%Y")})

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
		insertSign(NPM,Nilai,Pembimbing,Topik)
		return "done"

def insertRec(NPM,Nilai,Pembimbing,Topik):
	db.sign
	doc = {"NPM":NPM,"Nilai":int(Nilai),"waktu":time.strftime("%d/%m/%Y"),"Pembimbing":Pembimbing,"Topik":Topik}
	idProcess = db.sign.insert_one(doc).inserted_id
	return str(doc)