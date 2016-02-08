from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\alexs_print.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = [
            'A',
            'B',
            'C', 
            #'D'
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
        'origin': (90,110),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (10,10),
    },
    'slide2': {
        'origin': (150,110),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (10,10),
    },
    'slide3': {
        'origin': (230,110),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (10,10),
    }
}

#Defining profilometry parameters
automator = AerotechAutomator(
    calfile_path=r'C:\Users\Lewis Group\Desktop\Calibration\CAL_output.cal',
    axes=AXES_USED,
    axes_data = AXES_DATA,
    substrates = SUBSTRATES,
)

#Defining mecode parameters
g = G(
    direct_write=False,
    outfile=outfile,
    header=None,
    footer=None,
    print_lines=False,
    )




############### VARIABLE AND PARAMTER DEFINITIONS ###############



#ORIGIN OF PRINTING AREA IS DEFINED AS BOTTOM LEFT CORNER OF SUBSTRATE (glass 2"x3")

zA  = zB = zC = zD =0



#ORIGIN OF PRINTING AREA IS DEFINED AS BOTTOM LEFT CORNER OF SUBSTRATE (glass 2"x3")

zA  = zB = zC = zD =0

pressure_box = 4       # COM port of pressure box    

vacuum = 18                 # value of vacuum, "H20

#### ATMEGA328
#        outer pin perimeter: 9mm x 9mm
#        inner packaging perimeter: 7mm x 7mm
#        'pad target' at end of each pin is approx. 0.4mm x 0.4mm
#        pad positions are the CENTER of each of these pad targets
#
#        set bottom left corner of outer border as 0,0, pad position 
#
#        pads numbered using SAME convention as pin numbering - #1 is top left pin on left side, continues counterclockwise around chip

    


ATMEGA328_pad_positions = (

((0.2,7.3),(0.2,6.5),(0.2,5.7),(0.2,4.9),(0.2,4.1),(0.2,3.3),(0.2,2.5),(0.2,1.7)),
((1.7,0.2),(2.5,0.2),(3.3,0.2),(4.1,0.2),(4.9,0.2),(5.7,0.2),(6.5,0.2),(7.3,0.2)),
((8.8,1.7),(8.8,2.5),(8.8,3.3),(8.8,4.1),(8.8,4.9),(8.8,5.7),(8.8,6.5),(8.8,7.3)),
((7.3,8.8),(6.5,8.8),(5.7,8.8),(4.9,8.8),(4.1,8.8),(3.3,8.8),(2.5,8.8),(1.7,8.8))

)



###these coordinats are relative to the starting location of the VCC terminal, which changes print to print

LED_HARVARD_POSITIONS = [[[5,29.6],[5,24.8],[5,20],[5,15.2]],[[5,10],[8.65,20],[11.65,20],[15.5,10.1]],[[15.4,29.6],[15.4,24.8],[15.4,20],[15.4,15.2]],]


############### END OF VARIABLE AND PARAMTER DEFINITIONS ###############


############################# FUNCTION DEFINITIONS ###########################


def set_home_in_z():
    g.write('POSOFFSET CLEAR A B C D')
    g.feed(25)
    g.abs_move(A=-2, B=-2, C=-2, D=-2)
    g.set_home(A=(-zA -2), B=(-zB -2), C = (-zC - 2), D=(-zD - 2))
    print "zB post set home: {}".format(zB)
def clear_XYhome():
    g.write('POSOFFSET CLEAR X Y U')

def pressure_purge(delay, valve = None):
    g.toggle_pressure(pressure_box)
    g.write('$DO6.0=1')
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(delay)
    g.write('$DO6.0=0')
    if valve is not None:
        g.set_valve(num = valve, value = 0)
    g.toggle_pressure(pressure_box)
    g.dwell(0.5)    

def pressure_clear(dwell_time, pressure, valve):
    g.set_pressure(pressure_box, pressure)
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell_time)
    g.toggle_pressure(pressure_box)
    g.set_pressure(pressure_box, 1)
    g.dwell(0.2)
    g.set_valve(num = valve, value = 0) 
    g.toggle_pressure(pressure_box)
    
    
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


