from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\alexs_print.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = [
            'A',
            #'B',
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


pdms_pillar_lid_locations = (                                  #(0,0) is center of bottom left well (C4), order proceed L to R across rows, down colums (A4-A3-A2-A1-B4-B3, etc)

((0.0,52.0),(26.0,52.0),(52.0,52.0),(78.0,52.0)),
((0.0,26.0),(26.0,26.0),(52.0,26.0),(78.0,26.0)),
((0.0,0.0),(26.0,0.0),(52.0,0.0),(78.0,0.0)),

)
###these coordinats are relative to the starting location of the VCC terminal, which changes print to print

LED_HARVARD_POSITIONS = [[[5,29.6],[5,24.8],[5,20],[5,15.2]],[[5,10],[8.65,20],[11.65,20],[15.5,10.1]],[[15.4,29.6],[15.4,24.8],[15.4,20],[15.4,15.2]],]

#### stock positions are absolute coordinates relative to 0,0 of the slide, after nozzle switches to 'C'
#### linear list of LED positions starting at bottom left corner, across the row in (+) x direction, then restart to original x and up one row in (+) y direction, acorss the row again in the (+) direction, etc 

LED_STOCK_POSITIONS_TOP = [

[18.371,58.66],[21.371,58.66],[24.371,58.66],[27.371,58.66],[30.371,58.66],[33.371,58.66],[36.371,58.66],[39.371,58.66],[42.371,58.66],[45.371,58.66],
[18.371,61.66],[21.371,61.66],[24.371,61.66],[27.371,61.66],[30.371,61.66],[33.371,61.66],[36.371,61.66],[39.371,61.66],[42.371,61.66],[45.371,61.66],
[18.371,64.66],[21.371,64.66],[24.371,64.66],[27.371,64.66],[30.371,64.66],[33.371,64.66],[36.371,64.66],[39.371,64.66],[42.371,64.66],[45.371,64.66],

]
LED_STOCK_POSITIONS_SIDE = [

#### linear list of LED positions starting at bottom left corner, up the column in [+] y direction, then restart to original y and over one column in [+] x direction, acorss the row again in the [+] direction, etc 

[-16.983,6.521],[-16.983,9.521],[-16.983,12.521],[-16.983,15.521],[-16.983,18.521],[-16.983,21.521],[-16.983,24.521],[-16.983,27.521],[-16.983,30.521],[-16.983,33.521],
[-13.983,6.521],[-13.983,9.521],[-13.983,12.521],[-13.983,15.521],[-13.983,18.521],[-13.983,21.521],[-13.983,24.521],[-13.983,27.521],[-13.983,30.521],[-13.983,33.521],
[-10.983,6.521],[-10.983,9.521],[-10.983,12.521],[-10.983,15.521],[-10.983,18.521],[-10.983,21.521],[-10.983,24.521],[-10.983,27.521],[-10.983,30.521],[-10.983,33.521],

]



#### all LED_WYSS_POSITIONS are relative to a (0,0) in the bottom left corner of the design, NOT relative to 0,0 of the slide
LED_WYSS_POSITIONS_W = (
(0,11.7),(0.8,9.36),(1.6,7.02),(2.4,4.68),(3.2,2.34),(4.0,0.00),
(4.8,2.34),(5.6,4.68),(6.4,7.02),(7.2,9.36),(8.0,11.7),
(8.8,9.36),(9.6,7.02),(10.4,4.68),(11.2,2.34),(12.0,0.00),
(12.8,2.34),(13.6,4.68),(14.4,7.02),(15.2,9.36),(16.0,11.7),
)
                            
LED_WYSS_POSITIONS_Y = (
(15.4+4,11.7),(16.6+4+0.2,9.36),(17.8+4+0.2,7.02),(19+4+0.2,4.68),(19+4+0.2,2.34),(19+4+0.2,0.00),
(20.2+4+0.2,7.02),(21.4+4+0.2,9.36),(22.6+4+0.2,11.7),
)

LED_WYSS_POSITIONS_S_1 = (
(30.72+5.5,10.53),(27.72+5.5,11.7),(25.22+5.5,10.53),(24.22+5.5,8.5025),(25.22+5.5,6.475),(27.22+5.5,5.85),
(29.47+5.5,5.125),(30.72+5.5,2.925),(29.47+5.5,1.17),(27.22+5.5,0.00),(24.22+5.5,1.17),
)

LED_WYSS_POSITIONS_S_2 = (
(30.72+8.5+6.5,10.53),(27.72+8.5+6.5,11.7),(25.22+8.5+6.5,10.53),(24.22+8.5+6.5,8.5025),(25.22+8.5+6.5,6.475),(27.22+8.5+6.5,5.85),
(29.47+8.5+6.5,5.125),(30.72+8.5+6.5,2.925),(29.47+8.5+6.5,1.17),(27.22+8.5+6.5,0.00),(24.22+8.5+6.5,1.17),
)




LED_GRID_POSITIONS = [
[0.0,0.0],[0.0,2.41],[0.0,4.82],[0.0,7.23],[0.0,9.64],
[2.41,0.0],[2.41,2.41],[2.41,4.82],[2.41,7.23],[2.41,9.64],
[4.82,0.0],[4.82,2.41],[4.82,4.82],[4.82,7.23],[4.82,9.64],
[7.23,0.0],[7.23,2.41],[7.23,4.82],[7.23,7.23],[7.23,9.64],
[9.64,0.0],[9.64,2.41],[9.64,4.82],[9.64,7.23],[9.64,9.64],
]



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

        


    
def TPU_lapshear_tests(valve,nozzle,height,speed,dwell,pressure):
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
          g.meander(x=7,y=24.5,orientation='y',spacing=my_space[i],start='LL')
          g.set_valve(num = valve, value = 0)
          g.feed(40)
          g.clip(axis=nozzle,height=5, direction='+x')
          
def AgTPU_lapshear_tests(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    ######test line
    #g.abs_move(x=2,y=1.)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=50)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='+y')
    
    my_space = [0.5,0.5,0.5,0.5,0.5,0.5,0.5,0.5]
    my_xstarts = [3.0, 11.825, 20.65, 29.474999999999998, 38.3, 47.125, 55.949999999999996, 64.77499999999999]

    #####first wire
    
        
    for i in [6,7]:
          g.abs_move(x=my_xstarts[i],y=45)
          g.abs_move(**{nozzle:height}) 
          g.feed(speed)
          if valve is not None:
              g.set_valve(num = valve, value = 1)
          g.dwell(dwell)
          g.meander(x=7,y=17.5,orientation='y',spacing=my_space[i],start='UL')
          g.abs_move(**{nozzle:height+.2})
          g.move(y=4)
          g.meander(x=7,y=11,orientation='y',spacing=my_space[i], start='UR')
          g.set_valve(num = valve, value = 0)
          g.feed(40)
          g.clip(axis=nozzle,height=5, direction='+x')
                    

def TPU_spacing_tests(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    #######test line
    #g.abs_move(x=2,y=1.)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=50)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='+y')
    
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
    ############BOTTOM LAYER
#            
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
#          g.abs_move(**{nozzle:height+0.15}) 
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
##    
    
#    ############3rd LAYER
    #g.dwell(20)
    for i in [0,1,2,3,4,5,6,7]:
          g.abs_move(x=my_xstarts[i]+1+2.5,y=3+2+7)
          g.abs_move(**{nozzle:height+0.4}) 
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
    g.abs_move(**{nozzle:height-.1})
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
          g.abs_move(x=my_xstarts[i]+1,y=3+2+1)
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
        
    
    
def connectors_agtpu(valve,nozzle,height,speed,dwell,pressure,LorR,startx,starty):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)    
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
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')
    
    g.move(x=17.5)
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle,height=2, direction='+x')


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
    g.move(y=-2.7)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
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
    g.move(y=6.3)
    g.set_valve(num = valve, value = 0)
    g.move(y=0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=0.9)
    g.move(x=1.6)
    g.move(y=8)
    g.move(x=1.35)
    g.set_valve(num = valve, value = 0)
    g.move(x=0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(x=0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=1.2)
    g.set_valve(num = valve, value = 0)
    g.move(x=0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(x=0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=0.95)
    g.move(y=-8.5)
    g.move(x=1.8)
    g.move(y=-0.7)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
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
    g.move(y=-2.7)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=-3.0)
    g.set_valve(num = valve, value = 0)
    g.move(y=-0.9,**{nozzle:1.4})
    g.move(**{nozzle:2})
    g.move(**{nozzle:-2})
    g.move(y=-0.9,**{nozzle:-1.4})
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
        g.dwell(5) 
        g.feed(2)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='+y')
        g.move(y=-1.8)
        g.abs_move(**{nozzle:height})
        g.dwell(5) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y') 
        g.feed(25)
#        
    


#####second wire
    g.abs_move(startx, starty)
    
    for i in [0,1,2,3]:
        g.abs_move(x = LED_HARVARD_POSITIONS[1][i][0], y = LED_HARVARD_POSITIONS[1][i][1]) 
        if i==0:
            g.move(y=0.8)
            g.abs_move(**{nozzle:height})
            g.dwell(5) 
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(y=-1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(5) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-y')
            g.abs_move(**{nozzle:height+2}) 
            g.feed(25)
        elif  i==3:
            g.move(y=0.8)
            g.abs_move(**{nozzle:height})
            g.dwell(5) 
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(y=-1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(5) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-y') 
            g.feed(25)
            
            
        elif i==1 or i==2:
            g.move(x=-0.8)
            g.abs_move(**{nozzle:height}) 
            g.dwell(5)
            g.feed(2)
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+x')
            g.move(x=1.8)
            g.abs_move(**{nozzle:height})
            g.dwell(5) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-x') 
            g.feed(25)
#            
#
#
#######third wire
    g.abs_move(startx, starty)
    
    for i in [0,1,2,3]:
        g.abs_move(x = LED_HARVARD_POSITIONS[2][i][0], y = LED_HARVARD_POSITIONS[2][i][1]) 
        g.move(y=0.8)
        g.abs_move(**{nozzle:height}) 
        g.dwell(5)
        g.feed(2)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='+y')
        g.move(y=-1.8)
        g.abs_move(**{nozzle:height})
        g.dwell(5) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')
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
          



def pickandplace_HARVARD(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    #if wire == 'first':

    ##LED 1
    g.abs_move(x = 18.9, y = 64.365)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][0][0], y = LED_HARVARD_POSITIONS[0][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.7})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
#
    ##LED 2
    g.abs_move(x = 18.90, y = 64.365-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][1][0], y = LED_HARVARD_POSITIONS[0][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    #LED 3
    g.abs_move(x = 18.90, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][2][0], y = LED_HARVARD_POSITIONS[0][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 4
    g.abs_move(x = 18.90+3, y = 64.365)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[0][3][0], y = LED_HARVARD_POSITIONS[0][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    

    
#elif wire == 'second':
    
    ##LED 5
    g.abs_move(x = 18.90+3+3+3, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][0][0], y = LED_HARVARD_POSITIONS[1][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    ##LED 6
    g.abs_move(x = 18.90-3-3, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][1][0], y = LED_HARVARD_POSITIONS[1][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 7
    g.abs_move(x = 18.90-3, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][2][0], y = LED_HARVARD_POSITIONS[1][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    
    ##LED 8
    g.abs_move(x = 18.90+3, y = 64.365-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[1][3][0], y = LED_HARVARD_POSITIONS[1][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
#

#else:
    
    ##LED 9
    g.abs_move(x = 18.90+3, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][0][0], y = LED_HARVARD_POSITIONS[2][0][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    ##LED 10
    g.abs_move(x = 18.90+3+3, y = 64.365)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][1][0], y = LED_HARVARD_POSITIONS[2][1][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

    
    ##LED 11
    g.abs_move(x = 18.90+3+3, y = 64.365-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][2][0], y = LED_HARVARD_POSITIONS[2][2][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})
    
    ##LED 12
    g.abs_move(x = 18.90+3, y = 64.365-3-3)
    g.feed(10) 
    g.abs_move(**{nozzle:2.4+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.4})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = LED_HARVARD_POSITIONS[2][3][0], y = LED_HARVARD_POSITIONS[2][3][1]) 
    g.abs_move(**{nozzle:0.7+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:0.65})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:9})

def pickandplace_WYSS(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)


    x_zero = 7.58+5+2          ####position (relative to 0,0 of slide) of bottom left corner of design
    y_zero = 15.4+3


    g.abs_move(x=x_zero,y=y_zero)  
    g.set_home(x=0,y=0)
    #g.abs_move(**{nozzle:1})
    #g.rect(x=44.47,y=11.7,start='LL')
    #g.abs_move(**{nozzle:15})

    for i in range(len(LED_STOCK_POSITIONS_TOP)):
        LED_STOCK_POSITIONS_TOP[i][0]=LED_STOCK_POSITIONS_TOP[i][0]-x_zero+0.063
        LED_STOCK_POSITIONS_TOP[i][1]=LED_STOCK_POSITIONS_TOP[i][1]-y_zero+.15-0.07
    
    for i in range(len(LED_STOCK_POSITIONS_SIDE)):
        LED_STOCK_POSITIONS_SIDE[i][0]=LED_STOCK_POSITIONS_SIDE[i][0]-x_zero+0.05
        LED_STOCK_POSITIONS_SIDE[i][1]=LED_STOCK_POSITIONS_SIDE[i][1]-y_zero-0.05

    ###z=2.169


    ## W ###
    
    for i in range(len(LED_WYSS_POSITIONS_W)):
    #for i in [20]:
         g.feed(25)
         g.abs_move(x=LED_STOCK_POSITIONS_TOP[i][0],y=LED_STOCK_POSITIONS_TOP[i][1])
         g.feed(25) 
         g.abs_move(**{nozzle:1.95+1})
         g.feed(0.4)
         g.abs_move(**{nozzle:1.95})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.move(**{nozzle:5})
         g.feed(20)
         g.abs_move(x=LED_WYSS_POSITIONS_W[i][0],y=LED_WYSS_POSITIONS_W[i][1])
         g.feed(25)
         #g.move(x=-0.3)
         #g.arc(x=0.6,y=0,direction='CW')
         #g.arc(x=-0.6,y=0,direction='CW')
         #g.move(x=0.3)
         g.abs_move(**{nozzle:0.54+1})
         g.feed(0.4) 
         g.abs_move(**{nozzle:0.54})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.abs_move(**{nozzle:3})
         g.feed(25)
         g.abs_move(**{nozzle:6})
    
    for i in range(len(LED_WYSS_POSITIONS_Y)):
    #for i in [2, 3, 4, 5, 6, 7, 8]:
        
         g.feed(25)
         g.abs_move(x=LED_STOCK_POSITIONS_TOP[i+21][0],y=LED_STOCK_POSITIONS_TOP[i+21][1])
         g.feed(20) 
         g.abs_move(**{nozzle:1.95+1})
         g.feed(0.4)
         g.abs_move(**{nozzle:1.95})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.move(**{nozzle:5})
         g.feed(25)
         g.abs_move(x=LED_WYSS_POSITIONS_Y[i][0],y=LED_WYSS_POSITIONS_Y[i][1])
         g.feed(20)
         #g.move(x=-0.3)
         #g.arc(x=0.6,y=0,direction='CW')
         #g.arc(x=-0.6,y=0,direction='CW')
         #g.move(x=0.3)
         g.abs_move(**{nozzle:0.54+1})
         g.feed(0.4) 
         g.abs_move(**{nozzle:0.54})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.abs_move(**{nozzle:3})
         g.feed(25)
         g.abs_move(**{nozzle:6})
    #    

    for i in range(len(LED_WYSS_POSITIONS_S_1)):
         g.feed(25)
         g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i][0],y=LED_STOCK_POSITIONS_SIDE[i][1])
         g.feed(20) 
         g.abs_move(**{nozzle:1.916+1})
         g.feed(0.4)
         g.abs_move(**{nozzle:1.916})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.move(**{nozzle:5})
         g.feed(25)
         g.abs_move(x=LED_WYSS_POSITIONS_S_1[i][0],y=LED_WYSS_POSITIONS_S_1[i][1])
         g.feed(20)
         #g.move(x=-0.3)
         #g.arc(x=0.6,y=0,direction='CW')
         #g.arc(x=-0.6,y=0,direction='CW')
         #g.move(x=0.3)
         g.abs_move(**{nozzle:0.54+1})
         g.feed(0.4) 
         g.abs_move(**{nozzle:0.54})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.abs_move(**{nozzle:3})
         g.feed(20)
         g.abs_move(**{nozzle:6})

    for i in range(len(LED_WYSS_POSITIONS_S_2)):
         g.feed(25)
         g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i+11][0],y=LED_STOCK_POSITIONS_SIDE[i+11][1])
         g.feed(20) 
         g.abs_move(**{nozzle:1.916+1})
         g.feed(0.4)
         g.abs_move(**{nozzle:1.916})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.move(**{nozzle:5})
         g.feed(25)
         g.abs_move(x=LED_WYSS_POSITIONS_S_2[i][0],y=LED_WYSS_POSITIONS_S_2[i][1])
         g.feed(20)
         #g.move(x=-0.3)
         #g.arc(x=0.6,y=0,direction='CW')
         #g.arc(x=-0.6,y=0,direction='CW')
         #g.move(x=0.3)
         g.abs_move(**{nozzle:0.54+1})
         g.feed(0.4) 
         g.abs_move(**{nozzle:0.54})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.abs_move(**{nozzle:3})
         g.feed(20)
         g.abs_move(**{nozzle:6})

def pickandplace_GRID(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    x_zero = 7.58+5+2          ####position (relative to 0,0 of slide) of bottom left corner of design
    y_zero = 15.4+3


    g.abs_move(x=x_zero,y=y_zero)  
    g.set_home(x=0,y=0)
    #g.abs_move(**{nozzle:1})
    #g.rect(x=44.47,y=11.7,start='LL')
    #g.abs_move(**{nozzle:15})

    for i in range(len(LED_STOCK_POSITIONS_TOP)):
        LED_STOCK_POSITIONS_TOP[i][0]=LED_STOCK_POSITIONS_TOP[i][0]-x_zero+0.063
        LED_STOCK_POSITIONS_TOP[i][1]=LED_STOCK_POSITIONS_TOP[i][1]-y_zero+.15-0.07
    
    for i in range(len(LED_STOCK_POSITIONS_SIDE)):
        LED_STOCK_POSITIONS_SIDE[i][0]=LED_STOCK_POSITIONS_SIDE[i][0]-x_zero+0.05
        LED_STOCK_POSITIONS_SIDE[i][1]=LED_STOCK_POSITIONS_SIDE[i][1]-y_zero-0.05

    ###z=2.169

#    x_offset = 8.5
#    y_offset = 0.523
#
#
#    for i in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
#        LED_GRID_POSITIONS[i][0]=LED_GRID_POSITIONS[i][0]+x_offset
#        LED_GRID_POSITIONS[i][1]=LED_GRID_POSITIONS[i][1]+y_offset


    x_offset = 30.91
    y_offset = 0.647


    for i in range(len(LED_GRID_POSITIONS)):
        LED_GRID_POSITIONS[i][0]=LED_GRID_POSITIONS[i][0]+x_offset
        LED_GRID_POSITIONS[i][1]=LED_GRID_POSITIONS[i][1]+y_offset


#x interval 2.41

    ## W ###
    
    #for i in [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
    for i in range(len(LED_GRID_POSITIONS)):
         g.feed(25)
         g.abs_move(x=LED_STOCK_POSITIONS_TOP[i][0],y=LED_STOCK_POSITIONS_TOP[i][1])
         g.feed(25) 
         g.abs_move(**{nozzle:1.95+1})
         g.feed(0.4)
         g.abs_move(**{nozzle:1.95})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.move(**{nozzle:5})
         g.feed(20)
         g.abs_move(x=LED_GRID_POSITIONS[i][0],y=LED_GRID_POSITIONS[i][1])
         g.feed(25)
         #g.move(x=-0.3)
         #g.arc(x=0.6,y=0,direction='CW')
         #g.arc(x=-0.6,y=0,direction='CW')
         #g.move(x=0.3)
         g.abs_move(**{nozzle:0.61+1})
         g.feed(0.4) 
         g.abs_move(**{nozzle:0.61})
         g.toggle_pressure(pressure_box)
         g.dwell(dwell)
         g.feed(1)
         g.abs_move(**{nozzle:3})
         g.feed(25)
         g.abs_move(**{nozzle:6})
    
def pdms_pillars(valve,nozzle,height,speed,dwell,pressure,layers):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    ########test line
    #g.abs_move(x=1+2,y=1)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=20)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='-x')
   ##
   # 
    layerheight = 0.35
    thickness = 2
    length = 8
    pillar_height = 15.
    layers = pillar_height/layerheight/2
    ramp_length = 5
    ramp_angle = np.tan(ramp_length/pillar_height)

    g.abs_move(x=14.31,y=6.72)
    g.set_home(x=0,y=0)
    layers=np.zeros(layers)

    for i in [0]:
        for j in [0,1,2,3]:
            g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
            g.move(x=-length/2,y=-5-thickness)
            g.abs_move(**{nozzle:height}) 
            g.feed(speed)
            if valve is not None:
                    g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            for k in range(len(layers)):
                current_height = k*layerheight*2
                extra_ramp = (pillar_height-current_height)*np.tan(ramp_angle)
                print k
                print extra_ramp
                g.meander(x=length+extra_ramp,y=thickness,orientation='x',spacing=0.5,start='LL')
                g.move(**{nozzle:layerheight})
                g.meander(x=length+extra_ramp,y=thickness,orientation='x',spacing=0.5,start='UR')
                g.move(**{nozzle:layerheight})
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            #

            g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
            g.move(x=-length/2,y=5)
            g.abs_move(**{nozzle:height}) 
            g.feed(speed)
            if valve is not None:
                    g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            for k in range(len(layers)):
                current_height = k*layerheight*2
                extra_ramp = (pillar_height-current_height)*np.tan(ramp_angle)
                print k
                print extra_ramp
                g.meander(x=length+extra_ramp,y=thickness,orientation='x',spacing=0.5,start='LL')
                g.move(**{nozzle:layerheight})
                g.meander(x=length+extra_ramp,y=thickness,orientation='x',spacing=0.5,start='UR')
                g.move(**{nozzle:layerheight})
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')            

        


def agtpu_pillars(valve,nozzle,height,speed,dwell,pressure,layers):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #########test line
    #g.abs_move(x=1+2,y=1)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(y=20)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=6, direction='-x')
    #g.abs_move(**{nozzle:25})
    #
    layerheight = 0.35
    thickness = 2
    length = 8
    pillar_height = 15.
    layers = pillar_height/layerheight/2
    ramp_length = 5
    ramp_angle = np.tan(ramp_length/pillar_height)

    g.abs_move(x=14.31,y=6.72)
    g.set_home(x=0,y=0)
    layers=np.zeros(layers)


    for i in [0]:
        for j in [0,1,2,3]:
            g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
            g.move(x=(length/2+ramp_length)+1,y=-5-thickness/2)
            g.abs_move(C=-38.989,**{nozzle:height+1}) 
            g.feed(speed)
            if valve is not None:
                    g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.move(x=-ramp_length-0.5,C=pillar_height,**{nozzle:pillar_height-0.5})
            g.feed(speed*1.5)
            g.move(x=-1)
            g.move(y=-0.4)
            g.move(x=-length+1)
            g.move(y=0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=-0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=-0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=-0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=0.8)
            g.move(x=length-1)
            g.move(**{nozzle:height*0.5})
            g.move(x=-length+1)
            g.move(y=-0.8)
            g.move(x=length-1)

            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')


#
#            g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
#            g.move(x=(length/2+ramp_length)+1,y=5+thickness/2)
#            g.abs_move(C=-38.989,**{nozzle:height+1}) 
#            g.feed(speed)
#            if valve is not None:
#                    g.set_valve(num = valve, value = 1)
#            g.dwell(dwell)
#            g.move(x=-ramp_length-0.5,C=pillar_height,**{nozzle:pillar_height-1.0})
#            g.feed(speed*1.5)
#            g.move(x=-1)
#            g.move(y=-0.4)
#            g.move(x=-length+1)
#            g.move(y=0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=-0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=-0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=-0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=0.8)
#            g.move(x=length-1)
#            g.move(**{nozzle:height*0.5})
#            g.move(x=-length+1)
#            g.move(y=-0.8)
#            g.move(x=length-1)
#            g.set_valve(num = valve, value = 0)
#            g.clip(axis=nozzle, height=2, direction='+y')
        
    #for i in [0]:
    #    for j in [0,1,2,3]:
    #        g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
    #        g.move(x=(length/2+ramp_length)+1,y=-5-thickness/2)
    #        g.abs_move(C=-38.989,**{nozzle:height}) 
    #        g.feed(speed)
    #        if valve is not None:
    #                g.set_valve(num = valve, value = 1)
    #        g.dwell(dwell)
    #        g.move(y=-4)
    #        g.set_valve(num = valve, value = 0)
    #        g.feed(20)
    #        g.clip(axis=nozzle, height=2, direction='+x')
    #        g.move(C=22,**{nozzle:20}) 

        #    g.abs_move(x=pdms_pillar_lid_locations[i][j][0],y=pdms_pillar_lid_locations[i][j][1])
        #    g.move(x=(length/2+ramp_length)+1,y=5+thickness/2)
        #    g.abs_move(C=-38.989,**{nozzle:height}) 
        #    g.feed(speed)
        #    if valve is not None:
        #            g.set_valve(num = valve, value = 1)
        #    g.dwell(dwell)
        #    g.move(y=4)
        #    g.set_valve(num = valve, value = 0)
        #    g.feed(20)
        #    g.clip(axis=nozzle, height=2, direction='+x')
        #    g.move(C=22,**{nozzle:20}) 
        #
    #g.abs_move(x=pdms_pillar_lid_locations[0][3][0],y=pdms_pillar_lid_locations[0][3][1])
    #g.move(x=(length/2+ramp_length)+1,y=5+thickness/2)
    #g.move(y=4)
    #g.abs_move(C=-38.989,**{nozzle:height}) 
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.abs_move(x=pdms_pillar_lid_locations[2][0][0]-17)
    #g.abs_move(y=pdms_pillar_lid_locations[1][0][1]+13)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=2, direction='+x')
    #g.move(C=22,**{nozzle:20}) 

#    g.abs_move(x=pdms_pillar_lid_locations[0][3][0],y=pdms_pillar_lid_locations[0][3][1])
#    g.move(x=(length/2+ramp_length)+1,y=-5-thickness/2)
#    g.move(y=-4)
#    g.abs_move(C=-38.989,**{nozzle:height}) 
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)
#    g.abs_move(x=pdms_pillar_lid_locations[2][0][0]-15)
#    g.abs_move(y=pdms_pillar_lid_locations[2][0][1]+13)
#    g.set_valve(num = valve, value = 0)
#    g.feed(20)
#    g.clip(axis=nozzle, height=2, direction='+x')
#    g.move(C=22,**{nozzle:20}) 
#

def pickandplace_magnets(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    ##magnet 1  (bottom left)
    g.abs_move(x = -22.466, y = -1.182)
    g.feed(10) 
    g.abs_move(**{nozzle:2.+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = 8.00, y = 5.00) 
    g.abs_move(**{nozzle:1+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:1})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.abs_move(**{nozzle:3})
    g.feed(10)
    g.abs_move(**{nozzle:20})

    ##magnet 2  (top right)
    g.abs_move(x = 53.568, y = 70.82)
    g.feed(10) 
    g.abs_move(**{nozzle:2.+1})
    g.feed(0.08)
    g.abs_move(**{nozzle:2.})
    #g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.feed(1)
    g.move(**{nozzle:5})
    g.feed(10)
    g.abs_move(x = 25.4, y = 5.00) 
    g.abs_move(**{nozzle:1+1})
    g.feed(0.08) 
    g.abs_move(**{nozzle:1})
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



def bacteria_electrodes(valve,nozzle,height,speed,dwell,pressure,spacing):#
    g.feed(25)
    g.set_pressure(pressure_box, pressure)

    
    
    
    g.abs_move(x=25,y=15)
    g.set_home(x=0, y=0)
    #g.abs_move(C=-35.09,**{nozzle:height+0.05}) 
    #g.rect(x=21,y=21,start='LL')
    
    ####OUTLINE OF SLIDE FOR ALIGNING PURPOSES
    #g.abs_move(x=-25,y=-15)
    #g.move(x=72.4)
    #g.move(y=50.8)
    #g.move(x=-72.4)
    #g.move(y=-50.8)
    #####OUTLINE OF SLIDE FOR ALIGNING PURPOSES
    
    
##########test line
#    g.abs_move(x=-2.25,y=2)
#    pressure_purge(delay = 2)
#    g.abs_move(C=-34.4,**{nozzle:height})
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)
#    g.feed(speed)
#    g.move(y=20)
#    g.feed(20)
#    g.set_valve(num = valve, value = 0)
#    g.clip(axis=nozzle, height=2, direction='-x')
#    g.set_pressure(pressure_box, pressure)
#
    g.abs_move(x=0,y=0)
    g.move(x=2)   #starts first electrode farther up to avoid short circuit
    #g.move(x=14.4)
    #Print start
    g.dwell(0.1)
    if spacing=='400':    
#        top_electrode_connection=20.4
#        bottom_electrode_connection=0
#        for i in range(25):
#            g.abs_move(C=-34.4,**{nozzle:height}) 
#            g.feed(speed)
#            if valve is not None:
#                g.set_valve(num = valve, value = 1)
#            #g.dwell(dwell)
#            g.abs_move(x=top_electrode_connection)
#            g.set_valve(num = valve, value = 0)
#            g.clip(axis=nozzle, height=0.8, direction='+x')
#            g.move(x=2)
#            g.move(x=-4)
#            g.move(x=2)
#            g.move(y=0.4,x=-0.4)
#            g.abs_move(C=-34.4,**{nozzle:height})
#            if valve is not None:
#                g.set_valve(num = valve, value = 1)
#            #g.dwell(dwell)
#            g.abs_move(x=bottom_electrode_connection)
#            g.set_valve(num = valve, value = 0)
#            g.clip(axis=nozzle, height=0.8, direction='-x')
#            g.move(x=-2)
#            g.move(x=4)
#            g.move(x=-2)
#            if i<24:
#                g.move(y=0.4,x=0.4)
#        #
#
#        g.abs_move(x=0,y=0)
#        #g.abs_move(**{nozzle:10}) 
#        g.dwell(1)
#        g.abs_move(C=-34.4,**{nozzle:height}) 
#        if valve is not None:
#            g.set_valve(num = valve, value = 1)
#        g.dwell(dwell)
#        g.feed(speed*0.4)
#        g.abs_move(y=19.8,x=0)
#        g.move(x=3,y=3)
#        g.abs_move(**{nozzle:height+0.05})
#        g.set_pressure(pressure_box, pressure+3)
#        g.feed(speed*0.4)
#        g.arc(x=0,y=1.4,radius=0.7)
#        g.arc(x=0,y=-1.4,radius=0.7)
#        g.move(y=0.2)
#        g.arc(x=0,y=1.,radius=0.5)
#        g.arc(x=0,y=-1.,radius=0.5)
#        g.move(y=0.2)
#        g.arc(x=0,y=0.6,radius=0.3)
#        g.arc(x=0,y=-0.6,radius=0.3)
#        g.feed(10)
#        g.set_valve(num = valve, value = 0)
#        g.clip(axis=nozzle, height=1, direction='+y')

        g.feed(15)
        g.set_pressure(pressure_box, pressure)
        g.abs_move(y=0,x=20.4)
        g.dwell(1)
        g.abs_move(C=-34.4,**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.feed(speed*0.4)
        g.abs_move(y=19.8)
        g.move(x=-3,y=3)
        g.abs_move(**{nozzle:height+0.05})
        g.set_pressure(pressure_box, pressure+3)
        g.feed(speed*0.4)
        g.arc(x=0,y=1.4,radius=0.7)
        g.arc(x=0,y=-1.4,radius=0.7)
        g.move(y=0.2)
        g.arc(x=0,y=1.,radius=0.5)
        g.arc(x=0,y=-1.,radius=0.5)
        g.move(y=0.2)
        g.arc(x=0,y=0.6,radius=0.3)
        g.arc(x=0,y=-0.6,radius=0.3)
        g.set_valve(num = valve, value = 0)
        g.feed(10)
        g.clip(axis=nozzle, height=1, direction='+y')
        #
    elif spacing=='200':
        top_electrode_connection=20.4
        bottom_electrode_connection=0
        for i in range(50):
            g.abs_move(**{nozzle:height}) 
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=top_electrode_connection)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='+y')
            g.move(x=0.2,y=-0.4)
            g.abs_move(**{nozzle:height})
            if valve is not None:
                g.set_valve(num = valve, value = 1)
            g.dwell(dwell)
            g.abs_move(y=bottom_electrode_connection)
            if i<49:
                g.move(x=0.2,y=0.4)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, height=2, direction='-y')        
        g.abs_move(x=0,y=0)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.feed(speed*0.4)
        g.abs_move(x=22.4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')

        g.feed(speed)
        g.abs_move(x=0,y=20.4)
        g.abs_move(**{nozzle:height}) 
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell*0.4)
        g.feed(speed)
        g.abs_move(x=22.4)
        g.feed(speed*0.2)
        g.arc(x=1.,y=0,radius=0.5)
        g.arc(x=-1.,y=0,radius=0.5)
        g.move(x=0.2)
        g.arc(x=0.6,y=0,radius=0.3)
        g.arc(x=-0.6,y=0,radius=0.3)
        g.move(x=0.2)
        g.arc(x=0.2,y=0,radius=0.1)
        g.arc(x=-0.2,y=0,radius=0.1)
        g.set_valve(num = valve, value = 0)
        g.clip(axis=nozzle, height=2, direction='-y')
    














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
z_ref = -71.244

####
#active_slide = 'slide2'
#z_ref = -79.54625
###
#####
#active_slide = 'slide3'
#z_ref = -79.12

automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")

#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
g.write("POSOFFSET CLEAR X Y U A B C D")

  

#substrate_dif = 0
substrate_dif = automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref
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
####------------SOFT TPU BOTTOM
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
##tpu_Harvard_bottom(valve='2',nozzle='B',height=0.5,speed=8.4,dwell=0.2,pressure=6)
#
#
##tpu_bottom_LED_strain(valve='2',nozzle='B',height=0.5,speed=13,dwell=0.2,pressure=10)
#TPU_spacing_tests(valve='1',nozzle='A',height=0.4,speed=10.5,dwell=0.2,pressure=6)
##TPU_lapshear_tests(valve='1',nozzle='A',height=0.4,speed=10.5,dwell=0.2,pressure=6)
##
#g.toggle_pressure(pressure_box)



########------------ STIFF TPU LAYER
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
##
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ac')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##LED_Harvard(valve='1',nozzle='A',height=0.16+0.06+0.06+0.06,speed=7,dwell=0.1,pressure=45,LorR='R',startx=8,starty=7)
#stiffTPU_strain_speciman(valve='1',nozzle='A',height=0.26+0.6,speed=3,dwell=0.4,pressure=10)
#
#g.toggle_pressure(pressure_box)


###########------------SOFT AGTPU WIRING
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
##LED_Harvard_agtpu(valve='3',nozzle='C',height=1.0,speed=4,dwell=0.1,pressure=18,LorR='L',startx=5+3,starty=5)
##LED_Harvard_agtpu(valve='1',nozzle='A',height=.25+0.12+.08+.08,speed=8,dwell=0.3,pressure=13,LorR='L',startx=5+3,starty=5)
##connectors_agtpu(valve='1',nozzle='A',height=.25+0.12+.2,speed=8,dwell=4,pressure=13,LorR='L',startx=5+3,starty=5)
#
##LED_strain(valve='1',nozzle='A',height=0.08+.72+.12,speed=2,dwell=0.1,pressure=10)
#
#AgTPU_strain_speciman(valve='2',nozzle='B',height=0.32+0.12,speed=4,dwell=0.1,pressure=18) #soft
##AgTPU_strain_speciman(valve='2',nozzle='B',height=0.185+0.12,speed=4,dwell=0.1,pressure=13) #stiff
##AgTPU_lapshear_tests(valve='2',nozzle='B',height=0.08+0.2,speed=2,dwell=0.2,pressure=20)
#
#g.toggle_pressure(pressure_box)
####
####
#####
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



#
#############------------PICK+PLACE HARVARD
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
##pickandplace_HARVARD(valve='3',nozzle='C',speed=10,dwell=10)
#pickandplace_magnets(valve='3',nozzle='z',speed=10,dwell=10)
#g.set_vac(pressure_box,0)
##


############------------PICK+PLACE WYSS
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ac')
g.set_home(x=0, y=0)


startx=8
starty=5
#
for i in range(len(LED_HARVARD_POSITIONS)):
        for j in range(len(LED_HARVARD_POSITIONS[i])):
            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty

#g.dwell(60)

valve='3'
g.set_pressure(pressure_box, 0.2)
if valve is not None:
    g.set_valve(num = valve, value = 1)
g.set_vac(pressure_box,18)
g.dwell(2)
g.toggle_pressure(pressure_box)
#pickandplace_WYSS(valve='3',nozzle='C',speed=10,dwell=4)
pickandplace_GRID(valve='3',nozzle='C',speed=10,dwell=4)
g.set_vac(pressure_box,0)
#



###########------------STIFF AGTPU CONNECTORS 
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
###
#
#startx=8
#starty=5
##
#for i in range(len(LED_HARVARD_POSITIONS)):
#        for j in range(len(LED_HARVARD_POSITIONS[i])):
#            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
#            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty
#
#
#g.toggle_pressure(pressure_box)
#LED_Harvard_connectors(valve='1',nozzle='A',height=0.6+.2,speed=2,dwell=1,pressure=50,startx=8,starty=5)
#g.toggle_pressure(pressure_box)
####
####
#


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

##
#########------------------PRINT ME PDMS PILLARS
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
#pdms_pillars(valve='1',nozzle='A',height=0.6,speed=10,dwell=0.8,pressure=26,layers=30)
##pdms_pillars(valve='1',nozzle='A',height=0.3,speed=10,dwell=0.5,pressure=28,layers=30)
#
#
#g.toggle_pressure(pressure_box)

 

##########------------------PRINT ME AGTPU PILLAR SENSORS
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
##agtpu_pillars(valve='2',nozzle='B',height=0.2,speed=2,dwell=0.2,pressure=23,layers=30)
#agtpu_pillars(valve='2',nozzle='B',height=0.6,speed=5,dwell=1,pressure=10,layers=30)
#g.toggle_pressure(pressure_box)


##------------------PRINT ME BACTERIA ELECTRODES
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=-24, y=-4)
#
#g.toggle_pressure(pressure_box)
#bacteria_electrodes(valve='1',nozzle='A',height=0.06,speed=6.5,dwell=0.1,pressure=4,spacing='400')
#
#g.toggle_pressure(pressure_box)
#


g.view(backend='matplotlib')

##
g.teardown()
