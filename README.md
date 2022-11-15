# WiiChuck2Midi
![WiiChuck2Midi](/images/Wiichuck.jpg)



 Nintendo Wii Nunchuck to USB Midi for Theatre Purposes.
 
I wanted a way for an assistent to comfortably trigger Qlab/Theatremix software during our shows. We used to use a Streamdeck for this task but found the buttons had a tendancy to stick or be mispressed.

[![Here is a demo of it in action:]
(https://img.youtube.com/vi/ySVVfcEn-9I/maxresdefault.jpg)]
(https://www.youtube.com/watch?v=ySVVfcEn-9I)

This solution is achieved with the following hardware:

1. Nintendo Wii Nunchuck (Everybody has one of these kicking around somewhere!)
2. Adafruit QT Py RP2040 https://www.adafruit.com/product/4900
3. Adafruit Wii Nunchuck Breakout Adapter - Qwiic / STEMMA QT https://www.adafruit.com/product/4836
4. STEMMA QT / Qwiic JST SH 4-Pin Cable - 50mm Long https://www.adafruit.com/product/4399
5. Self 3d Printed case (See STL Folder)

Software:
The Qt Py Rp2040 is running a simple Circuit Python script which you can find ![here](/code.py).
This tells the Qt Py to emulate a USB Midi device which is then set up with Qlab (or SCS on Windows) to send OSC commands to Theatremix.

I have coded the Z & C Button as my primary Go and Back buttons for Theatremix, they will thusly turn the status LED Green and Red/White when triggered.
The joysticks 4 cardinal extremities (Up/Down/Left/Right) provide 4 more midi signals to do with what you will in Qlab, in my example video 
