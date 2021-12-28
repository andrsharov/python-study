#!/usr/bin/python3

from pyrob.api import *

def cross_fill():
    move_down()
    fill_cell()
    move_right()
    fill_cell()
    move_down()
    fill_cell()
    move_up()
    move_right()
    fill_cell()
    move_left()
    move_up()
    fill_cell()
    move_left()
    return

@task(delay=0.02)
def task_2_4():
    i = 5
    while i > 0:
        j = 10
        while j > 0:
            cross_fill()
            if j > 1:
                move_right(4)
            j -= 1
        if i > 1:
            move_left(36)
            move_down(4)
        if i == 1:
            move_left(36)
        i -= 1
    return

if __name__ == '__main__':
    run_tasks()
