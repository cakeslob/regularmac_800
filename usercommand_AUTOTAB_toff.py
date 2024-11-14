import linuxcnc
s = linuxcnc.stat()
s.poll()

#root_window.tk.call(".pane","configure","-height","300",'-width','700');
root_window.tk.call('.pane.top.tabs','configure','-width','425')
#root_window.tk.call('.pane.top.right','configure','-width','300')
root_window.tk.call("wm","geometry",".","+0+36")
### we will change this back to w later  ####
rC = root_window.tk.call



############################################
#######      MOVE THE GCODE   ##############
############################################

# remove bottom pane
rC('.pane','forget','.pane.bottom')

# new auto tab with gcode text
rC('.pane.top.tabs','insert','end','auto','-text',' Auto ')
rC('.pane.top.tabs.fauto','configure','-borderwidth',2)
rC('frame','.pane.top.tabs.fauto.t','-borderwidth',2,'-relief','sunken','-highlightthickness','1')
rC('text','.pane.top.tabs.fauto.t.text','-borderwidth','0','-exportselection','0','-highlightthickness','0','-relief','flat','-takefocus','0','-undo','0')
rC('bind','.pane.top.tabs.fauto.t.text','<Configure>','goto_sensible_line')
rC('scrollbar','.pane.top.tabs.fauto.t.sb','-width',20,'-borderwidth','0','-highlightthickness','0')
rC('.pane.top.tabs.fauto.t.text','configure','-state','normal','-yscrollcommand',['.pane.top.tabs.fauto.t.sb','set'])
rC('.pane.top.tabs.fauto.t.sb','configure','-command',['.pane.top.tabs.fauto.t.text','yview'])
rC('pack','.pane.top.tabs.fauto.t.sb','-fill','y','-side','right')
rC('pack','.pane.top.tabs.fauto.t.text','-expand','1','-fill','both','-side','left')
rC('pack','.pane.top.tabs.fauto.t','-fill','both')

# create a new widget list so we can "move" the gcode text
widget_list_new = []
for widget in widget_list:
    if '.t.text' in widget[2]:
        widget = ('text', Text, '.pane.top.tabs.fauto.t.text')
    widget_list_new.append(widget)
    widget_list_new.append(('varFrame', bwidget.ScrollableFrame, '.pane.top.tabs.fvar.t.tt'))
widgets = nf.Widgets(root_window,*widget_list_new)

# copied from axis.py (line 3857) to assign the "new" widgets.text to t
t = widgets.text
t.bind('<Button-3>', rClicker)
t.tag_configure("ignored", background="#ffffff", foreground="#808080")
t.tag_configure("lineno", foreground="#808080")
t.tag_configure("executing", background="#804040", foreground="#ffffff")
t.bind("<Button-1>", select_line)
t.bind("<Double-Button-1>", release_select_line)
t.bind("<B1-Motion>", lambda e: "break")
t.bind("<B1-Leave>", lambda e: "break")
t.bind("<Button-4>", scroll_up)
t.bind("<Button-5>", scroll_down)
t.configure(state="disabled")

############################################
#######  end MOVE THE GCODE   ##############
############################################




##########################################################
########       LOAS_LAST FILE   PY3  LCNC 2.9  #############
########   In ini file under [DISPLAY]  ##################
########     LOAD_LASTFILE = 	YES       ##################
##########################################################

loadlast = inifile.find('DISPLAY', 'LOAD_LASTFILE')
if loadlast == "YES" :
    load_lastfile = True
else:
    load_lastfile = False


lastfile = ""
recent = ap.getpref('recentfiles', [], repr)
if len(recent):
    lastfile = recent.pop(0)

code = []
addrecent = True
if args:
    initialfile = args[0]
elif "AXIS_OPEN_FILE" in os.environ:
    initialfile = os.environ["AXIS_OPEN_FILE"]
elif inifile.find("DISPLAY", "OPEN_FILE"):
    initialfile = inifile.find("DISPLAY", "OPEN_FILE")
elif os.path.exists(lastfile) and load_lastfile:
    initialfile = lastfile
    print ("Loading ") 
    print (initialfile)
elif lathe:
    initialfile = os.path.join(BASE, "share", "axis", "images","axis-lathe.ngc")
    addrecent = False
else:
    initialfile = os.path.join(BASE, "share", "axis", "images", "axis.ngc")
    addrecent = False

if os.path.exists(initialfile):
    open_file_guts(initialfile, False, addrecent)

###############################
######    end load last    ###############
#########################################

