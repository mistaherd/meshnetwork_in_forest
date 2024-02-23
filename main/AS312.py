#!/home/mistaherd/Documents/Github/meshnetwork_in_forest/env/lib/python3.11
import RPi.GPIO as GPIO
import time

pir_sensor = 2


GPIO.setmode(GPIO.BOARD)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
try:
    while True:
        time.sleep(0.1)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            print("GPIO pin %s is %s" % (pir_sensor, current_state))
        time.sleep(1)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
