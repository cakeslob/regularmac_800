# regularmac_800
Linuxcnc Axis/Plasmac2 based GUI, but without the plasma, Testing offset table and vars table, needs help
<img src="/20241027_22h30m51s_grim.png" >
<img src="/20241027_22h35m50s_grim.png" >



Heavily based on Plasmac2, this is an Axis GUI mod in the form of a usercommand.py file

Features include

- Gcode tab moved from bottom to left side tabs
- Basic Gcode editor Tab
- Plasmac style button add on
- Gui configuration via Setup menu, includes add/remove sliders, change gui colours, add buttons, etc
- Can be configured to fit within 800 x 480 pixels and smaller with 3 different screen configurations 

Still work in progress.

First time running, it will display an error. After that, the prefs file is created and it will run. 

To use, put the .py into the directory of your configuration and add the following to your .ini right under the axis line 
"USER_COMMAND_FILE=usercommand_regularmac_800.py"

[DISPLAY]
DISPLAY = axis

USER_COMMAND_FILE = usercommand_regularmac_800.py

http://linuxcnc.org/docs/2.9/html/gui/axis.html#_user_command_file
