from twython import TwythonStreamer
from vardata import *
import json
import MySQLdb as mysql

APP_KEY = app_key
APP_SECRET = app_secret
OAUTH_TOKEN = oauth_token
OAUTH_TOKEN_SECRET = oauth_token_secret


host = 'localhost'
user = 'root'
passwd = password
db = 'osndata'


# This function creates connection with the mysql server
def create_connection():
	connection = mysql.connect(host,user,passwd,db)
	cursor = connection.cursor()
	return connection, cursor


#this function closes the connection
def close_connection(cursor,connection):
	cursor.close()
	connection.commit()
	connection.close()

class MyStreamer(TwythonStreamer):
	def on_success(self,data):
		print "On success"
		if 'text' in data:
			connection,cursor = create_connection();
			text = data['text'].encode('utf-8')
			print text
			query = '''insert ignore into tweets (tweet_id,text) values (%s,%s)'''
			cursor.execute(query,(data['id_str'],text))
			close_connection(cursor,connection)

	def on_error(self,status_code,data):
		print status_code
		pass

stream = MyStreamer(APP_KEY,APP_SECRET,OAUTH_TOKEN,OAUTH_TOKEN_SECRET)

stream.statuses.filter(track='python')

	