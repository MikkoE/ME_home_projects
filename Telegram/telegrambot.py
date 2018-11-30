#coder :- Mikko Eberhardt

import sys
import csv
import time
import telepot

import my_chat



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    csv_reader = csv.reader(open("/home/pi/env/env.csv", "r"), delimiter=";")
    for row in csv_reader:
        if row[0] is not None:
            x = row[0]
            if x == "home_dir":
                home_dir = row[1]
            elif x == "work_dir":
                work_dir = row[1]
            elif x == "my_chatID":
                my_chatID = row[1]
            elif x == "edgar_chatID":
                edgar_chatID = row[1]

    # calculate user access
    #print "using message chat id: "
    #print chat_id

    if edgar_chatID == str(chat_id):
        bot.sendMessage(chat_id, text="Nice try Edgar!\n Stop cheating on me :smiley:")

    # using my chatID to verify ist me chatting with the bot
    if my_chatID == str(chat_id):
        #print "youre allowed to chat"
        bot.sendMessage(chat_id, text='Hey Mikko, hope youre doing great!')

        # Debug ausgabe der Commands
        ##print('Got command: %s' % command)

        my_chat.my_chat_command(bot, chat_id, command, home_dir, work_dir)

    if str(chat_id) != edgar_chatID and str(chat_id) != my_chatID:
        bot.sendMessage(chat_id, text="Hey Stranger,\nthis information is propably not for your eyes! :smiley:")



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
