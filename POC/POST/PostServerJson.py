#!/usr/bin/env python

import web
import json

print "matserver invoked"

urls = ('/post', 'post')
app = web.application(urls, globals())

class post:
    def POST(self):
		ji = web.data()
		pj = json.loads(ji)
		web.debug(pj.items())
		web.debug("is dict: " + str(isinstance(pj, dict)))
		web.debug(pj.keys())
		web.debug("is list: " + str(isinstance(pj['tables'], list)))
		web.debug(len(pj['tables']))
		for table in pj['tables']:
			web.debug("is dict: " + str(isinstance(table, dict)))
			web.debug("table: " + str(table))

if __name__ == "__main__":
    app.run()

class Database(object):
	def __init__(self, j):
		self.__dict__=json.loads(j)