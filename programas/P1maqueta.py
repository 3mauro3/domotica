from microbit import *
import neopixel


np = neopixel.NeoPixel(pin13, 2)

np.clear()
while True:

temp = temperature()

if temp > 24:
        np[0] = (255, 0, 0)
        np[1] = (255, 0, 0)
        np.show()
        pin16.write_digital(1)

elif temp > 24:
        np[0] = (255, 165, 0)
        np[1] = (255, 165, 0)
        np.show()
        pin16.write_digital(1)

elif temp > 20:
        np[0] = (0, 255, 0)
        np[1] = (0, 0, 255)
        np.show()
        pin16.write_digital(0)

elif temp >= 18 and temperatura <= 20:
        np[0] = (0, 0, 255)
        np[1] = (0, 0, 255)
        np.show()
        pin16.write_digital(0)

else:
        np[0] = (0, 0, 0)
        np[1] = (0, 0, 0)
        np.clenp.clear()
        pin16.write_digital()

