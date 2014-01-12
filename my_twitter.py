# coding: utf-8
import twitter
import secret
import urllib
import re

class Api(twitter.Api):
    def __init__(self):
        twitter.Api.__init__(
            self,
            consumer_key = secret.twDict['consumer_key'],
            consumer_secret = secret.twDict['consumer_secret'],
            access_token_key = secret.twDict['access_token_key'],
            access_token_secret = secret.twDict['access_token_secret']
            )
        self.search_api_counter = 0

def url_encode(word):
    return urllib.quote(word.encode('utf-8')) # OK

if __name__ == "__main__":
    api = Api()
    print api
