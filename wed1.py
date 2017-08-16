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

# Functions


# Variables for the frame, pong ball, and paddles
frameWidth   = 640
frameHeight  = 480

# Create the frame
frame = simplegui.create_frame('Pong!', frameWidth, frameHeight)

# Boilerplate
frame.set_draw_handler()
frame.set_keydown_handler()
frame.set_keyup_handler()

# Set up the restart button
frame.add_button('Restart', newGame, 200)

# Start the game!
newGame()
frame.start()
