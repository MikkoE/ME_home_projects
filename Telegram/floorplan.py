import datetime
from PIL import Image, ImageDraw, ImageFont

color_cold = (0,0,255)
color_warm = (255, 211, 0)
color_hot = (255,0,0)

offset = [(),]

def color_chooser(temp):
    if float(temp) < 18:
        return color_cold
    elif float(temp) > 18 and float(temp) < 24.1:
        return color_warm
    else:
        return color_hot

def createFloorPlan(bot, chat_id, datafile, outfile):
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

    draw.text(xy=(260,650), text=t[1], fill=color_chooser(t[1]),font=font_type) #Veranda
    draw.text(xy=(600,600), text=t[2], fill=color_chooser(t[2]),font=font_type) #Wohnzimmer
    draw.text(xy=(730,50), text=t[3], fill=color_chooser(t[3]),font=font_type) #Schlafzimmer
    draw.text(xy=(750,420), text=t[4], fill=color_chooser(t[4]),font=font_type) #Badezimmer
    draw.text(xy=(350,400), text=t[5], fill=color_chooser(t[5]),font=font_type) #Elektrik
    draw.text(xy=(100,130), text=t[6], fill=color_chooser(t[6]),font=font_type) #Carport




    fp.save(outfile)
