import random


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


health_of_crew_members(10)
