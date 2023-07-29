import time
import threading
from playsound import playsound

CLEAR = '\033[2J'
CLEAR_AND_RETURN = "\033[H"
GREEN = '\033[32m'
BOLD = '\033[1m'
RESET_FORMAT = '\033[0m'


def title():
    print(f''' Please choose from the list above:
                1.Timer
                2.Alarm-Clock
                3.Stopwatch
                4.Clock
    ''')


def mode():
    while True:
        clock_mode = input('Please insert here:')
        if clock_mode.isdigit():
            clock_mode = int(clock_mode)
            return clock_mode
        elif clock_mode == 'q' or clock_mode == 'quit':
            print('Goodbye, have a good day!')
            break
        else:
            print('Please choose form the list!')


def user_timer():
    alarm = None
    print('Insert  a time. Like(06:30:00) and to quit press "q" or "quit"')
    while not alarm:
        alarm = input('Insert...').strip()
        alarm_list = alarm.split(':')
        if alarm != 'q' or alarm != 'quit':
            print('Goodbye!')
            break
        elif alarm_list[0].isdigit() and alarm_list[1].isdigit() and alarm_list[1].isdigit():
            alarm_list[0] = int(alarm_list[0])
            alarm_list[1] = int(alarm_list[1])
            alarm_list[2] = int(alarm_list[2])
            if 0 <= int(alarm_list[0]) < 24 and 0 <= int(alarm_list[1]) <= 60 and 0 <= int(alarm_list[2]) <= 60:
                return alarm_list
            else:
                print('Please insert correct hours and minutes! The hours should be less than 24 and minutes less '
                      'than 60')
        else:
            print('Please you need to insert a valid hour, like 23:00:45.')


def clock_timer():
    alarm_set = user_timer()
    total_seconds = alarm_set[0] * 3600 + alarm_set[1] * 60 + alarm_set[2]
    total_seconds = int(total_seconds)
    count = 0
    print(CLEAR)
    while count <= total_seconds:
        try:
            time.sleep(1)
            count += 1
            time_left = total_seconds - count
            hours_left = time_left // 3600
            minutes_left = (time_left % 3600) // 60
            seconds_left = time_left % 60
            print(f'{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}')

        except KeyboardInterrupt:
            print('The clock is stopped')
            break
    playsound('')
    print('The time is up!')


def clock_alarm():
    alarm_set = user_timer()
    total_seconds = alarm_set[0] * 3600 + alarm_set[1] * 60 + alarm_set[2]
    total_seconds = int(total_seconds)

    print(CLEAR)
    while True:
        try:
            alarm = time.perf_counter()
            if alarm <= total_seconds:
                time.sleep(1)
                time_left = total_seconds - alarm
                hours_left = time_left // 3600
                minutes_left = (time_left % 3600) // 60
                seconds_left = time_left % 60
                print(f'{CLEAR_AND_RETURN}{hours_left:02d}:{minutes_left:02d}:{seconds_left:02d}')

        except KeyboardInterrupt:
            print('The clock is stopped')

        print('Wake Up!')
        playsound('Games_Lessons/Music/Alarm.mp3')


def clock():
    print(CLEAR)
    while True:
        time_format = f'%A {BOLD}{GREEN}%H:%M:%S {RESET_FORMAT}'
        print(time.strftime(f'{CLEAR_AND_RETURN} {time_format}'))
        time.sleep(1)


def main():
    title()
    mode_selected = mode()
    while True:
        if mode_selected == 'q' or mode_selected == 'quit':
            print('Goodbye')
            break
        elif mode_selected == 1:
            clock_timer()

        elif mode_selected == 2:
            clock_alarm()
        elif mode_selected == 3:
            pass
        elif mode_selected == 4:
            clock()


        else:
            print('Invalid!')


if __name__ == '__main__':
    main()
