import random


def health_of_crew_members(n):
    health_problem_list = ['fever', 'sneeze', 'stomachache']
    crew_numbers = random.randrange(1, n)
    i = random.choice(health_problem_list)
    print(f'There are {n} total members  and {crew_numbers} of them have/has {i}')


health_of_crew_members(10)
