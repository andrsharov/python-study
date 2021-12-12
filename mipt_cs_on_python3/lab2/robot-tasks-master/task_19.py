#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    while (wall_is_above() and not wall_is_on_the_left()):
        move_left()
    while (wall_is_above() and not wall_is_on_the_right()):
        move_right()
    if (wall_is_above()) : return
    while (not wall_is_above()):
        move_up()
    while (not wall_is_on_the_left()):
        move_left()
    return


if __name__ == '__main__':
    run_tasks()
