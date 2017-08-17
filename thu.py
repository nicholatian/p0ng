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
ballVelocity = [1, 1]
frameName    = 'Pong!'
LEFT  = False
RIGHT = True
paddle1Position = frameHeight / 2.5
paddle2Position = frameHeight / 2.5
paddle1Velocity = 0
paddle2Velocity = 0
paddleVelocity = 5

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
        halfFrameW, halfFrameH, ballPosition, ballVelocity, paddle1Position, \
        paddle2Position, score1, score2
    
    canvas.draw_line([halfFrameW, 0], [halfFrameW, frameHeight], 5, 'red')
    canvas.draw_line([paddleWidth, 0], [paddleWidth, frameHeight], 3, 'brown')
    canvas.draw_line([frameWidth - paddleWidth, 0], \
        [frameWidth - paddleWidth, frameHeight], 3, 'brown')
    
    # update ball
    ballPosition[0] += ballVelocity[0]
    ballPosition[1] += ballVelocity[1]
    
    if ballPosition[0] <= (ballRadius + paddleWidth) or ballPosition[0] >= (frameWidth - paddleWidth - ballRadius):        
        ballVelocity[0] *= -1
        
        if (ballPosition[0] > halfFrameW):             
            if (ballPosition[1] < paddle2Position or ballPosition[1] > paddle2Position + paddleHeight):
                score1 += 1 
                spawnBall(LEFT) 
            else: ballVelocity[0] += .1 * ballVelocity[0]
        
        if (ballPosition[0] < halfFrameW):
            if (ballPosition[1] < paddle1Position or ballPosition[1] > paddle1Position + paddleHeight):
                score2 += 1
                spawnBall(RIGHT)
            else: ballVelocity[0] += .1 * ballVelocity[0]
    
    if ballPosition[1] <= ballRadius or ballPosition[1] >= (frameHeight - ballRadius):
        ballVelocity[1] *= -1
    
    # draw the ball
    canvas.draw_circle(ballPosition, ballRadius, 2, "white", "green")
    
    # update paddle's vertical position, keep paddle on the screen
    
    if (paddle1Position <= frameHeight - paddleHeight and paddle1Velocity > 0) or (paddle1Position >= 0 and paddle1Velocity < 0):
        paddle1Position += paddle1Velocity
    elif (paddle2Position <= frameHeight - paddleHeight and paddle2Velocity > 0) or (paddle2Position >= 0 and paddle2Velocity < 0):
        paddle2Position += paddle2Velocity
    
    #c.draw_polygon([[0, paddle1Position], [pad_width, paddle1_pos],[pad_width, (paddle1_pos) + pad_height ],[0, (paddle1_pos) + pad_height]],1, "green", "white") 
    #c.draw_polygon([[width, paddle2_pos], [width - pad_width, paddle2_pos], [width - pad_width, paddle2_pos + pad_height], [width, paddle2_pos + pad_height]],1, "green", "white")
    canvas.draw_polygon([[0, paddle1Position], [paddleWidth, paddle1Position],\
    [paddleWidth, paddle1Position + paddleHeight], [0, paddle1Position + \
    paddleHeight]], 2, 'green', 'red')

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
