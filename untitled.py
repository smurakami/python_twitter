import my_twitter
api = my_twitter.Api()

result = api.GetUsersSearch("M084sky")
u = result[0]

friend_ids = api.GetFriendIDs(u.id)

for friend_id in friend_ids:
    friend = api.GetUser(friend_id)
    description = friend.description + friend.location
    if "eeic" in description:
        print friend.name
        print description
        # api.CreateFriendship(friend.id)