class Myclass(object):
    class_attr = "je suis la chaine officielle de cette class"
     
    def __init__(self, instanceVariable):
        print('in the constructor')	
        self.instanceVariable = instanceVariable

    
    def __setattr__(self, name, newVal):

        print('DEBUG: ', name, newVal)
        if isinstance(newVal, str):
            self.__dict__[name] = newVal
            print('instanceVariable has been updated')
        else:
            print('Wrong time, instanceVariable is left unchanged')
    
    @staticmethod
    def static_method():
        print("""
        in static_method, 
        this one have access to nothing 
        but is still inside the class namespace
        """)

    @classmethod
    def class_method(cls):
        print("""
        in class_method, 
        this one have access to the class object
        """)
        print(cls.class_attr)

    def instance_method(self):
        print("""
        in instance_method,
        this one has access to the intance reference
        """)
        print(self.instanceVariable)

