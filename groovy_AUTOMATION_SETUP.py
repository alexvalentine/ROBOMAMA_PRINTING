from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator

#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\cell_printing_out.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = [
            'A',
            'B',
           #'C', 
         #   'D'
            ]

#Defining positions of axes
AXES_DATA = {
    'A': {
        'number': 4,
        'alignment_location': (586.075, 367.82),
    },
    'B': {
        'number': 5,
        'alignment_location': (482.075, 367.82),
    },
    'C': {
        'number': 6,
        'alignment_location': (378.075, 367.82),
    },
    'D': {
        'number': 7,
        'alignment_location': (299.075, 367.82),
    },
}

#Defining substrate location and profilometry mesh size
SUBSTRATES = {
    'slide1': {
        'origin': (40,127.25),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (5,5),
    },
    #'slide2': {
    #    'origin': (150,40),
    #    'size': 'auto',
    #    'profile': True,
    #    'profile-spacing': (10,10),
    #},
    #'slide3': {
    #    'origin': (230,107),
    #    'size': 'auto',
    #    'profile': True,
    #    'profile-spacing': (10,10),
    #}
}
#Defining profilometry parameters
automator = AerotechAutomator(
    #calfile_path=r'C:\Users\Lewis Group\Desktop\Calibration\CAL_output.cal',
    axes=AXES_USED,
    axes_data = AXES_DATA,
    substrates = SUBSTRATES,
)

