import machine
import utime
led_onboard = machine.Pin(25, machine.Pin.OUT)
count = 0
while True:
    while (count < 20):
        led_onboard.value(1)
        utime.sleep(0.001)
        led_onboard.value(0)
        utime.sleep(0.019)
        count += 1

    count = 0
    while (count < 20):
        led_onboard.value(1)
        utime.sleep(0.010)
        led_onboard.value(0)
        utime.sleep(0.010)
        count += 1
        
    count = 0
    while (count < 20):
        led_onboard.value(1)
        utime.sleep(0.019)
        led_onboard.value(0)
        utime.sleep(0.001)
        count += 1
    count = 0