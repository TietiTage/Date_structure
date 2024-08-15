# 利用turtle库创建一个分形树
import turtle
from turtle import *


def tree(length, t):
    if length > 5:
        t.forward(length)
        t.right(20)
        tree(length - 15, t)
        t.left(40)
        tree(length - 15, t)
        t.right(20)
        t.backward(length)


t = Turtle()
t.left(90)
t.penup()
t.backward(100)
t.pendown()
t.pencolor('red')
t.pensize(2)
tree(100, t)
t.hideturtle()
turtle.done()