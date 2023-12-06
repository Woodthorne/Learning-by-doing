import os
from abc import ABC, abstractmethod
from datetime import datetime

class BrightnessError(Exception):
    pass

class DarknessError(Exception):
    pass

class Receiver:
    def perform_action(self):
        print('Action performed in receiver.')


class Command(ABC):
    def __init__(self, receiver: object) -> None:
        self.receiver = receiver
    
    def process(self):
        pass
    
    def __str__(self) -> str:
        return 'Command'


class Invoker:
    def command(self, cmd: Command):
        self.cmd = cmd
    
    def execute(self):
        self.cmd.process()


class Light:
    def __init__(self) -> None:
        self.shining = False

    def turn_on(self):
        if not self.shining:
            self.shining = True
        else:
            raise BrightnessError
    
    def turn_off(self):
        if self.shining:
            self.shining = False
        else:
            raise DarknessError
    
    def turn_on_off(self):
        if self.shining:
            self.shining = False
        else:
            self.shining = True
    

class LightOn(Command):
    def __init__(self, receiver: Light) -> None:
        self.receiver = receiver
    
    def process(self):
        self.receiver.turn_on()
    
    def __str__(self) -> str:
        return 'LightOn'


class LightOff(Command):
    def __init__(self, receiver: Light) -> None:
        self.receiver = receiver

    def process(self):
        self.receiver.turn_off()
    
    def __str__(self) -> str:
        return 'LightOff'


class LightSwitch(Command):
    def __init__(self, receiver: Light) -> None:
        self.receiver = receiver
    
    def process(self):
        self.receiver.turn_on_off()

    def __str__(self) -> str:
        return 'LightSwitch'

def dump_log(log:list[Command]):
    filename = f'commandlog_{datetime.now().strftime("%Y%m%d%H%M%S")}.txt'
    with open(filename,'w') as file:
        for command in log:
            file.write(f'{command.__str__()}\n')

def new_screen():
    '''
    Clears the screen, for windows and unix
    '''
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

if __name__ == '__main__':
    light = Light()
    button_on = LightOn(light)
    button_off = LightOff(light)
    button_switch = LightSwitch(light)
    invoker = Invoker()
    commands: list[Command] = []
    while True:
        new_screen()
        print('===Välkommen till lampan===\n 1. Slå på\n 2. Slå av\n 3. Växla på/av\n 4. Utför\n 0. Avsluta')
        opt = input('>>> ')
        if opt == '0':
            quit()
        elif opt == '1':
            commands.append(button_on)
        elif opt == '2':
            commands.append(button_off)
        elif opt == '3':
            commands.append(button_switch)
        elif opt == '4':
            executed_commands: list[Command] = []
            for command in commands:
                executed_commands.append(command)
                try:
                    invoker.command(command)
                    invoker.execute()
                except BrightnessError:
                    print('Lampan är redan på. Stänger ner.')
                    dump_log(executed_commands)
                    quit()
                except DarknessError:
                    print('Lampan är redan av. Stänger ner.')
                    dump_log(executed_commands)
                    quit()