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


pdms_pillar_lid_locations = (                                  #(0,0) is center of bottom left well (C4), order proceed L to R across rows, down colums (A4-A3-A2-A1-B4-B3, etc)

((0.0,52.0),(26.0,52.0),(52.0,52.0),(78.0,52.0)),
((0.0,26.0),(26.0,26.0),(52.0,26.0),(78.0,26.0)),
((0.0,0.0),(26.0,0.0),(52.0,0.0),(78.0,0.0)),

)
###these coordinats are relative to the starting location of the VCC terminal, which changes print to print

LED_HARVARD_POSITIONS = [
[5,29.6],[5,24.8],[5,20],[5,15.2],[5,10],[8.65,20],[11.65,20],[15.5,10.1],[15.4,29.6],[15.4,24.8],[15.4,20],[15.4,15.2]
]

#### stock positions are absolute coordinates relative to 0,0 of the slide, after nozzle switches to 'C'
#### linear list of LED positions starting at bottom left corner, across the row in (+) x direction, then restart to original x and up one row in (+) y direction, acorss the row again in the (+) direction, etc 

LED_STOCK_POSITIONS_TOP = [

[18.371,58.66],[21.371,58.66],[24.371,58.66],[27.371,58.66],[30.371,58.66],[33.371,58.66],[36.371,58.66],[39.371,58.66],[42.371,58.66],[45.371,58.66],
[18.371,61.66],[21.371,61.66],[24.371,61.66],[27.371,61.66],[30.371,61.66],[33.371,61.66],[36.371,61.66],[39.371,61.66],[42.371,61.66],[45.371,61.66],
[18.371,64.66],[21.371,64.66],[24.371,64.66],[27.371,64.66],[30.371,64.66],[33.371,64.66],[36.371,64.66],[39.371,64.66],[42.371,64.66],[45.371,64.66],
[53.6,63.76]
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
(30.72+5.,10.53),(27.72+5.5,11.7),(25.22+5.5,10.53),(24.22+5.75,8.5025),(25.22+5.5,6.475+0.2),(27.72+5.5,5.85),
(29.47+5.5,5.125-.2),(30.72+5.,2.925),(29.47+5.5,1.17),(27.22+5.5,0.00),(24.22+6.0,1.17),
)

LED_WYSS_POSITIONS_S_2 = (
(30.72+8.+6.5,10.53),(27.72+8.5+6.5,11.7),(25.22+8.5+6.5,10.53),(24.22+8.5+6.75,8.5025),(25.22+8.5+6.5,6.475+.2),(27.72+8.5+6.5,5.85),
(29.47+8.5+6.5,5.125-.2),(30.72+8.5+6.,2.925),(29.47+8.5+6.5,1.17),(27.22+8.5+6.5,0.00),(24.22+8.5+7.0,1.17),
)




LED_GRID_POSITIONS = [
[0.0,0.0],[0.0,2.41],[0.0,4.82],[0.0,7.23],[0.0,9.64],
[2.41,0.0],[2.41,2.41],[2.41,4.82],[2.41,7.23],[2.41,9.64],
[4.82,0.0],[4.82,2.41],[4.82,4.82],[4.82,7.23],[4.82,9.64],
[7.23,0.0],[7.23,2.41],[7.23,4.82],[7.23,7.23],[7.23,9.64],
[9.64,0.0],[9.64,2.41],[9.64,4.82],[9.64,7.23],[9.64,9.64],
]





arduino_gen2_LED_POSITIONS = [
[2.0,-3.0],[4.0,-3.0],[6.0,-3.0],[8.0,-3.0],[10.0,-3.0],
]

arduino_gen2_LED_RES_POSITIONS = [
[2.0,-5.1],[4.0,-5.1],[6.0,-5.1],[8.0,-5.1],[10.0,-5.1],
]

arduino_gen2_RESET_RES_POSITION = [4.1,11.2]

arduino_gen2_SENSOR_RES_POSITION = [11.0,4.9]

