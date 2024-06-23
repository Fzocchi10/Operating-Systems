from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm

class SJFSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    """ Implementation of Shortest Job First Scheduling Algorithm. """

    # TODO (2) Complete the class
    def __init__(self, kernel, quantum):
        super().__init__(kernel,quantum)
        self.__priority_queue = PriorityQueue()
        
    @property
    def next_process_id(self):
        """ Returns the next process ID to execute. """
        self.__priority_queue.front
       
    def move_to_ready(self,pid, pcb):
        """ Move a process with the given pid and matching pcb to the ready state. """
        priority = pcb.__burst_time
        self.__priority_queue.enqueue(pid,priority)

    def move_to_running(self, pid, pcb):
        """ Move a process with the given pid and matching pcb to the running state. """
        self.__priority_queue.pop()
    
    def move_to_waiting(self, pid, pcb):
        """ Move a process with the given pid and matching pcb to the waiting state. """
        
    
    def __repr__(self):
        # The repr should return the processes ready in their corresponding order.
        return str(self.__priority_queue)