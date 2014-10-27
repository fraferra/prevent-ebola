from flask import *
import os
import jinja2
import requests
#from utils import *

import re
app = Flask(__name__)
#from stream2 import returnTweets
import feedparser

@app.route('/',methods=['GET'])
def home():
  if request.method == 'GET':
    articles=getBBCEbolafeeds()
    a=getNYTEbolafeeds()
    for aa in a:
      articles.append(aa)
  return render_template('new_index.html', articles=articles)



def getBBCEbolafeeds():
  python_wiki_rss_url = "http://feeds.bbci.co.uk/news/health/rss.xml"
  feed = feedparser.parse( python_wiki_rss_url )
  articles=feed['entries']
  new_articles=[]
  for article in articles:
    r=re.search(r'ebola', article['summary'].lower())
    if r:
      article['site']='BBC'
      new_articles.append(article)
  return new_articles

def getNYTEbolafeeds():
  python_wiki_rss_url = "http://rss.nytimes.com/services/xml/rss/nyt/Health.xml"
  feed = feedparser.parse( python_wiki_rss_url )
  articles=feed['entries']
  new_articles=[]
  for article in articles:
    r=re.search(r'ebola', article['summary'].lower())
    if r:
      article['site']='New York Times'
      new_articles.append(article)
  return new_articles




'''
@app.route('/', methods=['GET'])
def index():

    #results=search()
    results = [
      ['Bondi Beach', -33.890542, 151.274856, 4],
      ['Coogee Beach', -33.923036, 151.259052, 5],
      ['Cronulla Beach', -34.028249, 151.157507, 3],
      ['Manly Beach', -33.80010128657071, 151.28747820854187, 2],
      ['Maroubra Beach', -33.950198, 151.259302, 1]
    ]

    #return render_template('index2.html', results=results)
    return returnTweets()
'''


if __name__ == "__main__":
    app.run(debug=True)