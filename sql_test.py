# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 16:52:06 2015

@author: hugobowne-anderson
"""


#http://zetcode.com/db/sqlitepythontutorial/
import sqlite3 as lite
import sys
import json
import unicodedata


###########MAKE LIST OF TWEETS:################
##set deirectory here:
tweets_data_path = '/Users/hugobowne-anderson/repos/selenium-auto-posting/listening_to_tweets/some_stream_pol.txt'

tweets_data = []
tweets_file = open(tweets_data_path, "r")
for line in tweets_file:
    try:
        tweet = json.loads(line)
        tweets_data.append(tweet)
    except:
        continue    
print len(tweets_data)
tweets_data.pop(0)

tweets_data[0].keys()
tweets_data[0]['place']

type(i['place'])

for i in tweets_data:
    try:
        print i['place']['full_name']
    except:
        print "Shiiiiiiiite: something missing in data"    
############################################

####SQLITE#EG#########
con = lite.connect('test.db') ##connect to db
cur = con.cursor() #get cursor objet to traverse records from result set
cur.execute('SELECT SQLITE_VERSION()') ##execute method of cursor to execute an SQL statement/query

data = cur.fetchone() ##fetch data (one record for the time being)

print "SQLite version: %s" % data
con.close()

############################################
    
###add tweets to db
con = lite.connect('/Users/hugobowne-anderson/repos/selenium-auto-posting/listening_to_tweets//test.db') ##connect to db  
cur = con.cursor()  
cur.execute("DROP TABLE Tweets")
cur.execute("CREATE TABLE Tweets(Name TEXT, Tweet TEXT, Language TEXT, Created_at TEXT, Geo TEXT, Place TEXT)")
for i in tweets_data:
    #aaaaaaand do check this out: http://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html
    #print i['text']
    try:
        user = i['user']['name'];
    except KeyError:
        user = None;
    try:
        place = i['place']['full_name'];
    except:
        place = None;
    try:
        cur.execute("INSERT INTO Tweets VALUES(? , ? , ? , ? , ? , ?)", 
                (user, i['text'] , i['lang'] , i['timestamp_ms'] , i['geo'] , place));
    except:
        print "Shiiiiiiiite: something missing in data"
            
con.commit() #commit changes to db
con.close() #close connection

i.user()

#####test & select################
#cur.execute("SELECT * FROM Tweets");
con = lite.connect('/Users/hugobowne-anderson/repos/selenium-auto-posting/listening_to_tweets//test.db') ##connect to db  
cur = con.cursor()
#cur.execute("SELECT Language FROM Tweets");
#rows = cur.fetchall()
#for row in rows:
#        print row

cur.execute("SELECT place, count(place) from Tweets group by place");
rows = cur.fetchall()
for row in rows:
    print row




cur.execute("SELECT Language, count(Language) from Tweets group by Language");
rows = cur.fetchall()

type(rows)

#plot(rows)

x = [];
y = [];
for row in rows:
        x.append(row[0]);
        y.append(row[1]);
    
import numpy as np
import matplotlib.pyplot as plt

#http://matplotlib.org/api/pyplot_api.html
N = len(x)
ind = np.arange(N)    # the x locations for the groups
width = 0.35       # the width of the bars: can also be len(x) sequence

plt.bar(ind, y )

plt.xticks(ind + width/2., x , rotation=90)
plt.ylabel('Number of tweets')
plt.ylabel('Language')


#####################################


        
        

########################################################



