#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    for k in range(13):
        for i in range(k):
            fill_cell()
            if k % 2:
                move_right()
            else:
                move_left()
        fill_cell()
        move_down()
        if k % 2:
            move_right()




if __name__ == '__main__':
    run_tasks()
