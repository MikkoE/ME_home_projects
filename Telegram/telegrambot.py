#coder :- Mikko Eberhardt

import sys
import csv
import time
import telepot

import commands
import floorplan



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    home_dir = '/home/pi/ME_home_projects/Telegram/'
    work_dir = '/home/pi/Weather/data/'

    csv_reader = csv.reader(open("/home/pi/env/env.csv", "r"), delimiter=";")
    for row in csv_reader:
        if row[0] == "my_chatID":
            my_chatID = row[1]

    #if my_chatID == chat_id:

    print chat_id

    # Debug ausgabe der Commands
    ##print('Got command: %s' % command)
    #---------------------------------------------------------------------------
    # Temperature
    #---------------------------------------------------------------------------
    # print current temperature
    if command == "/status_temp":
        commands.temp(bot, chat_id, work_dir + 'temp/temp2018.csv')
    # plot current temperature
    if command == "/graph_temp":
        commands.plot_temp(bot, chat_id, work_dir + 'temp/temp2018.csv', home_dir + 'test_temperature.png')
    # print current temperature on a floorplan
    if command == "/floorplan_temp":
        floorplan.createFloorPlan(bot, chat_id, work_dir + 'temp/temp2018.csv', home_dir + 'test_floorplan.png')

    #---------------------------------------------------------------------------
    # Humidity
    #---------------------------------------------------------------------------
    # print current humidity
    if command == "/status_humi":
        commands.humi(bot, chat_id, work_dir + 'humidity/humidity2018.csv')

    # plot current humidity
    if command == "/graph_humi":
        commands.plot_humi(bot, chat_id, work_dir + 'humidity/humidity2018.csv', home_dir + 'test_humidity.png')

    #---------------------------------------------------------------------------
    # Dewpoint
    #---------------------------------------------------------------------------
    # print current dewpoint
    if command == "/status_dewpoint":
        commands.dewpoint(bot, chat_id, work_dir + 'dewpoint/dewpoint2018.csv')

    # print current dewpoint
    if command == "/graph_dewpoint":
        commands.plot_dewpoint(bot, chat_id, work_dir + 'dewpoint/dewpoint2018.csv', home_dir + 'test_dewpoint.png')

    #---------------------------------------------------------------------------
    # System Voltage
    #---------------------------------------------------------------------------
    # print current system voltage
    if command == "/status_systemv":
        commands.systemv(bot, chat_id, work_dir + 'systemV/systemV2018.csv')

    # print current system voltage
    if command == "/graph_systemv":
        commands.plot_systemv(bot, chat_id, work_dir + 'systemV/systemV2018.csv', home_dir + 'test_systemv.png')

    #---------------------------------------------------------------------------
    # WLAN Signal
    #---------------------------------------------------------------------------
    # print system wlan signal
    if command == "/status_wlan":
        commands.wlan(bot, chat_id, work_dir + 'wlanSignal/wlanSignal2018.csv')

    if command == "/graph_wlan":
        commands.plot_wlan(bot, chat_id, work_dir + 'wlanSignal/wlanSignal2018.csv', home_dir + 'test_wlan.png')

#-------------------------------------------------------------------------------
# Main related code
#-------------------------------------------------------------------------------

#loading environment values
csv_reader = csv.reader(open("/home/pi/env/env.csv", "r"), delimiter=";")
for row in csv_reader:
    if row[0] == "bot-key":
        # bot privte key
        bot = telepot.Bot(row[1])
bot.message_loop(handle)
print('I am listening...')

while 1:
    try:
        time.sleep(10)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        exit()

    except:
        print('Other error or exception occured!')
