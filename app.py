"""Launch Module for the app"""

import time
import pygame


def start_timer(interval, volume, debug_mode=False):
    """Run the timer"""
    print("starting timer...")
    pygame.mixer.init()
    sound = pygame.mixer.Sound("coin.mp3")
    sound.set_volume(volume)
    coins = 0
    try:
        while True:
            time.sleep(interval)
            coins += 1
            print("Gained 1 coin! That's", coins, "coins total!")
            sound.play()
            if debug_mode:
                print("Interval:", interval, "seconds")
    except KeyboardInterrupt:
        print("Timer stopped with", coins, "coins")


start_timer(2, 0.1, True)
