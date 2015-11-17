#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

print "GetService invoked"

urls = ('/', 'index',
        '/getdatabase/(.+)', 'getdatabase',
		'/getstatic', 'getstatic')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "The address /getdatabase returns a database where ?user=xxx?pwd=xxx?name=xxx"

class getdatabase:
    def GET(self, dbname):
        return "get db: " + dbname

class getstatic:
    def GET(self):
        raise web.seeother('/static/exportedDB.mgt')

if __name__ == "__main__":
    app.run()