import time
import pyautogui
import random

def simulate_continuous_mouse_movement():
    try:
        while True:
            x, y = random.randint(0, 1920), random.randint(0, 1080)
            pyautogui.moveTo(x, y, duration=0.25)   
            time.sleep(15)
            pyautogui.press('space')
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    # Run the mouse movement
    simulate_continuous_mouse_movement()
 