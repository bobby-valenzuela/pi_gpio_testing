# bluedot to trigger pic

from bluedot import BlueDot
import os

bd = BlueDot()

while True:

    bd.wait_for_press()
    print("M. Scott pressed the blue dot!")
    
    os.system("libcamera-jpeg -o img.jpg")