#Defining mecode parameters
g = G(
    direct_write=True,
    #outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )

#slide array settings
x_space = 30
y_space = 30


#groove settings
movement_feed = 25
#array = (-95, -94, -93, -92, -91, -90, -90,-91,-91,-92,-92.5, -92.6, -92.6,-92.6,-92.7)
groove_space = (0.04,0.06,0.08,0.1)
groove_height = (0.1,)*15
groove_pressure = (10,)*15
groove_speed = (3,)*15

bottom_height = (0.015,)*15
bottom_speed = (15,)*15
bottom_pressure = (3.5,)*15
bottom_space = (0.13,)*15

cant_width = 3.5
cant_length = 3.5

cant_width_groove = 4
cant_length_groove = 4
cant_width_tpu = 10#(12,)*15
cant_length_tpu = 10#(12,)*15

def setup(active_slide, ref, move_to_ref = False):
    automator.setup()
    automator.automate()
    automator.save_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
    automator.teardown()
    g.direct_write = True
    #g.set_cal_file(r'C:\Users\Lewis Group\Desktop\Calibration\CAL_output.cal')
    g.direct_write = False
    if move_to_ref is True:
        g.direct_write = True
        g.abs_move(x=automator.substrate_origins[active_slide][ref][0]+11, y=automator.substrate_origins[active_slide][ref][1] + 11)
        g.abs_move(**{ref:(automator.substrate_origins[active_slide][ref][2]+ 1)})
        g.direct_write = False


#def identify_slide(origin = (40,127.25)):
#    g.direct_write = True
#    g.write('POSOFFSET CLEAR X Y U A B C D')
#    g.feed(25)
#    g.abs_move(A=-0.5, B=-0.5, C=-0.5, D=-0.5)
#    g.feed(40)
#    g.abs_move(x=origin[0], y= origin[1])
#    x_values = automator.find_substrate_bounds(dimension='x')
#    g.abs_move(x=origin[0], y= origin[1])
#    y_values = automator.find_substrate_bounds(dimension='y')
#    x_mid = (x_values[1]-x_values[0])/2+x_values[0]
#    y_mid = (y_values[1]-y_values[0])/2+y_values[0]
#    return x_mid, y_mid
#    


def collect_array(prof_A_offset):
    zero_vals = np.zeros(15)
     #for i, x in enumerate(y_range):
     #       for j, y in enumerate(x_range):
    g.feed(25)
    for i in range(15):
        g.abs_move(x=cantilever_position[i][0]-prof_A_offset[0], y=cantilever_position[i][1]-prof_A_offset[1])
        zero_vals[i] = automator.find_profilometer_middle(z_start=-94)
    return zero_vals
    g.abs_move(D=-2)

    
def normalize_array(array):
    z_ref = array[0]
    #z_ref = (array[0],)*15
    #z_ref_array = (z_ref,)*15
    norm_array = np.zeros(15)
    norm_array = np.subtract(array, z_ref)
    return norm_array        




def nozzle_change(nozzles = 'ab'):
    g.feed(25)
    #g.home()
    g.dwell(0.25)
    g.write(';----------nozzle change------------')
    if nozzles=='ab':
        g.abs_move(A=50)
        g.move(x=(automator.home_positions['B'][0] - automator.home_positions['A'][0]), y = (automator.home_positions['B'][1] - automator.home_positions['A'][1]))
    elif nozzles=='ac':
        g.abs_move(A=50)
        g.move(x=(automator.home_positions['C'][0] - automator.home_positions['A'][0]), y = (automator.home_positions['C'][1] - automator.home_positions['A'][1]))    
    elif nozzles=='ad':
        g.abs_move(A=50)
        g.move(x=(automator.home_positions['D'][0] - automator.home_positions['A'][0]), y = (automator.home_positions['D'][1] - automator.home_positions['A'][1]))
    elif nozzles=='ba':
        g.abs_move(B=50)
        g.move(x=(automator.home_positions['A'][0] - automator.home_positions['B'][0]), y = (automator.home_positions['A'][1] - automator.home_positions['B'][1]))
    elif nozzles=='bc':
        g.abs_move(B=50)
        g.move(x=(automator.home_positions['C'][0] - automator.home_positions['B'][0]), y = (automator.home_positions['C'][1] - automator.home_positions['B'][1]))
    elif nozzles=='bd':
        g.abs_move(B=50)
        g.move(x=(automator.home_positions['D'][0] - automator.home_positions['B'][0]), y = (automator.home_positions['D'][1] - automator.home_positions['B'][1]))
    elif nozzles=='ca':
        g.abs_move(C=50)
        g.move(x=(automator.home_positions['A'][0] - automator.home_positions['C'][0]), y = (automator.home_positions['A'][1] - automator.home_positions['C'][1]))
    elif nozzles=='cb':
        g.abs_move(C=50)
        g.move(x=(automator.home_positions['B'][0] - automator.home_positions['C'][0]), y = (automator.home_positions['B'][1] - automator.home_positions['C'][1]))
    elif nozzles=='cd':
        g.abs_move(C=50)
        g.move(x=(automator.home_positions['D'][0] - automator.home_positions['C'][0]), y = (automator.home_positions['D'][1] - automator.home_positions['C'][1]))
    elif nozzles=='da':
        g.abs_move(D=50)
        g.move(x=(automator.home_positions['A'][0] - automator.home_positions['D'][0]), y = (automator.home_positions['A'][1] - automator.home_positions['D'][1]))
    elif nozzles=='db':
        g.abs_move(D=50)
        g.move(x=(automator.home_positions['B'][0] - automator.home_positions['D'][0]), y = (automator.home_positions['B'][1] - automator.home_positions['D'][1]))
    elif nozzles=='dc':
        g.abs_move(D=50)
        g.move(x=(automator.home_positions['C'][0] - automator.home_positions['D'][0]), y = (automator.home_positions['C'][1] - automator.home_positions['D'][1]))
    else:
        g.write('; ---------- input a real nozzle change input...ya idiot--------')


def print_bottom(cant_width, cant_length, spacing, startz, speed,  nozzle, valve):
    g.feed(movement_feed)
    g.abs_move(**{nozzle:startz})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.15)    
    g.move(x=2,y=2)
    g.meander(x = cant_width, y = cant_length, spacing = spacing, orientation = 'y')
    g.set_valve(num = valve, value = 0)

def print_grooves(cant_width, cant_length, spacing, startz, speed, nozzle, valve):
    g.feed(movement_feed)
    g.abs_move(**{nozzle:startz})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.15)    
    g.meander(x = cant_width, y = cant_length, spacing = spacing, orientation = 'y')
    g.set_valve(num = valve, value = 0)                       
                                                                     
                    