#########
##################################

###  do you want to exit linuxcnc
rC("wm","protocol",".","WM_DELETE_WINDOW","destroy .")

rC('grid','forget','.pane.top.gcodel')
rC('grid','forget','.pane.top.right')
rC('grid','forget','.pane.top.gcodes')
rC('grid','.pane.top.right','-sticky','nesw','-column','1','-row','1')
rC('grid','.pane.top.gcodes','-sticky','nesw','-column','1','-row','2','-rowspan','2')



########################################################
###############  choose/remove sliders ########################
########################################################

#rC('grid','forget','.pane.top.feedoverride')
#rC('grid','forget','.pane.top.rapidoverride')
#rC('grid','forget','.pane.top.spinoverride')
#rC('grid','forget','.pane.top.jogspeed')
#rC('grid','forget','.pane.top.ajogspeed')
rC('grid','forget','.pane.top.maxvel')




#######   EDIT TAB   ######

def load_editfile():
    print (s.file)
    parameter = inifile.find("RS274NGC", "PARAMETER_FILE")
    open_filea = open(os.path.basename(parameter),'r')
    #open_filea = open(s.file,'r')
    rC('.pane.top.tabs.fedit.t.text','delete','1.0','end')
    rC('.pane.top.tabs.fedit.t.text','insert','end',open_filea.read())
    
    



def save_editfile():
    print (s.file)
    #open_filea = open(s.file,'w')
    #edit_gcode = rC('.pane.top.tabs.fedit.t.text','get','1.0','end')
    #open_filea.write(edit_gcode)
    #reload_file()
    return 1


def print_file():
    print ('breaking')
    return "break"

def print_file2():
    print_file





rC('.pane.top.tabs','insert','end','edit','-text',' edit ','-raisecmd','load_editfile','-leavecmd','save_editfile')
#rC('.pane.top.tabs','insert','end','edit','-text',' edit ')
rC('.pane.top.tabs.fedit','configure','-borderwidth',2)
rC('frame','.pane.top.tabs.fedit.t','-borderwidth',2,'-relief','sunken','-highlightthickness','1')
#rC('text','.pane.top.tabs.fedit.t.text','-borderwidth','0','-exportselection','1','-highlightthickness','0','-relief','flat','-takefocus','1','-undo','1')
rC('text','.pane.top.tabs.fedit.t.text','-borderwidth','0','-relief','flat','-takefocus','1','-undo','1')

#rC('bind','.pane.top.tabs.fedit.t.text','<Configure>','goto_sensible_line')
rC('scrollbar','.pane.top.tabs.fedit.t.sb','-width',20,'-borderwidth','0','-highlightthickness','0')
rC('.pane.top.tabs.fedit.t.text','configure','-yscrollcommand',['.pane.top.tabs.fedit.t.sb','set'])
rC('.pane.top.tabs.fedit.t.sb','configure','-command',['.pane.top.tabs.fedit.t.text','yview'])
rC('pack','.pane.top.tabs.fedit.t.sb','-fill','y','-side','right')
rC('pack','.pane.top.tabs.fedit.t.text','-expand','1','-fill','both','-side','left')
rC('pack','.pane.top.tabs.fedit.t','-fill','both')



###### test entry  ####

rC('button','.pane.top.tabs.fedit.edit','-text','edit','-command','load_editfile')
rC('button','.pane.top.tabs.fedit.save','-text','save','-command','save_editfile')
rC('pack','.pane.top.tabs.fedit.edit')
rC('pack','.pane.top.tabs.fedit.save')

rC('.pane.top.tabs','itemconfigure','manual','-text',' MANUAL ')
rC('.pane.top.tabs','itemconfigure','mdi','-text',' MDI ')
rC('.pane.top.tabs','itemconfigure','auto','-text',' AUTO ')
rC('.pane.top.tabs','itemconfigure','edit','-text',' EDIT ')
rC('.pane.top.right','itemconfigure','preview','-text',' PREVIEW ')
rC('.pane.top.right','itemconfigure','numbers','-text',' DRO ')




#rC('scrollbar','.pane.top.tabs.fvar.t.sb','-width',20,'-orient','vertical','-command','.pane.top.tabs.fvar.t.tt yview','-takefocus',1)

