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
def task_2_1():
    move_down()
    move_right()
    cross_fill()

    return


if __name__ == '__main__':
    run_tasks()
