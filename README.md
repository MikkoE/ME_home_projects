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
TODO
#### CRON Job
TODO

## Sensor Daten Kollektor

TODO

## NodeMCU Sensoren

TODO
