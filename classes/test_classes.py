
from LiveUpdater import LiveUpdater
from PhilipsLights import PhilipsLights
from Script import Script
import time


def main():
    print("Starting test program")
    updater = LiveUpdater()
    # updater.all_on()

    updater.get_phil_lights().output_light_info()
    # updater.get_phil_lights().set_blue()

    # time.sleep(3)

    print("DEBUGGING")
    script = []
    script.append({'start_loop':1})
    script.append({ \
    # hue 0 = red
    # hue 20000 = green
    "Cris Bedroom 1":{'hue':0, 'sat':254, 'bri':254, 'transitiontime':100}, \
    "Cris Bedroom 2":{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':12} \
    })
    script.append({"Cris Bedroom 1":{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':50}})
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
    script.append({"Cris Bedroom 1":{'hue':0, 'sat':254, 'bri':254, 'transitiontime':35}})
    # hue 35000 = light blue
    script.append({"Cris Bedroom 1":{'hue':35000, 'sat':254, 'bri':254, 'transitiontime':30}})
    script.append({'end_loop':0})

    my_script_obj = Script(script, "Test_Script")
    temp = Script(None, "replacement")
    temp.load_from_json(my_script_obj.json_format())

    updater.run_script(temp.steps)
    # updater.run_script(temp.steps)

main()
