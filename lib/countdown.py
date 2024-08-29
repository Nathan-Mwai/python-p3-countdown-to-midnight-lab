# your code goes here!
import time

def countdown(start):
    while start > 0:
        print(f"{start} SECOND(S)!")
        start -=1
    print("HAPPY NEW YEAR!")
    pass

def countdown_with_sleep(start):
    while start > 0:
        # if start == 1:
        #     print(f'{start} SECOND!')
        # else:
        print(f"{start} SECOND(S)!")
        time.sleep(1)
        start -=1
    print("HAPPY NEW YEAR!")
    pass

countdown_with_sleep(15)