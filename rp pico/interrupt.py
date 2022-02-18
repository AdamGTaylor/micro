import machine
import utime
import _thread

count = 0

led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)
button = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_DOWN)

global button_pressed
button_pressed = False

def ledON():
    led1.value(1)
    utime.sleep(0.003)
    led1.value(0)
    utime.sleep(0.007)
    

def button_reader_thread():
    global button_pressed
    while True:
        if button.value() == 1:
            button_pressed = True
        if button.value() == 0:
            button_pressed = False
        utime.sleep(0.01)
_thread.start_new_thread(button_reader_thread, ())



while True:
    if button_pressed == True:
        led1.value(0)
        led2.value(1)
        utime.sleep(0.1)
    if button_pressed == False:
        led2.value(0)
        ledON()
