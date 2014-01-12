import twitter
import secret

api = twitter.Api(
    consumer_key = secret.twDict['consumer_key'],
    consumer_secret = secret.twDict['consumer_secret'],
    access_token_key = secret.twDict['access_token_key'],
    access_token_secret = secret.twDict['access_token_secret']
)

msg = u'Pythonからおはようせかい'
api.PostUpdate(msg)
api.PostUpdate('お、できた')
