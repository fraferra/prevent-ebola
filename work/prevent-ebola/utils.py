import re
from TwitterSearch import *
from googlemaps import GoogleMaps
import json
def search():

    try:
        locations=[]
        tso = TwitterSearchOrder() # create a TwitterSearchOrder object
        tso.setKeywords(['preventebola2014',]) # let's define all words we would like to have a look for
        tso.setCount(7) # please dear Mr Twitter, only give us 7 results per page
        tso.setIncludeEntities(False) # and don't give us all those entity information
        # it's about time to create a TwitterSearch object with our secret tokens
        ts = TwitterSearch(
            consumer_key = 'OLLpwcWlXf3vKPzr3qMxUJkUO',
            consumer_secret = 'zDBSRAZLrvmouX5XInvgu8eObEjAfxM7iDCreUqyEbjPMyze03',
            access_token = '1974376242-XNEKCtqSrkiHnUfzf4dFjFCf61fmbzyWXnN8QNy',
            access_token_secret = 'IMCNi88B7Jz0WSODVq1e5wszeCgR63VsyuiVUf9Ns0GFa'
         )
        locations=returnCoordinate(ts.searchTweetsIterable(tso))
        return locations
    except TwitterSearchException as e: # take care of all those ugly errors if there are some
        print(e)



def returnCoordinate(tweets):
    gmaps = GoogleMaps('AIzaSyB8YS_1RgpdLZogrpNsZ6V7Yc6mKJAE_og')
    updated=[]
    for tweet in tweets:
        location=re.search('where:([\w]+)', lower(tweet['text']))
        if location:
            address = location.group(1)
            lat, lng = gmaps.address_to_latlng(address)
            updated.append([location, lat, lng])
    return updated

