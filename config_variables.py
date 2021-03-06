import sys
import pygame 

pygame.font.init()

#************************* General Constants ***************************************
FPS = 240
WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900
STARTING_POS = (WINDOW_WIDTH/2, WINDOW_HEIGHT-100)
SCORE_VELOCITY_MULTIPLYER = 0.00                        # Bonus scoring for faster
BAD_GENONE_TRESHOLD = 200                               # Car will be remove if it is too far off the screen
NUMBER_OF_INPUT_NEURONS = 9                             # Neuron Input node to help for input learning (Car Track Distance from center of the track(8 Node Sensor around the car), Speed)
NUMBER_OF_OUTPUT_NEURONS = 4                            # Neuron Output for controlling the Car (Acceleration, Brake, Left, Right)

#************************* Car Specification ***************************************
CAR_DBG = False
FRICTION = -0.1                                         # Car Friction, The higher the slower
MAX_VELOCITY = 10                                       # Max Velocity of the Car
MAX_VELOCITY_REDUCTION = 1                              # Reduce Maximum Velocity during start
ACCELETATION_STRENGTH = 0.2                             # Acceleration Strength
BRAKE_STREGTH = 1                                       # Brake Strength
TURN_VELOCITY = 2                                       # How fast it turn
SENSOR_DISTANCE = 200                                   # How far is the sensor sens
ACTIVATION_TRESHOLD = 0.5                               # When will the sensor triggered

#************************* Road Specification ***************************************

ROAD_DBG = False        
MAX_ANGLE = 1                                            # Maximum turn angle a road can generate
MAX_DEVIATION = 300                                      # Maximum Deviation a road can generate
SPACING = 200                                            # How wide the road spacing 
NUMBER_Pt  = 15                                          # Points for each segment
SAFE_SPACE = SPACING + 50                                # Space of buffer above the screen
ROAD_WIDTH = 200                                         # Road Width

#************************* Display and Colors ***************************************
NODE_RADIUS = 20
NODE_SPACING = 5
LAYER_SPACING = 100
CONNECTION_WIDTH = 1

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
DARK_RED = (100, 0, 0)
RED_PALE = (250, 200, 200)
DARK_RED_PALE = (150, 100, 100)
GREEN = (0, 200, 0)
DARK_GREEN = (0, 100, 0)
GREEN_PALE = (200, 250, 200)
DARK_GREEN_PALE = (100, 150, 100)
BLUE = (0,0,255)
BLUE_PALE = (200, 200, 255)
DARK_BLUE = (100, 100, 150)

NODE_FONT = pygame.font.SysFont("comicsans", 15)
STAT_FONT = pygame.font.SysFont("comicsans", 50)

#************************* Internal Constants ***************************************
GENENRATION = 0

#enum
ACCELETATION = 0
BRAKE = 1
TURNLEFT = 2
TURNRIGHT = 3

INPUT = 0
MIDDLE = 1
OUTPUT = 2