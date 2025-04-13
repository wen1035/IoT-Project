import RPi.GPIO as GPIO
import time

LED_PINS = [15, 16]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(LED_PINS[0], GPIO.OUT)
GPIO.setup(LED_PINS[1], GPIO.OUT)

#GPIO.setmode(GPIO.BOARD)
#BTN_PIN = 13
#WAIT_TIME = 0.2
#GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
#previousStatus = None
#previousTime = time.time()
#currentTime = None
a=0
def ButtonPressed(btn):
    global a
    a+=1
GPIO.setmode(GPIO.BOARD)
BTN_PIN = 13
GPIO.setup(BTN_PIN, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.add_event_detect(BTN_PIN, GPIO.FALLING, ButtonPressed, 200)


try:
    while True:
        """input = GPIO.input(BTN_PIN)
        currentTime = time.time()
        if input == GPIO.LOW and previousStatus == GPIO.HIGH and (currentTime - previousTime) > WAIT_TIME:
            previousTime = currentTime
            a+=1 
        previousStatus = input"""

        if a%3==0:
            GPIO.output(LED_PINS[0], GPIO.HIGH)
            GPIO.output(LED_PINS[1], GPIO.HIGH)
        elif a%3==1:
            GPIO.output(LED_PINS[0], GPIO.LOW)
            GPIO.output(LED_PINS[1], GPIO.LOW)
        else:
            counter = 1
            while True :
                if a%3==0:
                    break
                for i in range(2):
                    if (counter >> i) & 0x00000001:
                        GPIO.output(LED_PINS[i], GPIO.HIGH)
                    elif a%3==0:
                        break
                    else:
                        GPIO.output(LED_PINS[i], GPIO.LOW)
                        
                counter = counter << 1
                if counter > 2:
                    counter = 1
                time.sleep(1)

except KeyboardInterrupt:
    print("Exception: KeyboardInterrupt")

finally:
    GPIO.cleanup()