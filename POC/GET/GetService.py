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
		
		n = (request.db,)
		cursor.execute('SELECT * FROM Databases WHERE Name=?', n)
		logging.info('matching rows: ' + str(cursor.rowcount))

		raise web.seeother('/static/' + request.db + '.mgt')

if __name__ == "__main__":
    app.run()