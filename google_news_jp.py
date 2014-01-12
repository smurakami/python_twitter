# coding: UTF-8
import twitter
import secret

class GoogleNewsJP():
    def __init__(self, api):
        result = api.GetUsersSearch('Google_News_jp')
        for user in result:
            if user.name == 'Google_News_jp':
                self.user = user
                return
        print "Error: Google_News_jp not found"


# def getGoogleNewsJP(api = None):
#     if api == None:
#         print "Error: No API"
#         print "usage: g = getGoogleNewsJP(twitterApi)"
#     result = api.GetUsersSearch('Google_News_jp')
#     for user in result:
#         if user.name == 'Google_News_jp':
#             return user
#     print "Error: Google_News_jp not found"

if __name__ == "__main__":
    api = twitter.Api(
        consumer_key = secret.twDict['consumer_key'],
        consumer_secret = secret.twDict['consumer_secret'],
        access_token_key = secret.twDict['access_token_key'],
        access_token_secret = secret.twDict['access_token_secret']
        )

    result = api.GetUsersSearch('Google_News_jp')
    for user in result:
        if user.name == 'Google_News_jp':
            googleNewsJP = user
            break

    max_id = None
    for _counter in range(2):
        timeline = api.GetUserTimeline(googleNewsJP.id, max_id = max_id)
        for tweet in timeline:
            print tweet.text
            print tweet.created_at
            for url in tweet.urls:
                print url.expanded_url





