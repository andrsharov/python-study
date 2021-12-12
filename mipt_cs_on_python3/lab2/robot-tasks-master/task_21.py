#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    n = 1
    while n < 13:
        move_down()
        for i in range(n):
            fill_cell()
            move_right()
        fill_cell()
        for i in range(n):
            move_left()
        n += 1
    move_down()
    return








if __name__ == '__main__':
    run_tasks()
