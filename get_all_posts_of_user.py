from get_user_id import get_user_id
from constant import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib

def get_all_posts(username) :
    user_id = get_user_id(username)
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s" % (user_id, APP_ACCESS_TOKEN))
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            for post in range(0,len(user_info['data'])):  #getting post via loop
                pic_no = post + 1
                pic_id = user_info['data'][post]['id']
                image_name ="shawn"+str(pic_no)+".jpg"
                image_url = user_info['data'][post]['images']['standard_resolution']['url']
                urllib.urlretrieve(image_url,image_name)
                print(str(pic_no) + " pics has been saved.")
        else:
            print("No info exist")
    else:
        print("Incorrect code")