
from xjobs import JobIdLocal

class Job():
    
    # init method or constructor 
    def __init__(self, name, command, ready_condition=None,
               success_condition=None):
        self.name = name
        self.command = command
        self.ready_condition = ready_condition
        self.success_condition = success_condition
        #self.started_condition = started_condition
        #self.completed_condition = completed_condition
        self.id = JobIdLocal()

    def get_states(self):
        return {'ready'     :self.is_ready(),
                'started'   :self.is_started(),
                'completed' :self.is_done(),
                'successful':self.is_successful(),
                 }

    #def to_dict(self):
    #    return {'name': self.name, 
    #            'command': self.command, 
    #            'ready_to_launch': self.ready_to_launch,
    #            'success_condition': self.success_condition, 
    #            'id': self.id,
    #            'state':  self.state}

    def is_running(self):
        return self.id.is_running()
    
    def is_started(self):
        return self.id.is_started()

    def is_done(self):
        return self.id.is_done()

    def is_ready(self):
        if self.ready_condition is None:
            return None
        return self.ready_condition.is_verified()

    def is_successful(self):
        if self.is_done():
            if self.ready_condition is None:
                return None
            return self.success_condition.is_verified()
        return False

    def kill(self):
        if self.is_running():
            self.id.kill()

    def __repr__(self):
        return self.name