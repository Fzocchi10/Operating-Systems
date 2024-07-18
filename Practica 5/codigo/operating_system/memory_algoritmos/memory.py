from utilities.queue import Queue
from hardware.hardware import HARDWARE

class Memory:

    def __init__(self, kernel):
        self.__kernel = kernel
        self.__huecos = Queue()


   
    @property
    def kernel(self):
        return self.__kernel 


    @property
    def todosLosHuecos(self):
        return self.__huecos
    
    @property
    def hardware(self):
        return HARDWARE