#!/usr/bin/python3

from pyrob.api import *
def make_x():
    move_right()
    move_down()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up(2)
    # move_right(4)

@task
def task_2_2():
    for k in range(4):
        make_x()
        move_right(4)
    make_x()
    move_down()





if __name__ == '__main__':
    run_tasks()
