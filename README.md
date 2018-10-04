# Bastelprojekte in und ums Haus

# Inhalt
* Mein Setup
* Telegram Bot
* Sensor Daten Kollektor
* NodeMCU Sensoren


## Mein aktuelles Setup besteht aus

#### Telegram bot
Der Telegram Bot läuft aktuell auf einem Raspberry Pi 2-B und hat folgende Befehle:
```shell
status_temp - Auflistung der Temperaturen
graph_temp - Graph der Temp
floorplan_temp - Zeigt Grundris mit Temperaturen
status_humi - Auflistung der Feuchtigkeitswerte
graph_humi - Graph der Feuchtigkeit
status_dewpoint - Auflistung der Kondensationspunkte
graph_dewpoint - Graph der Dewpoint
status_systemv - Auflistung der Systemversorgung
graph_systemv - Graph der System Voltage versorgung
status_wlan - Auflistung der WLAN-Signalstärken
graph_wlan - Graph der WLAN Signalstärke
```

#### Sensor Daten Kollektor
Der Daten Kollektor läuft ebenfalls auf dem Raspberry Pi 2-B und speichert mittels eines CRON jobs jede Minute die Daten der Sensoren weg. Aktuell sind ```6``` NodeMCU mit Sensoren im Einsatz für:

```shell
Veranda, Wohnzimmer, Schlafzimmer, Badezimmer, Elektrik, Carport
```

#### NodeMCU Sensoren
Als Sensoren verwende ich die NodeMCU die mit dem ESP8266 und einem WLAN chip super dafür geeignet sind. An den NodeMCU habe ich bei den meisten einen DHT22 bis auf an einem dort hängt noch ein DHT11. Dieser soll aber auch noch nachgerüstet werden, da die DHT11 keine Minusgrade vertragen bzw anzeigen können.

## Telegram Bot
#### Installation
Die installation gestaltet sich sehr einfach indem man mittels pip die packages installiert:
```shell
pip install relepot
pip install telepot --upgrade
```
Ein bisschen aufwendiger ist dann der [Telegram Bot Token](https://www.instructables.com/id/Set-up-Telegram-Bot-on-Raspberry-Pi/) und die Erstellung eines Bots indem man mit dem BotFather chattet. Danach sind aber alle Vorbedingungen erfüllt und der Bot sollte laufen.

#### Environment
Um sicher zu stellen, dass der Token für den Bot geheim bleibt liegt dieser in einem extra Verzeichnis ausserhalb des Repositories zusammen mit allen anderen persöhnlichen Daten wie auch unter anderen der Grundris.
Da mehrere Key benötigt werden wie der Bot Token, WLAN SSID und Passwort und so weiter liegen die daten alle bei mir in dem Environment Verzechnis in einer .csv Datei nach dem Key - Value Prinzip:
```shell
bot-key;TOKEN
```
Diese Werte können nun sehr einfach zB in Python mit einem csv reader eingelesen werden.

#### CRON Job
Der CRON job gestaltet hier sehr einfach da dieser lediglich beim reboot wieder den bot startet.
```shell
@reboot python <path/to/file/>telegrambot.py
```

## Sensor Daten Kollektor

TODO

## NodeMCU Sensoren

TODO
