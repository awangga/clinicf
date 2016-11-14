#!/usr/bin/env python

from cgi import parse_qs
from lib import signapp
import re

def application(environ, start_response):
	## passing environ uwsgi PARAM
	try:
		request_body_size = int(environ.get('CONTENT_LENGTH', 0))
	except (ValueError):
		request_body_size = 0
	origin = environ['REQUEST_URI']
	request_body = environ['wsgi.input'].read(request_body_size)
	post = parse_qs(request_body)
	## Declare apps
	sign = signapp.Signapp()
	## Menu Logic
	url=sign.urlDecode16(origin[1:])
	uri=url.split('%')
	if sign.getMenu(uri[0])=="key":
		mod = 'apps.controllers.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=[func])
		m = getattr(a,func)
		rep = m(uri[3])
		text = sign.getHtml(uri[1])
		
		rep = dict((re.escape(k), v) for k, v in rep.iteritems())
		pattern = re.compile("|".join(rep.keys()))
		result = pattern.sub(lambda m: rep[re.escape(m.group(0))], text)
		
		hbegin = sign.getHtmlBegin()
		hend = sign.getHtmlEnd()

		respon = hbegin + result + hend
	elif sign.getMenu(uri[0])=="token":
		mod = 'apps.controllers.'+uri[1]
		func = uri[2]
		a = __import__(mod,fromlist=[func])
		m = getattr(a,func)
		respon = m(uri[3],post)
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

