# Pomodoro Timer

Pomodoro Timer is a time management script that will help you to balance focus with deliberate breaks. Pomodoro technique breaks up the work process into chunks of focused work of 25 minutes and short breaks of 5 minutes. Together, work and rest make 1 pomodoro :tomato:

## How it works
1. Select a task to complete. Run the script and start the timer.
2. Do 1 pomodoro. Focus on the work for 25 minutes, then take a short break. `pomodoro.py` will notify you when it's time to rest and get back to work!
3. Repeat until you complete 4 pomodoros. Then take a longer, 15 minute break. After this, the cycle starts again.
4. Continue working until your task is complete!

## Dependencies
This script depends on `notify-py` library to send notifications to the user.

## Running the script

Run the following in the command prompt:
```
python pomodoro.py
```

To stop the pomodoro timer, press `Ctrl + C`. When paused, press Enter to resume, or type `STOP` to go back to the menu. Once stopped, the timer and number of pomodoros completed will be reset.