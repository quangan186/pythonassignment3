import turtle
from datetime import datetime


def create_hours(first_column, second_column):
    first_column.penup()
    second_column.penup()
    for distance in range(0, 100, 50):
        first_column.sety(distance)
        first_column.dot(10, "black")

    for distance in range(0, 200, 50):
        second_column.sety(distance)
        second_column.dot(10, "black")

    first_column.sety(0)
    second_column.sety(0)
    first_column.pendown()
    second_column.pendown()


def create_minute(third_column, fourth_column):
    third_column.penup()
    fourth_column.penup()
    for distance in range(0, 150, 50):
        third_column.sety(distance)
        third_column.dot(10, "black")

    for distance in range(0, 200, 50):
        fourth_column.sety(distance)
        fourth_column.dot(10, "black")

    third_column.sety(0)
    fourth_column.sety(0)
    third_column.pendown()
    fourth_column.pendown()


def create_second(firth_column, sixth_column):
    firth_column.penup()
    sixth_column.penup()
    for distance in range(0, 150, 50):
        firth_column.sety(distance)
        firth_column.dot(10, "black")

    for distance in range(0, 200, 50):
        sixth_column.sety(distance)
        sixth_column.dot(10, "black")

    firth_column.sety(0)
    sixth_column.sety(0)

    firth_column.pendown()
    sixth_column.pendown()


def go_to(x, y, name):
    name.penup()
    name.setpos(x, y)
    name.pendown()


def create_clock(column_name: list):
    create_second(column_name[4], column_name[5])
    create_minute(column_name[2], column_name[3])
    create_hours(column_name[0], column_name[1])


def run_clock(time: str, column_name: list):
    binary = [8, 4, 2, 1]
    index = 0
    for i in time:
        i = int(i)
        calculate = i
        n = 0
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
    win = turtle.Screen()
    clock = turtle.Turtle()
    clock.ht()
    first_column = turtle.Turtle()
    first_column.speed(0)
    second_column = turtle.Turtle()
    second_column.speed(0)
    third_column = turtle.Turtle()
    third_column.speed(0)
    fourth_column = turtle.Turtle()
    fourth_column.speed(0)
    firth_column = turtle.Turtle()
    firth_column.speed(0)
    sixth_column = turtle.Turtle()
    sixth_column.speed(0)
    n = 0
    last = datetime.now()
    last_time = last.strftime("%H%M%S")
    column_name = [first_column, second_column, third_column, fourth_column, firth_column, sixth_column]
    for i in column_name:
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
        if current_time[0] != last_time[0] or current_time[1] != last_time[1]:
            create_hours(column_name[0], column_name[1])
        if current_time[2] != last_time[2] or current_time[3] != last_time[3]:
            create_minute(column_name[2], column_name[3])
        if current_time[4] != last_time[4] or current_time[5] != last_time[5]:
            create_second(column_name[4], column_name[5])
        last_time = current_time
        clock.clear()
