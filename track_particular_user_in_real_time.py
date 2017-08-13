from twython import TwythonStreamer
from vardata import *
import json

APP_KEY = app_key
APP_SECRET = app_secret
OAUTH_TOKEN = oauth_token
OAUTH_TOKEN_SECRET = oauth_token_secret

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		print "On success"
		print data['text'].encode('utf-8')

	def on_error(self,status_code,data):
		print status_code
		pass

stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

stream.statuses.filter(follow='849503183529545728')

	