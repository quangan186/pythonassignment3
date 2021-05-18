import random
import time
from time import gmtime, strftime

from datetime import datetime

# Inquire the info on current status of the spaceship

distance_from_mars = 10000  # km
distance_from_earth = 100
velocity = 500  # km/s


def distance_and_time_cal(dis_mars, dis_earth, velo):
    """
        Calculate distance from Earth to current spaceship location, current spaceship location to Mars and
    the estimated time to go to Mars
        :param velo:
        :param dis_earth:
        :param dis_mars:
        :param s: dis tance between Earth and Mars
        :param v: current velocity of spaceship
        :return: distance from Earth to current spaceship location, current spaceship location to Mars and
    the estimated time to go to Mars
    """
    while dis_mars >= 0:
        print(str(strftime("%a, %d %b %Y %H:%M:%S", gmtime())))
        print("Distance from Mars to Spaceship : {} km".format(dis_mars))
        print("Distance from Earth to Spaceship : {} km".format(dis_earth))
        print("Estimate time arrived: {} seconds \n".format(dis_mars / velocity))
        time.sleep(1)
        dis_mars -= velocity
        dis_earth += velocity
        estimate_time = dis_mars / velocity
    else:
        print("Ur at Mars")
    print("U have arrived!!")


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
        time.sleep(60)  # delay 60 seconds
        print(f'Current fuel: {current_fuel_level} liters')
    else:
        print('Out of energy')


def health_of_crew_members(number_of_members):
    """
    Define the number of members and define how many victims are there and their symptoms
    :param number_of_members: the quantity of members in spaceship
    :return: the number of members, number of victims and their symptoms in spaceship
    """
    # list of symptoms
    health_problem_list = ['fever', 'sneeze', 'stomachache', 'sore throat']

    # random the number of victims
    victims = random.randrange(0, number_of_members)

    # random the symptom
    problem = random.choice(health_problem_list)

    # if the number of victims larger than 2 and have symptom
    if victims >= 2:
        print(f'There are {number_of_members} total members and {victims} members have {problem}')

    # if the number of victims equal to 1 and have symptom
    elif victims == 1:
        print(f'There are {number_of_members} total members and {victims} member has {problem}')

    # if no one has symptom
    else:
        print(f'There are {number_of_members} total members and all of them are normal')


def spaceship_health(health_of_spaceship, problems):
    print(health_of_spaceship)
    for name, damage in problems.items():
        if random.random() < 0.5:  # random the possibility of problems happen
            continue
        print(f'Problems: {name}')  # print problems
        health_of_spaceship -= damage
        print(f'current_health: {health_of_spaceship}')
        if health_of_spaceship <= 0:
            print("Your spaceship is stop working")
            break


print("*** Welcome to RMIT Spaceship")
print("Good morning captain William and vice captain Diablo")
start_button = input("Do you want to start: ")


def button():
    print("1. Check time and distance")
    print("2. Check fuel")
    print("3. Check health of spaceship")
    print("4. Check health of crew members")
    print("5. Exit")


if start_button == 'start' or 'Start':
    print("Menu")
    print(button())

choose = input("Which one do you want to see: ")
if choose == '1':
    print(distance_and_time_cal(distance_from_mars, distance_from_earth, velocity))
elif choose == '2':
    print(fuel_cal(100, 5))
elif choose == '3':
    print(spaceship_health(100, problems={"fan": 20, "heat": 30, "vision": 40, "radar": 40}))
elif choose == '4':
    print(health_of_crew_members(10))
else:
    print('Stop the process')
