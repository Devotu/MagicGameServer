#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import sqlite3
import logging
import os

print "PostService invoked"

urls = ('/', 'index',
        '/postdatabase', 'postdatabase')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "The address /postdatabase?xxx posts a database where xxx is the database"

class postdatabase:
	def GET(self):
		web.header("Content-Type","text/html; charset=utf-8")
		return """<html><head></head><body>
<form method="POST" enctype="multipart/form-data" action="">
<input type="file" name="thefile" />
<br/>
<input type="submit" />
</form>
</body></html>"""

	def POST(self):
		logging.basicConfig(filename='postlog.log',level=logging.INFO)

		post = web.input(thefile={})
		cwd = os.getcwd()
		saveDir = os.path.join(cwd, '/Databases')
		web.debug(saveDir)
		#web.debug(post)
		
		if 'thefile' in post:
			web.debug(post['thefile'].filename)
			filename = os.getcwd() +'/Databases/'+ post['thefile'].filename
			fout = open(filename,'w+')
			fout.write(post.thefile.file.read())
			fout.close()


if __name__ == "__main__":
    app.run()