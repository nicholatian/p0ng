#!/usr/bin/env python3
#
## This Source Code Form is subject to the terms of the Mozilla Public
## License, v. 2.0. If a copy of the MPL was not distributed with this
## file, You can obtain one at http://mozilla.org/MPL/2.0/.

##    8 888888888o       ,o888888o.     b.             8     ,o888888o.
##    8 8888    `88.  . 8888     `88.   888o.          8    8888     `88.
##    8 8888     `88 ,8 8888       `8b  Y88888o.       8 ,8 8888       `8.
##    8 8888     ,88 88 8888        `8b .`Y888888o.    8 88 8888
##    8 8888.   ,88' 88 8888         88 8o. `Y888888o. 8 88 8888
##    8 888888888P'  88 8888         88 8`Y8o. `Y88888o8 88 8888
##    8 8888         88 8888        ,8P 8   `Y8o. `Y8888 88 8888   8888888
##    8 8888         `8 8888       ,8P  8      `Y8o. `Y8 `8 8888       .8'
##    8 8888          ` 8888     ,88'   8         `Y8o.`    8888     ,88'
##    8 8888             `8888888P'     8            `Yo     `8888888P'

# Import our modules
import simplegui
import random

# Variables
gameStarted  = False
score1       = 0
score2       = 0
ballRadius   = 20
paddleWidth  = 8
paddleHeight = 96
frameWidth   = 640
frameHeight  = 480
halfFrameW   = frameWidth / 2
halfFrameH   = frameHeight / 2
ballPosition = [halfFrameW, halfFrameH]
ballVelocity = [0, 1]
frameName    = 'Pong!'
LEFT  = False
RIGHT = True

# Functions
def spawnBall(direction):
    global ballPosition, ballVelocity
    ballPosition = [halfFrameW, halfFrameH]
    ballVelocity[0] = -random.randrange(120, 240) / 100
    if direction == RIGHT:
        ballVelocity[0] *= -1
    ballVelocity[1] = -random.randrange(60, 180) / 100

def restart():
    global gameStarted
    if gameStarted == True:
        pass
    else:
        return

def newGame():
    global gameStarted
    gameStarted = True
    spawnBall(LEFT)

def draw(canvas):
    global ballRadius, paddleWidth, paddleHeight, frameWidth, frameHeight, \
        halfFrameW, halfFrameH, ballPosition, ballVelocity
    
    canvas.draw_line([halfFrameW, 0], [halfFrameW, frameHeight], 5, 'red')
    canvas.draw_line([paddleWidth, 0], [paddleWidth, frameHeight], 3, 'brown')
    canvas.draw_line([frameWidth - paddleWidth, 0], \
        [frameWidth - paddleWidth, frameHeight], 3, 'brown')
    
    # update ball
    ballPosition[0] += ballVelocity[0]
    ballPosition[1] += ballVelocity[1]

def keyDown(key):
    pass

def keyUp(key):
    pass

# Create the frame
frame = simplegui.create_frame(frameName, frameWidth, frameHeight)

# Boilerplate
frame.set_draw_handler(draw)
frame.set_keydown_handler(keyDown)
frame.set_keyup_handler(keyUp)

# Set up the restart button
frame.add_button('Restart', restart, 150)
frame.add_button('New Game', newGame, 150)

# Start the game!
#newGame()
frame.start()