def tpu_Harvard_bottom(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
########test line
    #g.abs_move(x=2,y=1)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=20)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.set_pressure(pressure_box, pressure)
    
########printing 
    g.abs_move(4, 1)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.meander(x=26,y=42,spacing=0.55,start='LL',orientation='y')
    #g.rect(x=60,y=10,start='LL')
    g.set_valve(num = valve, value = 0)
    g.feed(20)
    g.clip(axis=nozzle, height=5, direction='-y')





def tpu_bottom_LED_strain(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
#######test line
    g.abs_move(x=1,y=1)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=20)   
    g.move(y=.5)
    g.move(x=-20) 
    g.set_valve(num = valve, value = 0)
    g.feed(20)
    g.clip(axis=nozzle, height=6, direction='-x')
    g.set_pressure(pressure_box, pressure)
    
#########printing 
    g.abs_move(6, 6)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.meander(x=26,y=13,spacing=0.55,start='LL',orientation='x')
    #g.rect(x=60,y=10,start='LL')
    g.set_valve(num = valve, value = 0)
    g.feed(20)
    g.clip(axis=nozzle, height=5, direction='-y')
    
#    g.abs_move(4, 18)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)
#    g.meander(x=60,y=10,spacing=0.8,start='LL',orientation='x')
#    #g.rect(x=60,y=10,start='LL')
#    g.set_valve(num = valve, value = 0)
#    g.feed(20)
#    g.clip(axis=nozzle, height=5, direction='-y')
#
#    g.abs_move(4, 32)    
#    g.abs_move(**{nozzle:height}) 
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)
#    g.meander(x=60,y=10,spacing=0.8,start='LL',orientation='x')
#    #g.rect(x=60,y=10,start='LL')
#    g.set_valve(num = valve, value = 0)
#    g.feed(20)
#    g.clip(axis=nozzle, height=5, direction='-y')


def LED_strain(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    #########test line
    #g.abs_move(x=1.5,y=20)
    #g.abs_move(**{nozzle:height-.72})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=8)
    #g.move(x=0.5)
    #g.move(y=-8)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='-x')
    
    
#    #####first wire
#    
    g.abs_move(x=19, y=9) 
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)

  
    ####PAD
    g.feed(speed*0.8)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.move(x=1.3)
    g.move(x=-0.7,y=0.5)
    g.move(y=-1)
    g.move(x=0.7,y=0.5)
    g.move(x=-0.5)

    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.move(x=0.5)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
#    g.set_valve(num = valve, value = 0)
#    g.feed(10)
#    g.clip(axis=nozzle,height=2, direction='+x')
##
    ####PAD
    g.feed(speed*0.8)
    g.move(x=0.5)
    g.move(x=-0.5)
    g.move(x=0.7,y=0.5)
    g.move(y=-1)
    g.move(x=-0.7,y=0.5)
    g.move(x=1.3)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')
#    
    
    
    g.abs_move(x=19, y=23) 
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    
    ####PAD
    g.feed(speed*0.8)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.move(x=1.3)
    g.move(x=-0.7,y=0.5)
    g.move(y=-1)
    g.move(x=0.7,y=0.5)
    g.move(x=-0.5)
    

    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.move(x=0.5)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    #g.set_valve(num = valve, value = 0)
    #g.feed(10)
    #g.clip(axis=nozzle,height=2, direction='+x')


    ####PAD
    g.feed(speed*0.8)
    g.move(x=0.5)
    g.move(x=-0.5)
    g.move(x=0.7,y=0.5)
    g.move(y=-1)
    g.move(x=-0.7,y=0.5)
    g.move(x=1.3)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')
    
#    #
#    #
#    #
    g.abs_move(x=19, y=37) 
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)

    ####PAD    
    g.feed(speed*0.8)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.move(x=1.3)
    g.move(x=-0.7,y=0.5)
    g.move(y=-1)
    g.move(x=0.7,y=0.5)
    g.move(x=-0.5)
    
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.move(x=0.5)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1})
    g.move(x=1.1,**{nozzle:-1})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=5.2)
    #g.set_valve(num = valve, value = 0)
    #g.feed(10)
    #g.clip(axis=nozzle,height=2, direction='+x')


    ####PAD
    g.feed(speed*0.8)
    g.move(x=0.5)
    g.move(x=-0.5)
    g.move(x=0.7,y=0.5)
    g.move(y=-1)
    g.move(x=-0.7,y=0.5)
    g.move(x=1.3)
    g.move(x=0.8)  
    g.arc(x=-1.6,y=0,radius=0.8)
    g.arc(x=1.6,y=0,radius=0.8)
    g.move(x=-0.2)
    g.arc(x=-1.2,y=0,radius=0.6)
    g.arc(x=1.2,y=0,radius=0.6)
    g.move(x=-0.2)
    g.arc(x=-0.8,y=0,radius=0.4)
    g.arc(x=0.8,y=0,radius=0.4)
    g.move(x=-0.2)
    g.arc(x=-0.4,y=0,radius=0.2)
    g.arc(x=0.4,y=0,radius=0.2)
    g.move(x=-0.2)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')

        


    
