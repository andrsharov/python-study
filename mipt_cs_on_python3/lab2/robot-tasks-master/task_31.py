#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    k = 0
    while not (k == 2):
        while not wall_is_beneath():
            move_down()
            k = 0
        while not wall_is_on_the_right():
            move_right()
            if not wall_is_beneath():
                move_down()
                k = 0
        while not wall_is_on_the_left():
            move_left()
            if not wall_is_beneath():
                move_down()
                k = 0
        k += 1
    return


if __name__ == '__main__':
    run_tasks()
