import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt, mpld3

# open file
reader = []
file = open('test.csv','r')
reader = list(file)
print(reader)

# get data from csv
hours = []
sentiment = []
for i in range(len(reader)):
    temp = reader[i].split(',')
    hours.append(float(temp[0]))
    test = temp[1]
    test = test[0:-1]
    sentiment.append(float(test))
print(hours)
print(sentiment)

# determining if sentiment is positive or negative
positive_sentiment = 0
negative_sentiment = 0
neutral_sentiment = 0
for i in range(len(sentiment)):
    if sentiment[i] < -0.45:
        negative_sentiment += 1
    elif sentiment[i] > 0.5:
        positive_sentiment += 1
    else:
        neutral_sentiment += 1

# plot data
plt.plot(hours,sentiment,'r')
zero_array = np.zeros(24)
plt.plot(range(0,24),zero_array,'b--')
#plt.title('Feelr Graph for 12/1/2018:')
plt.xlabel('Time(Hours)')
plt.ylabel('Sentiment scale')
plt.savefig('hours_vs_sent.png')
plt.show()

# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Negative Mood', 'Positive Mood', 'Neutral Mood'
sizes = [negative_sentiment,positive_sentiment,neutral_sentiment]
# explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice
# fig1, ax1 = plt.subplots()
plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90, colors=['#DA727E','#685C79','lightblue'])
plt.axis('equal')
plt.title('')
plt.savefig('piechart.png')
plt.show()
file.close()
##############################################################################
# monthly plot view
dates = []
average_sentiment = []
file1 = open('days.csv','r') ## formatted as date,avg_sentiment value
reader1 = list(file1)
for i in range(len(reader1)):
    temp = reader1[i].split(',')
    dates.append((temp[0]))
    test = temp[1]
    test = test[0:-1]
    average_sentiment.append(float(test))
print(dates)
print(average_sentiment)
plt.plot(range(1,31),average_sentiment)
zero_array = np.zeros(35)
plt.plot(range(0,35),zero_array,'b--')
plt.xlabel('Days')
plt.ylabel('Average Sentiment')
plt.savefig('average.png')
plt.show()
file1.close()

# weekly at a glance
def pie_chart(name, negative = 0, postive = 0, neutral = 0): #format as pos, neg, neutral
    labels = 'Negative Mood', 'Positive Mood', 'Neutral Mood'
    sum = negative + postive + neutral
    sizes = [(negative/sum)*100, (postive/sum)*100, (neutral/sum)*100]
    # explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice
    # fig1, ax1 = plt.subplots()
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90,colors=['#DA727E','#685C79','lightblue'])
    plt.axis('equal')
    plt.title('')
    plt.savefig(name)
    plt.show()

pie_chart('day1.png',35,35,35)
pie_chart('day2.png',34,48,22)
pie_chart('day3.png',34,48,22)
pie_chart('day4.png',100,120,80)
pie_chart('day5.png',34,48,22)
pie_chart('day6.png',33,52,42)
pie_chart('day7.png',34,48,22)
