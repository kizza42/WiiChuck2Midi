############################################################################
# Wii Nunchuck to Midi
# import time  #If we need to do waits
import board
import adafruit_nunchuk
import usb_midi
import adafruit_midi
import neopixel

from adafruit_midi.note_on import NoteOn
from adafruit_midi.note_off import NoteOff

# neopixel setup
pixels = neopixel.NeoPixel(board.NEOPIXEL, 1)
RED = (255, 0, 0)
YELLOW = (255, 150, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
BLUE = (0, 0, 255)
PURPLE = (180, 0, 255)
OFF = (0, 0, 0)
WHITE = (200, 200, 200)
# Usage: pixels.fill(RED)


#  nunchuck setup
nc = adafruit_nunchuk.Nunchuk(board.STEMMA_I2C())
centerX = 128  # Not in use
centerY = 128  # Not in use
scaleX = 0.3  # Not in use
scaleY = 0.3  # Not in use
cDown = False
zDown = False
jLeft = False
jRight = False
jUp = False
jDown = False
CHECK_COUNT = 0  # This is to allow double checking not sure it works


#  midi setup
usb_midi = adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=0, debug=True)

print("Wii Nunchuck to Midi")
while True:

    x, y = nc.joystick
    if x == 255 or y == 255:  # Eliminate spurious reads
        continue
    right = x >= 200
    left = x <= 64
    up = y >= 200
    down = y <= 64
    # print("joystick = {},{}".format(x, y)) # Joystick Output debugging

    buttons = nc.buttons
    c = buttons.C
    z = buttons.Z
    
    ### Z Button ###
    if z and not zDown:
        stillDown = True
        for n in range(CHECK_COUNT):
            if nc.button_Z:
                stillDown = False
                break
        if stillDown:
            print("button Z")
            usb_midi.send(NoteOn(10, 127))  # Turn midi note on 10 velocity 127.
            pixels.fill(GREEN)
            zDown = True
    elif not z and zDown:
        stillDown = True
        for n in range(CHECK_COUNT):
            if not nc.button_Z:
                stillDown = False
                break
        if stillDown:
            usb_midi.send(NoteOff(10, 0))  # Turn midi note off 10 velocity 0.
            pixels.fill(OFF)
            zDown = False
    ### C Button ###
    if c and not cDown:
        print("button C")
        usb_midi.send(NoteOn(11, 127))
        pixels.fill(RED)
        cDown = True
    elif not c and cDown:
        usb_midi.send(NoteOff(11, 0))
        pixels.fill(WHITE)
        cDown = False
    ### Joystick Left ###
    if left and not jLeft:
        print("Joystick Left")
        usb_midi.send(NoteOn(12, 127))
        pixels.fill(BLUE)
        jLeft = True
    elif not left and jLeft:
        usb_midi.send(NoteOff(12, 0))
        pixels.fill(OFF)
        jLeft = False
    ### Joystick Right ###
    if right and not jRight:
        print("Joystick Right")
        usb_midi.send(NoteOn(13, 127))
        pixels.fill(PURPLE)
        jRight = True
    elif not right and jRight:
        usb_midi.send(NoteOff(13, 0))
        pixels.fill(OFF)
        jRight = False
    ### Joystick Up ###
    if up and not jUp:
        print("Joystick Up")
        usb_midi.send(NoteOn(14, 127))
        pixels.fill(YELLOW)
        jUp = True
    elif not up and jUp:
        usb_midi.send(NoteOff(14, 0))
        pixels.fill(OFF)
        jUp = False
    ### Joystick Down ###
    if down and not jDown:
        print("Joystick Down")
        usb_midi.send(NoteOn(15, 127))
        pixels.fill(CYAN)
        jDown = True
    elif not down and jDown:
        usb_midi.send(NoteOff(15, 0))
        pixels.fill(OFF)
        jDown = False
