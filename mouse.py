import math
import pyautogui as pg

class Mouse():
    def __init__(self):
        self.right_down = False
        self.left_down = False
        self.current_pos = None
        self.prev_pos = None

    def distanceBetweenFingers(self, x, X, y, Y):
        distance = math.sqrt(((x-X)**2)+((y-Y)**2))
        return distance

    def leftClick(self, distanceI, distanceM, x, y):
        if distanceI <= 70 and distanceM > 100:
            pg.click(x, y)
    
    def rightClick(self, distanceR, distanceM, x, y):
        if distanceR <= 70 and distanceM > 100:
            pg.click(x, y, button="right")

    def updatePos(self, x, y):
        pg.moveTo(x, y)

    def volume(self, distanceM, distaneR, distanceI):
        if  distanceM <= 70 and distaneR <= 70:
            volume_increment = distanceI
            print(volume_increment)
            if volume_increment > 175:
                    pg.press('volumeup')
            else:
                    pg.press('volumedown')
