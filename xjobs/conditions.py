import os

class Condition():
    def is_verified():
        pass

class ConditionFileExists(Condition):
    def __init__(self, path):
        self.path = path
    
    def is_verified(self):
        return os.path.isfile(self.path)

class ConditionFileContains(Condition):
    def __init__(self, path, content):
        self.path = path
        self.content = content
    
    def is_verified(self):
        if ConditionFileExists(self.path).is_verified():
            with open(self.path) as f:
                if self.content in f.read():
                    return True
        return False

