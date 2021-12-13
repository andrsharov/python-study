#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_6_6():
    i = 0
    while (not wall_is_on_the_right()):
        move_right()
        i += 1
        while (not wall_is_above()):
            move_up()
            fill_cell()
        while (not wall_is_beneath()):
            move_down()
    move_left(i)
    return

if __name__ == '__main__':
    run_tasks()
