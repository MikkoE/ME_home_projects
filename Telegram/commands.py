import datetime
import time
import os
import os.path

#user imports
import matplot as mp

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
def plot_temp(bot, chat_id, datafile, outFileName):
    if os.path.isfile(outFileName):
        #print ('remove file ' + outFileName)
        os.remove(outFileName)
    bot.sendMessage(chat_id, text='okay i\'m plotting wait a sec')
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title

    mp.plotGraph(24*60*60, time.time(), datafile, 'Temperature', outFileName)
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
    bot.sendMessage(chat_id, text='okay i\'m plotting wait a sec')
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(24*60*60, time.time(), datafile, 'Humidity', outFileName)
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
    bot.sendMessage(chat_id, text='okay i\'m plotting wait a sec')
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(24*60*60, time.time(), datafile, 'Dewpoit', outFileName)
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
    bot.sendMessage(chat_id, text='okay i\'m plotting wait a sec')
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(24*60*60, time.time(), datafile, 'System Voltage', outFileName)
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
    bot.sendMessage(chat_id, text='okay i\'m plotting wait a sec')
    year = datetime.datetime.now().year
    # range(24*60*60), timestamp, filelocation as stream, title
    mp.plotGraph(24*60*60, time.time(), datafile, 'WLAN Signal', outFileName)
    bot.sendPhoto(chat_id, photo=open(outFileName, 'rb'))