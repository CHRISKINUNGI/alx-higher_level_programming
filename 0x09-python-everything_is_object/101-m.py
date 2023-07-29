#!/usr/bin/python3
""" first module """



class LockedClass:
    """ class LockedClass """
    
    def __setattr__(self, name, value):
    """ __setattr__ function 
        
        args:
            self
            name
            value
        raise:
            AttributeError
    """
        if not hasattr(self, name) and name != "first_name":
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
        super().__setattr__(name, value)
