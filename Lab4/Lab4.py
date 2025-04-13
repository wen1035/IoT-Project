import RPi.GPIO as GPIO
import time
import serial

BUZZ_PIN = 16
pitches = [262, 294, 330, 349, 392, 440, 493]
arr={'C':262,'D':294,'E':330,'F':349,'G':392,'A':440,'B':493}

LED_PIN = 12
# pitches = [262, 294, 330, 349, 392, 440, 493, 523, 587, 659, 698, 784, 880, 932, 988]
GPIO.setmode(GPIO.BOARD)
GPIO.setup(BUZZ_PIN, GPIO.OUT)
GPIO.setup(LED_PIN, GPIO.OUT)

def play(pitch,i):
    pwm.ChangeFrequency(pitch)
    time.sleep(i)

pwm1 = GPIO.PWM(BUZZ_PIN, pitches[0])
pwm = GPIO.PWM(LED_PIN, 100)
pwm1.start(0)
pwm.start(0)
ser = serial.Serial('/dev/ttyAMA1', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )

try:
    while True :   

        #b = ser.readline()
        #print(b.decode("utf-8").strip())
        #ser.write(b)
        #ser.flushInput()
        b=input()
       # print(b.decode("utf-8").strip())
        time.sleep(0.1)

        if str(b)=="play C":  #.decode("utf-8").strip()
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(262))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=="play D":
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(294))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=='play E':            
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(330))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=='play F':
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(349))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=='play G':
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(392))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=='play A':
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(440))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        elif str(b)=='play B':           
                pwm1.ChangeDutyCycle(50)            
                pwm1.ChangeFrequency(int(493))
                time.sleep(1)              
                pwm1.ChangeDutyCycle(0)
        else :  
            n = b
            if not int(n) > 100 or int(n) < 0: # n.isdigit() or 
                pwm.ChangeDutyCycle(int(n))
                time.sleep(5)
except KeyboardInterrupt:
    pass
pwm.stop()
pwm1.stop()
GPIO.cleanup()



'''
try:
    while True:
        pwm.ChangeDutyCycle(50)
        for pitch in pitches:
            play(pitch)
        pwm.ChangeDutyCycle(0)
        time.sleep(5)
except KeyboardInterrupt:
    pass
pwm.stop()
GPIO.cleanup()


ser = serial.Serial('/dev/ttyAMA1', baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE,
                    bytesize=serial.EIGHTBITS
                    )
try:
    ser.write(b'Hello World\r\n')
    ser.write(b'Serial Communication Using Raspberry Pi\r\n')
    while True:    
        data = ser.readline()
        print(data.decode("utf-8").strip())
        ser.write(data)
        ser.flushInput()
        time.sleep(0.1)
except KeyboardInterrupt:
    pass
finally:
    ser.close()


'''