def print_all_bottoms(nozzle = 'A', valve = 1):
    if nozzle == 'A':
        ZZ=zA
    if nozzle == 'B':
        ZZ=zB
    if nozzle == 'C':
        ZZ = zC
    if nozzle == 'D':
        ZZ=zD
    count = 0
    g.abs_move(**{nozzle:ZZ+40})
    for i in np.arange(0,15):
        starting= (cantilever_position[i][0], cantilever_position[i][1])
        z_start = ZZ+relative_zeros[count]
        g.feed(movement_feed)
        g.set_pressure(com_port = pressure_box, value = bottom_pressure[0])
        g.abs_move(starting[0]-7, starting[1]-7)
        g.abs_move(**{nozzle:z_start+bottom_height[i]})
        print_bottom(cant_width_tpu, cant_length_tpu, spacing=bottom_space[count], startz=z_start+bottom_height[i], speed = bottom_speed[count], nozzle = nozzle, valve = valve)
        g.feed(movement_feed)
        g.abs_move(**{nozzle:z_start+10})
        count = count + 1
    g.abs_move(**{nozzle:ZZ+60})

def print_all_grooves(nozzle = 'B', valve = 2):
    if nozzle == 'A':
        ZZ=zA
    if nozzle == 'B':
        ZZ=zB
    if nozzle == 'C':
        ZZ=zC
    if nozzle == 'D':
        ZZ=zD
    count = 0
    BA_offset = (automator.substrate_origins['slide1']['A'][0]-automator.substrate_origins['slide1']['B'][0], 
                automator.substrate_origins['slide1']['A'][1]-automator.substrate_origins['slide1']['B'][1])
    for i in np.arange(0,15):
        starting= (cantilever_position[i][0]-BA_offset[0], cantilever_position[i][1]-BA_offset[1])
        #starting= (cantilever_position[i][0]-(cant_width/2), cantilever_position[i][1]-(cant_length/2))
        z_start = ZZ+relative_zeros[count]
        g.feed(movement_feed)
        g.set_pressure(com_port = pressure_box, value = groove_pressure[0])
        for j in range(4):
            if j==0:
                g.abs_move(starting[0]-4.5, starting[1]+0.5)
                g.abs_move(**{nozzle:z_start+groove_height[i]})
                print_grooves(cant_width_groove, cant_length_groove, spacing=groove_space[j], startz=z_start+groove_height[i], speed = groove_speed[count], nozzle = nozzle, valve = valve)
                g.feed(movement_feed)
                g.abs_move(**{nozzle:z_start+10})
            elif j==1:
                g.abs_move(starting[0]+0.5, starting[1]+0.5)
                g.abs_move(**{nozzle:z_start+groove_height[i]})
                print_grooves(cant_width_groove, cant_length_groove, spacing=groove_space[j], startz=z_start+groove_height[i], speed = groove_speed[count], nozzle = nozzle, valve = valve)
                g.feed(movement_feed)
                g.abs_move(**{nozzle:z_start+10})
            elif j==2:
                g.abs_move(starting[0]-4.5, starting[1]-4.5)
                g.abs_move(**{nozzle:z_start+groove_height[i]})
                print_grooves(cant_width_groove, cant_length_groove, spacing=groove_space[j], startz=z_start+groove_height[i], speed = groove_speed[count], nozzle = nozzle, valve = valve)
                g.feed(movement_feed)
                g.abs_move(**{nozzle:z_start+10})
            else:
                g.abs_move(starting[0]+0.5, starting[1]-4.5)
                g.abs_move(**{nozzle:z_start+groove_height[i]})
                print_grooves(cant_width_groove, cant_length_groove, spacing=groove_space[j], startz=z_start+groove_height[i], speed = groove_speed[count], nozzle = nozzle, valve = valve)
                g.feed(movement_feed)
                g.abs_move(**{nozzle:z_start+10})
                    
        count = count + 1
    g.abs_move(**{nozzle:ZZ+60})
        

################### don't ever uncomment this###
g.write("POSOFFSET CLEAR X Y U A B C D") 
reference_nozzle = 'A' 
active_slide = 'slide1'
z_ref = -88.641972
automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#
### run full alignment###
#
#setup(active_slide, ref = reference_nozzle, move_to_ref = True)


#################Rezero some nozzles but use the rest of the old info ###
#automator.setup()
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#automator.rezero_nozzles(['A'], alignment_path=r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt", cal_file=True)


