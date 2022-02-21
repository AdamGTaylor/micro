import machine
import utime
import _thread
import math


#conts
count = 0
period = 0.02
on1 = 0
on2 = 0
on3 = 0
on4 = 0
global sr; sr = 100;

global sav1; global sav2; sav1 = 0; sav2 = 0;
global av1; global av2; av1 = 0; av2 = 0;
global array1; global array2; array1 = []; array2 = [];
for i in range(sr):
    array1.append(0)
    array2.append(0)

#setup
led1f = machine.PWM(machine.Pin(15))
led2b = machine.PWM(machine.Pin(17))
led3r = machine.PWM(machine.Pin(16))
led4l = machine.PWM(machine.Pin(13))

led1f.freq(1000); led2b.freq(1000); led3r.freq(1000); led4l.freq(1000);

#joystick
vx = machine.ADC(27)
vy = machine.ADC(26)

def joys():
    global av1; global av2;
    global sav1; global sav2;
    av1 = 0; av2 = 0

    for i in range(sr):
        av1 += (vx.read_u16()/sr)
        av2 += (vy.read_u16()/sr)
        utime.sleep(0.0001)

    sav1 = av1; sav2 = av2;
    av1 = 0; av2 = 0;



utime.sleep(0.2)

while True:
    joys()
    #print("T: {0}\tX:{1}\tY: {2}\tSR : {3}".format((count),(round(sav1) ),(round(sav2) ),sr) )
    led1f.duty_u16(round(sav1))
    led2b.duty_u16(2**16 - round(sav1))
    led3r.duty_u16(round(sav2))
    led4l.duty_u16(2**16 - round(sav2))
    count += 1
    utime.sleep(0.01)
    