def TPU_spacing_tests(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ######test line
    g.abs_move(x=2,y=1.)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=50)
    g.set_valve(num = valve, value = 0)
    g.feed(20)
    g.clip(axis=nozzle, height=6, direction='+y')
    
    my_space = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]

    #####first wire
    
        
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i],y=3)
          g.abs_move(**{nozzle:height}) 
          g.feed(speed)
          if valve is not None:
              g.set_valve(num = valve, value = 1)
          g.dwell(dwell)
          g.meander(x=7,y=43,orientation='y',spacing=my_space[i],start='LL')
          g.set_valve(num = valve, value = 0)
          g.feed(40)
          g.clip(axis=nozzle,height=5, direction='+x')



def AgTPU_strain_speciman(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    #####test line
    #g.abs_move(x=2,y=0)
    #g.abs_move(**{nozzle:height-.2})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=10)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='+y')
    
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]
##
##    ############BOTTOM LAYER
##            
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1,y=3+2+3)
#          g.abs_move(**{nozzle:height}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.meander(x=5,y=4,spacing=0.32,orientation='y')
#          g.move(x=-2.5)
#          g.move(y=1.5)
#          g.move(x=-0.8,y=-1.3)
#          g.move(x=1.6)
#          g.move(x=-0.8,y=1.3)
#          
#          
#          g.move(y=21)
#          
#          
#          g.move(x=-0.8,y=1.3)
#          g.move(x=1.6)
#          g.move(x=-0.8,y=-1.3)
#          g.move(y=1.5)
#          g.move(x=-2.5)
#          g.meander(x=5,y=4,spacing=0.32,orientation='y')
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+x')
#        
#    ###########2nd LAYER     
#    #g.dwell(20)            
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
#          g.abs_move(**{nozzle:height+0.1}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.move(y=24)  
#
#
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+y')
    
    
#    ############3rd LAYER
    #g.dwell(20)
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
          g.abs_move(**{nozzle:height+0.2}) 
          g.feed(speed)
          if valve is not None:
              g.set_valve(num = valve, value = 1)
          g.dwell(dwell)

          g.move(y=24)

          g.set_valve(num = valve, value = 0)
          g.feed(40)
          g.clip(axis=nozzle,height=5, direction='+y')
###          
###          
##    ############4th LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
#          g.abs_move(**{nozzle:height+0.24}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+y')
#          
#    ############5th LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
#          g.abs_move(**{nozzle:height+0.32}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+y')
#
#    ############6th LAYER
#    #g.dwell(20)
#    for i in [0,1,2,3,4,5,6,7]:
#          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
#          g.abs_move(**{nozzle:height+0.4}) 
#          g.feed(speed)
#          if valve is not None:
#              g.set_valve(num = valve, value = 1)
#          g.dwell(dwell)
#
#          g.move(y=25)
#
#          g.set_valve(num = valve, value = 0)
#          g.feed(40)
#          g.clip(axis=nozzle,height=5, direction='+y')



def stiffTPU_strain_speciman(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    #####test line
    g.abs_move(x=2,y=1)
    g.abs_move(**{nozzle:height-.125})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=10)
    g.set_valve(num = valve, value = 0)
    g.feed(20)
    g.clip(axis=nozzle, height=6, direction='-y')
    
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]
##
##    ############BOTTOM LAYER
##            
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]+1,y=3+2+3)
          g.abs_move(**{nozzle:height}) 
          g.feed(speed)
          if valve is not None:
              g.set_valve(num = valve, value = 1)
          g.dwell(dwell)

          g.meander(x=5,y=4,spacing=0.5,orientation='y')
          g.move(x=-2.5)
          g.move(y=1.5)
          g.move(x=-0.8,y=-1.3)
          g.move(x=1.6)
          g.move(x=-0.8,y=1.3)
          
          
          g.move(y=21)
          
          
          g.move(x=-0.8,y=1.3)
          g.move(x=1.6)
          g.move(x=-0.8,y=-1.3)
          g.move(y=1.5)
          g.move(x=-2.5)
          g.meander(x=5,y=4,spacing=0.5,orientation='y')
          g.set_valve(num = valve, value = 0)
          g.feed(40)
          g.clip(axis=nozzle,height=5, direction='+x')
        
    
    
    