#######   table test
rC('.pane.top.tabs','insert','end','off','-text',' OFF ')
rC('frame','.pane.top.tabs.foff.t','-borderwidth',2,'-relief','solid','-highlightthickness','1')
rC('.pane.top.tabs.foff','configure','-borderwidth',2)
rC('scrollbar','.pane.top.tabs.foff.t.sb','-width',20,'-borderwidth','0','-highlightthickness','0','-command','.pane.top.tabs.foff.t.tbl yview')
rC('scrollbar','.pane.top.tabs.foff.t.sbx','-width',20,'-borderwidth','0','-highlightthickness','0','-orient','h','-command','.pane.top.tabs.foff.t.tbl xview')
#rC('frame','.pane.top.tabs.foff.t.tbl','-borderwidth',2,'-relief','solid','-highlightthickness','1')
rC('ScrollableFrame','.pane.top.tabs.foff.t.tbl')
rC('.pane.top.tabs.foff.t.tbl','configure','-yscrollcommand','.pane.top.tabs.foff.t.sb set')
rC('.pane.top.tabs.foff.t.tbl','configure','-xscrollcommand','.pane.top.tabs.foff.t.sbx set')
#rC('.pane.top.tabs.fedit.t.text','configure','-yscrollcommand',['.pane.top.tabs.fedit.t.sb','set'])
#rC('.pane.top.tabs.fedit.t.sb','configure','-command',['.pane.top.tabs.fedit.t.text','yview'])
rC('pack','.pane.top.tabs.foff.t','-fill','both')
rC('pack','.pane.top.tabs.foff.t.sb','-fill','y','-side','left')
rC('pack','.pane.top.tabs.foff.t.tbl','-fill','both')
rC('pack','.pane.top.tabs.foff.t.sbx','-fill','x','-side','bottom')
#rC('grid','forget','.pane.top.right')
#rC('grid','.pane.top.tabs','-sticky','nesw','-columnspan',2)

rC('.pane.top.tabs','raise','off')



####### pre
# ~ parameter = inifile.find("RS274NGC", "PARAMETER_FILE")
# ~ temp_parameter = os.path.join(tempdir, os.path.basename(parameter))
# ~ if os.path.exists(parameter):
    # ~ shutil.copy(parameter, temp_parameter)
# ~ canon.parameter_file = temp_parameter

#print(os.path.basename(parameter)))

#######   start   table

conversion = {0:"X", 1:"Y", 2:"Z", 3:"A", 4:"B", 5:"C", 6:"U", 7:"V", 8:"W"}
# set the table model
header = ['X', 'Y', 'Z', 'A', 'B', 'C', 'U', 'V', 'W']
vheader = ['ABS', 'Rot', 'G92', 'Tool', 'G54', 'G55', 'G56', 'G57', 'G58', 'G59', 'G59.1', 'G59.2', 'G59.3']

offset = '.pane.top.tabs.foff.t.tbl.frame'
count = 1
row = len(vheader)
heightL = len(vheader)
column = int(masked_axes_count())
#print(s.axes())
RL= 1
tl = 1 
print(column)
#####  top header   

tabledata = [[0, 0, 1, 0, 0, 0, 0, 0, 0],
              [None, None, 2, None, None, None, None, None, None],
              [0, 0, 3, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 4, 0, 0, 0, 0, 0, 0],
              [0, 0, 5, 0, 0, 0, 0, 0, 0],
              [0, 0, 6, 0, 0, 0, 0, 0, 0],
              [0, 0, 7, 0, 0, 0, 0, 0, 0],
              [0, 0, 8, 0, 0, 0, 0, 0, 0],
              [0, 0, 9, 0, 0, 0, 0, 0, 0],
              [0, 0, 10, 0, 0, 0, 0, 0, 0],
              [0, 0, 11, 0, 0, 0, 0, 0, 0],
              [0, 0, 12, 0, 0, 0, 0, 0, 0]]

for letter in 'xyzabcuvw':
    rC('label',offset +'.label' + str(letter), '-text', letter,'-width','5')
    #print(letter)
      # populate the axes frame
count = 0
letters = 'xyzabcuvw'
first_axis = ''

for column in range(0,column):
    column = (column + 1)
    if letters[count] in trajcoordinates:
                if first_axis == '':
                    first_axis = letters[count]
                #print(first_axis)
                pad = (0,0) if column == 0 else (8,0)
                if column == 0:
                    print("butt")
                else:
                    #column = (column + 1)
                    rC('grid',offset +'.label' + letters[count],'-row',0,'-column',column,'-padx',pad)
                
                
    count += 1
    #print(letters[count])
    if count == 9: break

