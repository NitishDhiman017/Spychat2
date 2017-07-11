from get_ownpost_id import get_own_post_id
from constant import BASE_URL,APP_ACCESS_TOKEN
from textblob import TextBlob                            #library for sentiment analysis
from textblob.sentiments import NaiveBayesAnalyzer       #classifier for sentiment analysis
import requests

positive_comments_list=[]
negative_comments_list=[]
total_comments_list=[]

def delete_negative_comment():
    media_id = get_own_post_id()
    request_url = (BASE_URL + 'media/%s/comments/?access_token=%s') % (media_id, APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    comment_info = requests.get(request_url).json()

    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            for x in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][x]['id']
                comment_text = comment_info['data'][x]['text']
                total_comments_list.append(comment_text)
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if (blob.sentiment.p_neg > blob.sentiment.p_pos):
                    negative_comments_list.append(comment_text)             #adding neg comment
                    print 'Negative comment : %s' % (comment_text)
                    delete_url = (BASE_URL + 'media/%s/comments/%s/?access_token=%s') % (
                    media_id, comment_id, APP_ACCESS_TOKEN)
                    print 'DELETE request url : %s' % (delete_url)
                    delete_info = requests.delete(delete_url).json()

                    if delete_info['meta']['code'] == 200:
                        print 'Comment successfully deleted!\n'
                    else:
                        print 'Unable to delete comment!'
                else:
                    positive_comments_list.append(comment_text)
                    print 'Positive comment : %s\n' % (comment_text.encode('utf-8'))
        else:
            print 'There are no existing comments on the post!'
    else:
        print 'Status code other than 200 received!'
delete_negative_comment()