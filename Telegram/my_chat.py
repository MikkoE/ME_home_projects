import datetime
import commands
import floorplan



def my_chat_command(bot, chat_id, command, home_dir, work_dir):

    year = datetime.datetime.now().year

    temp_file = work_dir + 'temp/temp' + str(year) + '.csv'
    humi_file = work_dir + 'humidity/humidity' + str(year) + '.csv'


    #---------------------------------------------------------------------------
    # Temperature
    #---------------------------------------------------------------------------
    # print current temperature
    if command == "/status_temp":
        commands.temp(bot, chat_id, temp_file)
    # plot current temperature
    if command == "/graph_temp_day":
        commands.plot_temp_day(bot, chat_id, temp_file, home_dir + 'test_temperature.png')
    # plot current temperature
    if command == "/graph_temp_week":
        commands.plot_temp_week(bot, chat_id, temp_file, home_dir + 'test_temperature.png')
    # plot current temperature
    if command == "/graph_temp_month":
        commands.plot_temp_month(bot, chat_id, temp_file, home_dir + 'test_temperature.png')
    # print current temperature on a floorplan
    if command == "/floorplan_temp":
        floorplan.createFloorPlan(bot, chat_id, temp_file, home_dir + 'test_floorplan.png')

    #---------------------------------------------------------------------------
    # Humidity
    #---------------------------------------------------------------------------
    # print current humidity
    if command == "/status_humi":
        commands.humi(bot, chat_id, humi_file)

    # plot current humidity
    if command == "/graph_humi":
        commands.plot_humi(bot, chat_id, humi_file, home_dir + 'test_humidity.png')

    #---------------------------------------------------------------------------
    # Dewpoint
    #---------------------------------------------------------------------------
    # print current dewpoint
    if command == "/status_dewpoint":
        commands.dewpoint(bot, chat_id, work_dir + 'dewpoint/dewpoint' + str(year) + '.csv')

    # print current dewpoint
    if command == "/graph_dewpoint":
        commands.plot_dewpoint(bot, chat_id, work_dir + 'dewpoint/dewpoint' + str(year) + '.csv', home_dir + 'test_dewpoint.png')

    #---------------------------------------------------------------------------
    # System Voltage
    #---------------------------------------------------------------------------
    # print current system voltage
    if command == "/status_systemv":
        commands.systemv(bot, chat_id, work_dir + 'systemV/systemV' + str(year) + '.csv')

    # print current system voltage
    if command == "/graph_systemv":
        commands.plot_systemv(bot, chat_id, work_dir + 'systemV/systemV' + str(year) + '.csv', home_dir + 'test_systemv.png')

    #---------------------------------------------------------------------------
    # WLAN Signal
    #---------------------------------------------------------------------------
    # print system wlan signal
    if command == "/status_wlan":
        commands.wlan(bot, chat_id, work_dir + 'wlanSignal/wlanSignal' + str(year) + '.csv')

    if command == "/graph_wlan":
        commands.plot_wlan(bot, chat_id, work_dir + 'wlanSignal/wlanSignal' + str(year) + '.csv', home_dir + 'test_wlan.png')
