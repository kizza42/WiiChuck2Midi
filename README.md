# WiiChuck2Midi
 Nintendo Wii Nunchuck to USB Midi for Theatre Purposes.
 
I wanted a way for an assistent to comfortably trigger Qlab/Theatremix software during our shows. We used to use a Streamdeck for this task but found the buttons had a tendancy to stick or be mispressed.

This solution is achieved with the following hardware:

1. Nintendo Wii Nunchuck
2. Adafruit QT Py RP2040 https://www.adafruit.com/product/4900
3. Adafruit Wii Nunchuck Breakout Adapter - Qwiic / STEMMA QT https://www.adafruit.com/product/4836
4. STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long https://www.adafruit.com/product/4399
5. Self 3d Printed case (See STL Folder)

Software:
The Qt Py Rp2040 is running circuit python and the code in this repo.
This tells the Qt Py to emulate a USB Midi device which is then set up with Qlab to send OSC commands to Theatremix
