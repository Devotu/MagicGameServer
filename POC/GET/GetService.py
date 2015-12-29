#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web
import sqlite3
import logging

print "GetService invoked"

urls = ('/', 'index',
        '/getdatabase', 'getdatabase',
		'/getjson', 'getjson')
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

class getjson:
	def GET(self):
		tables = ['Alterations', 'Decks', 'Games', 'Opponents']
		jsonTables = []

		request = web.input(user="xxx", pwd='xxx', db='xxx')

		usersConnection = sqlite3.connect('Users.mgt')
		userCursor = usersConnection.cursor()

		u = (request.user, request.pwd)
		userCursor.execute('SELECT * FROM Users WHERE Username=? AND Password=?', u)
		if len(userCursor.fetchall()) == 1:
			n = (request.db,)
			userCursor.execute('SELECT Name FROM Databases WHERE Name=?', n)
			requestedDatabaseRow = userCursor.fetchall()
			if len(requestedDatabaseRow) == 1:
				web.debug(str(requestedDatabaseRow[0][0]) + '.mgt')
				dataConnection = sqlite3.connect(str(requestedDatabaseRow[0][0]) + '.mgt')
				dataCursor = dataConnection.cursor()

				for table in tables:
					dataCursor.execute('SELECT * FROM ' + table)
					web.debug(table)


if __name__ == "__main__":
    app.run()