
import time


def fuel_cal(current_fuel_level, fuel_burn_rate):
    """
    Calculate the current fuel level of spaceship
    :param current_fuel_level: current fuel level
    :param fuel_burn_rate: fuel burn rate
    :return: the change of spaceship's fuel
    """

    print(f'Current fuel level: {current_fuel_level} liters')
    while current_fuel_level != 0:
        current_fuel_level -= fuel_burn_rate
        time.sleep(1)  # delay 60 seconds
        print(f'Current fuel: {current_fuel_level} liters')
    else:
        print('Out of energy')


fuel_cal(100, 10)
