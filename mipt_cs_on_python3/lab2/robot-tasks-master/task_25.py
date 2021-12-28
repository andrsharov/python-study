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


@task
def task_2_2():
    move_down()
    i = 5
    while i > 0:
        cross_fill()
        if i > 1:
            move_right(4)
        i -= 1
    return

if __name__ == '__main__':
    run_tasks()
