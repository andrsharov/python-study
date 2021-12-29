#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i: int = 0
    while not wall_is_on_the_right():
        move_right()
        fill_cell()
        if i > 0:
            for k in range(1, i+1):
                if (not wall_is_on_the_right()):
                     move_right()
        i += 1
    return

if __name__ == '__main__':
    run_tasks()
