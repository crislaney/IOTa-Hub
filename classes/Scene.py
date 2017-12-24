class Step():
    def __init__(self):
        self.step_dict = {}

    def __init__(self, step_dict):
        self.step_dict = step_dict

    def get_step(self):
        return self.step_dict

    def set_step(self, step_dict):
        self.step_dict = step_dict
