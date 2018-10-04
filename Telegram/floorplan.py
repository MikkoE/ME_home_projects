from PIL import Image, ImageDraw, ImageFont

color_cold = (0,0,255)
color_warm = (255, 211, 0)
color_hot = (255,0,0)

offset = [(),]

def color_chooser(temp):
    if temp > 24:
        return color_hot
    elif temp > 18 and temp < 24.1:
        return color_warm
    else
        return color_cold

def createFlooPlan(bot, chat_id, datafile):
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

    draw.text(xy=(500,1200), text=t[1], fill=color_chooser(t[1]),font=font_type)
    draw.text(xy=(1100,1000), text=t[2], fill=color_chooser(t[2]),font=font_type)
    draw.text(xy=(1100,100), text=t[3], fill=color_chooser(t[3]),font=font_type)
    draw.text(xy=(1100,700), text=t[4], fill=color_chooser(t[4]),font=font_type)
    draw.text(xy=(600,800), text=t[5], fill=color_chooser(t[5]),font=font_type)
    draw.text(xy=(200,200), text=t[6], fill=color_chooser(t[6]),font=font_type)




    fp.save('out.png')
