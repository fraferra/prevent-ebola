from TwitterAPI import TwitterAPI


TRACK_TERM = 'preventebola2014'


CONSUMER_KEY = 'OLLpwcWlXf3vKPzr3qMxUJkUO'
CONSUMER_SECRET = 'zDBSRAZLrvmouX5XInvgu8eObEjAfxM7iDCreUqyEbjPMyze03'
ACCESS_TOKEN_KEY = '1974376242-XNEKCtqSrkiHnUfzf4dFjFCf61fmbzyWXnN8QNy'
ACCESS_TOKEN_SECRET = 'IMCNi88B7Jz0WSODVq1e5wszeCgR63VsyuiVUf9Ns0GFa'
list_tweets=[]

api = TwitterAPI(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN_KEY,
    ACCESS_TOKEN_SECRET)

r = api.request('statuses/filter', {'track': TRACK_TERM})

for item in r:
    #print(item['text'] if 'text' in item else item)
    if 'text' in item:
    	list_tweets.append(item['text'])
    #print list_tweets


def returnTweets():
	return list_tweets
