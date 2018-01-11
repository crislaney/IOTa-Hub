
from LiveUpdater import LiveUpdater
from PhilipsLights import PhilipsLights
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
    script.append({'start_loop':3})
    script.append({ \
    11:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':100}, \
    12:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':12} \
    })
    script.append({11:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':50}})
    script.append({'start_loop':3})
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
    script.append({11:{'hue':35000, 'sat':254, 'bri':254, 'transitiontime':30}})
    script.append({'end_loop':0})

    updater.run_script(script)

main()