def LED_Harvard_agtpu(valve,nozzle,height,speed,dwell,pressure,LorR,startx,starty):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #
    #########test line
    #g.abs_move(x=1,y=1)
    #g.abs_move(**{nozzle:height-.4})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=20)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='-x')
    
    
    #####first wire
    if LorR == 'L':
        g.abs_move(startx, starty) 
    else:
        g.abs_move(startx+31, starty) 

    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=33)
    g.move(x=5)
    g.move(y=-2.3)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-0.3)
    g.move(x=0.9)
    g.move(y=8.5)
    g.move(x=8.5)
    g.move(y=-10)
    g.move(x=3.1)
    g.abs_move(y=9)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')


    #
    #####second wire
    if LorR == 'L':
        g.abs_move(startx, starty) 
    else:
        g.abs_move(startx+31, starty)     
    g.abs_move(**{nozzle:height+0.04}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=3)
    g.move(x=1,**{nozzle:-0.04})
    g.move(x=4)
    g.move(y=5.9)
    g.set_valve(num = valve, value = 0)
    g.move(y=1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=0.9)
    g.move(x=1.6)
    g.move(y=8)
    g.move(x=0.95)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(x=1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=0.8)
    g.set_valve(num = valve, value = 0)
    g.move(x=1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(x=1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=0.95)
    g.move(y=-8.5)
    g.move(x=1.8)
    g.move(y=-0.3)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-0.3)
    g.move(x=2)
    g.abs_move(y=9)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')


    ######third wire
    if LorR == 'L':
        g.abs_move(startx, starty) 
    else:
        g.abs_move(startx+31, starty)     
    g.abs_move(**{nozzle:height+0.05}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=33)
    g.move(x=5)
    g.move(x=1,**{nozzle:-0.05})
    g.move(x=9.4)
    g.move(y=-2.3)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-2.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=-1.1,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-1.1,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-0.5)
    g.move(x=2.1)
    g.abs_move(y=starty)


    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')





#
#    #####anode/cathode
#    g.feed(speed*0.4)
#    g.move(x=0.8)  
#    g.arc(x=-1.6,y=0,radius=0.8)
#    g.arc(x=1.6,y=0,radius=0.8)
#    g.move(x=-0.2)
#    g.arc(x=-1.2,y=0,radius=0.6)
#    g.arc(x=1.2,y=0,radius=0.6)
#    g.move(x=-0.2)
#    g.arc(x=-0.8,y=0,radius=0.4)
#    g.arc(x=0.8,y=0,radius=0.4)
#    g.move(x=-0.2)
#    g.arc(x=-0.4,y=0,radius=0.2)
#    g.arc(x=0.4,y=0,radius=0.2)
#    g.move(x=-0.2)
#    g.set_valve(num = valve, value = 0)
#    g.feed(10)
#    g.clip(axis=nozzle,height=2, direction='+x')
#
#    if LorR == 'L':
#        g.abs_move(startx, starty) 
#    else:
#        g.abs_move(startx+31, starty) 
#    g.abs_move(**{nozzle:height+0.03}) 
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)
#    g.feed(speed*0.4)
#    g.move(x=0.8)  
#    g.arc(x=-1.6,y=0,radius=0.8)
#    g.arc(x=1.6,y=0,radius=0.8)
#    g.move(x=-0.2)
#    g.arc(x=-1.2,y=0,radius=0.6)
#    g.arc(x=1.2,y=0,radius=0.6)
#    g.move(x=-0.2)
#    g.arc(x=-0.8,y=0,radius=0.4)
#    g.arc(x=0.8,y=0,radius=0.4)
#    g.move(x=-0.2)
#    g.arc(x=-0.4,y=0,radius=0.2)
#    g.arc(x=0.4,y=0,radius=0.2)
#    g.move(x=-0.2)
#    g.set_valve(num = valve, value = 0)
#    g.feed(10)
#    g.clip(axis=nozzle,height=2, direction='+x')


