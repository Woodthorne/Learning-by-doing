#   ASSIGNMENT
#   We have been tasked with building a booking
#   system for a leisure center (with menu and
#   everything). In the leisure center are 3
#   bowling areas, 5 badminton areas, and 3
#   tennis areas.
#
#   Each area can be booked for an hour at a time
#   from 09:00 to 21:00 at night (closing at 22)
#
#   It's important here to make sure you can't
#   double book an area during the same hour.


#   Sets up dictionaries with the types of the areas as well as the
#   main dictionary with all the locales, time slots, and individual areas.
sport = {1:'bowling',2:'badminton',3:'tennis'}
locales = {}
for sports in range(1,4):
    locales[sports] = {}
    for time in range(9,22):
        locales[sports][time] = {}
        if sports in [1,3]:
            for slots in range(1,4):
                locales[sports][time][slots] = 0
        else:
            for slots in range(1,6):
                locales[sports][time][slots] = 0

#   Main loop of the menu. Takes an input of desired sport followed
#   by the desired time slot.
while True:
    booked = False
    print('==========BOOKING==========')
    print('Which type of area is desired?\n 1. Bowling\n 2. Badminton\n 3. Tennis\n 4. End booking')
    opt = (input('Option: '))
    if opt.isnumeric():
        opt = int(opt)
    if opt == 4:
        quit()
    elif opt in [1,2,3]:
        slot = input('(Input desired time between 9 and 21: ')
        if slot.isnumeric():
            slot = int(slot)
            for course in locales[opt][slot]:
                if locales[opt][slot][course] == 0 and not booked:
                    locales[opt][slot][course] = 1
                    print(f'You have booked {sport[opt]} area {course} between {slot}-{slot+1}')
                    booked = True
            if booked is not True:
                print(f'There is no {sport[opt]} area available for booking at that time.')
        else:
            print('That is not an available time. Try again.')
    else:
        print('That option is not available. Try again.')