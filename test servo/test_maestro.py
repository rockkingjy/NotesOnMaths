import maestro


servo = maestro.Controller()


servo.setTarget(0, 6000) #control the yaw, 5000 left, 7000 right
servo.setTarget(1, 8000) #control the pitch, 5000 down, 8000 up
