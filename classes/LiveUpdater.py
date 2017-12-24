import sys
from phue import Bridge
import time
import os.path
import random

class LiveUpdater():
    def __init__(self):
        #press button
        # need to do a check here to see if already connected
        config_file_path = "./.python_hue"
        need_to_connect = False
        if not os.path.isfile(config_file_path):
            print("Press button... You have 5 seconds...")
            time.sleep(5)

        self.bridge = Bridge('192.168.0.104', None, config_file_path)
        self.lights = self.bridge.get_light_objects()

    def all_off(self):
        for light in self.lights:
            self.bridge.set_light(light.light_id, 'on', False)

    def all_on(self):
        for light in self.lights:
            self.bridge.set_light(light.light_id, 'on', True)

    def create_step(self, step_time=0, lights=None):
        lights_in_step = {}

        all_lights = []
        # if light id list is specified, grab all light objects in that list
        if lights is not None:
            all_lights = [self.bridge.get_light_objects('id')[x] for x in lights]
        # otherwise grab all lights
        else:
            all_lights = self.bridge.get_light_objects()

        # build dict for each light in step
        for light in all_lights:
            if light.transitiontime is None:
                light.transitiontime = 0
            lights_in_step[light.light_id] = \
                {'hue':light.hue, 'sat':light.saturation, \
                 'bri':light.brightness, 'transitiontime':step_time}

        return lights_in_step


    # step is a dictionary of the form
    # {'hue':int, 'sat':int, 'bri':lint, 'transitiontime':int}
    def run_step(self, step):
        for key, value in step.items():
            self.bridge.set_light(key, value, transitiontime=step[key]['transitiontime'] )
            time.sleep(step[key]['transitiontime']/10)

    def run_script(self, script):
        i = 0
        for step in script:
            print(step[4]['hue'])
            self.run_step(step)
        return
    # Debug stuff

    def DEFCON(self):
        '''
        temp_lights = self.bridge.get_light_objects('id')
        temp_lights[1].hue = 0
        for light in self.lights:
            temp_lights[light.light_id].hue = 0
        '''
        self.set_red()

        for i in range(10):
            for light in self.lights:
                self.bridge.set_light(light.light_id, 'bri', value=254, transitiontime=10)
            time.sleep(1)
            for light in self.lights:
                self.bridge.set_light(light.light_id, 'bri', value=50, transitiontime=10)
            time.sleep(1)

    def set_red(self):
        for light in self.lights:
            light.brightness = 254
            light.saturation = 254
            light.hue = 0

    def set_blue(self):
        for light in self.lights:
            light.brightness = 254
            light.saturation = 254
            light.hue = 46920

    def party_mode(self):
        self.set_red()
        for i in range(1000):
            for light in self.lights:
                #self.bridge.set_light(light.light_id, 'bri', value=random.randrange(50, 254), transitiontime=0)
                self.bridge.set_light(light.light_id, 'hue', value=random.randrange(0, 60000), transitiontime=0)
            time.sleep(.01)

    def print_values(self):
        return self.lights[0]
