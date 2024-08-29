class Person:
    def __init__(self,förnamn,efternamn,ålder) -> None:
        self._förnamn = förnamn
        self._efternamn = efternamn
        self._ålder = ålder
    
    def get_förnamn(self):
        return self._förnamn
    
    def get_efternamn(self):
        return self._efternamn
    
    def get_ålder(self):
        return self._ålder
    
    def set_förnamn(self,namn):
        self._förnamn = namn

    def set_efternamn(self,namn):
        self._efternamn = namn
    
    def set_ålder(self,ålder):
        self._ålder = ålder

    def get_self(self):
        print(self)

erik = Person('Erik','Andersson',30)
print(erik.get_förnamn())
erik.set_förnamn('Kire')
print(erik.get_förnamn())
erik.get_self()