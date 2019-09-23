import RPi.GPIO as GPIO
from smbus2 import SMBus, i2c_msg
import time
import threading


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

A_Bttn = 18 #Remote Button A
B_Bttn = 23 #Remote Button B
C_Bttn = 24 #Remote Button C
D_Bttn = 25 #Remote Button D, Extra - not used for now

GPIO.setup(A_Bttn,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(B_Bttn,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(C_Bttn,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Button A logic 
def Button_A(): 
    while True:
        if GPIO.input(A_Bttn) == GPIO.HIGH:
            print("A_button is ON")
        elif GPIO.input(A_Bttn)  == GPIO.LOW:
            print("A_button is OFF")
        time.sleep(1)

#Button B logic
def Button_B(): 
    while True:
        if GPIO.input(B_Bttn) == GPIO.HIGH:
            print("B_button is ON")
        elif GPIO.input(B_Bttn) == GPIO.LOW:
            print("B_button is OFF")
        time.sleep(1)
        
#Button C logic
def Button_C(): 
    while True:
        if GPIO.input(C_Bttn) == GPIO.HIGH:
            print("B_button is ON")
        elif GPIO.input(C_Bttn) == GPIO.LOW:
            print("B_button is OFF")
        time.sleep(1)

def main():
    thread1 = threading.Thread(target= Button_A,args=())
    thread1.setDaemon = True
    thread1.start()
    time.sleep(.5)
    thread2 = threading.Thread(target= Button_B,args=())
    thread2.setDaemon = True
    thread2.start()
    
if __name__ == '__main__':
    main()








            
            
        
