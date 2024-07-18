from utilities.queue import Queue

from hardware.irq import IRQ

from operating_system.pcb import *
from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class RRSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Round Robin Scheduling Algorithm. """

    # TODO (5) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel,quantum)
        
        self.__quantumDescount = quantum
        self.__ready_queue = Queue()
        


    @property
    def next_process_id(self):
        return self.__ready_queue.front

    
    def move_to_waiting(self, pid, pcb):
        pass


    def move_to_ready(self, pid, pcb):
        self.__ready_queue.enqueue(pid)


    def move_to_running(self, pid, pcb):
            if pcb.remaining_time > self.quantum:
                while self.__quantumDescount > 0:
                    self.__quantumDescount -= 1
                    return pcb.memory_start
                pcb.memory_start(self.quantum)
                pcb.recalculate_remaining_time
                self.__ready_queue.enqueue(pid)
            else:
                self.__ready_queue.dequeue()
                
    def __repr__(self):
        return str(self.__ready_queue)
                