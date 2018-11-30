
import commands
import floorplan



def my_chat_command(bot, chat_id, command, home_dir, work_dir):

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
