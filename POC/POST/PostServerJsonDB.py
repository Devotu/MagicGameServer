#!/usr/bin/env python

import web
import json

print "matserver invoked"

urls = ('/post', 'postdb')
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
			web.debug("is list: " + str(isinstance(table, list)))
			web.debug("table: " + str(table))

class postdb:
    def POST(self):
		input = web.input(user="user", pwd="pwd", dbName="db", db="dbJson")
		web.debug("u:" + input.user)
		web.debug("p:" + input.pwd)
		web.debug("n:" + input.dbName)

		parsedJson = json.loads(input.db)

		tables = parsedJson['tables']
		web.debug(tables)
		
		alterations = tables[0]
		decks = tables[1]['decks']
		games = tables[2]
		opponents = tables[3]

		#web.debug("decks is dict:" + str(isinstance(decks, dict)))
		#web.debug("decks is list:" + str(isinstance(decks, list)))

		for deck in decks:
			web.debug("deck: " + str(deck['name']))

if __name__ == "__main__":
    app.run()

class Database(object):
	def __init__(self, j):
		self.__dict__=json.loads(j)