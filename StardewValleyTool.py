import cv2
import time
import ctypes
import random
import numpy as np
from vncdotool import api


class StardewValleyTool():
    # Windows API constants
    MOUSEEVENTF_MOVE = 0x0001
    MOUSEEVENTF_LEFTDOWN = 0x0002
    MOUSEEVENTF_LEFTUP = 0x0004

    user32 = ctypes.windll.user32
    SetForegroundWindow = ctypes.windll.user32.SetForegroundWindow

    # Store the found window
    hwnd = []

    def foreach_window(self, testhwnd, lParam):
        if self.user32.IsWindowVisible(testhwnd):
            length = self.user32.GetWindowTextLengthW(testhwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            self.user32.GetWindowTextW(testhwnd, buff, length + 1)
            title = buff.value
            if title.startswith("Stardew Valley"):  # Only match the beginning of the title
                self.hwnd.append(testhwnd)
                return False  # Stop enumeration when found
        return True

    def __init__(self):
        pass 
    
    def run(self):
        # Define the callback function prototype
        self.user32.EnumWindows(ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.c_int)(self.foreach_window), 0)

        if len(self.hwnd) == 0:
            print("Cannot find Stardew Valley window")
            exit(1)
        else:
            self.hwnd = self.hwnd[0]
            self.SetForegroundWindow(self.hwnd)

        # Simulate mouse movement and clicking function
        offset = 100
        def click(x, y):
            # Move to a nearby position (random offset of a few pixels)
            start_x = x + random.randint(-offset, offset)
            start_y = y + random.randint(-offset, offset)
            self.user32.SetCursorPos(start_x, start_y)
            time.sleep(0.1)

            # Smoothly move to the target
            steps = max(abs(x - start_x), abs(y - start_y), 10)
            dx = (x - start_x) / steps
            dy = (y - start_y) / steps
            delay = 0.01  # Delay per step

            for i in range(steps):
                self.user32.SetCursorPos(int(start_x + dx*i), int(start_y + dy*i))
                time.sleep(delay)

            self.user32.SetCursorPos(x, y)
            time.sleep(0.05)

            # Double click
            for _ in range(2):
                self.user32.mouse_event(self.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                time.sleep(0.3)
                self.user32.mouse_event(self.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                time.sleep(0.3)
                
            self.user32.SetCursorPos(10, 10)


        # Load the target image
        template = cv2.imread("ok.png", cv2.IMREAD_COLOR)
        if template is None:
            raise Exception("Cannot find ok.png")

        # Get the template size
        h, w = template.shape[:2]

        # Set the scaling range (0.8~1.2)
        scales = np.linspace(0.8, 1.2, 9)

        # Set the matching threshold
        threshold = 0.8


        # Connect to local TightVNC (no password)
        client = api.connect('127.0.0.1::5900')

        while True:
            self.SetForegroundWindow(self.hwnd)
            
            # Capture screen from VNC server and save it
            filename = 'vnc_frame.png'
            client.captureScreen(filename)

            # Read the screenshot and perform template matching
            screen = cv2.imread(filename, cv2.IMREAD_COLOR)

            found = False

            for scale in scales:
                # Scale the template
                scaled_template = cv2.resize(template, (int(w*scale), int(h*scale)))
                th, tw = scaled_template.shape[:2]

                # Perform template matching
                res = cv2.matchTemplate(screen, scaled_template, cv2.TM_CCOEFF_NORMED)
                min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

                if max_val >= threshold:
                    x, y = max_loc
                    # Calculate the center of the match
                    cx = x + tw // 2
                    cy = y + th // 2
                    click(cx, cy)  # Use Windows API to click
                    print(f"Found button! Scale {scale:.2f}, Click position ({cx},{cy})")
                    found = True
                    break

            if not found:
                print("Button not found")

            time.sleep(1)

        # Disconnect when finished
        client.disconnect()


if __name__ == "__main__":
    tool = StardewValleyTool()
    
    tool.run()