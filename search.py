# coding: UTF-8
import twitter
import secret
import urllib

def url_encode(word):
  return urllib.quote(word.encode('utf-8')) # OK

# ログイン
def login():
    api = twitter.Api(
      consumer_key = secret.twDict['consumer_key'],
      consumer_secret = secret.twDict['consumer_secret'],
      access_token_key = secret.twDict['access_token_key'],
      access_token_secret = secret.twDict['access_token_secret']
      )
    return api

if __name__ == "__main__":

    api = login()
    word = u'アフリカで皆既日食 「黒い太陽」に歓声'
    search_word = url_encode(word)
    result = api.GetSearch(term=search_word, lang="ja")
    # for status in result:
    #     print status.text
    #     print '-' * 30
