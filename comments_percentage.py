import matplotlib.pyplot as plt       #library for making pie chart
from get_comments_percentage import comment_percentage
from get_comments_percentage import positive_comments_list,negative_comments_list,total_comments_list

comment_percentage()

def show_pie_chart():
    pos_comments = float(len(positive_comments_list))
    neg_comments = float(len(negative_comments_list))
    tot_comments = float(len(total_comments_list))

    pos_perc=(pos_comments/tot_comments) * 100
    neg_perc=(neg_comments/tot_comments) * 100
    tot_perc=(tot_comments/tot_comments) * 100

    slices = [pos_perc, neg_perc, tot_perc]
    activities = ['positive_comments_'+str(pos_perc), 'negative_comments_'+str(neg_perc), 'total_comments_'+str(tot_perc)]
    cols = ['c', 'm', 'g']
    plt.pie(slices, labels=activities, colors=cols, startangle=90)
    plt.title('PIE CHART')
    plt.show()              #it will show pie chart
    exit()
#show_pie_chart()