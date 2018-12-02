from textblob import TextBlob


def run():
    #Initialize the lists
    output_list = []
    QC_list = []

    #Open the CSV of input

    infile = open("feelings.csv", 'r')

    #Read every line in the input
    #Process data, the date is transformed to mm/dd/yyyy and only hour is sliced
    #Place into the respective list

    for line in infile:
        print(line)
        data = line.split('�')
        full_time = data[0]
        date = (full_time[5:7] + "-" + full_time[9:10] + "-" + full_time[:4])
        hour = (full_time[11:13])
        blob = TextBlob(data[1])
        output_list.append((date, hour, blob.sentiment.polarity))
        QC_list.append((blob.sentiment, data[1]))
    infile.close()

    #Write the output to a csv file
    #Columns are Date, Time, and Sentiment Score
    #This CSV is used for the visualization on the web interface
    outfile = open("output.csv", 'w')
    for item in output_list:
        outfile.write(item[0]+","+item[1]+","+str(item[2])+"\n")
    outfile.close()

    #Wirte a file for QC
    #This is the Sentiment Polarity (-1 to 1), Subjectivity, and the full text
    outfile = open("QC_output.csv", 'w')
    for item in QC_list:
        outfile.write(str(item[0])+","+str(item[1])+"\n")
    outfile.close()
