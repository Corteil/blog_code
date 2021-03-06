#!/usr/bin/env python
# coding: Latin-1

# Load library functions we want

from inputs import get_gamepad


try:
    print('Press CTRL+C to quit')

    # Loop indefinitely
    while True:

        events = get_gamepad()
        for event in events:
            print(event.code, event.state)
            if event.code == "ABS_Y":
                if event.state > 130:
                    print("Backwards")
                elif event.state < 125:
                    print("Forward")
            if event.code == "ABS_Z":
                if event.state > 130:
                    print("Right")
                elif event.state < 125:
                    print("Left")
            if event.code == "BTN_TL":
                if event.state == True:
                    print("Turbo")
            if event.code == "BTN_TR":
                if event.state == True:
                    print("Tank")
            if event.code == "BTN_NORTH":
                if event.state == True:
                    print("Triangle")
            if event.code == "BTN_SOUTH":
                if event.state == True:
                    print("Square")
            if event.code == "BTN_EAST":
                if event.state == True:
                    print("Cross")
            if event.code == "BTN_C":
                if event.state == True:
                    print("Circle")
            if event.code == "BTN_TR2":
                if event.state == True:
                    print("Start")
            if event.code == "BTN_TL2":
                if event.state == True:
                    print("Select")
            if event.code == "ABS_HAT0Y":
                if event.state == -1:
                    print("D pad Up")
                elif event.state == 1:
                    print("D pad Down")
            if event.code == "ABS_HAT0X":
                if event.state == -1:
                    print("D pad Left")
                elif event.state == 1:
                    print("D pad Right")
            if event.code == "BTN_WEST":
                if event.state == True:
                    print("Top left")
            if event.code == "BTN_Z":
                if event.state == True:
                    print("Top right")

            print("#### End ####")




            # print(event.ev_type, event.code, event.state)


except KeyboardInterrupt:

    # CTRL+C exit, disable all drives
    print("stop")
print("bye")