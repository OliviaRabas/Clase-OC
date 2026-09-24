import time
import board
import neopixel
import random
import RPi.GPIO as GPIO
def leerboton ():
    return GPIO.input(17) 

boton=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(boton,GPIO.IN)



pixel_pin = board.D18
num_pixels = 16
ORDER = neopixel.GRB 

pixels = neopixel.NeoPixel(
    pixel_pin, num_pixels, brightness=0.2, auto_write=False, pixel_order=ORDER
)


while True:
    tiempo=1
    A=0
    eleccion= random.randint(1,10)
    while A==0:
        
        for indice in range(16):
            pixels[indice]=(0,0,255)
            pixels[eleccion]=(255,0,0)
            pixels.show()
            print(leerboton())
               
           # if leerboton()==False:
           #     if indice==eleccion:
           #         pixels.fill=(0,255,0)
           #         time.sleep(2)
           #         pixels.fill=(0,0,0)
        #         tiempo=tiempo-0.2

                
              
         #       else:
          #          pixels.fill=(255,0,0)
           #         time.sleep(2)
            #        pixels.fill=(0,0,0)
            #        A=A+1
             #       break
                       
            time.sleep(tiempo)
            pixels[indice]=(0,0,0)
            pixels.show()
            

