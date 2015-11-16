#!/usr/bin/env python
# -*- coding: utf-8 -*-

import web

print "GetService invoked"

urls = ('/', 'index',
        '/getdatabase', 'getdatabase')
app = web.application(urls, globals())

class index:
    def GET(self):
        return "The address /getdatabase returns a database where ?user=xxx?pwd=xxx?name=xxx"

class getdatabase:
    def GET(self):
        return "Test"

if __name__ == "__main__":
    app.run()