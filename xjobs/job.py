
class Job():
    
    # init method or constructor 
    def __init__(self, name, command, started_condition, 
                completed_condition, ready_condition,
               success_condition):
        self.name = name
        self.command = command
        self.ready_condition = ready_condition
        self.success_condition = success_condition
        self.started_condition = started_condition
        self.completed_condition = completed_condition
        self.id = None
        self.state = 'Not launched'

    def get_state(self):
        return {'started'   :self.is_started(),
                'ready'     :self.is_ready(),
                'completed' :self.is_completed(),
                'successful':self.is_successful(),
                 }

    #def to_dict(self):
    #    return {'name': self.name, 
    #            'command': self.command, 
    #            'ready_to_launch': self.ready_to_launch,
    #            'success_condition': self.success_condition, 
    #            'id': self.id,
    #            'state':  self.state}
    
    def is_started(self):
        if self.started_condition[0](**self.started_condition[1]):
            return True
        else:
            return False

    def is_ready(self):
        if self.ready_condition[0](**self.ready_condition[1]):
            return True
        else:
            return False

    def is_completed(self):
        if self.completed_condition[0](**self.completed_condition[1]):
            return True
        else:
            return False

    def is_successful(self):
        if self.success_condition[0](**self.success_condition[1]):
            return True
        else:
            return False