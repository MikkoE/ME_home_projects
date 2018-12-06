import datetime
import time
import os
import os.path

#user imports
import matplot as mp

plot_msg = 'I\'m plotting, wait a moment pls'
day_title = '\nlast 24h'
week_title = '\nlast 7 days'
month_title = '\nlast 30 days'

day_range = 24*60*60
week_range = day_range*7
month_range = day_range*30

##################################################
#   Handle Temperature Commands
##################################################
#status temp
def temp(bot, chat_id, datafile):
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        temperature = lines[-1]

    t = temperature.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)
    out = "Temperaturen\nUhrzeit: " + time_str + "\n" + \
            "Veranda: " + t[1] + "\n" + \
            "Wohnzimmer: " + t[2] + "\n" + \
            "Schlafzimmer: " + t[3] + "\n" + \
            "Badezimmer: " + t[4] + "\n" + \
            "Elektrik: " + t[5] + "\n" + \
            "Carport: " + t[6] + "\n"

    bot.sendMessage(chat_id, text=out)

# plot teperature 24 h
def plot_temp_day(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title

    mp.plotGraph(day_range, time.time(), datafile, 'Temperature' + day_title, 'temp', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))

# plot teperature 1 week
def plot_temp_week(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title

    mp.plotGraph(week_range, time.time(), datafile, 'Temperature' + day_title, 'temp', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))

# plot teperature 1 week
def plot_temp_month(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title

    mp.plotGraph(month_range, time.time(), datafile, 'Temperature' + day_title, 'temp', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))



##################################################
#   Handle Humidity Commands
##################################################
def humi(bot, chat_id, datafile):
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        values = lines[-1]

    t = values.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)
    out = "Luftfeuchtigkeit\nUhrzeit: " + time_str + "\n" + \
            "Veranda: " + t[1] + " %\n" + \
            "Wohnzimmer: " + t[2] + " %\n" + \
            "Schlafzimmer: " + t[3] + " %\n" + \
            "Badezimmer: " + t[4] + " %\n" + \
            "Elektrik: " + t[5] + " %\n" + \
            "Carport: " + t[6] + " %\n"

    bot.sendMessage(chat_id, text=out)

# plot humidity 24 h
def plot_humi(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(day_range, time.time(), datafile, 'Humidity' + day_title, 'humi', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))

##################################################
#   Handle Dewpoint Commands
##################################################
def dewpoint(bot, chat_id, datafile):
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        values = lines[-1]

    t = values.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)
    out = "Dewpoint\nUhrzeit: " + time_str + "\n" + \
            "Veranda: " + t[1] + "\n" + \
            "Wohnzimmer: " + t[2] + "\n" + \
            "Schlafzimmer: " + t[3] + "\n" + \
            "Badezimmer: " + t[4] + "\n" + \
            "Elektrik: " + t[5] + "\n" + \
            "Carport: " + t[6] + "\n"

    bot.sendMessage(chat_id, text=out)

# plot humidity 24 h
def plot_dewpoint(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(day_range, time.time(), datafile, 'Dewpoit' + day_title, 'dewpoint', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))


##################################################
#   Handle System Voltage Commands
##################################################
def systemv(bot, chat_id, datafile):
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        values = lines[-1]

    t = values.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)
    out = "System Voltage\nUhrzeit: " + time_str + "\n" + \
            "Veranda: " + t[1] + " V\n" + \
            "Wohnzimmer: " + t[2] + " V\n" + \
            "Schlafzimmer: " + t[3] + " V\n" + \
            "Badezimmer: " + t[4] + " V\n" + \
            "Elektrik: " + t[5] + " V\n" + \
            "Carport: " + t[6] + " V\n"

    bot.sendMessage(chat_id, text=out)

# plot humidity 24 h
def plot_systemv(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(day_range, time.time(), datafile, 'System Voltage + day_title', 'voltage', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))

##################################################
#   Handle WLAN Signal commands
##################################################
def wlan(bot, chat_id, datafile):
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        values = lines[-1]

    t = values.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)
    out = "WLAN Signal\nUhrzeit: " + time_str + "\n" + \
            "Veranda: " + t[1] + " dBm\n" + \
            "Wohnzimmer: " + t[2] + " dBm\n" + \
            "Schlafzimmer: " + t[3] + " dBm\n" + \
            "Badezimmer: " + t[4] + " dBm\n" + \
            "Elektrik: " + t[5] + " dBm\n" + \
            "Carport: " + t[6] + " dBm\n"

    bot.sendMessage(chat_id, text=out)

# plot humidity 24 h
def plot_wlan(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text=plot_msg)
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(day_range, time.time(), datafile, 'WLAN Signal' + day_title, 'WLAN Signal', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))
