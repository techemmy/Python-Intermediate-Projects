import time

def start_timer(hour, minute, seconds):
    if (hour > 60) or (minute > 60) or (seconds > 60):
        print("Hour, minute, or seconds cannot be greater than 60")
        return None
    while True:
        print("{0}:{1:02d}:{2:02d}".format(hour, minute, seconds))
        if (hour == 0) and (minute == 0) and (seconds == 0):
            print("Time's up")
            break

        if (seconds == 0) and (minute > 0):
            minute -= 1
            seconds += 60

        if (minute == 0) and (hour > 0):
            hour -= 1
            minute += 60

        seconds -= 1
        time.sleep(1)

try:
    timer = input("Enter time > ").split(":")
    hour, minute, seconds = int(timer[0]), int(timer[1]), int(timer[2])
    start_timer(hour, minute, seconds)
except ValueError:
    print("Invalid input(s) given.")