arduino_gen2_CAPS_POSITION=[[-2.8,-1],[-2.8,4.1]]

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




def pickandplace_arduino_gen2(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    g.abs_move(x=30,y=20)
    g.set_home(x=0,y=0)


    for i in range(len(LED_STOCK_POSITIONS_TOP)):
        LED_STOCK_POSITIONS_TOP[i][0]=LED_STOCK_POSITIONS_TOP[i][0]-30+0.7
        LED_STOCK_POSITIONS_TOP[i][1]=LED_STOCK_POSITIONS_TOP[i][1]-20+2.1
    
    for i in range(len(LED_STOCK_POSITIONS_SIDE)):
        LED_STOCK_POSITIONS_SIDE[i][0]=LED_STOCK_POSITIONS_SIDE[i][0]-30+0.7
        LED_STOCK_POSITIONS_SIDE[i][1]=LED_STOCK_POSITIONS_SIDE[i][1]-20+2.2


#
#
#    #### LEDs
#    for i in [0,1,2,3,4]:
#        g.feed(25)
#        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i][0],y=LED_STOCK_POSITIONS_TOP[i][1])
#        g.feed(25) 
#        g.abs_move(**{nozzle:1.97+1})
#        g.feed(0.4)
#        g.abs_move(**{nozzle:1.97})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.move(**{nozzle:5})
#        g.feed(20)
#        g.abs_move(x=arduino_gen2_LED_POSITIONS[i][0],y=arduino_gen2_LED_POSITIONS[i][1]) 
#        g.feed(25)
#        #g.move(x=-0.3)
#        #g.arc(x=0.6,y=0,direction='CW')
#        #g.arc(x=-0.6,y=0,direction='CW')
#        #g.move(x=0.3)
#        g.abs_move(**{nozzle:0.55+1})
#        g.feed(0.4) 
#        g.abs_move(**{nozzle:0.55})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.abs_move(**{nozzle:3})
#        g.feed(25)
##        g.abs_move(**{nozzle:6})    
#
#    ### LED RESISTORS (1kOhm)
#    for i in [0,1,2,3,4]:
#        g.feed(25)
#        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i+10][0],y=LED_STOCK_POSITIONS_TOP[i+10][1])
#        g.feed(25) 
#        g.abs_move(**{nozzle:1.97+1})
#        g.feed(0.4)
#        g.abs_move(**{nozzle:1.97})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.move(**{nozzle:5})
#        g.feed(20)
#        g.abs_move(x=arduino_gen2_LED_RES_POSITIONS[i][0],y=arduino_gen2_LED_RES_POSITIONS[i][1]) 
#        g.feed(25)
#        #g.move(x=-0.3)
#        #g.arc(x=0.6,y=0,direction='CW')
#        #g.arc(x=-0.6,y=0,direction='CW')
#        #g.move(x=0.3)
#        g.abs_move(**{nozzle:0.55+1})
#        g.feed(0.4) 
#        g.abs_move(**{nozzle:0.55})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.abs_move(**{nozzle:3})
#        g.feed(25)
#        g.abs_move(**{nozzle:6})    
#
#
#    ###RESET RES (22kOhm)
#    for i in [0]:
#        g.feed(25)
#        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i+20][0],y=LED_STOCK_POSITIONS_TOP[i+20][1])
#        g.feed(25) 
#        g.abs_move(**{nozzle:1.97+1})
#        g.feed(0.4)
#        g.abs_move(**{nozzle:1.97})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.move(**{nozzle:5})
#        g.feed(20)
#        g.abs_move(x=arduino_gen2_RESET_RES_POSITION[0],y=arduino_gen2_RESET_RES_POSITION[1]) 
#        g.feed(25)
#        #g.move(x=-0.3)
#        #g.arc(x=0.6,y=0,direction='CW')
#        #g.arc(x=-0.6,y=0,direction='CW')
#        #g.move(x=0.3)
#        g.abs_move(**{nozzle:0.55+1})
#        g.feed(0.4) 
#        g.abs_move(**{nozzle:0.55})
#        g.toggle_pressure(pressure_box)
#        g.dwell(dwell)
#        g.feed(1)
#        g.abs_move(**{nozzle:3})
#        g.feed(25)
#        g.abs_move(**{nozzle:6})    
    
    #
    ####SENSOR RES (100Ohm)
    #for i in [0]:
    #    g.feed(25)
    #    g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i][0],y=LED_STOCK_POSITIONS_SIDE[i][1])
    #    g.feed(25) 
    #    g.abs_move(**{nozzle:1.97+1})
    #    g.feed(0.4)
    #    g.abs_move(**{nozzle:1.97})
    #    g.toggle_pressure(pressure_box)
    #    g.dwell(dwell)
    #    g.feed(1)
    #    g.move(**{nozzle:5})
    #    g.feed(20)
    #    g.abs_move(x=arduino_gen2_SENSOR_RES_POSITION[0],y=arduino_gen2_SENSOR_RES_POSITION[1]) 
    #    g.feed(25)
    #    #g.move(x=-0.3)
    #    #g.arc(x=0.6,y=0,direction='CW')
    #    #g.arc(x=-0.6,y=0,direction='CW')
    #    #g.move(x=0.3)
    #    g.abs_move(**{nozzle:0.55+1})
    #    g.feed(0.4) 
    #    g.abs_move(**{nozzle:0.55})
    #    g.toggle_pressure(pressure_box)
    #    g.dwell(dwell)
    #    g.feed(1)
    #    g.abs_move(**{nozzle:3})
    #    g.feed(25)
    #    g.abs_move(**{nozzle:6})    
    
    ###CAPACITORS(22pF)
    for i in [1,2]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i][0],y=LED_STOCK_POSITIONS_SIDE[i][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_CAPS_POSITION[i-1][0],y=arduino_gen2_CAPS_POSITION[i-1][1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
        g.abs_move(**{nozzle:6})  
    

    
        
def pickandplace_chip(valve,nozzle,speed,dwell):            
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    g.abs_move(x=30,y=20)
    g.set_home(x=0,y=0)

    for i in range(len(LED_STOCK_POSITIONS_TOP)):
        LED_STOCK_POSITIONS_TOP[i][0]=LED_STOCK_POSITIONS_TOP[i][0]-30
        LED_STOCK_POSITIONS_TOP[i][1]=LED_STOCK_POSITIONS_TOP[i][1]-20
    
    for i in range(len(LED_STOCK_POSITIONS_SIDE)):
        LED_STOCK_POSITIONS_SIDE[i][0]=LED_STOCK_POSITIONS_SIDE[i][0]-30
        LED_STOCK_POSITIONS_SIDE[i][1]=LED_STOCK_POSITIONS_SIDE[i][1]-20

#
    #### CHIP
    for i in [30]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i][0],y=LED_STOCK_POSITIONS_TOP[i][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.98+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.98})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=4.5,y=4.5) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
