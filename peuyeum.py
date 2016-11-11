#!/usr/bin/env python

from cgi import parse_qs
from lib import signapp

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	uri = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	post = parse_qs(request_body)
	## Declare apps
	sign = signapp.Signapp()
	## Menu Logic
	url=sign.urlDecode16(uri[1:])
	if sign.getMenu(url[:3])=="key":
		data = url[3:]

		hbegin = sign.getHtmlBegin()
		result = sign.getHtml(data)
		hend = sign.getHtmlEnd()

		respon = hbegin + result + hend
	elif sign.getMenu(url[:3])=="token":
		token = post.get('token', [''])[0]
		npm = post.get('NPM', [''])[0]
		numb = post.get('Nilai', [''])[0]
		pemb = post.get('Topik', [''])[0]
		html = sign.getTokenData(token)
		email = sign.getJsonData('email',html)
		if sign.emailAcl(email):
			if sign.getTTL(uri[1:]):
				respon = sign.insertTodayOnly(npm,numb,email,pemb)
			else:
				respon = "expire"
		else:
			respon = "invalid"
	else:
		respon = """
		<html>
		<head><title>403 Porbidden</title></head>
		<body bgcolor="white">
		<center><h1>403 Porbidden</h1></center>
		<hr><center>peuyeum/bdg</center>
		</body>
		</html>
		"""
	## Passing HTML to client
	start_response('200 OK', [('Content-Type', 'text/html'),('Content-Length', str(len(respon)))])
	return [respon]

