from self_info import self_info
from get_own_post import get_own_post
from recent_liked_pic import get_my_recent_liked_post
from like_a_post import like_a_post
from post_comment import post_a_comment
from delete_own_negative_comments import delete_own_negative_comment
from comments_percentage import show_pie_chart
from get_user_info import  get_user_info
from get_users_post import get_users_post
from get_most_liked_users_post import most_liked_post
from most_commented_users_post import most_commented_post
from most_liked_own_post import most_liked_own_post
from most_commented_own_post import most_commented_post
from comments_list import comment_list
from get_comments_percentage import comment_percentage
from get_post_id import get_post_id
from get_all_posts_of_user import get_all_posts
from naturalcalamity import caption_comment

#other _data function
def other_data():

    username = raw_input("Please enter the username of the person ")

    choice = True
    while choice:

        print "\nWhat do you want to do ?"

        print "Enter 1 to get his/her info"
        print "Enter 2 to get his/her recent post id"
        print "Enter 3 to download recent post"
        print "Enter 4 to like recent post"
        print "Enter 5 to post a comment on recent post"
        print "Enter 6 to download all posts"
        print "Enter 7 to get most liked post"
        print "Enter 8 to get most commented post"
        print "Enter 9 to get list of comments on recnet post"
        print  "Enter 10 to to the extra objective"
        print "Enter 11 to Exit."

        get_num = int(raw_input("Please Enter "))
        print('\n')
        if   get_num == 1:
            get_user_info(username)
        elif get_num == 2:
            print "The post_ID is %s" % (get_post_id(username))
        elif get_num == 3:
            get_users_post(username)
        elif get_num == 4:
            like_a_post(username)
        elif get_num == 5:
            post_a_comment(username)
        elif get_num == 6:
            get_all_posts(username)
        elif get_num == 7:
            most_liked_post(username)
        elif get_num == 8:
            most_commented_post(username)
        elif get_num == 9:
            comment_list(username)
        elif get_num ==10:
            caption_comment()
        elif get_num == 11:
            choice = False
        else:
            print"Please enter valid number"


#our_own_data_function
def own_data():
    print "\nWhat do you want to do"

    choice = True
    while choice:
        print "Enter 1 to download recent post"
        print "Enter 2 to download recent liked post"
        print "Enter 3 to get your info"
        print "Enter 4 to download most liked post"
        print "Enter 5 to download most commented post"
        print "Enter 6 to delete negative comments of your posts"
        print "Enter 7 to get comments percentage of your posts with piechart"
        print "Enter 8 to access the extra objective "
        print "Enter 9 to Exit."

        get_num = int(raw_input("Please Enter"))
        print('\n')
        if  get_num == 1:
            get_own_post()
        elif get_num == 2:
            get_my_recent_liked_post()
        elif get_num == 3:
            self_info()
        elif get_num == 4:
            most_liked_own_post()
        elif get_num == 5:
            most_commented_post()
        elif get_num == 6:
            delete_own_negative_comment()
        elif get_num == 7:
            comment_percentage()
            show_pie_chart()
        elif get_num == 8:
            caption_comment()
        elif get_num == 9:
            choice = False
        else:
            print"Please enter valid number"


#main function
def main():
    print "\nWhat do you want to do"

    choice=True
    while choice:
        print "Enter 1 for accessing own data"
        print "Enter 2 for accessing other's data"
        print "Enter 3 for exit"
        get_num=int(raw_input("Please Enter "))
        print '\n'

        if(get_num==1):
            own_data()
        elif(get_num==2):
            other_data()
        elif(get_num==3):
            choice=False
        else:
            print"Please enter valid number"

    print"Thanks to use Insta bot"


#Program Starts
main()