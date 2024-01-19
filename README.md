# regularmac_800
Linuxcnc Axis/Plasmac2 based GUI, but without the plasma
<img src="/2022-10-09-215142_1024x768_scrot.png" >


Heavily based on Plasmac2, this is an Axis GUI mod in the form of a usercommand.py file

Features include

- Gcode tab moved from bottom to left side tabs
- Basic Gcode editor Tab
- Plasmac style button add on
- Gui configuration via Setup menu, includes add/remove sliders, change gui colours, add buttons, etc
- Can be configured to fit within 800 x 480 pixels and smaller with 3 different screen configurations 

Still work in progress

To use, put the .py into the directory of your configuration and add the following to your .ini
[DISPLAY]USER_COMMAND_FILE=usercommand_regularmac_800.py

http://linuxcnc.org/docs/2.9/html/gui/axis.html#_user_command_file
