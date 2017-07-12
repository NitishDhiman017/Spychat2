import requests
from constant import BASE_URL,APP_ACCESS_TOKEN
username=raw_input("please enter name")
def get_user_id(username):

    request_url = (BASE_URL + 'users/search?q=%s&access_token=%s') %(username, APP_ACCESS_TOKEN)
                                    #searching friend
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            print user_info['data'][0]['id']     #just to check
            return user_info['data'][0]['id']
        else:
            return None
    else:
        print 'Status code other than 200 received!'
        exit()
#get_user_id(username)    #function call