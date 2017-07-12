from constant import BASE_URL,APP_ACCESS_TOKEN
import requests
import urllib

like_list = []
post_id_list = []

def most_liked_own_post() :
    request_url = (BASE_URL + "users/self/media/recent/?access_token=%s") % (APP_ACCESS_TOKEN)
    #print("Get request url: " + request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data']):
            for temp in range(0,len(user_info['data'])) :
                post_id = user_info['data'][temp]['id']
                post_id_list.append(post_id)
                likes_count = user_info['data'][temp]['likes']['count']
                like_list.append(likes_count)
            maximum = max(like_list)
            print("No of likes for the post: %d"%(maximum))
            index = like_list.index(maximum)
            post_index = post_id_list[index]
            image_name = "mypicclike"+str(post_index)+'.jpg'
            image_url = user_info['data'][index]['images']['standard_resolution']['url']
            urllib.urlretrieve(image_url, image_name)
            print("Your image has been successfully saved..")
        else:
            print("No info exist")
    else:
        print("Incorrect code..")
#most_liked_own_post()