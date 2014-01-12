# coding: utf-8
import twitter
import secret

# ログイン
def login():
    api = twitter.Api(
        consumer_key = secret.twDict['consumer_key'],
        consumer_secret = secret.twDict['consumer_secret'],
        access_token_key = secret.twDict['access_token_key'],
        access_token_secret = secret.twDict['access_token_secret']
        )
    return api

if __doc__ == "__main__":
    api = login()
