import turtle
from datetime import datetime


def create_hours(first_column, second_column):
    """
    Function which is used to show the hour section of the binary clock
    :param first_column: the first column which displays hours
    :param second_column: the second column which displays hours
    :return: none
    """
    first_column.penup()
    second_column.penup()
    for distance in range(0, 100, 50):                # set up location for the dot which represent column 1
        first_column.sety(distance)                   # Start from 0, every time it gains 50, draw a dot
        first_column.dot(10, "black")                 # Stop when it hits 100

    for distance in range(0, 200, 50):                # set up location for the dot which represent column 2
        second_column.sety(distance)                  # Start from 0, everytime it gains 50, draw a dot
        second_column.dot(10, "black")                # Stop when it hits 200

    first_column.sety(0)
    second_column.sety(0)
    first_column.pendown()
    second_column.pendown()


def create_minute(third_column, fourth_column):
    """
    Function which is used to show the minute section of the binary clock
    :param third_column: the first column which displays minute
    :param fourth_column: the second column which displays minute
    :return: none
    """
    third_column.penup()
    fourth_column.penup()
    for distance in range(0, 150, 50):              # Set up location for the dot which represent column 3
        third_column.sety(distance)                 # Start from 0, every time it gains 50, draw a dot
        third_column.dot(10, "black")               # Stop when it hits 150

    for distance in range(0, 200, 50):              # set up location for the dot which represent column 4
        fourth_column.sety(distance)                # Start from 0, everytime it gains 50, draw a dot
        fourth_column.dot(10, "black")              # Stop when it hits 200

    third_column.sety(0)
    fourth_column.sety(0)
    third_column.pendown()
    fourth_column.pendown()


def create_second(firth_column, sixth_column):
    """
    Function which is used to show the second section of the binary clock
    :param firth_column: the first column which displays seconds
    :param sixth_column:the second column which displays seconds
    :return: none
    """
    firth_column.penup()
    sixth_column.penup()
    for distance in range(0, 150, 50):              # Set up location for the dot which represent column 5
        firth_column.sety(distance)                 # Start from 0, every time it gains 50, draw a dot
        firth_column.dot(10, "black")               # Stop when it hits 150

    for distance in range(0, 200, 50):              # Set up location for the dot which represent column 6
        sixth_column.sety(distance)                 # Start from 0, everytime it gains 50, draw a dot
        sixth_column.dot(10, "black")               # Stop when it hits 200

    firth_column.sety(0)
    sixth_column.sety(0)

    firth_column.pendown()
    sixth_column.pendown()


def go_to(x, y, name):
    """
    Function that is used to identify the name of the turtle
    and the coordinate which that turtle is moved to
    :param x: x coordinate of the destination
    :param y:  y coordinate of the destination
    :param name: name of the turtle which takes action
    :return: none
    """
    name.penup()
    name.setpos(x, y)
    name.pendown()


def create_clock(column_name: list):
    """
    Function that use all the "create" functions above to call out all the columns of a binary clock
    :param column_name: name of the column which contain a specific information (hours, minutes or seconds)
    :return: none
    """
    create_second(column_name[4], column_name[5])
    create_minute(column_name[2], column_name[3])
    create_hours(column_name[0], column_name[1])


def run_clock(time: str, column_name: list):
    """
    Function which is used to run the binary clock
    :param time: the current time which will be displayed
    :param column_name: the list of columns which displayed the time in order from hours to seconds
    :return: none
    """
    binary = [8, 4, 2, 1]
    index = 0
    for i in time:
        i = int(i)
        calculate = i
        n = 0            # n: position of the binary number
        if index == 0:
            distance = 50
            n = 2
        elif index == 2 or index == 4:
            distance = 100
            n = 1
        else:
            distance = 150
            n = 0

        while True:
            if index == 7 or n == 4:
                break
            column_name[index].penup()
            if calculate < binary[n]:
                n += 1
                distance -= 50
                continue
            calculate -= binary[n]

            if calculate >= 0:
                column_name[index].sety(distance)
                column_name[index].dot(10, "red")

            column_name[index].pendown()

        index += 1


def binary_clock():
    """
    Function that is used to draw binary clock
    :return: none
    """
    win = turtle.Screen()
    clock = turtle.Turtle()
    clock.ht()
    first_column = turtle.Turtle()          # The first column of hours
    first_column.speed(0)
    second_column = turtle.Turtle()         # The second column of hours
    second_column.speed(0)
    third_column = turtle.Turtle()          # The first column of minutes
    third_column.speed(0)
    fourth_column = turtle.Turtle()         # The second column of minutes
    fourth_column.speed(0)
    firth_column = turtle.Turtle()          # The first column of seconds
    firth_column.speed(0)
    sixth_column = turtle.Turtle()          # The second column of seconds
    sixth_column.speed(0)
    n = 0
    last = datetime.now()
    last_time = last.strftime("%H%M%S")
    column_name = [first_column, second_column, third_column, fourth_column, firth_column, sixth_column]
    for i in column_name:               # writing the name of column with a specific distance from one to another
        i.ht()
        go_to(n, 0, i)
        n += 20
    go_to(20, 160, clock)
    create_clock(column_name)
    while True:
        now = datetime.now()
        current_time = now.strftime("%H%M%S")
        current_time_write = now.strftime("%H:%M:%S")
        clock.write(current_time_write, font=("Arial", 18, "normal"))
        run_clock(current_time, column_name)
        if current_time[0] != last_time[0] or current_time[1] != last_time[1]:      # Call the columns of hour out
            create_hours(column_name[0], column_name[1])
        if current_time[2] != last_time[2] or current_time[3] != last_time[3]:      # Call the columns of minute out
            create_minute(column_name[2], column_name[3])
        if current_time[4] != last_time[4] or current_time[5] != last_time[5]:      # Call the columns of seconds out
            create_second(column_name[4], column_name[5])
        last_time = current_time
        clock.clear()
