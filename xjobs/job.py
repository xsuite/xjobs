
class Job():
    
    # init method or constructor 
    def __init__(self, name, command, started_condition, 
                completed_condition, ready_to_launch=True,
               success_condition=True):
        self.name = name
        self.command = command
        self.ready_to_launch = ready_to_launch
        self.success_condition = success_condition
        self.started_condition = started_condition
        self.completed_condition = completed_condition
        self.id = None
        self.state = 'Not launched'

    def get_state(self):
        return self.state

    #def to_dict(self):
    #    return {'name': self.name, 
    #            'command': self.command, 
    #            'ready_to_launch': self.ready_to_launch,
    #            'success_condition': self.success_condition, 
    #            'id': self.id,
    #            'state':  self.state}
    
    def started(self):
        if self.started_condition[0](**self.started_condition[1]):
            return True
        else:
            return False