######## COMMANDS TO MOVE REF NOZZLE TO SUBSTRATE ORIGIN (0,5)
######
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#g.direct_write = True
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1] + 5)
#g.abs_move(**{'A':(automator.substrate_origins[active_slide]['A'][2]+ .2)})
#g.dirct_write = False
#    
    
################### all the printing and array stuff below


#####All stuff below here should be commented during alignment section, then comment out setup(), and uncomment everything below and run. 
# it will profile an array, then output the printing to an outfile
                
######### Profiling and Array building ########################

g.abs_move(A=-1, B=-1, C=-1, D=-1)

slide0=(automator.substrate_origins[active_slide]['A'][0]+11, automator.substrate_origins[active_slide]['A'][1]+11)
prof_A_offset = (automator.home_positions['A'][0]-automator.groove_crosshair[0], automator.home_positions['A'][1]-automator.groove_crosshair[1])
x_space = 30
y_space = 30
cantilever_position = ((slide0[0], slide0[1]), (slide0[0]+x_space*1, slide0[1]+y_space*0), (slide0[0]+x_space*2, slide0[1]+y_space*0), (slide0[0]+x_space*3, slide0[1]+y_space*0), (slide0[0]+x_space*4, slide0[1]+y_space*0), 
                      (slide0[0]+x_space*0, slide0[1]+y_space*-1), (slide0[0]+x_space*1, slide0[1]+y_space*-1), (slide0[0]+x_space*2, slide0[1]+y_space*-1),(slide0[0]+x_space*3, slide0[1]+y_space*-1),(slide0[0]+x_space*4, slide0[1]+y_space*-1),
                       (slide0[0]+x_space*0, slide0[1]+y_space*-2), (slide0[0]+x_space*1, slide0[1]+y_space*-2), (slide0[0]+x_space*2, slide0[1]+y_space*-2),(slide0[0]+x_space*3, slide0[1]+y_space*-2),(slide0[0]+x_space*4, slide0[1]+y_space*-2))
print slide0                
#(100,100)                                                
cantilever_position = ((slide0[0], slide0[1]), (slide0[0]+x_space*1, slide0[1]+y_space*0), (slide0[0]+x_space*2, slide0[1]+y_space*0), (slide0[0]+x_space*3, slide0[1]+y_space*0), (slide0[0]+x_space*4, slide0[1]+y_space*0), 
                      (slide0[0]+x_space*0, slide0[1]+y_space*-1), (slide0[0]+x_space*1, slide0[1]+y_space*-1), (slide0[0]+x_space*2, slide0[1]+y_space*-1),(slide0[0]+x_space*3, slide0[1]+y_space*-1),(slide0[0]+x_space*4, slide0[1]+y_space*-1),
                       (slide0[0]+x_space*0, slide0[1]+y_space*-2), (slide0[0]+x_space*1, slide0[1]+y_space*-2), (slide0[0]+x_space*2, slide0[1]+y_space*-2),(slide0[0]+x_space*3, slide0[1]+y_space*-2),(slide0[0]+x_space*4, slide0[1]+y_space*-2))
automator.setup()
g.direct_write=True
array = collect_array(prof_A_offset)
relative_zeros = normalize_array(array)
print relative_zeros


################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
#
substrate_dif = automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref

if 'A' in AXES_USED:
    zA = automator.substrate_origins[active_slide]['A'][2] - substrate_dif
if 'B' in AXES_USED:
    zB = automator.substrate_origins[active_slide]['B'][2] - substrate_dif
if 'C' in AXES_USED:
    zC = automator.substrate_origins[active_slide]['C'][2] - substrate_dif
if 'D' in AXES_USED:
    zD = automator.substrate_origins[active_slide]['D'][2] - substrate_dif    

outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\print_groovy_out.pgm"
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )

pressure_box = 4       # COM port of pressure box   

g.feed(20)

g.write("POSOFFSET CLEAR X Y U A B C D")    
g.abs_move(A=-1, B=-1, C=-1, D=-1)
g.toggle_pressure(pressure_box)   
print_all_bottoms()
g.toggle_pressure(pressure_box)
g.dwell(60)
g.toggle_pressure(pressure_box)
print_all_grooves()
g.toggle_pressure(pressure_box)
#
#
###########

g.write("POSOFFSET CLEAR X Y U A B C D")       
g.teardown()