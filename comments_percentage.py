import matplotlib.pyplot as plt
from get_comments_percentage import positive_comments_list,negative_comments_list,total_comments_list
from get_comments_percentage import delete_negative_comment

delete_negative_comment()
pos_comments = len(positive_comments_list)
neg_comments = len(negative_comments_list)
tot_comments = len(total_comments_list)

slices     = [pos_comments,neg_comments,tot_comments]
activities = ['positive_comments','negative_comments','total_comments']
cols       = ['c','m','g']
plt.pie(slices,labels=activities,colors=cols,startangle=90)
plt.title('as')
plt.show()
exit()