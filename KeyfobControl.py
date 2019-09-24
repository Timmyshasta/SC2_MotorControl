from gpiozero import LED, Button
from signal import pause
import time

door_open = None #Flag
remote = None

class Remote_Keyfob():
    def __init__(self):
        self.A_Button = Button(18)   #Remote Button A
        self.B_Button = Button(23)   #Remote Button B
        self.C_Button = Button(24)   #Remote Button B
        self.D_Button = Button(25)   #Remote Button B

        #Connect keyfob A button with Button_A function
        self.A_Button.when_pressed = self.Button_A

        #Connect keyfob B button with Button_A function
        self.B_Button.when_pressed = self.Button_B
        
        #Connect keyfob C button with Button_A function
        self.C_Button.when_pressed = self.Button_C

    
    def Button_A(self):  
        #### This is a place holder for function logic ######
        #### when keyfob A button is pressed ################
        
        global door_open
        
        if door_open:
            print("Now closing door A")
            time.sleep(.5)
            door_open = False
        else:
            print("Now opening door A")
            door_open = True
            
    def Button_B(self):        
        #### This is a place holder for function logic ######
        #### when keyfob B button is pressed ################
        
        global door_open
        
        if door_open:
            print("Now closing door B")
            time.sleep(.5)
            door_open = False
        else:
            print("Now opening door B")
            door_open = True

    def Button_C(self):        
        #### This is a place holder for function logic ######
        #### when keyfob C button is pressed ################
        
        global door_open
        
        if door_open:
            print("Now closing door C")
            time.sleep(.5)
            door_open = False
        else:
            print("Now opening door C")
            door_open = True         


def main():
    global door_open
    global rem
    door_open = True 
    remote = Remote_Keyfob()
    remote
    while True:
        pass

        
if __name__ == '__main__':
    main()
