
import psutil 

# use base_classes.py
class JobId():
    pass

class JobIdLocal(JobId):

    def __init__(self):
        self.pid = None
        self.start_time = None
        self.process = None
    
    def __eq__(self, other):
        return self.pid == other.pid and self.start_time == other.start_time

    def is_started(self):
        return not(self.pid is None)

    def is_running(self):
        if not self.is_started():
            return False

        assert self.pid is not None
        assert self.start_time is not None
        
        if not (psutil.pid_exists(self.pid)):
            return False
        
        if (psutil.Process(self.pid).status()=='zombie'):
            self.process.wait()
            return False
        else:
            return True

    def is_done(self):
        # if it is started and not running
        # the is completed
        if not self.is_started():
            return False
        else:
            if not(self.is_running()):
                return True
            else:
                return False
