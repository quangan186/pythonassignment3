import random
health_of_spaceship = 100
problem_list = ["fan", "heat", "vision", "radar"]
i = random.choice(problem_list)
print(i)
if i == "fan":
    current_health = health_of_spaceship - 20
    print(f'current_health: {current_health}')
elif i == "heat":
    current_health = health_of_spaceship - 30
    print(f'current_health: {current_health}')
else:
    current_health = health_of_spaceship - 40
    print(f'current_health: {current_health}')