def LED_Harvard_connectors(valve,nozzle,height,speed,dwell,pressure,startx,starty):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    
######first wire
    #g.abs_move(startx, starty)
    
    for i in [0,1,2,3]:
        g.abs_move(x = LED_HARVARD_POSITIONS[0][i][0], y = LED_HARVARD_POSITIONS[0][i][1]) 
        g.move(y=0.8)
        g.abs_move(**{nozzle:height})
        g.dwell(15) 
        g.feed(2)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=1, direction='+y')
        g.move(y=-1.8)
        g.abs_move(**{nozzle:height})
        g.dwell(15) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=1, direction='-y') 
        g.feed(25)
#        
    


#####second wire
    g.abs_move(startx, starty)
    
    for i in [0,1,2,3]:
        g.abs_move(x = LED_HARVARD_POSITIONS[1][i][0], y = LED_HARVARD_POSITIONS[1][i][1]) 
        if i==0:
            g.move(y=0.8)
            g.abs_move(**{nozzle:height})
            g.dwell(15) 
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='+y')
            g.move(y=-1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(15) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='-y')
            g.abs_move(**{nozzle:height+2}) 
            g.feed(25)
        elif  i==3:
            g.move(y=0.8)
            g.abs_move(**{nozzle:height})
            g.dwell(15) 
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='+y')
            g.move(y=-1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(15) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='-y') 
            g.feed(25)
            
            
        elif i==1 or i==2:
            g.move(x=-0.8)
            g.abs_move(**{nozzle:height}) 
            g.dwell(15)
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='+x')
            g.move(x=1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(15) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=1, direction='-x') 
            g.feed(25)
            


######third wire
    g.abs_move(startx, starty)
    
    for i in [0,1,2,3]:
        g.abs_move(x = LED_HARVARD_POSITIONS[2][i][0], y = LED_HARVARD_POSITIONS[2][i][1]) 
        g.move(y=0.8)
        g.abs_move(**{nozzle:height}) 
        g.dwell(15)
        g.feed(2)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=1, direction='+y')
        g.move(y=-1.8)
        g.abs_move(**{nozzle:height})
        g.dwell(15) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=1, direction='-y')
        g.feed(25)
        


def LED_Harvard_adhesive(valve,nozzle,height,speed,dwell,pressure,startx,starty,LorR):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    for j in [0,1,2]:

        if LorR == 'L':
            g.abs_move(startx, starty) 
        else:
            g.abs_move(startx+31, starty) 
        
        
        
        
        
        for i in [0,1,2,3]:
            g.abs_move(x = LED_HARVARD_POSITIONS[j][i][0], y = LED_HARVARD_POSITIONS[j][i][1]) 
            g.feed(10)
            g.abs_move(**{nozzle:height})
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell) 
            g.set_valve(num = valve, value = 0)
            g.feed(10)
            g.clip(axis=nozzle, height=1, direction='+y')
            g.feed(25)
          



def pickandplace(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    #if wire == 'first':

    ##LED 1
    g.abs_move(x = 19.00, y = 64.634)
    g.feed(10) 
    g.abs_move(**{nozzle:2.178+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.178})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][0][0], y = LED_HARVARD_POSITIONS[0][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
#
    ##LED 2
    g.abs_move(x = 19.000, y = 64.634-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.178+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.178})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][1][0], y = LED_HARVARD_POSITIONS[0][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    #LED 3
    g.abs_move(x = 19.000, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][2][0], y = LED_HARVARD_POSITIONS[0][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 4
    g.abs_move(x = 19.000+3, y = 64.634)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][3][0], y = LED_HARVARD_POSITIONS[0][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    

    
#elif wire == 'second':
    
    ##LED 5
    g.abs_move(x = 19.000+3+3+3, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][0][0], y = LED_HARVARD_POSITIONS[1][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    ##LED 6
    g.abs_move(x = 19.000-3-3, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][1][0], y = LED_HARVARD_POSITIONS[1][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 7
    g.abs_move(x = 19.000-3, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][2][0], y = LED_HARVARD_POSITIONS[1][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    
    ##LED 8
    g.abs_move(x = 19.000+3, y = 64.634-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][3][0], y = LED_HARVARD_POSITIONS[1][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})


#else:
    
    ##LED 9
    g.abs_move(x = 19.000+3, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][0][0], y = LED_HARVARD_POSITIONS[2][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    ##LED 10
    g.abs_move(x = 19.000+3+3, y = 64.634)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][1][0], y = LED_HARVARD_POSITIONS[2][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 11
    g.abs_move(x = 19.000+3+3, y = 64.634-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][2][0], y = LED_HARVARD_POSITIONS[2][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    
    ##LED 12
    g.abs_move(x = 19.000+3, y = 64.634-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.3+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.3})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][3][0], y = LED_HARVARD_POSITIONS[2][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7+.1+.1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})


def pickandplace_magnets(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    ##magnet 1  (bottom left)
    g.abs_move(x = -22.466, y = -1.182)
    g.feed(10) 
    g.abs_move(**{nozzle:1.837+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:1.837})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = 8.00, y = 5.00) 
    g.abs_move(**{nozzle:0.952+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.952})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:20})

    ##magnet 2  (top right)
    g.abs_move(x = 53.568, y = 70.82)
    g.feed(10) 
    g.abs_move(**{nozzle:1.86+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:1.86})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = 25.4, y = 5.00) 
    g.abs_move(**{nozzle:0.952+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.952})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:20})