####   this is the entry grid
count = 0
for i in range(row): #Rows

    for j in range(column): #Columns
        #column = (column + 1)        
        if column == 0:
            print("butt")
        else:
            
            #b = rC('Entry',offset +'.entry' + str(count), '-text', (i,j),'-width','5')
            b = rC('Entry',offset +'.entry' + str(count), '-text', str(count),'-width','10')
            rC('grid', str(b) ,'-row',i + 1,'-column',j + 1 )
            count += 1
        
####   side header  
  
for v in vheader: #Rows
    l = rC('label',offset +'.labelv' + str(RL), '-text', v,'-width','5')
    rC('grid', str(l) ,'-row',RL ,'-column',0)
    RL += 1 


parameter = inifile.find("RS274NGC", "PARAMETER_FILE")



def reload_offsets():

    # read the var file so we get all of the user offsets.
    temp = read_file()

    # overwrite with motion's version of the current system offset
    # this should be more up to date
    
    temp[s.g5x_index-1] = s.g5x_offset

    g54, g55, g56, g57, g58, g59, g59_1, g59_2, g59_3 = temp
    if g54 is None: return



    # Get the offsets arrays and convert the units if the display
    # is not in machine native units

    ap = s.actual_position
    tool = s.tool_offset
    g92 = s.g92_offset
    rot = s.rotation_xy
    #column = int(masked_axes_count())
    count = 0
    # fill each row of the liststore from the offsets arrays
    for row, i in enumerate([ap, rot, g92, tool, g54, g55, g56, g57, g58, g59, g59_1, g59_2, g59_3]):
        for column in range(0, int(masked_axes_count())):
            rC(offset +'.entry' + str(count),'configure','-text', (tabledata[row][column]),'-width','10')
            #print(tabledata[row][column])
            #print('column')
            count += 1
        


       


def read_file():
    print("reaaaad")
    try:
        g54 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g55 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g56 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g57 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g58 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g59 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g59_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g59_2 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        g59_3 = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if os.path.basename(parameter)is None:
            return g54, g55, g56, g57, g58, g59, g59_1, g59_2, g59_3
            print("ASS")
        if not os.path.exists(parameter):
            print('File does not exist: yellow<{}>')
            return g54, g55, g56, g57, g58, g59, g59_1, g59_2, g59_3
        logfile = open(os.path.basename(parameter), "r").readlines()
        for line in logfile:
            temp = line.split()
            param = int(temp[0])
            data = float(temp[1])
    
            if 5229 >= param >= 5221:
                g54[param - 5221] = data
                #print(data)
            elif 5249 >= param >= 5241:
                g55[param - 5241] = data
            elif 5269 >= param >= 5261:
                g56[param - 5261] = data
            elif 5289 >= param >= 5281:
                g57[param - 5281] = data
            elif 5309 >= param >= 5301:
                g58[param - 5301] = data
            elif 5329 >= param >= 5321:
                g59[param - 5321] = data
            elif 5349 >= param >= 5341:
                g59_1[param - 5341] = data
            elif 5369 >= param >= 5361:
                g59_2[param - 5361] = data
            elif 5389 >= param >= 5381:
                g59_3[param - 5381] = data
        return [g54, g55, g56, g57, g58, g59, g59_1, g59_2, g59_3]
        print("BUTTTTTTT")
    except:
        return [None, None, None, None, None, None, None, None, None]
    print("reaaajjjad")

def dataChanged( new, old, x):
    row = new.row()
    col = new.column()
    data = tabledata[row][col]

    if row == 0: return
    # Hack to not edit any rotational offset but Z axis
    if row == 1 and not col == 2: return

    # dont evaluate text column
    if col == 0 :return

    # make sure we switch to correct units for machine and rotational, row 2, does not get converted
    try:
            qualified = float(data)
            #qualified = float(locale.atof(data))
    except Exception as e:
        print(e)
    # now update linuxcnc to the change
    try:
        if row == 1:  # current Origin
            commands.send_mdi_command("G10 L2 P0 %s %10.4f" % (self.axisletters[col], qualified))
        elif row == 2:  # rotational
            if col == 2:  # Z axis only
                commands.send_mdi_command("G10 L2 P0 R %10.4f" % (qualified))
        elif row == 3:  # G92 offset
            commands.send_mdi_command("G92 %s %10.4f" % (self.axisletters[col], qualified))
        elif row == 4:  # Tool
            if not self.current_tool == 0:
                commands.send_mdi_command("G10 L1 P%d %s %10.4f" % (self.current_tool, self.axisletters[col], qualified))
                commands.send_mdi_command('g43')
        else:
                commands.send_mdi_command("G10 L2 P%d %s %10.4f" % (row-4, self.axisletters[col], qualified))

        #ACTION.UPDATE_VAR_FILE()
        #ACTION.RESTORE_RECORDED_MODE()
        #STATUS.emit('reload-display')
        reload_offsets()
    except Exception as e:
        print("offsetpage widget error: MDI call error")
        reload_offsets()