#        g.abs_move(**{nozzle:6})    
        
                    
def component_adhesive_arduino_gen2(valve,nozzle,speed,dwell):
    g.feed(25) 
    if valve is not None:
        g.set_valve(num = valve, value = 1)

    g.abs_move(x=30,y=20)
    g.set_home(x=0,y=0)


    for i in range(len(LED_STOCK_POSITIONS_TOP)):
        LED_STOCK_POSITIONS_TOP[i][0]=LED_STOCK_POSITIONS_TOP[i][0]-30
        LED_STOCK_POSITIONS_TOP[i][1]=LED_STOCK_POSITIONS_TOP[i][1]-20
    
    for i in range(len(LED_STOCK_POSITIONS_SIDE)):
        LED_STOCK_POSITIONS_SIDE[i][0]=LED_STOCK_POSITIONS_SIDE[i][0]-30
        LED_STOCK_POSITIONS_SIDE[i][1]=LED_STOCK_POSITIONS_SIDE[i][1]-20


#
#
    #### LEDs
    for i in [0,1,2,3,4]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i][0],y=LED_STOCK_POSITIONS_TOP[i][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_LED_POSITIONS[i][0],y=arduino_gen2_LED_POSITIONS[i][1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
#        g.abs_move(**{nozzle:6})    

    ### LED RESISTORS (1kOhm)
    for i in [0,1,2,3,4]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i+10][0],y=LED_STOCK_POSITIONS_TOP[i+10][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_LED_RES_POSITIONS[i][0],y=arduino_gen2_LED_RES_POSITIONS[i][1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
        g.abs_move(**{nozzle:6})    


    ###RESET RES (22kOhm)
    for i in [0]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_TOP[i+20][0],y=LED_STOCK_POSITIONS_TOP[i+20][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_RESET_RES_POSITION[0],y=arduino_gen2_RESET_RES_POSITION[1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
        g.abs_move(**{nozzle:6})    
    
    
    ###SENSOR RES (100Ohm)
    for i in [0]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i][0],y=LED_STOCK_POSITIONS_SIDE[i][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_SENSOR_RES_POSITION[0],y=arduino_gen2_SENSOR_RES_POSITION[1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
        g.abs_move(**{nozzle:6})    
    
    ###CAPACITORS(22pF)
    for i in [1,2]:
        g.feed(25)
        g.abs_move(x=LED_STOCK_POSITIONS_SIDE[i][0],y=LED_STOCK_POSITIONS_SIDE[i][1])
        g.feed(25) 
        g.abs_move(**{nozzle:1.97+1})
        g.feed(0.4)
        g.abs_move(**{nozzle:1.97})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.move(**{nozzle:5})
        g.feed(20)
        g.abs_move(x=arduino_gen2_CAPS_POSITION[i-1][0],y=arduino_gen2_CAPS_POSITION[i-1][1]) 
        g.feed(25)
        #g.move(x=-0.3)
        #g.arc(x=0.6,y=0,direction='CW')
        #g.arc(x=-0.6,y=0,direction='CW')
        #g.move(x=0.3)
        g.abs_move(**{nozzle:0.55+1})
        g.feed(0.4) 
        g.abs_move(**{nozzle:0.55})
        g.toggle_pressure(pressure_box)
        g.dwell(dwell)
        g.feed(1)
        g.abs_move(**{nozzle:3})
        g.feed(25)
        g.abs_move(**{nozzle:6})                          
                            
                                
                                    
                                        
                                            
                                                
                                                    
                                                        
                                                                

def arduino_gen2(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
   
    
    
    ##########test line
    #g.abs_move(x=2,y=2)
    #g.abs_move(**{nozzle:height})
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.feed(speed)
    #g.move(x=15)
    #g.set_valve(num = valve, value = 0)
    #g.feed(20)
    #g.clip(axis=nozzle, height=2, direction='-x')
    ##########test line
    
    g.abs_move(x=30,y=20)
    g.set_home(x=0,y=0)
        
    
    #for i in range(4):
    #    for j in range (8):
    #        g.abs_move(x = ATMEGA328_pad_positions[i][j][0], y = ATMEGA328_pad_positions[i][j][1])
    #        g.move(x = 0.2, y = 0.2)
    #        g.rect(x = 0.4, y = 0.4, start = 'UR')
    
    #### SENSOR_VCC, PIN 29
    
    g.abs_move(x=20,y=15)                        ###sensor vcc contact
    g.abs_move(C=-41.4,**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=-2,y=-2)
    g.abs_move(x=ATMEGA328_pad_positions[3][4][0])
    g.move(y=-1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.abs_move(y=ATMEGA328_pad_positions[3][4][1])   ##pin 29
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=1.6)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.abs_move(x=-10)
    g.move(x=-2,y=2)                                ##VCC contact
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=2,y=-2)
    g.abs_move(x=ATMEGA328_pad_positions[0][3][0]-1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.abs_move(y=ATMEGA328_pad_positions[0][3][1])   
    g.abs_move(x=ATMEGA328_pad_positions[0][3][0])   ##pin 4
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')



    ##### SENSOR_GND, PIN 29
    
    g.abs_move(x=20,y=-6)                         ###sensor gnd contact
    g.abs_move(C=-41.4,**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=-2,y=2)
    g.abs_move(x=ATMEGA328_pad_positions[2][4][0]+4)
    g.abs_move(y=ATMEGA328_pad_positions[2][6][1])
    g.abs_move(x=ATMEGA328_pad_positions[2][6][0])   ###pin 23, A0
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=4)
    g.abs_move(y=ATMEGA328_pad_positions[2][4][1])
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=-1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(x=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.abs_move(x=ATMEGA328_pad_positions[2][4][0])   ####pin 21, GND
    g.abs_move(x=4.4,y=4.4)
    g.abs_move(x=0,y=0)
    
    ####5 OUTPUT LEDs
    
    g.abs_move(y=-6)
    g.move(x=2)
    g.move(y=0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=0.8+0.9)
    g.abs_move(x=ATMEGA328_pad_positions[1][4][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][4][1])   ###pin 13, DIGITAL OUT1
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-0.7)
    g.move(x=-2.9)
    g.move(y=-0.8-0.9)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=-0.1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=2.0)

    g.move(y=0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=0.8+0.5)
    g.abs_move(x=ATMEGA328_pad_positions[1][5][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][5][1])   ###pin 14, DIGITAL OUT2
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.1)
    g.move(x=-2.2+0.5)
    g.move(y=-0.8-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=-0.1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(2.0)
    
    g.move(y=0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=0.8+0.1)
    g.abs_move(x=ATMEGA328_pad_positions[1][6][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][6][1])   ###pin 15, DIGITAL OUT3
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.5)
    g.move(x=-0.5)
    g.move(y=-0.8-0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=-0.1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=2)
    
    g.move(y=0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=0.8+0.1)
    g.abs_move(x=ATMEGA328_pad_positions[1][7][0])
    g.abs_move(y=ATMEGA328_pad_positions[1][7][1])   ###pin 16. DIGITAL OUT4
    g.abs_move(**{nozzle:height+0.1})
    g.move(y=-1.5)
    g.move(x=0.7)
    g.move(y=-0.8-0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=-0.1)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=2)
    
    g.move(y=0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.abs_move(y=ATMEGA328_pad_positions[2][0][1])
    g.abs_move(x=ATMEGA328_pad_positions[2][0][0])   ###pin 17. DIGITAL OUT5
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=1.2)
    g.move(y=-3.9)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(y=-0.5)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1) 
    g.dwell(0.3)
    g.move(y=-0.1)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
    
    
    g.abs_move(x=4.4,y=4.4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.abs_move(x=-1,y=-1)
    g.move(x=-1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(x=-0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=-0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.move(x=-1)
    g.abs_move(y=ATMEGA328_pad_positions[0][7][1])
    g.abs_move(x=ATMEGA328_pad_positions[0][7][0])  ####pin 8, bottom crystal pin
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=-5)
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=-1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(y=1.0,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(y=1.0,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.abs_move(y=ATMEGA328_pad_positions[0][4][1])
    g.move(x=1)
    g.abs_move(y=ATMEGA328_pad_positions[0][6][1])
    g.abs_move(x=ATMEGA328_pad_positions[0][6][0])   ####pin 7, top cystal pin
    g.abs_move(**{nozzle:height+0.1})
    g.move(x=-5)
    g.abs_move(y=ATMEGA328_pad_positions[0][4][1])
    g.abs_move(**{nozzle:height})
    g.dwell(0.1)
    g.move(x=1)
    g.set_valve(num = valve, value = 0)
    g.feed(speed*3)
    g.move(x=0.8,**{nozzle:2.0})
    g.dwell(0.5)
    g.move(**{nozzle:2})
    g.dwell(0.5)
    g.move(**{nozzle:-2})
    g.move(x=0.8,**{nozzle:-2.0})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.3)
    g.abs_move(x=ATMEGA328_pad_positions[0][4][0])   ####pin 5, crystal/cap 
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')


    g.abs_move(x=-12,y=-6)                    ###GND
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=2,y=2)
    g.abs_move(x=0)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')




#################################### END OF FUNCTION DEFINITIONS #######################################



#################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
reference_nozzle = 'A'

active_slide = 'slide1'
z_ref = -79.365

#####
#active_slide = 'slide2'
#z_ref = -79.565
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
##
##g.toggle_pressure(pressure_box)
##tpu_Harvard_bottom(valve='1',nozzle='A',height=0.4,speed=11,dwell=0.2,pressure=8)
##g.toggle_pressure(pressure_box)
#
##
###tpu_bottom_LED_strain(valve='2',nozzle='B',height=0.5,speed=13,dwell=0.2,pressure=10)
#
#g.toggle_pressure(pressure_box)
#TPU_spacing_tests(valve='1',nozzle='A',height=0.4,speed=15,dwell=0.2,pressure=12)
#g.toggle_pressure(pressure_box)
#
#

##

#
###########------------SOFT AGTPU WIRING
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
#arduino_gen2(valve='1',nozzle='z',height=0.22,speed=5,dwell=0.3,pressure=20)
#g.toggle_pressure(pressure_box)


#
###########------------COMPONENT ADHESIVE
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
##
#
#g.toggle_pressure(pressure_box)
#component_adhesive_arduino_gen2(valve='2',nozzle='B',height=0.12,speed=7,dwell=0.8,pressure=20)
#g.toggle_pressure(pressure_box)


#




############------------PICK+PLACE ARDUINO
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ac')
g.set_home(x=0, y=0)

#
#startx=35
#starty=0
##
#for i in range(len(LED_HARVARD_POSITIONS)):
#            LED_HARVARD_POSITIONS[i][0]=LED_HARVARD_POSITIONS[i][0]+startx
#            LED_HARVARD_POSITIONS[i][1]=LED_HARVARD_POSITIONS[i][1]+starty

#g.dwell(60)

g.toggle_pressure(pressure_box)
valve='3'
g.set_pressure(pressure_box, 0.1)
if valve is not None:
    g.set_valve(num = valve, value = 1)
g.set_vac(pressure_box,18)
g.dwell(2)
#pickandplace_arduino_gen2(valve='3',nozzle='C',speed=10,dwell=10)
pickandplace_chip(valve='3',nozzle='C',speed=10,dwell=10)
g.set_vac(pressure_box,0)
g.toggle_pressure(pressure_box)



#
###########------------ AGTPU CONNECTORS 
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
####
##
##startx=8
##starty=5
###
##for i in range(len(LED_HARVARD_POSITIONS)):
##        for j in range(len(LED_HARVARD_POSITIONS[i])):
##            LED_HARVARD_POSITIONS[i][j][0]=LED_HARVARD_POSITIONS[i][j][0]+startx
##            LED_HARVARD_POSITIONS[i][j][1]=LED_HARVARD_POSITIONS[i][j][1]+starty
##
##
##g.toggle_pressure(pressure_box)
##LED_Harvard_connectors(valve='1',nozzle='A',height=0.6+.2,speed=2,dwell=1,pressure=50,startx=8,starty=5)
##g.toggle_pressure(pressure_box)
#
#g.toggle_pressure(pressure_box)
##AgTPU_strain_speciman_LEDconnectors(valve='1',nozzle='A',height=0.45,speed=4,dwell=1.2,pressure=26) #soft
#AgTPU_strain_speciman_LEDconnectors(valve='2',nozzle='B',height=0.45,speed=4,dwell=1.2,pressure=18) #stiff
#
#g.toggle_pressure(pressure_box)

####
####
#


#


g.view(backend='matplotlib')

##
g.teardown()
