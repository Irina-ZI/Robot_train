#!/usr/bin/python3

from pyrob.api import *

def make_x():
    move_right()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()

def make_x_1():
    # move_left()
    fill_cell()
    move_down(2)
    fill_cell()
    move_up()
    fill_cell()
    move_right()
    fill_cell()
    move_left(2)
    fill_cell()
    move_up()





@task(delay=0.02)
def task_2_4():
    finish = False
    # while not wall_is_beneath():
    while finish == False:
        while not wall_is_on_the_right():
            make_x()
            move_right(2)
            if not wall_is_on_the_right():
                move_right(2)
            else:
                move_down(2)
                if wall_is_beneath():
                    finish = True
                else:
                    move_down(2)
        move_left()
        while not wall_is_on_the_left():
            if wall_is_beneath():
                while not wall_is_on_the_left():
                    move_left()
                # move_up(2)
            else:
                make_x_1()
                if not wall_is_on_the_left():
                    move_left(3)
                else:
                    move_down(4)


        if finish == True:
            while not wall_is_on_the_left():
                move_left()
            move_up(2)











if __name__ == '__main__':
    run_tasks()
