from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\cell_printing_out.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = ['A',
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
        'origin': (230,107),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (45,45),
    },
    'slide2': {
        'origin': (230,51),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (45,45),
    },
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
    outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )


def setup(active_slide, ref, move_to_ref = False):
    automator.setup()
    automator.automate()
    automator.save_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
    automator.teardown()
    g.direct_write = True
    g.set_cal_file(r'C:\Users\Lewis Group\Desktop\Calibration\CAL_output.cal')
    g.direct_write = False
    if move_to_ref is True:
        g.direct_write = True
        g.abs_move(x=automator.substrate_origins[active_slide][ref][0], y=automator.substrate_origins[active_slide][ref][1] + 5)
        g.abs_move(**{ref:(automator.substrate_origins[active_slide][ref][2]+ 1)})
        g.direct_write = False
        
        

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
################Rezero some nozzles but use the rest of the old info ###
#automator.setup()
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#automator.rezero_nozzles(['A','C'], alignment_path=r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt", cal_file=True)

##
###
######## COMMANDS TO MOVE REF NOZZLE TO SUBSTRATE ORIGIN (0,5)
##
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
#g.direct_write = True
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1] + 5)
#g.abs_move(**{'A':(automator.substrate_origins[active_slide]['A'][2]+ 0.2)})
#g.dirct_write = False

######Reset zeros ############


#automator.substrate_origins['slide1']['B'][2]



        #automator.substrate_origins['slide1'][reference_nozzle][2]-0.01
        

g.write("POSOFFSET CLEAR X Y U A B C D")
        
        
        
        
        
        
        
        
        
        