def tpu_top_LED_Harvard(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
########printing 
    g.abs_move(4, 2)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.meander(x=6.5,y=45,spacing=0.2,start='LL',orientation='y')

    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle, height=5, direction='-y')

















def tpu_layered_serpentine(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.dwell(2)
    g.abs_move(30, 30)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    
    g.dwell(dwell)
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=2.5,y=0,radius=-1.7,direction=direc)
    g.move(x=2)
    g.dwell(dwell)
    
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, height=10, direction='-y')

def arduino_gen1(valve,nozzle,height,speed,dwell,pressure,testline):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
   
    #if testline == 'y':
    #    #########test line
    #    g.abs_move(x=30,y=-17)
    #    g.abs_move(**{nozzle:height-.35})
    #    if valve is not None:
    #        g.set_valve(num = valve, value = 1)
    #    g.dwell(dwell)
    #    g.feed(speed)
    #    g.move(x=15)
    #    g.set_valve(num = valve, value = 0)
    #    g.feed(20)
    #    g.clip(axis=nozzle, height=2, direction='-x')
    #    ########test line
    

    
    
    #for i in range(4):
    #    for j in range (8):
    #        g.abs_move(x = ATMEGA328_pad_positions[i][j][0], y = ATMEGA328_pad_positions[i][j][1])
    #        g.move(x = 0.2, y = 0.2)
    #        g.rect(x = 0.4, y = 0.4, start = 'UR')


    #g.abs_move(x=-5.5,y=-5.5)
    #g.rect(x=20,y=20,start='LL')
    
    ##### RESET WIRE, PIN 29
    
    g.abs_move(x=12.5,y=12.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=-1,y=-1)
    g.move(x=0.5)
    g.move(x=-0.5,y=0.5)
    g.move(y=-0.5)
    g.move(x=-1,y=-1)
    g.move(x=-3)
    g.set_valve(num = valve, value = 0)
    g.move(x=-0.6,**{nozzle:1})
    g.move(x=-0.6,**{nozzle:-1})
    g.dwell(0.2)
    g.set_valve(num = valve, value = 1)
    g.abs_move(x = ATMEGA328_pad_positions[3][4][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][4][1])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')

    ##### VCC WIRE, PIN 4
    
    g.abs_move(x=12.5,y=12.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)   
    g.move(x=-7,y=-7)
    g.abs_move(y = ATMEGA328_pad_positions[0][3][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][3][0])
    g.move(x=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    #
    ##### Rx WIRE, PIN 30
    #
    #g.abs_move(x = ATMEGA328_pad_positions[3][5][0], y=13.5)
    #g.abs_move(**{nozzle:height})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)  
    #g.abs_move(y = ATMEGA328_pad_positions[3][5][1])
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='+y')
    
    
    #### Tx WIRE, PIN 30
    
    #g.abs_move(x=-4,y=13.5)
    #g.abs_move(**{nozzle:height})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)  
    #g.move(x=3,y=-3)
    #g.abs_move(x = ATMEGA328_pad_positions[3][6][0])
    #g.abs_move(y = ATMEGA328_pad_positions[3][6][1])
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='+y')
    
    
    ##### GND WIRE (LED), PIN 17
    
    g.abs_move(x=12.5,y=-3.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1,y=1)
    g.move(y=-0.5)
    g.move(x=0.5,y=0.5)
    g.move(x=-0.5)
    g.move(x=-0.5,y=0.5)    
    g.move(x=-1)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.move(y=0.8,**{nozzle:1})
    g.move(y=0.8,**{nozzle:-1})
    g.dwell(0.2)
    g.set_valve(num = valve, value = 1)
    g.move(y=0.6)
    g.set_valve(num = valve, value = 0)
    g.move(y=0.5,**{nozzle:1})
    g.move(y=0.5,**{nozzle:-1})
    g.dwell(0.2)
    g.set_valve(num = valve, value = 1)
    g.abs_move(y = ATMEGA328_pad_positions[2][0][1])
    g.abs_move(x = ATMEGA328_pad_positions[2][0][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    


    ##### GND WIRE (cap, half of oscillator), PIN 20, 5, 7
    
    g.abs_move(x=12.5,y=-3.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.abs_move(y = ATMEGA328_pad_positions[0][4][1])
    g.move(x=-7.5)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.dwell(0.2)
    g.set_valve(num = valve, value = 1)
    g.abs_move(y = ATMEGA328_pad_positions[0][6][1])
    g.move(x=-1.5)
    g.move(x=1.5)
    g.abs_move(x = ATMEGA328_pad_positions[0][6][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')
#
#
    ##### GND WIRE (other cap, other half of oscillator), PIN 8
    
    g.abs_move(x=12.5,y=-3.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.move(y=-2,)
    g.move(x=-4)
    g.abs_move(x=0,y=0)
    g.move(y=-3)
    g.move(x=-1)
    g.move(y=2.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=0.8,**{nozzle:1})
    g.move(y=0.8,**{nozzle:-1})
    g.dwell(0.2)
    g.set_valve(num = valve, value = 1)
    g.move(x=-3.5)
    g.move(y=1)    
    g.move(y=-1)
    g.move(x=3.5)
    g.abs_move(y = ATMEGA328_pad_positions[0][7][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][7][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')















#
#    ##### Tx terminal
#
#    g.abs_move(x=-4,y=13.5)
#    g.abs_move(**{nozzle:height+0.09})
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)  
#    g.move(x=-0.75,y=-0.75)
#    g.rect(x=1.5,y=1.5)
#    g.set_valve(num = valve, value = 0)
#    g.feed(15)
#    g.clip(axis=nozzle, height=2,direction='-x')
#
#
#    ##### Rx terminal
#
#    g.abs_move(x = ATMEGA328_pad_positions[3][5][0], y=13.5)
#    g.abs_move(**{nozzle:height})
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)  
#    g.move(x=-0.75,y=-0.75)
#    g.rect(x=1.5,y=1.5)
#    g.set_valve(num = valve, value = 0)
#    g.feed(15)
#    g.clip(axis=nozzle, height=2,direction='-x')
#
#
#
    ##### VCC terminal
    #
    #g.abs_move(x=13.5,y=13.5)
    #g.abs_move(**{nozzle:height})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)  
    #g.move(x=-0.75,y=-0.75)
    #g.rect(x=1.5,y=1.5)
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='-x')
#    
#    
    ###### GND WIRE (LED), PIN 17
    #
    #g.abs_move(x=13.5,y=-4)
    #g.abs_move(**{nozzle:height})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)  
    #g.move(x=-0.75,y=-0.75)
    #g.rect(x=1.5,y=1.5)
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='-x')


#################################### END OF FUNCTION DEFINITIONS #######################################



#################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
reference_nozzle = 'A'

active_slide = 'slide1'
z_ref = -79.77875

####
#active_slide = 'slide2'
#z_ref = -79.54625
###
#####
#active_slide = 'slide3'
#z_ref = -79.12

automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
g.write("POSOFFSET CLEAR X Y U A B C D")

  

substrate_dif = 0

#substrate_dif = automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref
#

#automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref

if 'A' in AXES_USED:
    zA = automator.substrate_origins[active_slide]['A'][2] - substrate_dif
if 'B' in AXES_USED:
    zB = automator.substrate_origins[active_slide]['B'][2] - substrate_dif
if 'C' in AXES_USED:
    zC = automator.substrate_origins[active_slide]['C'][2] - substrate_dif
if 'D' in AXES_USED:
    zD = automator.substrate_origins[active_slide]['D'][2] - substrate_dif    

###############################------------------ TPU HARVARD LED ARRAY DEVICE-------------------###############################

#
########------------SOFT TPU BOTTOM
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
#tpu_Harvard_bottom(valve='2',nozzle='B',height=0.7,speed=11,dwell=0.2,pressure=6)
#
#
##tpu_bottom_LED_strain(valve='2',nozzle='B',height=0.5,speed=13,dwell=0.2,pressure=10)
##TPU_spacing_tests(valve='1',nozzle='A',height=0.5,speed=10.5,dwell=0.2,pressure=6)
#g.toggle_pressure(pressure_box)



##########------------ STIFF TPU LAYER
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##LED_Harvard(valve='1',nozzle='A',height=0.16+0.06+0.06+0.06,speed=7,dwell=0.1,pressure=45,LorR='R',startx=8,starty=7)
#stiffTPU_strain_speciman(valve='1',nozzle='A',height=0.7,speed=3,dwell=0.4,pressure=10)
#
#g.toggle_pressure(pressure_box)


##########------------SOFT AGTPU WIRING
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ac')
#g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##LED_Harvard_agtpu(valve='3',nozzle='C',height=1.0,speed=4,dwell=0.1,pressure=18,LorR='L',startx=5+3,starty=5)
#LED_Harvard_agtpu(valve='3',nozzle='C',height=0.23+0.12,speed=8,dwell=0.3,pressure=13,LorR='L',startx=5+3,starty=5)
#
##LED_strain(valve='1',nozzle='A',height=0.08+.72+.12,speed=2,dwell=0.1,pressure=10)
#
##AgTPU_strain_speciman(valve='2',nozzle='B',height=0.65,speed=4,dwell=0.1,pressure=18) #soft
##AgTPU_strain_speciman(valve='2',nozzle='B',height=0.6,speed=2.2,dwell=0.1,pressure=18) #stiff
#
#
#g.toggle_pressure(pressure_box)

#
##
#



######------------------PRINT ME ARDUINO
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#g.set_home(x=-17.5,y=-17.5)
#
#g.toggle_pressure(pressure_box)
#arduino_gen1(valve='2',nozzle='B',height=.38+.08+.02,speed=3.5,dwell=0.1,pressure=7,testline='y')
##arduino_gen1(valve='1',nozzle='A',height=0.02,speed=9,dwell=0.1,pressure=20,startx=35,testline='y')
#
#g.toggle_pressure(pressure_box)





###########------------LED ADHESIVE
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#
#startx=9+31
#starty=7
##
##
#for i in range(len(LED_HARVARD_POSITIONS)):
#        for j in range(len(LED_HARVARD_POSITIONS[i])):
#            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
#            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty
#
#
#
#g.toggle_pressure(pressure_box)
#LED_Harvard_adhesive(valve='2',nozzle='B',height=0.3,speed=7,dwell=0.8,pressure=40,LorR='R',startx=8,starty=7)
#g.toggle_pressure(pressure_box)




###########------------PICK+PLACE
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#
#startx=8
#starty=5
##
#for i in range(len(LED_HARVARD_POSITIONS)):
#        for j in range(len(LED_HARVARD_POSITIONS[i])):
#            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
#            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty
#
##g.dwell(60)
#
#valve='1'
#g.set_pressure(pressure_box, 0.1)
#if valve is not None:
#    g.set_valve(num = valve, value = 1)
#g.set_vac(pressure_box,18)
#g.dwell(2)
#pickandplace(valve='1',nozzle='A',speed=10,dwell=10)
##pickandplace_magnets(valve='1',nozzle='A',speed=10,dwell=10)
#g.set_vac(pressure_box,0)


############------------STIFF AGTPU CONNECTORS 
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
##

startx=8
starty=5
#
for i in range(len(LED_HARVARD_POSITIONS)):
        for j in range(len(LED_HARVARD_POSITIONS[i])):
            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty


g.toggle_pressure(pressure_box)
LED_Harvard_connectors(valve='1',nozzle='A',height=0.5,speed=2,dwell=2.8,pressure=70,startx=8,starty=5)
g.toggle_pressure(pressure_box)
#
###



##########------------TPU TOP
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
#tpu_top_LED_Harvard(valve='1',nozzle='A',height=0.05,speed=20,dwell=0.2,pressure=1.5)
#g.toggle_pressure(pressure_box)








#######------------------PRINT ME ARDUINO
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
#arduino_gen1(valve='1',nozzle='A',height=0.05,speed=4,dwell=0.1,pressure=23,startx=420.766728,starty=108.626399,testline='y')
##arduino_gen1(valve='1',nozzle='A',height=0.02,speed=9,dwell=0.1,pressure=20,startx=35,testline='y')
#
#g.toggle_pressure(pressure_box)










g.view(backend='matplotlib')

##
g.teardown()
