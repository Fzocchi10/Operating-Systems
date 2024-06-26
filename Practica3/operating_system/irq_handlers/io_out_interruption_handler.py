from hardware.hardware import HARDWARE
from hardware.irq import IRQ

from operating_system.irq_handlers.abstract_interruption_handler import AbstractInterruptionHandler

class IoOutInterruptionHandler(AbstractInterruptionHandler):

    def execute(self, irq):
        """
        The current process has requested the use of IO.
        We need to put it in WAITING state and set next process to RUNNING.
        """
        # The device that was requested for use
        device_id = irq.arguments[0]
        # TODO: (4)
        # The first step is to retrieve the process id of the process that
        # was currently using the device. We can achieve this trough the
        # io controller of the device.
        pid = self.kernel.io_contollers_vector.get_by_id(device_id).active_pid()
        # The request for the device has finished. So we need to inform
        # the corresponding controller for that device, so the process
        # can be removed from te queue, and the next process in the
        # queue, if any, sends the request to the device.
        self.kernel.io_contollers_vector.get_by_id(device_id).finish()
        # Now we need to inform the scheduler that the process
        # that was using the device is no longer waiting, but
        # instead, it's ready.
        self.kernel.scheduler.move_to_ready(pid)
        # As there may happen that the CPU was idle, and now there is one
        # in the ready queue, it may happen that it also needs to be run,
        # the last step is to tell the scheduler to run the next process
        # in the ready queue, if any.
        if (self.kernel.scheduler.currently_running_pid is None):
            next_pid = self.kernel.scheduler.next_process
            if(next_pid is not None):
             self.kernel.scheduler.move_to_running(pid)
