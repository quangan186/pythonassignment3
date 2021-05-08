import random


def health_of_crew_members(n):
    health_problem_list = ['fever', 'sneeze', 'stomachache', 'none', 'sore throat']
    crew_numbers = random.randrange(1, n)
    i = random.choice(health_problem_list)
    if crew_numbers >= 2:
        print(f'There are {n} total members  and {crew_numbers} of them have {i}')
    else:
        print(f'There are {n} total members  and {crew_numbers} member has {i}')
    if i == 'none':
        print(f'There are {n} total members  and all of them are normal')


health_of_crew_members(10)
