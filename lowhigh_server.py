#!/usr/bin/python3
'''
Subclasses BluetoothSocket to serve messages "LOW" and "HIGH" based on values received from
client

Copyright Simon D. Levy 2018

MIT License
'''

from bluetooth_server import BluetoothServer
import Motor
import Actions
class LowHighServer(BluetoothServer):

    def __init__(self):

        BluetoothServer.__init__(self)

    def handleMessage(self, message):

        print(message)

        if message == "forward":
            Motor.Motor_Forward()

        if message == "backward":
            Motor.Motor_Backward()

        if message == "left":
            Motor.Motor_TurnLeft()

        if message == "right":
            Motor.Motor_TurnRight()

        if message == "stop":
            Motor.Motor_Stop()

        if message == "forwardwaypoint":
            Actions.moveToAForwardWayPoint()

        if message == "backwardwaypoint":
            Actions.moveToABackwardWayPoint()

        if message == "leftwaypoint":
            Actions.moveToALeftWayPoint()

        if message == "rightwaypoint":
            Actions.moveToARightWayPoint()

        if message == "stopwaypoint":
            Motor.Motor_Stop()


        self.send(' Success '+message)


        #self.send('LOW' if int(message) < 50 else 'HIGH')

if __name__ == '__main__':

    server = LowHighServer()

    server.start()
