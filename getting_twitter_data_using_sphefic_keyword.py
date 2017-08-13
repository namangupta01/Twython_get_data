from twython import Twython
from vardata import *
import json

APP_KEY = app_key
APP_SECRET = app_secret
OAUTH_TOKEN = oauth_token
OAUTH_TOKEN_SECRET = oauth_token_secret

twitter = Twython(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)
timeline = twitter.get_home_timeline();
data = twitter.search(q='python',result_type = 'popular',count = 100)

for text in data['statuses']:
	print text['text']
	