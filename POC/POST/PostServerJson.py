#!/usr/bin/env python

import web
import json

print "matserver invoked"

urls = ('/post', 'post')
app = web.application(urls, globals())

class post:
    def POST(self):
		js = web.data()
		pj = json.loads(js)
		web.debug(pj['tables'])

if __name__ == "__main__":
    app.run()



