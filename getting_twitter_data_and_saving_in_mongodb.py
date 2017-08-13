import pymongo
from pymongo import MongoClient
from twython import TwythonStreamer
from vardata import *
import json
import MySQLdb as mysql

APP_KEY = app_key
APP_SECRET = app_secret
OAUTH_TOKEN = oauth_token
OAUTH_TOKEN_SECRET = oauth_token_secret


# This creates connection with the mysql server
connection = MongoClient()
db = connection['osndata']

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		print "On success"
		if 'text' in data:
			text = data['text'].encode('utf-8')
			print text
			tweet_record = data
			tweet_record['_id']=data['id_str']
			db['tweets'].insert(tweet_record)

	def on_error(self,status_code,data):
		print status_code
		pass

stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='python')

	