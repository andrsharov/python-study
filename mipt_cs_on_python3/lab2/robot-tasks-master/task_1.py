#!/usr/bin/python3

from pyrob.api import *


@task
def task_1_1():
    move_right()
    move_down()
    move_right()
    return


if __name__ == '__main__':
    run_tasks()
