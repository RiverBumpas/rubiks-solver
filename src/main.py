# import twophase.solver as sv
# import twophase.cubie as cubie
#import RPi.GPIO as GPIO
#import stepper
from camera import CubeCamera, CubeFace, FaceCaptureGroup
import web.app

# MOTOR PIN MAPPINGS
# DO NOT CHANGE
STEP_1 = 37
STEP_2 = 33
STEP_3 = 15
STEP_4 = 38
STEP_5 = 32
STEP_6 = 16

DIR_1 = 35
DIR_2 = 31
DIR_3 = 13
DIR_4 = 40
DIR_5 = 36
DIR_6 = 18

# TODO: Setup cameras in static position
# TODO: Create capture groups for each face
g_up = FaceCaptureGroup(CubeFace.UP, [[(5,5), (200, 200), (260, 250)]])


upper_cam = CubeCamera(0, [g_up], True) # start upper camera capture
web.app.add_camera_feed(upper_cam.gen_bytes(), "upper") # send cam feed to flask app

lower_cam = CubeCamera(1, [g_up], True) 
web.app.add_camera_feed(lower_cam.gen_bytes(), "lower") 


# GPIO.setmode(GPIO.BOARD)

#motor1 = stepper.Motor(STEP_1, DIR_1)
#motor2 = stepper.Motor(STEP_2, DIR_2)
#motor3 = stepper.Motor(STEP_3, DIR_3)
#motor4 = stepper.Motor(STEP_4, DIR_4)
#motor5 = stepper.Motor(STEP_5, DIR_5)
#motor6 = stepper.Motor(STEP_6, DIR_6)
#
#
#motor3.rotate_180()


#GPIO.cleanup()


def solve() -> bool:
    # cc = cubie.CubieCube()
    # cc.randomize()
    # fc = cc.to_facelet_cube()
    # cubestring = fc.to_string()
    # cubestring = "ULRRUBUBFDRFURBRFLRDLFFRLLDBUBUDDUDBBDFRLULBUDFRLBFDLF"
    # print(sv.solve(cubestring, 20, 1))
    print("solving")
    return True

# Bind solve to the web app's /solve route
web.app.bind_solve_fn(solve)

# Start flask server
web.app.start()
