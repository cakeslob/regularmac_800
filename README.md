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

Still work in progress.

First time running, it will display an error. After that, the prefs file is created and it will run. 

To use, put the .py into the directory of your configuration and add the following to your .ini right under the axis line 
"USER_COMMAND_FILE=usercommand_regularmac_800.py"

[DISPLAY]
DISPLAY = axis

USER_COMMAND_FILE = usercommand_regularmac_800.py

http://linuxcnc.org/docs/2.9/html/gui/axis.html#_user_command_file


## Quick Start
<img src="/images/" >
<img src="/images/default_auto1.png" >

Regularmac800 is noticably different from Original Axis, but the code remains the same. 

The first thing you should do after starting up, is configure your Regularmac800 Screen Layout. You can get to that menu from the top using the "Setup" menu button. 

<img src="/images/default_setup2.png" >


The setup menu is where you will find the following Configuration Options

" Save All " - Save the current setup , otherwise it will reload the last saved setup used if you do not save

" Add " - For "Button" setup tab.  Add a button to the Button Frame. Max buttons is xx

" Close " - Exit the setup menu

### GUI Tab 

<img src="/images/default_setup1.png" >

" Close Dialog "  - Enable or disable the "Would you like to close LinuxCNC" Dialog box when closing LinuxCNC

" Window Size " - This is where you choose your screen layout style. Options : Default, Medium, Small 

<img src="/images/default_man1.png" >
Default 
<img src="/images/med_man1.png" >
Medium
<img src="/images/small_man1.png" >
Small 

" Window Screen " - This is where you choose your windowing style. Options : Maximized, Fullscreen, Default (windowed) 

" Font Size " - Choose the font size of the text

<img src="/images/default_setup3.png" >

" Show Button Label " - Display text labels in the button bar 
<img src="/images/default_buttbar3.png" >


" Load Last File " - At startup, automatically load the last file opened in LinuxCNC

" Hide Jog " - Hide the Jog Slider

" Hide Rapid " - Hide the Rapid Slider

" Hide Max Vel. " - Hide the Max Velocity Slider

" Hide Button Frame " - Hide the User Button Frame

<img src="/images/default_buttbar3.png" >

" Colors " - Choose the colours of the background, foreground, etc of the Axis GUI 

<img src="/images/default_colour2.png" >
<img src="/images/default_colour4.png" >

### Buttons 

<img src="/images/default_butt1.png" >

Add User Buttons to run MDI commands, trigger halpins, etc 

" Name " - The name of the button displayed in the GUI

" Code " - the command the button will exacute. These can be Gcode, subroutines/macro files, toggle halpins, etc. 


To add a User Button , 

<img src="/images/default_butt2.png" >

Click "Add"

<img src="/images/default_butt3.png" >

Fill out the Name and Code boxes

<img src="/images/default_butt4.png" >

Click "Save All"

<img src="/images/default_butt5.png" >

Click Close to return to Axis  


### Auto Tab

The Gcode display has been moved from the bottom of Axis, and is now part of the right tab. Scroll through the gcode using the Up and Down arrow keys. The Auto tab can be expanded to full screen by clicking the "AUTO" button in the left corner. 

<img src="/images/default_auto1.png" >

### Edit Tab

New addition is the Edit tab, where you can edit your gcode file within axis. This is handy for minor changes. The current loaded gcode file is opened in the editor, and saved when leaving the editor. The file is then reloaded in Axis to update any changed

<img src="/images/default_edit2.png" >

