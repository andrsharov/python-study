#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_21():
    if wall_is_above():
        step_v = move_down
        step_v_limit = wall_is_beneath
    if wall_is_beneath():
        step_v = move_up
        step_v_limit = wall_is_above
    if wall_is_on_the_left():
        step_h = move_right
        step_h_limit = wall_is_on_the_right
    if wall_is_on_the_right():
        step_h = move_left
        step_h_limit = wall_is_on_the_left
    while ((not step_v_limit()) and (not step_h_limit())):
        if (not step_v_limit()):
            step_v()
        if (not step_h_limit()):
            step_h()
    return



if __name__ == '__main__':
    run_tasks()
