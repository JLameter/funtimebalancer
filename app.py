"""Launch Module for the app"""

import time


def start_timer(interval, debug_mode=False):
    """Run the timer"""
    print("starting timer...")
    coins = 0
    try:
        while True:
            time.sleep(interval)
            coins += 1
            print("Gained 1 coin! That's", coins, "coins total!")
            if debug_mode:
                print("Interval:", interval)
    except KeyboardInterrupt:
        print("Timer stopped with", coins, "coins")


start_timer(2, True)
