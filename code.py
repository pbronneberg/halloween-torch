# SPDX-FileCopyrightText: 2023 Patrick Bronneberg
#
# SPDX-License-Identifier: MIT

import board
import neopixel

# 1 Neopixel LED on the MCU Board
BOARDPIXEL = neopixel.NeoPixel(board.NEOPIXEL, 1)

# External Neopixel ring on GPIO
NUMPIX = 7
PIXELS = neopixel.NeoPixel(board.GP4, NUMPIX)

while True:
    BOARDPIXEL[0] = (100, 0, 255)

    # Flame effect
    for i in range(0, NUMPIX):
        PIXELS[i] = (100, 0, 0)
