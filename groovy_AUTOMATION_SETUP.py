from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator

#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\cell_printing_out.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = [
            'A',
           #  'B',
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
meander_length = 6
meander_width = 4
groove_spacing = (0.06,)*15

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
        g.abs_move(x=automator.substrate_origins[active_slide][ref][0], y=automator.substrate_origins[active_slide][ref][1] + 5)
        g.abs_move(**{ref:(automator.substrate_origins[active_slide][ref][2]+ 1)})
        g.direct_write = False


def identify_slide(origin = (40,127.25)):
    g.direct_write = True
    g.write('POSOFFSET CLEAR X Y U A B C D')
    g.feed(25)
    g.abs_move(A=-0.5, B=-0.5, C=-0.5, D=-0.5)
    g.feed(40)
    g.abs_move(x=origin[0], y= origin[1])
    x_values = automator.find_substrate_bounds(dimension='x')
    g.abs_move(x=origin[0], y= origin[1])
    y_values = automator.find_substrate_bounds(dimension='y')
    x_mid = (x_values[1]-x_values[0])/2+x_values[0]
    y_mid = (y_values[1]-y_values[0])/2+y_values[0]
    return x_mid, y_mid
    


def collect_array():
    zero_vals = np.zeros(15)
     #for i, x in enumerate(y_range):
     #       for j, y in enumerate(x_range):
    for i in range(15):
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1])
        zero_vals[i] = automator.find_profilometer_middle(z_start=-94)
    return zero_vals

def normalize_array(array):
    z_ref = array[0]
    norm_array = np.zeros(15)
            
                        


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

#def print_all_grooves():
#    for i in range(15):
#        g.abs_move(
#        
        
        
        
################### Full Setup Run
reference_nozzle = 'A' 
active_slide = 'slide1'
#active_slide = 'slide2'
#active_slide = 'slide3'

#
setup(active_slide, ref = reference_nozzle, move_to_ref = True)

##########
#
#


#
#################Rezero some nozzles but use the rest of the old info ###
#automator.setup()
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#automator.rezero_nozzles(['B',], alignment_path=r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt", cal_file=True)
#
###
###
######## COMMANDS TO MOVE REF NOZZLE TO SUBSTRATE ORIGIN (0,5)
####
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#g.direct_write = True
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1] + 5)
#g.abs_move(**{'A':(automator.substrate_origins[active_slide]['A'][2]+ .2)})
#g.dirct_write = False

#####Reset zeros ############


#automator.substrate_origins['slide1']['B'][2]



        #automator.substrate_origins['slide1'][reference_nozzle][2]-0.01
        

g.write("POSOFFSET CLEAR X Y U A B C D")        
        
        
#profiling and date collection
automator.setup()                
slide0= identify_slide()

print slide0                
#(100,100)                                                
cantilever_position = ((slide0[0], slide0[1]), (slide0[0]+x_space*1, slide0[1]+y_space*0), (slide0[0]+x_space*2, slide0[1]+y_space*0), (slide0[0]+x_space*3, slide0[1]+y_space*0), (slide0[0]+x_space*4, slide0[1]+y_space*0), 
                      (slide0[0]+x_space*0, slide0[1]+y_space*-1), (slide0[0]+x_space*1, slide0[1]+y_space*-1), (slide0[0]+x_space*2, slide0[1]+y_space*-1),(slide0[0]+x_space*3, slide0[1]+y_space*-1),(slide0[0]+x_space*4, slide0[1]+y_space*-1),
                       (slide0[0]+x_space*0, slide0[1]+y_space*-2), (slide0[0]+x_space*1, slide0[1]+y_space*-2), (slide0[0]+x_space*2, slide0[1]+y_space*-2),(slide0[0]+x_space*3, slide0[1]+y_space*-2),(slide0[0]+x_space*4, slide0[1]+y_space*-2))
zero_vals = collect_array()
print zero_vals