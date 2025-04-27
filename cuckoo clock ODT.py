from machine import Pin, PWM
import time

servo_motor = PWM(Pin(4), freq=50)
servo_motor2 = PWM(Pin(5), freq=50)
Buzz = Pin(15, Pin.OUT)

duty_0 = 28
duty_90 = 77
duty_45 = 52

servo_motor.duty(duty_0)
servo_motor2.duty(duty_0)

servo2_state = False

while True:
    servo_motor.duty(duty_45)
    Buzz.value(1)
    time.sleep(0.5)
    Buzz.value(0)
    time.sleep(0.5)
    servo_motor.duty(duty_0)

    for i in range(15):
        if servo2_state:
            servo_motor2.duty(duty_0)
        else:
            servo_motor2.duty(duty_90)
        servo2_state = not servo2_state
        time.sleep(1)
