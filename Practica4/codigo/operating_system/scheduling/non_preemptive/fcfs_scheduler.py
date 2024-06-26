from utilities.queue import Queue

from operating_system.scheduling.non_preemptive.non_preemptive_scheduler import NonPreemptiveSchedulerAlgorithm

class FCFSSchedulingAlgorithm(NonPreemptiveSchedulerAlgorithm):
    """ Implementation of First Come, First Served Scheduling Algorithm. """

    # TODO (1) Complete the class
    def __init__(self, kernel,quantum):
        super().__init__(kernel,quantum)
        self.__ready_queue = Queue()
    

    
    @property
    def next_process_id(self):
        return self.__ready_queue.front


    def move_to_ready(self, pid, pcb):
        """ Move a process with the given pid to the ready state. """
        self.__ready_queue.enqueue(pid)

    def move_to_running(self, pid,pcb):
        """ Move a process with the given pid to the running state. """
        self.__ready_queue.dequeue()
    

    def move_to_waiting(self, pid,pcb):
        """ Move a process with the given pid to the waiting state. """
        pass
        
    
    def __repr__(self):
        # The repr should return the processes ready in their corresponding order.
        return str(self.__ready_queue)