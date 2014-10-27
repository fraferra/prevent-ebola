from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Go to http://dev.twitter.com and create an app.
# The consumer key and secret will be generated for you after
consumer_key="OLLpwcWlXf3vKPzr3qMxUJkUO"
consumer_secret="zDBSRAZLrvmouX5XInvgu8eObEjAfxM7iDCreUqyEbjPMyze03"

# After the step above, you will be redirected to your app's page.
# Create an access token under the the "Your access token" section
access_token="1974376242-XNEKCtqSrkiHnUfzf4dFjFCf61fmbzyWXnN8QNy"
access_token_secret="IMCNi88B7Jz0WSODVq1e5wszeCgR63VsyuiVUf9Ns0GFa"

class StdOutListener(StreamListener):
    """ A listener handles tweets are the received from the stream.
    This is a basic listener that just prints received tweets to stdout.

    """
    def on_data(self, data):
        print data
        return True

    def on_error(self, status):
        print status

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    l = stream.filter(track=['preventebola2014'])

