#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import sqlite3
import logging

print "GetService invoked"

urls = ('/', 'index',
        '/getdatabase', 'getdatabase')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "The address /getdatabase/xxx returns a database where xxx is the database name"

class getdatabase:
    def GET(self):
		logging.basicConfig(filename='getlog.log',level=logging.INFO)

		request = web.input(user="xxx", pwd='xxx', db='xxx')
		logging.info("user: "+ request.user +", pwd: "+ request.pwd +", db: "+ request.db)

		connection = sqlite3.connect('Users.mgt')
		cursor = connection.cursor()

		u = (request.user, request.pwd)
		cursor.execute('SELECT * FROM Users WHERE Username=? AND Password=?', u)
		if len(cursor.fetchall()) == 1:
			n = (request.db,)
			cursor.execute('SELECT * FROM Databases WHERE Name=?', n)
			if len(cursor.fetchall()) == 1:
				raise web.seeother('/static/' + request.db + '.mgt')
			else:
				return "DatabaseDoesNotExist"
		else:
			return "UserOrPasswordIncorrect"		

if __name__ == "__main__":
    app.run()