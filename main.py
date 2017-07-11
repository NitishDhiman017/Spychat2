from self_info import self_info
from get_user_id import get_user_id
from get_user_info import  get_user_info
from get_own_post import get_own_post
from get_users_post import get_users_post
from recent_liked_pic import get_my_recent_liked_post
from like_a_post import like_a_post
from post_comment import post_a_comment
from delete_negative_comments import delete_negative_comment
from delete_own_negative_comments import delete_own_negative_comment

def insta_bot():

    username =raw_input("Please enter the username")

    print "Please choose any one from below"

    print (" Enter 1 for your info\n Enter 2 for getting user_id\n Enter 3 for getting user_info \n Enter 4 for getting your own post\n Enter"
          "5 for getting user's post\n Enter 6 for getting your recent liked post\n Enter 7 to hit a like on others post\n Enter"
          "8 for post a comment on other's post\n Enter 9 to delete comments on other's post")

    num=int(raw_input())
            #fetching own information

    if(num==1):
        get_user_id(username)             #just to check(this function's actual need is in get_user_info)

    if(num==2):
        get_user_info(username)

    if(num==5):
        get_users_post("username")


    if(num==7):
        like_a_post("username")

    if(num==8):
        post_a_comment("username")

    if(num==9):
        delete_negative_comment('username')

    if(num==10):
        delete_own_negative_comment()



def main():

    #your data
    self_info()
    get_own_post()
    get_my_recent_liked_post()

    #data based upon username
    insta_bot()

main()