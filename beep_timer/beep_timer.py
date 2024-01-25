#!/usr/bin/python3
"""
This script plays a beep sound at regular intervals using the pygame library.

The script defines two functions:
- play_sound(): Plays a beep sound with optional volume adjustment.
- beep_every_10_minutes(): Continuously plays a beep sound every 10
                           minutes with optional volume adjustment.

Example:
    To run the script:
    ```
    python script_name.py
    ```

Dependencies:
- pygame: The pygame library is used to handle sound playback.

Note:
- Replace "beep.wav" with the path to your own sound file.
"""
import time
# import winsound
import sys
import pygame


def play_sound(volume=1.0):
    """
    Play a beep sound with optional volume adjustment.

    Args:
    - volume (float): The volume of the sound to be played (0.0 to 1.0).
                      Default is 1.0 (maximum volume).
    """
    pygame.mixer.init()
    sound = pygame.mixer.Sound("beep.wav")
    sound.set_volume(volume)  # Set the volume (0.0 to 1.0)
    sound.play()
    time.sleep(1)  # Wait for the sound to finish playing


def beep_every_10_minutes():
    """
    Continuously play a beep sound every 10 minutes.
    """
    try:
        while True:
            # Wait for 10 minutes
            time.sleep(600)  # 10 minutes = 600 seconds
            # Produce a beep sound
            # winsound.Beep(1000,1000) # Freq = 1000Hz, Dur = 1000ms (1 second)
            # sys.stdout.write('\a')
            # sys.stdout.flush()
            play_sound()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
        sys.exit()


if __name__ == "__main__":
    beep_every_10_minutes()
