import csv
import datetime
import time
import matplotlib
matplotlib.use('Agg') # no use of display driver
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Funktion to plot data with
def plot(title, data, outFileName):
    plt.plot(data[0], data[1], label='Veranda', color='r')
    plt.plot(data[0], data[2], label='Wohnzimmer', color='b')
    plt.plot(data[0], data[3], label='Schlafzimmer', color='y')
    plt.plot(data[0], data[4], label='Badezimmer', color='g')
    plt.plot(data[0], data[5], label='Elektrik', color='c')
    plt.plot(data[0], data[6], label='Carport', color='orange')

    plt.gcf().autofmt_xdate()

    plt.xlabel('time')
    plt.ylabel(title)
    plt.title(title +'\nlast 24h')
    plt.legend()

    plt.savefig(outFileName)
    plt.clf()

def plotGraph(range, timestamp, file_name, title, outFileName): #range for the time, file_name with data
    # Values to store
    timestamps = []
    Veranda = []
    Wohnzimmer = []
    Schlafzimmer = []
    Badezimmer = []
    Elektrik = []
    Carport = []
    container = [timestamps, Veranda, Wohnzimmer, Schlafzimmer, Badezimmer, Elektrik, Carport]
    print file_name

    # calculate time range
    last_date = timestamp - range
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

    # call the actally plotting function
    plot(title, container, outFileName)

# demo calls
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/temp/temp2018.csv', 'Temperature')
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/humidity/humidity2018.csv', 'Humidity')
#plotGraph(24*60*60, time.time(), '/home/pi/Weather/data/dewpoint/dewpoint2018.csv', 'Dewpoint')
