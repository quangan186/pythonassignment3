import turtle

win = turtle.Screen()
turtle.ht()


def go_to(x, y, name):
    name.penup()
    name.setpos(x, y)
    name.pendown()


n = 0

first_column = turtle.Turtle()

second_column = turtle.Turtle()

third_column = turtle.Turtle()

fourth_column = turtle.Turtle()

firth_column = turtle.Turtle()

sixth_column = turtle.Turtle()
column_name = [first_column, second_column, third_column, fourth_column, firth_column, sixth_column]

for i in column_name:
    i.ht()
    go_to(n, 0, i)

    n += 20

for i in column_name:
    n = 0
    while True:
        i.penup()
        i.sety(n)
        i.dot(10, "black")
        i.pendown()
        n += 50
        if n == 100 and i == column_name[0]:
            i.penup()
            i.sety(0)
            i.pendown()
            break
        elif n == 150 and (i == column_name[2] or i == column_name[4]):
            i.penup()
            i.sety(0)
            i.pendown()
            break
        elif n == 200:
            i.penup()
            i.sety(0)
            i.pendown()
            break

time = "112509"
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



#
# print(binary)
# stt = 1
# count = 0
# remain = 0
#
# for i in binary[:]:
#     turtle.left(90)
#
#     for j in i:
#         remain = default - len(i)
#         print(remain)
#         if j == '1':
#             turtle.dot(10, "red")
#             go_to(distance)
#         elif j == '':
#             turtle.dot(10, "black")
#             go_to(distance)
#         if remain != 0:
#             turtle.dot(10, "black")
#             go_to(distance)
#             remain -= 1
#     count += 10
#     turtle.penup()
#     turtle.home()
#     turtle.setx(count)
#     turtle.pendown()

win.exitonclick()
