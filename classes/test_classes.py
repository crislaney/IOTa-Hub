
from LiveUpdater import LiveUpdater
from PhilipsLights import PhilipsLights
from Script import Script
import time


def main():
    print("Starting test program")
    updater = LiveUpdater()
    updater.all_on()

    updater.get_phil_lights().output_light_info()
    updater.get_phil_lights().set_blue()

    time.sleep(3)

    print("DEBUGGING")
    script = []
    script.append({'start_loop':1})
    script.append({ \
    # hue 0 = red
    # hue 20000 = green
    11:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':100}, \
    12:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':12} \
    })
    script.append({11:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':50}})
    script.append({'start_loop':3})
    # pulse green lights on both bulbs
    script.append({ \
    11:{'hue':20000, 'sat':254, 'bri':50, 'transitiontime':10}, \
    12:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':10} \
    })
    script.append({ \
    11:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':10}, \
    12:{'hue':20000, 'sat':254, 'bri':50, 'transitiontime':10} \
    })
    script.append({'end_loop':0})
    script.append({11:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':35}})
    # hue 35000 = light blue
    script.append({11:{'hue':35000, 'sat':254, 'bri':254, 'transitiontime':30}})
    script.append({'end_loop':0})

    my_script_obj = Script(script, "Test_Script")

    updater.run_script(my_script_obj.steps)

main()
