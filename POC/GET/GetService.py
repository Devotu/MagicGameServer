#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

print "GetService invoked"

urls = ('/', 'index',
        '/getdatabase/(.+)', 'getdatabase')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "The address /getdatabase/xxx returns a database where xxx is the database name"

class getdatabase:
    def GET(self, dbname):
		raise web.seeother('/static/' + dbname + '.mgt')

if __name__ == "__main__":
    app.run()