from constant import BASE_URL,APP_ACCESS_TOKEN
from get_user_id import get_user_id

import requests

def get_post_id(insta_username):            #similar to get_users post() with little change

    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    user_media = requests.get(request_url).json()

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            return user_media['data'][0]['id']
        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    return None
#get_post_id('shawnrajput007')    #function call