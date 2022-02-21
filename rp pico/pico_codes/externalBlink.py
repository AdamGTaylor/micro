import machine
import utime

led1 = machine.Pin(14, machine.Pin.OUT)
led2 = machine.Pin(17, machine.Pin.OUT)
count = 0
limit = 20
test = False

led1.value(0)
led2.value(0)

if (not test):
    while (count < limit):
        led1.value(1)
        led2.value(1)
        utime.sleep(0.1)
        led1.value(0)
        led2.value(0)
        utime.sleep(0.1)
        count += 1

if (test):
    while (count < limit):
        led1.value(1)
        utime.sleep(0.005)
        led1.value(0)
        utime.sleep(0.005)
        count += 1
    
led1.value(0)
led2.value(0)