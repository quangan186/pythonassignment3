import random

health_of_spaceship = 100
problems = {
    "fan": 20,
    "heat": 30,
    "vision": 40,
    "radar": 40,
}
for name, damage in problems.items():
    if random.random() < 0.5:
        continue
    print(name)
    health_of_spaceship -= damage
    print(f'current_health: {health_of_spaceship}')
    if health_of_spaceship <= 0:
        print("Your spaceship is stop working")
        break
