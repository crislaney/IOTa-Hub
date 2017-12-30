import sys
from phue import Bridge
import time
import os.path
import random
from PhilipsLights import PhilipsLights

class LiveUpdater():
    def __init__(self):
        self.phil_lights = PhilipsLights()


    def all_on(self):
        self.phil_lights.all_on()

    def all_off(self):
        self.phil_lights.all_off()

    # need to somehow determine what objects will be activated here
    def create_step(self, step_time=0, obj_index=None):
        return self.phil_lights.create_step(step_time, obj_index)


    # step is a dictionary of the form
    # {'hue':int, 'sat':int, 'bri':lint, 'transitiontime':int}
    def run_step(self, step):
        self.phil_lights.run_step(step)


    def run_script(self, script):
        # interpretation here
        for step in script:
            self.phil_lights.run_step(step)

    def get_phil_lights(self):
        return self.phil_lights
