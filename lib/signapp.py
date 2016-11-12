#!/usr/bin/env python
"""
signapp.py 
created by Rolly Maulana Awangga

"""
import config
import pymongo
import urllib
import random
import time
import redis
from Crypto.Cipher import AES

class Signapp(object):
	def __init__(self):
		self.key = config.key
		self.iv = config.iv
		self.redis = redis.Redis()
		self.opendb()
		self.viewspath="./apps/views/"

	def opendb(self): 
		self.conn = pymongo.MongoClient(config.mongohost, config.mongoport)
		self.db = self.conn.klinik
	
	def tokenUri(self):
		return config.tokenuri

	def random(self,ln):
                ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
                chars=[]
                for i in range(ln):
                        chars.append(random.choice(ALPHABET))
                return "".join(chars)

	def urlEncode16(self,uri):
		ln = len(uri)
		multihex = (ln/16)*16+16
		sp = multihex - ln - len(str(ln))
		if ln>9:
			dt = str(ln)+uri+self.random(sp)
		else:
			dt = "0"+str(ln)+uri+self.random(sp-1)
		return self.encodeData16(dt)

	def urlDecode16(self,uri):
		if len(uri)%16 == 0:
			dt = self.decodeData16(uri)
			try:
				int(dt[:2])
				ln = int(dt[:2])
				ret = dt[2:2+ln]
			except ValueError:
				ret = dt
		else:
			ret = uri
		return ret		

	def setTTL(self,token):
		return self.redis.setex(token,"valid",config.urltimeout)
	
	def getTTL(self,token):
		return self.redis.get(token)

	def getAllSign(self,NPM):
		self.db.sign
		return self.db.sign.find({"NPM":NPM},{ "waktu": 1, "Nilai": 1, "Topik": 1,"_id": 0 })
	
	def getLastSign(self,NPM):
		self.db.sign
		return self.db.sign.find_one({"NPM":NPM})

	def getToday(self,NPM):
		self.db.sign
		return self.db.sign.find({"NPM":NPM,"waktu":time.strftime("%d/%m/%Y")})
	
	def isIndexExist(self,cursor):
		try:
			cursor[0]
			return True
		except IndexError:
    			return False  

	def insertTodayOnly(self,NPM,Nilai,Pembimbing,Topik):
		cur = self.getToday(NPM)
		if self.isIndexExist(cur):
			return "exist"
		else:
			self.insertSign(NPM,Nilai,Pembimbing,Topik)
			return "done"

	def insertSign(self,NPM,Nilai,Pembimbing,Topik):
		self.db.cat
		doc = {"NPM":NPM,"Nilai":int(Nilai),"waktu":time.strftime("%d/%m/%Y"),"Pembimbing":Pembimbing,"Topik":Topik}
		idProcess = self.db.cat.insert_one(doc).inserted_id
		return str(doc)

	def encodeData(self,msg):
		obj=AES.new(self.key,AES.MODE_CFB,self.iv)
		cp = obj.encrypt(msg)
		return cp.encode("hex")

	def decodeData(self,msg):
		obj=AES.new(self.key,AES.MODE_CFB,self.iv)
		dec = msg.decode("hex")
		return obj.decrypt(dec)

	def encodeData16(self,msg):
		obj=AES.new(self.key,AES.MODE_CBC,self.iv)
		cp = obj.encrypt(msg)
		return cp.encode("hex")

	def decodeData16(self,msg):
		obj=AES.new(self.key,AES.MODE_CBC,self.iv)
		dec = msg.decode("hex")
		return obj.decrypt(dec)

	def getHtmlBegin(self):
		with open(self.viewspath+'begin.batik', 'r') as myfile:
		    data=myfile.read().replace('\n', '')
		return data

	def getHtmlEnd(self):
		with open(self.viewspath+'end.batik', 'r') as myfile:
		    data=myfile.read().replace('\n', '')
		return data

	def getHtml(self,route):
		with open(self.viewspath+route+'/index.batik', 'r') as myfile:
		    data=myfile.read().replace('\n', '')
		return data
		
	def getHtmlForm(self):
		return config.html_form

	def getMenu(self,uri):
		if uri == config.keyuri:
			opsi = "key"
		elif uri == config.tokenuri:
			opsi = "token"
		else:
			opsi = "other"
		return opsi
	
	def getTokenData(self,token):
		url = config.tokenurl+token
		response = urllib.urlopen(url)
		html = response.read()
		return html

	def emailAcl(self,email):
		if email.split('@')[1] == config.domainacl:
			return True
		else:
			return False

	def tokenValidation(self,token):
		html = self.getTokenData(token)
		if (html.find(config.aud)>0) and (html.find(config.iss)>0):
			ret = "valid"
		else:
			ret = "invalid"
		return ret

	def getJsonData(self,name,json):
		lookup = '"%s": "'%name
		b = json.find(lookup)
		c = json[b:].find(':')
		c+=1
		b = b+c
		c = json[b:].find(',')
		c = b+c
		data = json[b:c].strip().strip('"')
		return data

