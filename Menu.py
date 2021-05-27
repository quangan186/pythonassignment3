
print("*** Welcome to RMIT Spaceship")
print("Good morning captain William and vice captain Diablo")
start_button = input("Do you want to start: ")


def button():
    print("Menu")
    print("1. Check time and distance")
    print("2. Check fuel")
    print("3. Check health of spaceship")
    print("4. Check health of crew members")
    print("5. Exit")
# def go_back():
#     go_back_button = input("Press 5 to go back: ")
#     if go_back_button == 5:
#         print(button())

#     else:
#         print("Stop the process")
if start_button == "start" or start_button == "Start":
    print(button())
    choose_button = input("Which one do you want to choose: ")
    if choose_button == '1':
        from basic_info import distance_and_time_cal
        print(distance_and_time_cal(230000000))
    elif choose_button == '2':
        from basic_info import fuel_cal
        print(fuel_cal(100, 5))
    elif choose_button == '3':
        from basic_info import spaceship_health
        print(spaceship_health(problems={"fan": 20, "heat": 30, "vision": 40, "radar": 40}))
    elif choose_button == '4':
        from basic_info import health_of_crew_members
        print(health_of_crew_members(10))

    else:
        print('Stop the process')
else:
    print("Stop the process")
