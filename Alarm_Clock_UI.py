import time
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
                3.Clock
    ''')


def mode():
    while True:
        clock_mode = input('Please insert here:')
        if clock_mode.isdigit():
            clock_mode = int(clock_mode)
            return clock_mode
        elif clock_mode == 'q' or clock_mode == 'quit':
            print('Goodbye, have a good day!')
            return clock_mode
        else:
            print('Please choose form the list!')


def user_timer():
    print(f'Insert  a time. Like(09:00) and to quit press "q" or "quit"')

    alarm = input('Insert...').strip()
    alarm_list = alarm.split(':')
    if alarm == 'q' or alarm == 'quit':
        print('Goodbye!')

    elif alarm_list[0].isdigit() and alarm_list[1].isdigit() and alarm_list[1].isdigit():
        alarm_list[0] = int(alarm_list[0])
        alarm_list[1] = int(alarm_list[1])
        alarm_list[2] = int(alarm_list[2])
        if 0 <= int(alarm_list[0]) < 24 and 0 <= int(alarm_list[1]) <= 59 and 0 <= int(alarm_list[2]) <= 60:
            return alarm_list
        else:
            print('Please insert correct hours and minutes! The hours should be less than 24 and minutes less '
                  'than 60')
    else:
        print('Please you need to insert a valid hour, like 23:00:45.')


def clock_timer():
    try:
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
        playsound('Music/Alarm.mp3')
        print('The time is up!')
    except IndexError:
        print('Not enough numbers')
    except TypeError:
        print("Is not the correct type!")
    except Exception:
        print('Sorry this is bad!')


def clock_alarm():
    try:
        print(CLEAR)
        alarm_set = user_timer()
        current_time = time.localtime()
        time_tuple = (current_time.tm_year,
                      current_time.tm_mon,
                      current_time.tm_mday,
                      int(alarm_set[0]),
                      int(alarm_set[1]),
                      int(alarm_set[2]),
                      current_time.tm_wday,
                      current_time.tm_yday,
                      current_time.tm_isdst)
        alarm_ = time.mktime(time_tuple)
        alarm_ = int(alarm_)

        while True:
            time_ = time.time()
            time.sleep(1)
            if alarm_ <= time_:
                print(f'Wake_up')
                playsound('Music/Alarm.mp3')
                break

            else:
                print(f'Tic Tac....')
    except IndexError:
        print('Not enough numbers')
    except TypeError:
        print("Is not the correct type!")
    except Exception:
        print('Sorry this is bad!')


def clock():
    try:
        print(CLEAR)
        while True:
            time_format = f'%A {BOLD}{GREEN}%H:%M:%S {RESET_FORMAT}'
            print(time.strftime(f'{CLEAR_AND_RETURN} {time_format}'))
            time.sleep(1)
    except IndexError:
        print('Not enough numbers')
    except TypeError:
        print("Is not the correct type!")
    except Exception:
        print('Sorry this is bad!')


def main():
    title()
    while True:

        mode_selected = mode()
        if mode_selected == 'q' or mode_selected == 'quit':
            break
        elif mode_selected == 1:
            clock_timer()

        elif mode_selected == 2:
            clock_alarm()
        elif mode_selected == 3:
            clock()
        else:
            print('Invalid input!')


if __name__ == '__main__':
    main()
