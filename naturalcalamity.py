from get_user_id import get_user_id,username
from constant import BASE_URL,APP_ACCESS_TOKEN
import requests

service = ['#food' ,'#shop' ,'#bike' ,'#weather' ,'#iphoneonly' ,'#cool' ,'#life' ,'#lol' ,'#instamood' ,'#life' ,'#style'
           ,'#amazing' ,'#summer' ,'#fashion' ,'#friends' ,'#cute' ,'#happy' ,'#feeling','#monogram','#thanks_everyone']


def caption_comment() :
    user_id = get_user_id(username)
    request_url = (BASE_URL + "users/%s/media/recent/?access_token=%s" % (user_id, APP_ACCESS_TOKEN))
    print("Get request url: " + request_url)
    username = requests.get(request_url).json()
    if username['meta']['code'] == 200:

        if len(username['data']):

            for post in range(0, len(username['data'])):
                pic_no = post + 1
                for temp in service:
                    if username['data'][post]['caption'] == None:
                        print("Sorry there is no hashtag inside the image...")

                    elif temp in username['data'][post]['caption']['text']:
                        print(username['data'][post]['caption']['text'])
                        pic_id = username['data'][post]['id']
                        comment_text = raw_input("Your comment: ")
                        payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
                        request_url = (BASE_URL + 'media/%s/comments') % (pic_id)
                        print 'POST request url : %s' % (request_url)

                        make_comment = requests.post(request_url, payload).json()

                        if make_comment['meta']['code'] == 200:
                            print "Successfully added a new comment!"
                        else:
                            print "Unable to add comment. Try again!"
                    else :
                        print("Sorry hashtag didn't match.Go further...")
            print("End of images...")