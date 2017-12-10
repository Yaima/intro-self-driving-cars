# CODE CELL
#
# Write the park function so that it actually parks your vehicle.

from Car import Car
import time


def park(car):
    # TODO: Fix this function!
    #  currently it just drives back and forth
    #  Note that the allowed steering angles are
    #  between -25.0 and 25.0 degrees and the
    #  allowed values for gas are between -1.0 and 1.0

    car.steer(24.0)
    car.gas(-0.1)
    time.sleep(4.0)  # note how time.sleep works

    car.steer(-25.0)
    car.gas(-0.1)
    time.sleep(2.9)

    car.steer(0)
    car.gas(0.2)
    time.sleep(0.9)

    car.gas(0)


car = Car()
park(car)