#dataChanged(x,x,1)
read_file()
reload_offsets()
# ~ parameter = inifile.find("RS274NGC", "PARAMETER_FILE")
    # ~ #open_filea = open(os.path.basename(parameter),'r')
# ~ with open(os.path.basename(parameter)) as infile:
    # ~ lines = infile.readlines()
    # ~ splitted = [line.strip().partition("\t") for line in lines]
    # ~ linuxCNCVar = {int(splitResult[0]): float(splitResult[-1]) for splitResult in splitted}
    # ~ print(linuxCNCVar)


##################################################
#@#########   end OFFSET TEST    ###################
#######################################################


#################################################
######   DO PARAMETER VARS THING    #################
##########################################

#######   table test
rC('.pane.top.tabs','insert','end','var','-text',' var ')
rC('.pane.top.tabs.fvar','configure','-borderwidth',2)

#rC('grid','forget','.pane.top.right')
#rC('grid','.pane.top.tabs','-sticky','nesw','-columnspan',2)

#rC('.pane.top.tabs','raise','var')




rC('frame','.pane.top.tabs.fvar.t','-borderwidth',2,'-relief','solid','-highlightthickness','1')

rC('ScrollableFrame','.pane.top.tabs.fvar.t.tt')
rC('scrollbar','.pane.top.tabs.fvar.t.sb','-width',20,'-orient','vertical','-command','.pane.top.tabs.fvar.t.tt yview','-takefocus',1)
#rC('ScrollableFrame','.pane.top.tabs.fvar.t.tt','create')

rC('pack','.pane.top.tabs.fvar.t','-fill','both','-expand',1)
rC('pack','.pane.top.tabs.fvar.t.sb','-fill','y','-side','left')
rC('pack','.pane.top.tabs.fvar.t.tt','-fill','both','-expand',1)

#varset = '.pane.top.tabs.fvar.t.cnvs.tbl'
varset = rC('.pane.top.tabs.fvar.t.tt','getframe')
#varset = '.pane.top.tabs.fvar.t.tt'
parameter = inifile.find("RS274NGC", "PARAMETER_FILE")

    
    
# ~ with open(os.path.basename(parameter)) as infile:
    # ~ lines = infile.readlines()
    # ~ #rows = len(lines)
    # ~ splitted = [line.strip().partition("\t") for line in lines]
    # ~ #linuxCNCVar = {int(splitResult[0]): float(splitResult[-1]) for splitResult in splitted}
    # ~ #print(linuxCNCVar)
    # ~ lcount = 0
    # ~ count = 0
    # ~ for splitResult in splitted:
            # ~ l = rC('label',varset +'.labelv' + str(lcount), '-text', int(splitResult[0]),'-width','5')
            # ~ rC('grid', str(l) ,'-row',lcount ,'-column',0,'-sticky','nw')
            # ~ #b = rC('Entry',offset +'.entry' + str(count), '-text', (i,j),'-width','5')
            # ~ b = rC('Entry',varset +'.entry' + str(count), '-text', float(splitResult[-1]) ,'-width','10')
            # ~ rC('grid', str(b) ,'-row',count,'-column', 1 ,'-sticky','nesw')
            # ~ lcount += 1
            # ~ count += 1



rC('.pane.top.tabs.fvar.t.tt','configure','-yscrollcommand','.pane.top.tabs.fvar.t.sb set')


with open(os.path.basename(parameter)) as infile:
    lines = infile.readlines()
    splitted = [line.strip().partition("\t") for line in lines]
    count = 0
    for splitResult in splitted:
            l = rC('LabelEntry',varset +'.para' + str(count), '-label', int(splitResult[0]),'-labelwidth','5', '-text', float(splitResult[-1]) ,'-width','10')
            #l = rC('LabelEntry',('.pane.top.tabs.fvar.t.tt','getframe') +'.para' + str(count), '-label', int(splitResult[0]),'-labelwidth','5', '-text', float(splitResult[-1]) ,'-width','10')

            rC('grid', str(l) ,'-row',count,'-column', 1 ,'-sticky','nesw')
            #rC('pack', str(l) ,'-side','top')
            #rC('.pane.top.tabs.fvar.t.tt','see','.pane.top.tabs.fvar.t.tt.frame.para' + str(count),'bottom')
            #print(l)
            count += 1





