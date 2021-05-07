import time


def fuel_cal(a, b):
    current_fuel_level = a
    fuel_burn_rate = b
    print(f'Current fuel level: {current_fuel_level}')
    while True:
        current_fuel_level -= fuel_burn_rate
        time.sleep(1)  # delay 1 second
        print(f'Current fuel: {current_fuel_level}')
        if current_fuel_level == 0:
            print('Out of energy')
            break


fuel_cal(100, 10)
