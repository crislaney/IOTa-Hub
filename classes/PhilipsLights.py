import sys
sys.path.append("..")
from .IOTObject import IOTObject
#from IOTObject import IOTObject
from phue import Bridge
import time
import os
import random
import rgbxy
from rgbxy import Converter
from rgbxy import get_light_gamut
import http.client
import json
import time


class PhilipsLights(IOTObject):
    def __init__(self):
        #press button
        # need to do a check here to see if already connected
        debug_config_file = "/home/cris/Projects/IOTa-Hub/classes/.python_hue"
        prod_config_file = "./.python_hue"

        correct_path = debug_config_file
        current_dir = os.getcwd()

        need_to_connect = False
        self.ip = None
        
        try:
            ip_json = http.client.HTTPSConnection('www.meethue.com', timeout=10)
            ip_json.request('GET', '/api/nupnp')
            ip_dict = json.loads(ip_json.getresponse().read())
            ip_dict[0]['internalipaddress']
        except Exception as e:
            print("Error occured Please restart setup")
            print(e)
            exit(1)

        if os.path.isfile(debug_config_file):
            print("Checking debug")
            correct_path = debug_config_file

        elif os.path.isfile(prod_config_file):
            print("Checking prod")
            correct_path = prod_config_file

        else:
            print("Press button... You have 5 seconds...")
            time.sleep(5)

        self.lights = []
        self.bridge = Bridge(self.ip, None, correct_path)
        self.lights = self.bridge.get_light_objects()
        self.converter = Converter()


    def turn_on(self):
        self.all_on()


    def turn_off(self):
        self.all_of()


    # returns a dict
    def get_step(self):
        return self.create_step()


    # takes a dict
    def set_step(self, step):
        self.run_step(step)


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
                model_id = self.bridge.get_light(light.light_id, parameter="modelid")

                lights_in_step[light.name] = \
                {'xy':light.xy, 'sat':light.saturation, \
                'bri':light.brightness, 'transitiontime':step_time, \
                'on':light.on, 'hue':light.hue}

        return lights_in_step


    def _convert_dict_to_xy(self, key, value):
        new_value = value
        model = self.bridge.get_light(key, parameter="modelid")
        converter = Converter(get_light_gamut(model))
        new_value['xy'] = converter.rgb_to_xy(value['rgb'][0], \
        value['rgb'][1], value['rgb'][2])
        new_value.pop('rgb', None)
        return new_value


    # step is a dictionary of the form
    # {'hue':int, 'sat':int, 'bri':lint, 'transitiontime':int}
    def run_step(self, step):
        # take the bigger value between 1/10 (max request per second) and
        # the longest transitiontime in the step
        max_trans_time = .1
        max_step_time = int(step[max(step.keys(), key=lambda k:step[k]['transitiontime'])]['transitiontime'])

        if max_step_time > max_trans_time:
            max_trans_time = max_step_time

        for key, value in step.items():
            '''
            if 'is_on' in value:
                step[key]['on'] = step[key]['is_on']
                step[key].pop('is_on')
            '''

            if key == "Cris Bedroom 1" or key == "Cris Bedroom 2":
                print(value)

            if 'xy' in step[key]:
                step[key].pop('xy')
            value['hue'] = int(value['hue'])
            value['bri'] = int(value['bri'])
            value['sat'] = int(value['sat'])

            try:
                self.bridge.set_light(key, value, transitiontime=max_trans_time)
            except Exception as e:
                print("Error: " + str(e))


        time.sleep(max_trans_time/10)
        print("Done Sleeping")


    def run_script(self, script):
        i = 0
        for step in converted_dict:
            self.run_step(step)
        return


    # Debug stuff
    def output_light_info(self):
        for light in self.lights:
            print("name: {} \nID: {} \nType: {}\n\n".format(light.name, \
            light.light_id, light.modelid))

    def DEFCON(self):
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
            self.bridge.set_light(light.light_id, 'hue', value=0, \
            transitiontime=0)
            self.bridge.set_light(light.light_id, 'bri', value=254, \
            transitiontime=0)


    def set_blue(self):
        for light in self.lights:
            self.bridge.set_light(light.light_id, 'hue', value=46920, \
            transitiontime=0)
            self.bridge.set_light(light.light_id, 'bri', value=254, \
            transitiontime=0)


    def party_mode(self):
        self.set_red()
        for i in range(1000):
            for light in self.lights:
                #self.bridge.set_light(light.light_id, 'bri', value=random.randrange(50, 254), transitiontime=0)
                self.bridge.set_light(light.light_id, 'hue', value=random.randrange(0, 60000), transitiontime=0)
                time.sleep(.01)


    def print_values(self):
        return self.lights[0]
