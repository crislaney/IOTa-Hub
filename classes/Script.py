
class Script():
    def __init__(self):
        # this is a list of dictionaries representing steps
        self._steps = []
        # name of the script in the databse and on front end
        # name must be unique
        self._name = ""


    def __init__(self, steps):
        self._steps = steps


    def __init__(self, steps, name):
        self._steps = steps
        self._name = name

    @property
    def steps(self):
        return self._steps


    @steps.setter
    def steps(self, value):
        # good place to run the validator
        self._steps = value


    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # check db for existing name
        self.name = value
