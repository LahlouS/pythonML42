
class GotCharacter:
    def __init__(self, firstname, is_alive = True):
        try:
            if firstname and isinstance(firstname, str):
                self.firstname = firstname
            else:
                raise AttributeError('ERROR: firstname must be a string')
            if isinstance(is_alive, bool):
                self.is_alive = is_alive
            else:
                raise AttributeError("ERROR: is_alive must be a boolean")
        except AttributeError as a:
            print(a, '\n', 'Exiting program. . .')

class Stark(GotCharacter):
    def __init__(self, firstname=None, is_alive=True):
        super().__init__(firstname=firstname, is_alive=is_alive)
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    def print_house_words(self):
        print(self.house_words)
    
    def die(self):
        print(f'In die function: {self.firstname} is dead')
        self.is_alive = False


