
from LiveUpdater import LiveUpdater
from PhilipsLights import PhilipsLights
from Script import Script
from DB_Manager import DB_Manager
import random
import time
import threading

def long_script():
    script = []
    script.append({'start_loop':1})
    script.append({ \
    # hue 0 = red
    # hue 20000 = green
    "Cris Bedroom 1":{'hue':0, 'sat':254, 'bri':254, 'transitiontime':100}, \
    "Cris Bedroom 2":{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':12} \
    })
    script.append({"Cris Bedroom 1":{'hue':20000, 'sat':254, 'bri':254, \
    'transitiontime':50}})
    script.append({'start_loop':3})
    # pulse green lights on both bulbs
    script.append({ \
    "Cris Bedroom 1":{'hue':20000, 'sat':254, 'bri':50, 'transitiontime':10}, \
    "Cris Bedroom 2":{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':10} \
    })
    script.append({ \
    "Cris Bedroom 1":{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':10}, \
    "Cris Bedroom 2":{'hue':20000, 'sat':254, 'bri':50, 'transitiontime':10} \
    })
    script.append({'end_loop':0})
    script.append({"Cris Bedroom 1":{'hue':0, 'sat':254, 'bri':254, \
    'transitiontime':35}})
    # hue 35000 = light blue
    script.append({"Cris Bedroom 1":{'hue':35000, 'sat':254, 'bri':254, \
    'transitiontime':30}})
    script.append({'end_loop':0})

    return Script(script, "DB Test Script 1")

def stop_inf(updater):
    print("stopper thread sleeping")
    time.sleep(10)
    print("stopper thread stopping")
    updater.stop_script = True


def main():
    db = DB_Manager()
    db.Insert_User("Cristoph", "pass")
    db.Get_User("Katie")
    # print(db.Get_All_Scripts("Katie"))
main()
