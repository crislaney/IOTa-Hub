import sys
from phue import Bridge
import time
import os.path
import random
from PhilipsLights import PhilipsLights

class LiveUpdater():
    def __init__(self):
        self.phil_lights = PhilipsLights()


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

    '''
    def interpret_script(self, script, step_num, start_for, end_loop, cond):
        if step_num >= len(script):
            return
        elif 'start_loop' in script[step_num]:
            if cond < 0:
                self.interpret_script(script, step_num+1, step_num, -1, \
                script[step_num]['start_loop'])
            elif cond > 0:
                self.interpret_script(script, step_num + 1, step_num, end_loop, \
                cond -1)
                step_num += 1
            elif cond == 0:
                return
                # self.interpret_script(script, end_loop + 1, -1, -1, -1)
        elif 'end_loop' in script[step_num]:
            self.interpret_script(script, start_for, start_for, step_num, cond)
        else:
            self.phil_lights.run_step(script[step_num])
            step_num += 1

        print(step_num)
        self.interpret_script(script, step_num, start_for, end_loop, cond)
    '''

    def interpret_script(self, script, step_num, start_loop, end_loop, cond):
        while step_num < len(script):
            if 'start_loop' in script[step_num]:
                print('found start_loop')
                if step_num != start_loop:
                    print('recursing')
                    self.interpret_script(self, script, step_num, step_num, \
                    -1, script[step_num]['start_loop'])
                if cond < 0:
                    print('error')
                    # this should probs be an error case???
                    return end_loop
                elif cond == 0:
                    print('returning from recursion')
                    return end_loop
                else:
                    print('iterating in recursive call')
                    cond -= 1
                    step_num += 1
            elif 'end_loop' in script[step_num]:
                print('found end_loop')
                end_loop = step_num
                step_num = start_loop
            else:
                print('executing step')
                # self.run_step(script[step_num])
                step_num += 1



    def get_phil_lights(self):
        return self.phil_lights

def interpret_script(script, step_num, start_loop, end_loop, cond):
    while step_num < len(script):
        if 'start_loop' in script[step_num]:
            print('found start_loop')
            if step_num != start_loop:
                print('recursing')
                step_num = interpret_script(script, step_num, step_num, \
                -1, script[step_num]['start_loop']) + 1
                print('result from recursion ', step_num)
            if cond < 0:
                print(cond)
                print('error')
                # this should probs be an error case???
                return end_loop
            elif cond == 0:
                print('returning from recursion')
                return end_loop
            else:
                print('iterating in recursive call')
                cond -= 1
                step_num += 1
        elif 'end_loop' in script[step_num]:
            print('found end_loop')
            end_loop = step_num
            step_num = start_loop
        else:
            print('executing step')
            # self.run_step(script[step_num])
            step_num += 1
