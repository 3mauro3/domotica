"""| 𝕄𝔸ℚ𝕌𝔼𝕋𝔸 𝕋𝔼𝕀𝕊 𝟜 |𝔽𝕖𝕔𝕙𝕒: 𝟝/𝟘𝟝/𝟚𝟝"""


from microbit import *
import neopixel
import music

np = neopixel.NeoPixel(pin13, 2)  # 2 LED neopixel conectados ao pin 13

led = pin14 # LED branco conectado ao pin14
np.clear()
while True:
    temperatura = temperature() # gardamos valor da temperatura

    if temperatura > 20:
        np[0] = (0, 255, 0)  # Acender os Neopixel en vermello
        np[1] = (0, 255, 0)
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(1)  # Acender o LED normal
    else:
        np[0] = (255, 0, 0)  # Apagar os Neopixel
        np[1] = (255, 0, 0)  # Acender os Neopixel en verde
        np.show()  # Mostrar a cor nos neopixel
        led.write_digital(0)  # Apagar o LED normal



#Programa 3 reproduce musica si se presiona el boton A#

while True:
    if button_a.is_pressed():
        pin14.write_digital(1)  # Encende o pin 14 LED
        music.play(music.RINGTONE)   # Reproduce o tono RINGTONE
        sleep(5000)   # Manten o LED acendido durante 5 segundos
        pin14.write_digital(0)   # Apaga o pin 14 (LED)

#Programa 5 Sistema de alarma con detección de  movemento#

# Configuración de pins
np = neopixel.NeoPixel(pin13, 6)
sensor_pir = pin15
led_blanco = pin14

def modo_normal():
    display.show(Image.HOUSE)

def alerta():
    # Sonar alerta 2 veces
    music.play(music.BA_DING, wait=True)
    sleep(100)
    music.play(music.BA_DING, wait=True)

    for i in range(5):
        # Encender todos los neopixels en rojo
        for j in range(6):
            np[j] = (255, 0, 0)
        np.show()

        led_blanco.write_digital(1)
        display.show(Image.ANGRY)
        sleep(500)

        # Apagar
        for j in range(6):
            np[j] = (0, 0, 0)
        np.show()

        led_blanco.write_digital(0)
        display.clear()
        sleep(500)

modo_normal()  # Mostrar estado normal al iniciar

# Loop principal
while True:
    if sensor_pir.read_digital() == 1:
        alerta()
    else:
        modo_normal()
    sleep(100)

