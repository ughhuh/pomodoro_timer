import time
from notifypy import Notify

# global variables 
pomodoro = None
s_break = None
l_break = None
pomo_num = None

notification = Notify(
    default_notification_application_name="Pomodoro Timer", 
    default_notification_icon="pomo_logo.png"
)

def init():
    global pomodoro 
    global s_break 
    global l_break
    global pomo_num
    try:
        with open("config.txt", 'r') as f:    
            pomodoro = f.readline().strip()
            s_break = f.readline().strip()
            l_break = f.readline().strip()
            pomo_num = f.readline().strip()
    except FileNotFoundError: # if config file isn't found, use these default values
        pomodoro = 25
        s_break = 5
        l_break = 15
        pomo_num = 4

def menu():
    while True:
        inp=input('=====POMODORO TIMER=====\n- Type START to start the timer.\n- Type SETTINGS to change time.\n- Type INFO to learn more about Pomodoro.\n- Type EXIT to exit the program\n').lower()
        if inp == 'start':
            break
        elif inp == 'settings':
            settings()
        elif inp == 'exit':
            exit()
        else:
            print('Invalid input. Please try again.')

def timer():
    print('Timer has started! Press Ctrl + C to pause.')

    pomo_count = 0
    break_count = 0

    while (True):    
        pomo_secs = int(pomodoro)*60
        s_break_secs = int(s_break)*60
        l_break_secs = int(l_break)*60

        while(pomo_secs):
            mins, secs = divmod(pomo_secs, 60)
            try:
                print(f'{mins:02d}:{secs:02d}', end='\r')
                time.sleep(1)
                pomo_secs -= 1
            except KeyboardInterrupt: # pause the timer
                pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count = pause(pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count)
                continue
        pomo_count += 1
        
        if (break_count % (int(pomo_num)-1) == 0) and (break_count != 0): # a long break after pomo_num pomodoros
            pomo_alert(f'Take a {l_break} minute break.', f'{pomo_count} pomodoros completed so far.')
            while(l_break_secs):
                mins, secs = divmod(s_break_secs, 60)
                try:
                    print(f'{mins:02d}:{secs:02d}', end='\r')
                    time.sleep(1)
                    l_break_secs -= 1 
                except KeyboardInterrupt:
                    pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count = pause(pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count)
                    continue
            break_count += 1
            print('Back to work!')
        else: # a short break 
            pomo_alert(f'Take a {s_break} minute break.', f'{pomo_count} pomodoros completed so far.')
            while(s_break_secs):
                mins, secs = divmod(s_break_secs, 60)
                try:
                    print(f'{mins:02d}:{secs:02d}', end='\r')
                    time.sleep(1)
                    s_break_secs -= 1 
                except KeyboardInterrupt:
                    pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count = pause(pomo_secs, s_break_secs, l_break_secs, pomo_count, break_count)
                    continue
            break_count += 1
            pomo_alert('Break is over!','It\'s time to go back to work.')

def settings():
    global pomodoro 
    global s_break 
    global l_break
    global pomo_num
    print(f'=====SETTINGS=====\nPomodoro: {pomodoro} minutes\nShort break: {s_break} minutes\nLong break: {l_break} minutes\nNumber of pomodoros: {pomo_num}\nTo change a value, type its name:')
    # get what value to change and what to change to, update global value and save info to config file
    while(True):
        inp=input().lower()
        if inp in ['pomodoro','short break','long break','number of pomodoros']:
            num = input('Input new value in minutes:\n')
            try:
                num = int(num)
                if inp == 'pomodoro': pomodoro = num
                elif inp == 'short break': s_break = num
                elif inp == 'long break': l_break = num
                elif inp == 'number of pomodoros': pomo_num = num
                # writing info to config file
                with open(r"C:\Users\lanav\Desktop\etc\Projects\pomodoro py\config.txt", 'w+') as f:
                    f.write(f'{pomodoro}\n{s_break}\n{l_break}\n{pomo_num}')
                print('Information has been saved successfully!\n')
                break
            except ValueError:
                print('Invalid input. Please try again.')
        else:
            print('Invalid input. Please try again.')
    menu()

def pause(a, b, c, d, e):
    while(True):
        inp = input('Timer is paused. Press ENTER to continue. Type STOP to reset the timer and go to the menu.\n').lower()
        if inp =='':
            return a, b, c, d, e
        elif inp == 'stop':
            print(f'Timer was stopped. You have completed {d} pomodoros!\n')
            menu()
            return int(pomodoro)*60, int(s_break)*60, int(l_break)*60, 0, 0
        else:
            print('Invalid input. Please try again')

def pomo_alert(title, msg):
    notification.title = title
    notification.message = msg
    notification.send(block=False)

def main():
    init()
    menu()
    timer()

if __name__ == '__main__':
    main()