### PT-CAN Gear Position Reader ###

import can
import can.interfaces
from can.interface import Bus
from can import Message
import subprocess
from subprocess import call
import time 
import datetime
import threading

listener = None
notifier = None
bus = None
gearPos = None

class Gear_Position_Rx():

    def __init__(self):
        self.GEAR_POSITION_ID = 0x196 #GearPosition ID
        
    def gear_stat(self,msg):
        if msg.arbitration_id == self.GEAR_POSITION_ID:
            self.gear_stat_pos(msg)
        else:
            print('Invalid ID')
            pass
    def gear_stat_pos(self,msg):
        actuated_gear = {0: "P", 1: "R", 2: "N", 3: "D"}
        self.actuated_gear_pos = (msg.data[0] & 0x7)
        current_gear = actuated_gear[self.actuated_gear_pos]
        self.gear = current_gear
        print(self.gear)
        
    def get_gear(self):
        return self.gear()
        

def recieve_thread():
    print('Start Receiving')
    while True:     
        try:        
            msg = listener.get_message(timeout = 0.05)
            if msg != None:
                gearPos.gear_stat(msg)     
        except Exception as e:
                print('Unable to read on CAN bus: ' + str(e))

        
def initCAN():
    global bus
    global listener
    global notifier
    can.rc['interface'] = 'socketcan'
    can.rc['bitrate'] = 500000
    can.rc['channel'] = 'can0'

    try:
        bus = Bus()
        listener = can.BufferedReader()
        notifier = can.Notifier(bus, [listener])
        
    except Exception as e:
        print ('ERR: ' + str(e))

def main():
    global gearPos
    initCAN()
    gearPos = Gear_Position_Rx()
    thread1 = threading.Thread(target = recieve_thread, args=())
    thread1.setDaemon = True
    thread1.start()
if __name__ == '__main__':
    main()


        
        
