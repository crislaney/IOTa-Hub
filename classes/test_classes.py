
from LiveUpdater import LiveUpdater
from PhilipsLights import PhilipsLights
import time


def main():
    print("Starting test program")
    updater = LiveUpdater()
    updater.all_on()
    '''
    updater.all_off()
    updater.set_red()
    step1 = updater.create_step(5, [4])
    time.sleep(1)
    updater.set_blue()
    step2 = updater.create_step(5, [4])
    time.sleep(1)
    step1 = {1:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':5}}
    step2 = {1:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':5}}
    updater.run_step(step1)
    time.sleep(1)
    updater.run_step(step2)
    time.sleep(1)
    '''

    print("DEBUGGING")
    script = []
    script.append({'start_loop':3})
    script.append({11:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':50}})
    script.append({11:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':50}})
    script.append({'start_loop':3})
    script.append({11:{'hue':20000, 'sat':254, 'bri':50, 'transitiontime':10}})
    script.append({11:{'hue':20000, 'sat':254, 'bri':254, 'transitiontime':10}})
    script.append({'end_loop':0})
    script.append({11:{'hue':0, 'sat':254, 'bri':254, 'transitiontime':35}})
    script.append({11:{'hue':35000, 'sat':254, 'bri':254, 'transitiontime':30}})
    script.append({'end_loop':0})

    updater.run_script(script)

main()
