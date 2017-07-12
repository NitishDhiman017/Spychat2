from constant import BASE_URL,APP_ACCESS_TOKEN
from get_user_id import get_user_id
import requests
import  urllib

def get_users_post(insta_username):

    user_id = get_user_id(insta_username)
    if user_id == None:
        print 'User does not exist!'
        exit()

    request_url = (BASE_URL + 'users/%s/media/recent/?access_token=%s') % (user_id, APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_media = requests.get(request_url).json()
    # print user_media

    if user_media['meta']['code'] == 200:
        if len(user_media['data']):
            #return user_media['data'][0]['id']           #just to check
            print user_media['data'][0]['id']

            image_name = "shawnpic.jpg"
            image_url = user_media['data'][0]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print 'Your image has been downloaded!'

        else:
            print "There is no recent post!"
    else:
        print "Status code other than 200 received!"
    return None
#get_users_post('shawnrajput007')    #function call