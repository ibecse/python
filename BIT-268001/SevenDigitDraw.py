#
import turtle


def draw_line(draw):
    if draw:
        turtle.pendown()
    else:
        turtle.penup()
    turtle.fd(50)
    turtle.right(90)
    turtle.penup()


def draw_digit(digit):
    if digit in [2, 3, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if digit in [0, 2, 3, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if digit in [0, 2, 6, 8]:
        draw_line(True)
    else:
        draw_line(False)
    turtle.left(90)
    if digit in [0, 4, 5, 6, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if digit in [0, 2, 3, 5, 6, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)
    if digit in [0, 1, 2, 3, 4, 7, 8, 9]:
        draw_line(True)
    else:
        draw_line(False)


def main():
    s = input("请输入日期yyyymmdd：")
    turtle.screensize(1000, 600)
    turtle.penup()
    turtle.fd(-400)
    n = 0
    for i in s:
        draw_digit(eval(i))
        turtle.right(180)
        turtle.fd(50)
        n += 1
        if n == 4:
            turtle.write("年")
            turtle.fd(50)
        if n == 6:
            turtle.write("月")
            turtle.fd(50)
        if n == 8:
            turtle.write("日")
            turtle.fd(50)


main()


