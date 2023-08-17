#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    for k in range(12):
        for i in range(26):
            fill_cell()
            if k % 2:
                move_left()
            else:
                move_right()
        fill_cell()
        move_down()


if __name__ == '__main__':
    run_tasks()
