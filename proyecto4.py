import time
import board
import neopixel

# Configuración del Pixel
pixel_pin = board.D18
num_pixels = 16
 # Número de LEDs en tu tira
ORDER = neopixel.GRB # Orden de colores (A veces es RGB)

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)



try:
    while True:
        for indice in range(0,16):
            pixels[indice]=(255,0,0)
            pixels.show()
            time.sleep(0.1)
            pixels[indice]=(0,0,0)
       

except KeyboardInterrupt:
    pixels.fill((0, 0, 0))
    pixels.show()
