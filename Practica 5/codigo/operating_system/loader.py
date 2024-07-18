from hardware.hardware import HARDWARE
from operating_system.memory_algoritmos.first_fit import FirstFitAlgorithm
from operating_system.memory_algoritmos.best_fit import BestFitAlgorithm
from operating_system.memory_algoritmos.worst_fit import WorstFitAlgorithm

class Loader:
    """
    The loader is in charge of loading programs into memory.
    Later, the loader may use different, more complex
    allocation strategies. For now, we use a super simple strategy.
    The problem with this strategy is that, even if a program is
    unloaded, the freed memory cannot be used back, yikes.
    """

    def __init__(self, kernel,algoritmo):
        self.__kernel = kernel
        self.__next_free_memory_addr = 0
        self.__current_algorithm = algoritmo
        self.__available_memory_algorithms = {
            'FF' : FirstFitAlgorithm(kernel),
            'WF' : WorstFitAlgorithm(kernel),
            'BF' : BestFitAlgorithm(kernel),
        }
    

    def load(self, data):
        """
        Load a given program data into memory. Return the location
        where the first instruction was allocated.
        Fails if there is not enough free contiguous memory.
        """
        if not self.__has_free_memory(len(data)):
            raise RuntimeError("Not enough free memory.")

        memory_location = self.__next_free_memory_addr
        for i in range(0, len(data)):
            HARDWARE.memory.write(memory_location + i, data[i])
        self.__next_free_memory_addr += len(data)
        return memory_location

    def unload(self, pcb):
        """
        Remove a program that is loaded into memory from the memory.
        The PCB is received and used to know where the program is
        stored in memory.
        """
        for i in range(pcb.memory_start, pcb.memory_end):
            HARDWARE.memory.write(i, '')

    def __has_free_memory(self, size):
        """ Answer if there is enough free contiguous memory to store some data. """
        return self.__free_memory() >= size

    def __free_memory(self):
        """ Returns the amount of free contiguous memory. """
        return HARDWARE.memory.size - self.__next_free_memory_addr