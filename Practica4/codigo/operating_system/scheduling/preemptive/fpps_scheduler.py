from utilities.priority_queue import PriorityQueue

from operating_system.scheduling.preemptive.preemptive_scheduler import PreemptiveSchedulerAlgorithm

class FPPSSchedulingAlgorithm(PreemptiveSchedulerAlgorithm):
    """ Implementation of Fixed Priority Preemtive Scheduling Algorithm. """

    # TODO (4) Complete the class
    
    def __init__(self, kernel, quantum):
        super().__init__(kernel,quantum)
        self.__ready_queue = PriorityQueue()
        self.__currently_running = None


    @property
    def next_process_id(self):
      return self.__ready_queue.front


    def move_to_waiting(self, pid, pcb):
        self.__currently_running = None

    
    def move_to_ready(self, pid, pcb):
        self.__ready_queue.enqueue(pid, pcb.priority)

    
    def move_to_running(self, pid, pcb):
        self.__ready_queue.dequeue()

    
    def __repr__(self):
        return str(self.__ready_queue)
   