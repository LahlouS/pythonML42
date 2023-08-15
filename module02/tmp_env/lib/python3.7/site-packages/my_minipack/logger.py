import os
import time
from random import randint


def log(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        ret = func(*args, **kwargs)
        end_time = time.time() - start_time
        with open('./machine.log', 'a') as outfile:
            
            func_name = str(func.__name__).translate(str.maketrans("_", " ")).ljust(20, ' ')
            user_name = os.environ['USER']
            outfile.write(f'({user_name})Running: {func_name.title()}[ exec-time = {end_time} ms ]\n')
        return ret

    return wrapper    

class CoffeeMachine():
    water_level = 100
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
        return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")
