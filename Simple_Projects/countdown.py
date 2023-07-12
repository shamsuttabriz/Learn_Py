import time

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        # timer = '{:02d}:{:02d}'.format(mins, secs)
        timer = f'{mins:02d}:{secs:02d}'
        print(timer)
        time.sleep(1)
        t -= 1

    print("Time is over!")

t = input("Enter the value of time: ")
countdown(int(t))