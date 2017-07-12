from get_ownpost_id import get_own_post_id
from constant import BASE_URL,APP_ACCESS_TOKEN
from textblob import TextBlob                            #library for sentiment analysis
from textblob.sentiments import NaiveBayesAnalyzer       #classifier for sentiment analysis
import requests

positive_comments_list=[]
negative_comments_list=[]
total_comments_list=[]

def comment_percentage():
    media_id = get_own_post_id()
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_text = comment_info['data'][x]['text']
                total_comments_list.append(comment_text)
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())   #checking comment type
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    negative_comments_list.append(comment_text)
                else:
                    positive_comments_list.append(comment_text)
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
