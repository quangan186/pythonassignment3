print("*** Welcome to RMIT Spaceship")
print("Good morning captain William and vice captain Diablo")
start_button = input("Do you want to start: ")
if start_button == 'start' or 'Start':
    print("Menu")
    print("1. Check time and distance")
    print("2. Check fuel")
    print("3. Check health of spaceship")
    print("4. Check health of crew members")
    print("5. Check journal")
    print("6. Exit")
    choose = input("Which one do you want to see: ")
    # if choose == 1:
    #     from basic_info import *
    #     from basic_info import distance_and_time_cal
    #     print(distance_and_time_cal(230000000, 11.11))
