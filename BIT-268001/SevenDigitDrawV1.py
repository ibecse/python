# SevenDigitDrawV1.py
import turtle


def draw_line(draw):
    turtle.pd() if draw else turtle.pu()
    turtle.fd(40)
    turtle.rt(90)


def draw_digit(digit):
    draw_line(True) if digit in [2, 3, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 3, 4, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 6, 8] else draw_line(False)
    turtle.lt(90)
    draw_line(True) if digit in [0, 4, 5, 6, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 2, 3, 5, 6, 7, 8, 9] else draw_line(False)
    draw_line(True) if digit in [0, 1, 2, 3, 4, 7, 8, 9] else draw_line(False)
    turtle.lt(180)
    turtle.pu()
    turtle.fd(20)


def draw_date(date):
    for i in date:
        draw_digit(eval(i))


def main():
    turtle.hideturtle()
    turtle.setup(800, 350, 200, 200)
    turtle.pu()
    turtle.fd(-300)
    turtle.pensize(5)
    draw_date('20190526')
    turtle.hideturtle()
    turtle.done()


main()
