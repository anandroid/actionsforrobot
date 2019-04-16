import Motor
import time
import Motor_Timers



def moveToALeftWayPoint():
    Motor.Motor_TurnLeft()
    time.sleep(Motor_Timers.NINETY_DEGREES_ROTATE_TIMER)
    Motor.Motor_Forward()
    time.sleep(Motor_Timers.WAYPOINT_FORWARD_TIMER)
    Motor.Motor_Stop()

def moveToARightWayPoint():
    Motor.Motor_TurnRight()
    time.sleep(Motor_Timers.NINETY_DEGREES_ROTATE_TIMER)
    Motor.Motor_Forward()
    time.sleep(Motor_Timers.WAYPOINT_FORWARD_TIMER)
    Motor.Motor_Stop()

def moveToAForwardWayPoint():
    Motor.Motor_Forward()
    time.sleep(Motor_Timers.WAYPOINT_FORWARD_TIMER)
    Motor.Motor_Stop()

def moveToABackwardWayPoint():
    Motor.Motor_TurnLeft()
    time.sleep(Motor_Timers.ONEIGHTY_DEGREES_ROTATE_TIME)
    Motor.Motor_Forward()
    time.sleep(Motor_Timers.WAYPOINT_FORWARD_TIMER)
    Motor.Motor_Stop()







