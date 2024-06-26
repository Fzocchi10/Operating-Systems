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
<<<<<<< HEAD:Practica4/codigo/operating_system/scheduling/non_preemptive/sjf_scheduler.py
        next_pcb = self.__priority_queue.front
        if (next_pcb == None):
            return None
        else:
            return next_pcb.pid
=======
        self.__priority_queue.front
>>>>>>> 168618576eca33d7c0fff2a434526d62fd78b225:Practica 4/codigo/operating_system/scheduling/non_preemptive/sjf_scheduler.py
       
    def move_to_ready(self,pid, pcb):
        """ Move a process with the given pid and matching pcb to the ready state. """
<<<<<<< HEAD:Practica4/codigo/operating_system/scheduling/non_preemptive/sjf_scheduler.py
        priority = - pcb.burst_time
        self.__priority_queue.enqueue(pcb,priority)

    def move_to_running(self, pid, pcb):
        """ Move a process with the given pid and matching pcb to the running state. """
        self.__priority_queue.dequeue()
=======
        priority = pcb.__burst_time
        self.__priority_queue.enqueue(pid,priority)

    def move_to_running(self, pid, pcb):
        """ Move a process with the given pid and matching pcb to the running state. """
        self.__priority_queue.pop()
>>>>>>> 168618576eca33d7c0fff2a434526d62fd78b225:Practica 4/codigo/operating_system/scheduling/non_preemptive/sjf_scheduler.py
    
    def move_to_waiting(self, pid, pcb):
        """ Move a process with the given pid and matching pcb to the waiting state. """
        
    
    def __repr__(self):
        # The repr should return the processes ready in their corresponding order.
        return str(self.__priority_queue)
    