rC('pack','.pane.top.tabs.fvar.t','-fill','both','-expand',1)
rC('pack','.pane.top.tabs.fvar.t.sb','-fill','y','-side','left')
rC('pack','.pane.top.tabs.fvar.t.tt','-fill','both','-expand',1)

#rC('.pane.top.tabs.fvar.t.tt','configure','-areaheight',500)
#print(rC('pack','slaves','.pane.top.tabs.fvar.t.tt.frame'))
#print(rC('.pane.top.tabs.fvar.t.tt','getframe'))
print(rC('winfo','viewable','.pane.top.tabs.fvar.t.tt.frame'))

yscrollinc = rC('winfo','height','.pane.top.tabs.fvar.t.tt.frame.para0')
rC('.pane.top.tabs.fvar.t.tt','configure','-yscrollincrement',yscrollinc)
#print(rC('.pane.top.tabs.fvar.t.tt','configure','-yscrollincrement'))
#print(rC('.pane.top.tabs.fvar.t.tt','yview'))
#rC('.pane.top.tabs.fvar.t.tt','see','.pane.top.tabs.fvar.t.tt.frame.para100','top')

#vrt = rC('.pane.top.tabs.fvar.t.tt')
vf = widgets.varFrame
def var_up(event):
    print(rC('winfo','y','.pane.top.tabs.fvar.t.tt.frame'))
    print(rC('winfo','y','.pane.top.tabs.fvar.t.tt.frame.para0'))
    yscrollinc = rC('winfo','height','.pane.top.tabs.fvar.t.tt.frame.para0')
    rC('.pane.top.tabs.fvar.t.tt','configure','-yscrollincrement',yscrollinc)
    #vf.yview_scroll(1, "units")
    print("butt")
    #print(rC('.pane.top.tabs.fvar.t.tt','yview'))
    #print(rC('winfo','height','.pane.top.tabs.fvar.t.tt.frame'))
    rC('.pane.top.tabs.fvar.t.tt','yview','scroll',1, "units")

foccus = rC('focus','-displayof','.pane.top.tabs.fvar.t.tt.frame')
def var_down(event):
    #print(rC('.pane.top.tabs.fvar.t.tt','yview'))
    foccus = rC('focus','-displayof','.pane.top.tabs.fvar.t.tt.frame')
    print(rC('focus','-displayof','.pane.top.tabs.fvar.t.tt.frame'))
    rC('.pane.top.tabs.fvar.t.tt','yview','scroll',-1, "units")
    print(foccus)
    #print(rC('winfo','parent',foccus))
    fparent = rC('winfo','parent',foccus)
    print(fparent)
    #print(rC('winfo','viewable',foccus))
    rC('.pane.top.tabs.fvar.t.tt','see',fparent,'bottom')

rC('bind','.pane.top.tabs.fvar.t.tt.frame',"<Button-4>", 'var_up')
rC('bind','.pane.top.tabs.fvar.t.tt',"<Button-5>", 'var_down')
#foccus.bind("<Button-4>", var_up)
#foccus.bind("<Button-5>", var_down)
#root_window.unbind("<Home>")
root_window.bind('<Key-F4>', var_up)
root_window.bind('<Key-F5>', var_down)
#root_window.bind('<Return>', var_down)

# ~ ####  scroll_into_view
# ~ def scroll_into_view:
    # ~ widget_top = rC('winfo','y','.pane.top.tabs.fvar.t.tt.frame')
    # ~ widget_bottom = widget_top + (rC('winfo','height','.pane.top.tabs.fvar.t.tt.frame'))
    


#################################################
######  end DO PARAMETER VARS THING    #################
##########################################
#def user_live_update():
    #rC('.pane.top.tabs.fvar.t.tt','configure')
    #print(rC('focus','-displayof','.pane.top.tabs.fvar.t.tt.frame'))
    #foccus = (rC('focus','-displayof','.pane.top.tabs.fvar.t.tt.frame'))
    #print(rC('winfo','ismapped',foccus))

TclCommands.var_down = var_down
TclCommands.var_up = var_up
TclCommands.dataChanged = dataChanged
TclCommands.reload_offsets = reload_offsets
TclCommands.read_file = read_file
TclCommands.save_editfile = save_editfile
TclCommands.load_editfile = load_editfile
TclCommands.printfile = print_file
commands = TclCommands(root_window)

