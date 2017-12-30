from abc import ABC, abstractmethod

class IOTObject(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    @abstractmethod
    def get_step(self):
        pass

    @abstractmethod
    def set_step(self, state):
        pass
