import os
from time import sleep


def console_clear(sleep_time=0):

    sleep(sleep_time)
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')
