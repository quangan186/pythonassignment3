import random
from datetime import datetime
import time

# set time to start the journey
start = "22/05/2021 06:00:00"
print(f'Start date is {start}')
d = datetime.strptime(start, "%d/%m/%Y %H:%M:%S")
t0 = time.mktime(d.timetuple())
fuel_burn_rate = 0.001/10000


# Information about the journey of the spaceship in space
def distance_and_time_cal(s):
    """
    This function is used to show the current velocity, time and distance from the spaceship to earth and vice versa
    :param s: distance between Earth and Mars
    :param v: current velocity of the spaceship
    :return: none
    """

    print(f'Distance between Earth and Mars: {s} km')
    distance_from_Earth = 0
    while True:
        current_fuel_level = 100
        time.sleep(1)
        v = random.uniform(11, 50)
        print(f'\nCurrent velocity:{v}')
        named_tuple = time.localtime()
        time_string = time.strftime("%d/%m/%Y, %H:%M:%S", named_tuple)
        print("- Time now {}".format(time_string))
        t1 = time.time()
        delta_time_seconds = t1 - t0

        distance_from_Earth += v * delta_time_seconds
        print(f'- Current distance from spaceship to Earth: {distance_from_Earth} km')

        distance_from_Mars = s - distance_from_Earth
        distance_from_Mars -= distance_from_Earth
        print(f'- Current distance from spaceship to Mars: {distance_from_Mars} km')

        # estimated time of arrival
        estimate_time = ((s - v * delta_time_seconds) / v) / 3600  # hours
        print(f'- Estimated time of arrival: {estimate_time} hours')

        current_fuel_level -= (fuel_burn_rate * distance_from_Earth)
        print(f'Current fuel: {current_fuel_level} liters')

        if distance_from_Earth >= s and distance_from_Mars <= 0:
            print("You have arrived")
            break
        else:
            print("You are on the way")



def spaceship_health(problems):
    """
    the current condition of the spaceship
    :param health_of_spaceship: the current condition of the spaceship
    :param problems: any issues that the spaceship met
    :return:
    """
    while True:
        health_of_spaceship = 100
        print(f"\nSpaceship health: {health_of_spaceship}")
        time.sleep(10)
        for name, damage in problems.items():
            if random.random() < 0.5:
                continue
            print(f'\nProblems: {name}')
            health_of_spaceship -= damage
            print(f'Current_health: {health_of_spaceship}')
            if health_of_spaceship > 0:
                print("We are going to fix it")
            else:
                print("Your spaceship is stop working")
                break
        time.sleep(30)  # delay 30 secs for fixing spaceship


# Health condition of crew members
def health_of_crew_members(number_of_members):
    """
    This function shows records of crew members about their health condition
    :param number_of_members:  number of people in the spaceship
    :return: none
    """
    health_problem_list = ['fever', 'sneeze', 'stomachache', 'sore throat']
    while True:
        victims = random.randrange(0, number_of_members)

        problem = random.choice(health_problem_list)

        if victims >= 2:
            print(f'There are {number_of_members} total members and {victims} members have {problem}')

        elif victims == 1:
            print(f'There are {number_of_members} total members and {victims} member has {problem}')

        else:
            print(f'There are {number_of_members} total members and all of them are normal')
        time.sleep(60)
