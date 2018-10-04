import datetime
from PIL import Image, ImageDraw, ImageFont

color_cold = (0,0,255)     # blue
color_warm = (253, 106, 2) # orange
color_hot = (255,0,0)      # red

# offset values for the playement in floorplan
offset = [(260,650), (600,600), (730,50), (750,420), (350,400), (100,130)]

def color_chooser(temp):
    if float(temp) < 18:
        return color_cold
    elif float(temp) > 18 and float(temp) < 24.1:
        return color_warm
    else:
        return color_hot

def createFloorPlan(bot, chat_id, datafile, outfile):
    bot.sendMessage(chat_id, text='okay i\'m doing stuff wait a sec')
    #floorplan
    fp = Image.open('/home/pi/env/floorplan.png')
    fp_w, fp_h = fp.size
    #print(fp_w, fp_h)

    # Load font type forthe text
    font_type = ImageFont.truetype('/home/pi/env/arial bold.TTF', 18)

    draw = ImageDraw.Draw(fp)

    # data
    a=open(datafile,'r')
    lines = a.readlines()
    if lines:
        temperature = lines[-1]

    t = temperature.split(';')
    value = datetime.datetime.fromtimestamp((int(t[0])/1000))
    time_str = unicode(value)

    draw.text(xy=offset[0], text=t[1], fill=color_chooser(t[1]),font=font_type) #Veranda
    draw.text(xy=offset[0], text=t[2], fill=color_chooser(t[2]),font=font_type) #Wohnzimmer
    draw.text(xy=offset[0], text=t[3], fill=color_chooser(t[3]),font=font_type) #Schlafzimmer
    draw.text(xy=offset[0], text=t[4], fill=color_chooser(t[4]),font=font_type) #Badezimmer
    draw.text(xy=offset[0], text=t[5], fill=color_chooser(t[5]),font=font_type) #Elektrik
    draw.text(xy=offset[0], text=t[6], fill=color_chooser(t[6]),font=font_type) #Carport

    fp.save(outfile)

    bot.sendPhoto(chat_id, photo=open(outfile, 'rb'))
