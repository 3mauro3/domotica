from microbit import *


while True:
    luz = pin1.read_analog()
    if luz < 700:# Comprobar si el valor de la luz es inferior a 600
        pin14.write_digital(1) # Encender el LED conectado al pin 14
    else:
        pin14.write_digital(0) # Apagar el LED conectado al pin 14
