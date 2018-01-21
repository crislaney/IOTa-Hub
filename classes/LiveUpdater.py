import sys
import time
import os.path
import random
from PhilipsLights import PhilipsLights

class LiveUpdater():
    def __init__(self):
        self.phil_lights = PhilipsLights()
        self._stop_script = False


    @property
    def stop_script(self):
        return self._stop_script

    @stop_script.setter
    def stop_script(self, value):
        self._stop_script = value


    def load_script(self):
        return


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
        self.interpret_script(script, 0, -1, -1, -1)


    # need to figure out a way to break infinite loop
    def interpret_script(self, script, step_num, start_loop, end_loop, cond):
        if cond == 'inf':
            cond = float('inf')
        while step_num < len(script):
            print("Step: ", step_num)
            if self._stop_script == True:
                return 0

            elif 'start_loop' in script[step_num]:
                if step_num != start_loop:
                    if script[step_num]['start_loop'] == 'inf':
                        script[step_num]['start_loop'] == float('inf')

                    step_num = self.interpret_script(script, step_num, \
                    step_num, -1, script[step_num]['start_loop']) + 1

                elif cond < 0:
                    print(cond)
                    # this should probs be an error case???
                    return end_loop
                elif cond == 0:
                    return end_loop
                else:
                    cond -= 1
                    step_num += 1
            elif 'end_loop' in script[step_num]:
                end_loop = step_num
                step_num = start_loop
            else:
                self.run_step(script[step_num])
                step_num += 1

    def get_phil_lights(self):
        return self.phil_lights
