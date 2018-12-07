import csv
import datetime
import time
import matplotlib
matplotlib.use('Agg') # no use of display driver
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# plot graph with normal lines
def plotGraph(rangeVal, timestamp, file_name, title, yLabelName, outFileName): #range for the time, file_name with data
    # Values to store
    timestamps = []
    Veranda = []
    Wohnzimmer = []
    Schlafzimmer = []
    Badezimmer = []
    Elektrik = []
    Carport = []
    container = [timestamps, Veranda, Wohnzimmer, Schlafzimmer, Badezimmer, Elektrik, Carport]
    #print file_name

    # calculate time range
    last_date = timestamp - rangeVal
    csv_file = open(file_name, "r")
    csv_reader = csv.reader((line.replace('\0','') for line in csv_file), delimiter=";")

    # split the values into container
    for row in csv_reader:
        if len(row) > 0 :
            times = int(row[0])/1000
            if times >= last_date:
                value = datetime.datetime.fromtimestamp((int(row[0])/1000))
                timestamps.append(value)
                Veranda.append(row[1])
                Wohnzimmer.append(row[2])
                Schlafzimmer.append(row[3])
                Badezimmer.append(row[4])
                Elektrik.append(row[5])
                Carport.append(row[6])
    csv_file.close()

    # start plot generation here
    plt.plot(container[0], container[1], label='Veranda', color='r')
    plt.plot(container[0], container[2], label='Wohnzimmer', color='b')
    plt.plot(container[0], container[3], label='Schlafzimmer', color='y')
    plt.plot(container[0], container[4], label='Badezimmer', color='g')
    plt.plot(container[0], container[5], label='Elektrik', color='c')
    plt.plot(container[0], container[6], label='Carport', color='orange')

    plt.gcf().autofmt_xdate()

    plt.xlabel('time')
    plt.ylabel(yLabelName)
    plt.title(title)
    plt.legend()

    plt.savefig(outFileName)
    plt.clf()

#plot graph as histogram for long range
def plotHisto(rangeVal, timestamp, file_name, title, yLabelName, outFileName): #range for the time, file_name with data
    # Values to store
    timestamps = []
    Veranda = []
    Wohnzimmer = []
    Schlafzimmer = []
    Badezimmer = []
    Elektrik = []
    Carport = []
    container = [timestamps, Veranda, Wohnzimmer, Schlafzimmer, Badezimmer, Elektrik, Carport]

    #calling average for long distance plot
    container = averageValue(24*60*60, rangeVal, file_name, container)


    # start plot generation here
    plt.plot(container[0], container[1], label='Veranda', color='r')
    plt.plot(container[0], container[2], label='Wohnzimmer', color='b')
    plt.plot(container[0], container[3], label='Schlafzimmer', color='y')
    plt.plot(container[0], container[4], label='Badezimmer', color='g')
    plt.plot(container[0], container[5], label='Elektrik', color='c')
    plt.plot(container[0], container[6], label='Carport', color='orange')

    plt.gcf().autofmt_xdate()

    plt.xlabel('time')
    plt.ylabel(yLabelName)
    plt.title(title)
    plt.legend()

    plt.savefig(outFileName)
    plt.clf()

def averageValue(average_range, rangeVal, file_name, container):

    time_stamp = 0
    av_Veranda = 0
    av_Wohnzimmer = 0
    av_Schlafzimmer = 0
    av_Badezimmer = 0
    av_Elektrik = 0
    av_Carport = 0

    av_Time = 0
    step_time = 0
    c = 1

    # calculate time range
    start_time = time.time()
    step_time = start_time - average_range
    last_date = start_time - rangeVal
    csv_file = open(file_name, "r")
    csv_reader = csv.reader((line.replace('\0','') for line in csv_file), delimiter=";")

    # create average for time period
    for row in csv_reader:
        if len(row) > 0 :
            times = int(row[0])/1000
            if times >= last_date:
                if times >= step_time:
                    av_Veranda = av_Veranda + float(row[1])
                    av_Wohnzimmer = av_Wohnzimmer + float(row[2])
                    av_Schlafzimmer = av_Schlafzimmer + float(row[3])
                    av_Badezimmer = av_Badezimmer + float(row[4])
                    av_Elektrik = av_Elektrik + float(row[5])
                    av_Carport = av_Carport + float(row[6])
                    c = c + 1

                else:
                    value = datetime.datetime.fromtimestamp((int(row[0])/1000))
                    container[0].append(value)
                    container[1].append(av_Veranda/c)
                    container[2].append(av_Wohnzimmer/c)
                    container[3].append(av_Schlafzimmer/c)
                    container[4].append(av_Badezimmer/c)
                    container[5].append(av_Elektrik/c)
                    container[6].append(av_Carport/c)
                    c = 1
                    step_time = step_time - average_range
                    time_stamp = 0

    csv_file.close()
    return container

# demo calls
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/temp/temp2018.csv', 'Temperature')
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/humidity/humidity2018.csv', 'Humidity')
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/dewpoint/dewpoint2018.csv', 'Dewpoint')
