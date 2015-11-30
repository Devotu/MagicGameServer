#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import sqlite3
import logging
import os

print "PostService invoked"

urls = ('/postdatabase', 'postdatabase')
app = web.application(urls, globals())

class postdatabase:
	def POST(self):
		logging.basicConfig(filename='postlog.log',level=logging.INFO)

		post = web.input(thefile={})
		
		if 'thefile' in post:
			#web.debug(post['thefile'].filename)
			filename = os.getcwd() +'/Databases/'+ 'databas.mgt'
			web.debug(filename)
			fout = open(filename,'w+')
			fout.write(post.thefile.file.read())
			fout.close()

if __name__ == "__main__":
    app.run()