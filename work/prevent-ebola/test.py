import re
from TwitterSearch import *
try:
    #locations=[]
    tso = TwitterSearchOrder() # create a TwitterSearchOrder object
    tso.setKeywords(['corniuzza',]) # let's define all words we would like to have a look for
   # tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
    #tso.setIncludeEntities(False) # and don't give us all those entity information
    # it's about time to create a TwitterSearch object with our secret tokens
    print 'TEST'
    ts = TwitterSearch(
        consumer_key = 'OLLpwcWlXf3vKPzr3qMxUJkUO',
        consumer_secret = 'zDBSRAZLrvmouX5XInvgu8eObEjAfxM7iDCreUqyEbjPMyze03',
        access_token = '1974376242-XNEKCtqSrkiHnUfzf4dFjFCf61fmbzyWXnN8QNy',
        access_token_secret = 'IMCNi88B7Jz0WSODVq1e5wszeCgR63VsyuiVUf9Ns0GFa'
     )

    for tweet in ts.searchTweetsIterable(tso): # this is where the fun actually starts :)
        print( '@%s tweeted: %s' % ( tweet['user']['screen_name'], tweet['text'] ) )
       # location=re.search('where:([\w]+)', tweet['text'])
      #  if location:
     #       locations.append(location)
    #return locations

except TwitterSearchException as e: # take care of all those ugly errors if there are some
    print(e)
