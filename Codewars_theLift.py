# My solution for the kata The Lift from codewars.com
# Full kata link: https://www.codewars.com/kata/58905bfa1decb981da00009e/python
# Added ability to generate random floorplan as well, due to misunderstanding
# the task initially.

import random

class Lift:
    def __init__(self,capacity:int) -> None:
        self._floor = 0
        self._capacity = capacity
        self._direction = 'up'
        self._content = []
        self._log = [0]
    
    def get_floor(self) -> int:
        return self._floor
    
    def unload(self) -> None:
        for passenger in self._content:
            if passenger == self._floor:
                self._content.remove(passenger)
                queues[self._floor].append(passenger)
    
    def load(self) -> None:
        loading = []
        for passenger in queues[self._floor]:
            if len(loading) + len(self._content) < self._capacity:
                if (passenger > self._floor and self._direction == 'up') or (passenger < self._floor and self._direction == 'down'):
                    loading.append(passenger)
            else:
                break
        for passenger in loading:
            queues[self._floor].remove(passenger)
        self._content.extend(loading)

    def move(self,end) -> None:
        if end == True and len(self._content) == 0:
            self._floor = 0
        elif self._direction == 'up':
            if len(self._content) == 0:
                for i in range(len(queues)-1,-1,-1):
                    if 'down' in buttons[i]:
                        self._floor = i
                        self._direction = 'down'
                        break
            if self._direction == 'up':
                off = len(queues)
                for i in self._content:
                    if i < off:
                        off = i
                on = len(queues)
                for i in range(self._floor+1,len(queues)-1,1):
                    if 'up' in buttons[i]:
                        on = i
                        break
                if on == off == len(queues):
                    self._floor = len(queues)-1
                elif off < on:
                    self._floor = off
                else:
                    self._floor = on
        elif self._direction == 'down':
            if len(self._content) == 0:
                for i in range(0,len(queues),1):
                    if 'up' in buttons[i]:
                        self._floor = i
                        self._direction = 'up'
                        break
            if self._direction == 'down':
                off = 0
                for i in self._content:
                    if i > off:
                        off = i
                on = 0
                for i in range(self._floor-1,0,-1):
                    if 'down' in buttons[i]:
                        on = i
                        break
                if off > on:
                    self._floor = off
                else:
                    self._floor = on
        if self._floor != self._log[-1]:
            self._log.append(self._floor)

        if self._floor == 0:
            self._direction = 'up'
        elif self._floor == len(queues)-1:
            self._direction = 'down'

error_dict = {'choice':'Invalid choice. Try again.'}

floor_samples = {'1':[[],[],[5,5,5],[],[],[],[],[0,2,5,0]],
                 '2':[[],[],[1,1],[],[],[],[],  [0,2,1,0]],
                 '3':[[],[3],[4],[],[5],[],[],  [0,1,2,3,4,5,0]],
                 '4':[[],[0],[],[],[2],[3],[],  [0,5,4,3,2,1,0]]}

queues = []
buttons = []
lift = Lift(3)

def setup():
    while True:
        method = input('Do you wish to [generate] a building or use the coded [sample]? ').lower()
        if method == 'generate':
            random_building()
            break
        elif method == 'sample':
            sample_building()
            break
        else:
            print(error_dict('choice'))
    input('Lift is ready to run. Press [ENTER]...')

def random_building():
    while True:
        floors = input('How many floors are in the building?' )
        if floors.isnumeric():
            break
        print(error_dict('choice'))
    for floor in range(floors):
        queues.append([])
        visitor_amount = random.randint(0,4)
        while len(queues[floor]) < visitor_amount:
            visitor = random.randint(0,floors-1)
            if visitor != floor:
                queues[floor].append(visitor)
        push_buttons(floor)

def sample_building():
    for key in floor_samples.keys():
        print(f'{key}: {floor_samples[key][:-1]} gives output {floor_samples[key][-1]}')
    while True:
        sample = input('Choose a sample floor: ')
        if sample in floor_samples.keys():
            queues.extend(floor_samples[sample][:-1])
            for floor in range(len(queues)):
                buttons.append([])
                push_buttons(floor)
            break
        print(error_dict['choice'])

def push_buttons(floor):
    buttons[floor] = []
    if any(destination > floor for destination in queues[floor]):
        buttons[floor].append('up')
    if any(destination < floor for destination in queues[floor]):
        buttons[floor].append('down')

def all_done():
    for floor in range(0,len(queues)-1):
        if any(button == 'up' for button in buttons[floor]) or any(button == 'down' for button in buttons[floor]):
            return False
    return True

def main():
    setup()
    end = False
    while len(lift._content) > 0 or not end:
        lift.unload()
        lift.load()
        push_buttons(lift.get_floor())
        end = all_done()
        lift.move(end)

main()

print('Queues at end of simulation:',queues)
print('Lift movements during simulation:',lift._log)