# coding: utf-8

import my_twitter
api = my_twitter.Api()
result = api.GetUsersSearch("M084sky")
u = result[0]
friend_ids = api.GetFriendIDs(u.id)
first_index = 360
last_index = None
try:
    for index, friend_id in enumerate(friend_ids):
        if index < first_index:
            continue
        print index, friend_id
        last_index = index
        friend = api.GetUser(friend_id)
        data = friend.description + friend.location + friend.name + friend.screen_name
        if "eeic" in data.lower():
            print "=" * 10
            print friend.name
            print data
            print "=" * 10
            api.CreateFriendship(friend.id)

except:
    print "api制限に引っかかりました。このインデックスから再開しよう"
    print last_index