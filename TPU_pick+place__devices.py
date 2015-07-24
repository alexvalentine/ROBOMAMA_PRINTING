from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\alexs_print.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = [
            'A',
            #'B',
            #'C', 
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
        'origin': (110,110),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (5,5),
    },
    #'slide2': {
    #    'origin': (144,90),
    #    'size': 'auto',
    #    'profile': True,
    #    'profile-spacing': (10,10),
    #},
    #'slide3': {
    #    'origin': (144,26),
    #    'size': 'auto',
    #    'profile': True,
    #    'profile-spacing': (10,10),
    #}
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


def tpu_bottom(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
########test line
    g.abs_move(x=1,y=1)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=20)
    g.move(x=0.2)
    g.move(y=-20)
    g.move(x=0.2)
    g.move(y=20)
    g.feed(20)
    g.clip(axis=nozzle, height=6, direction='-x')
    g.set_pressure(pressure_box, pressure)
    
########printing 
    g.abs_move(4, 2)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.meander(x=25,y=45,spacing=0.2,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(axis=nozzle, height=5, direction='-y')


def LED_Harvard(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    #####first wire
    g.abs_move(6, 4)    
    g.abs_move(**{nozzle:height}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(y=33)
    g.move(x=5)
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-0.6)
    g.move(x=0.9)
    g.move(y=8.5)
    g.move(x=8.5)
    g.move(y=-10)
    g.move(x=3.1)
    g.abs_move(y=4)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(height=2, direction='+x')


    #
    #####second wire
    g.abs_move(6, 4)    
    g.abs_move(**{nozzle:height+0.04}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(y=3)
    g.move(x=1,**{nozzle:-0.04})
    g.move(x=4)
    g.move(y=6.2)
    g.dwell(dwell)
    g.move(y=0.8,**{nozzle:1})
    g.move(y=0.8,**{nozzle:-1})
    g.move(y=1.2)
    g.move(x=1.6)
    g.move(y=8)
    g.move(x=1.25)
    g.dwell(dwell)
    g.move(x=0.8,**{nozzle:1})
    g.move(x=0.8,**{nozzle:-1})
    g.move(x=1.4)
    g.dwell(dwell)
    g.move(x=0.8,**{nozzle:1})
    g.move(x=0.8,**{nozzle:-1})
    g.move(x=1.25)
    g.move(y=-8.5)
    g.move(x=1.8)
    g.move(y=-0.6)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-0.6)
    g.move(x=2)
    g.abs_move(y=4)
    g.set_valve(num = valve, value = 0)
    g.feed(10)
    g.clip(height=2, direction='+x')


    ######third wire
    g.abs_move(6, 4)    
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
    g.move(y=-2.6)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-3.2)
    g.dwell(dwell)
    g.move(y=-0.8,**{nozzle:1})
    g.move(y=-0.8,**{nozzle:-1})
    g.move(y=-0.8)
    g.move(x=2.1)
    g.abs_move(y=4)


    #####anode/cathode
    g.feed(speed*0.4)
    g.move(x=1.5)  
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
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
    g.clip(height=2, direction='+x')

    g.abs_move(x=6,y=4)
    g.abs_move(**{nozzle:height+0.03}) 
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed*0.4)
    g.move(x=1.4)
    g.arc(x=-2.8,y=0,radius=1.4)
    g.arc(x=2.8,y=0,radius=1.4)
    g.move(x=-0.2)
    g.arc(x=-2.4,y=0,radius=1.2)
    g.arc(x=2.4,y=0,radius=1.2)
    g.move(x=-0.2)
    g.arc(x=-2.0,y=0,radius=1)
    g.arc(x=2.0,y=0,radius=1)
    g.move(x=-0.2)
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
    g.clip(height=2, direction='+x')


def LED_Harvard_connectors(valve,nozzle,height,speed,dwell,pressure,wire):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    
    
    if wire == 'first':
    
    #####first wire
        g.abs_move(6, 4)    
        g.abs_move(**{nozzle:height+3}) 
        g.feed(speed)
        g.move(y=33)
        g.move(x=5)
        g.move(y=-2.4)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
    
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.feed(10)
        g.clip(height=2, direction='+x')

    elif wire == 'second':
    
    #####second wire
        g.abs_move(6, 4)    
        g.abs_move(**{nozzle:height+3}) 
        g.feed(speed)
        g.move(y=3)
        g.move(x=5)
        g.move(y=6.0)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=1.0,**{nozzle:1})
        g.move(y=1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
    
        g.move(y=1.0)
        g.move(x=1.6)
        g.move(y=8)
        g.move(x=1.05)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(x=1.0,**{nozzle:1})
        g.move(x=1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
    
        g.move(x=1.0)
    
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(x=1.0,**{nozzle:1})
        g.move(x=1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
    
        g.move(x=1.05)
        g.move(y=-8.5)
        g.move(x=1.8)
        g.move(y=-0.4)
    
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.set_valve(num = valve, value = 0)
        g.feed(10)
        g.clip(height=2, direction='+x')

    else:

    ######third wire
        g.abs_move(6, 4)    
        g.abs_move(**{nozzle:height+3}) 
        g.feed(speed)
        
        g.move(y=33)
        g.move(x=15.4)
        g.move(y=-2.4)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
    
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.move(y=-2.8)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})
        g.move(y=-1.0,**{nozzle:-1})
        g.set_valve(num = valve, value = 0)
        g.abs_move(**{nozzle:height+3}) 
        g.feed(10)
        g.clip(height=2, direction='+x')


def pickandplace(valve,nozzle,speed,dwell):
    g.feed(25) 
    

    g.abs_move(x = -10, y = 20)
    g.feed(10) 
    g.abs_move(**{nozzle:-2})
    g.toggle_pressure(pressure_box)
    g.abs_move(**{nozzle:5})
    g.abs_move(x=6, y=4)    
    g.abs_move(x=11, y=33.6) 
    g.abs_move(**{nozzle:1}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.abs_move(**{nozzle:5})
    
    g.abs_move(x = -10, y = 20)
    g.feed(10) 
    g.abs_move(**{nozzle:-2})
    g.toggle_pressure(pressure_box)
    g.abs_move(**{nozzle:5})
    g.abs_move(x=6, y=4)    
    g.abs_move(x=11, y=33.6) 
    g.abs_move(**{nozzle:1}) 
    g.toggle_pressure(pressure_box)
    g.dwell(dwell)
    g.abs_move(**{nozzle:5})
    
    
    
    
    
    
    
    
    


        g.feed(speed)
        g.move(y=33)
        g.move(x=5)
        g.move(y=-2.4)
        
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.move(y=-1.0,**{nozzle:1})





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

def arduino_gen1(valve,nozzle,height,speed,dwell,pressure,testline,startx,starty):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
   
    if testline == 'y':
        #########test line
        g.abs_move(x=2,y=3.5)
        pressure_purge(delay = 2)
        g.abs_move(**{nozzle:height})
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(dwell)
        g.feed(speed)
        g.move(x=15)
        g.feed(20)
        g.clip(axis=nozzle, height=2, direction='-x')
        #########test line
    

    g.write("POSOFFSET CLEAR X Y")    
    g.abs_move(x=startx,y=starty) ####bottom left corner of TPU square
    g.set_home(x=-6.5,y=-6.5)
    
    
    for i in range(4):
        for j in range (8):
            g.abs_move(x = ATMEGA328_pad_positions[i][j][0], y = ATMEGA328_pad_positions[i][j][1])
            g.move(x = 0.2, y = 0.2)
            g.rect(x = 0.4, y = 0.4, start = 'UR')

    
    ###### RESET WIRE, PIN 29
    #
    #g.abs_move(x=13.5,y=13.5)
    #g.abs_move(**{nozzle:height})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.move(x=-3,y=-3)
    #g.move(x=-3)
    #g.move(x=-0.3,**{nozzle:1})
    #g.move(x=-0.3,**{nozzle:-1})
    #g.abs_move(x = ATMEGA328_pad_positions[3][4][0])
    #g.abs_move(y = ATMEGA328_pad_positions[3][4][1])
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='+y')

    ###### VCC WIRE, PIN 4
    #
    #g.abs_move(x=13.5,y=13.5)
    #g.abs_move(**{nozzle:height+0.04})
    #g.feed(speed)
    #if valve is not None:
    #    g.set_valve(num = valve, value = 1)
    #g.dwell(dwell)
    #g.move(x=-3,y=-3)
    #g.move(x=-1,y=-1,**{nozzle:-0.04})    
    #g.move(x=-4,y=-4)
    #g.abs_move(y = ATMEGA328_pad_positions[0][3][1])
    #g.abs_move(x = ATMEGA328_pad_positions[0][3][0])
    #g.set_valve(num = valve, value = 0)
    #g.feed(15)
    #g.clip(axis=nozzle, height=2,direction='+x')
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
    
    
#    ##### GND WIRE (LED), PIN 17
#    
#    g.abs_move(x=13.5,y=-4)
#    g.abs_move(**{nozzle:height})
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)  
#    g.move(x=-1.5,y=1.5)
#    g.move(x=-2)
#    g.move(y=1)
#    g.move(y=0.8,**{nozzle:1})
#    g.move(y=0.8,**{nozzle:-1})
#    g.move(y=1)
#    g.move(y=0.3,**{nozzle:1})
#    g.move(y=0.3,**{nozzle:-1})
#    g.abs_move(y = ATMEGA328_pad_positions[2][0][1])
#    g.abs_move(x = ATMEGA328_pad_positions[2][0][0])
#    g.set_valve(num = valve, value = 0)
#    g.feed(15)
#    g.clip(axis=nozzle, height=2,direction='+x')
#    
#
#    ##### GND WIRE (cap, half of oscillator), PIN 20, 5, 7
#    
#    g.abs_move(x=13.5,y=-4)
#    g.abs_move(**{nozzle:height+0.04})
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)  
#    g.move(x=-1.5,y=1.5)
#    g.move(1,**{nozzle:-0.04})
#    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
#    g.move(x=-5)
#    g.abs_move(y = ATMEGA328_pad_positions[0][4][1])
#    g.move(x=-8.5)
#    g.move(y=-0.5,**{nozzle:1})
#    g.move(y=-0.5,**{nozzle:-1})
#    g.abs_move(y = ATMEGA328_pad_positions[0][6][1])
#    g.move(x=-2)
#    g.move(x=2)
#    g.abs_move(x = ATMEGA328_pad_positions[0][6][0])
#    g.set_valve(num = valve, value = 0)
#    g.feed(15)
#    g.clip(axis=nozzle, height=2,direction='-x')
#
#
#    ##### GND WIRE (other cap, other half of oscillator), PIN 8
#    
#    g.abs_move(x=13.5,y=-4)
#    g.abs_move(**{nozzle:height+0.08})
#    g.feed(speed)
#    if valve is not None:
#        g.set_valve(num = valve, value = 1)
#    g.dwell(dwell)  
#    g.move(x=-1.5,y=1.5)
#    g.move(1,**{nozzle:-0.04})
#    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
#    g.move(x=-5)
#    g.move(y=-2,**{nozzle:-0.04})
#    g.move(x=-4)
#    g.abs_move(x=-1,y=-1)
#    g.move(y=0.6)
#    g.move(y=0.5,**{nozzle:1})
#    g.move(y=0.5,**{nozzle:-1})
#
#    g.move(x=-3.5)
#    g.move(y=1)    
#    g.move(y=-1)
#    g.move(x=3.5)
#    
#    g.abs_move(y = ATMEGA328_pad_positions[0][7][1])
#    g.abs_move(x = ATMEGA328_pad_positions[0][7][0])
#    g.set_valve(num = valve, value = 0)
#    g.feed(15)
#    g.clip(axis=nozzle, height=2,direction='-x')
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
#    #### VCC terminal
#    
#    g.abs_move(x=13.5,y=13.5)
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
#    ##### GND WIRE (LED), PIN 17
#    
#    g.abs_move(x=13.5,y=-4)
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


#################################### END OF FUNCTION DEFINITIONS #######################################



#################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
reference_nozzle = 'A'

active_slide = 'slide1'
z_ref = -86.993507

#active_slide = 'slide2'
#z_ref = -88.493860
#active_slide = 'slide3'
#z_ref = -88.3824

automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
g.write("POSOFFSET CLEAR X Y U A B C D")

  

substrate_dif = automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref

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


##########------------TPU BOTTOM
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)

g.toggle_pressure(pressure_box)
tpu_bottom(valve='1',nozzle='A',height=0.05,speed=20,dwell=0.2,pressure=1.5)
g.toggle_pressure(pressure_box)


##########------------SOFT AGTPU WIRING
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ab')
g.set_home(x=0, y=0)

g.toggle_pressure(pressure_box)
LED_Harvard(valve='2',nozzle='B',height=0.05,speed=20,dwell=0.2,pressure=1.5)
g.toggle_pressure(pressure_box)


##########------------STIFF AGTPU CONNECTORS / PICK+PLACE
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0], y=automator.substrate_origins[active_slide]['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ac')
g.set_home(x=0, y=0)

g.toggle_pressure(pressure_box)
LED_Harvard_connectors(valve='3',nozzle='C',height=0.05,speed=20,dwell=0.2,pressure=1.5,wire='first')
g.toggle_pressure(pressure_box)


g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'cd')
g.set_home(x=0, y=0)

valve='4'
g.set_pressure(pressure_box, 0)
if valve is not None:
    g.set_valve(num = valve, value = 1)
g.set_vac(pressure_box,vacuum)
g.toggle_pressure(pressure_box)


pickandplace(valve='4',nozzle='D',speed=10,dwell=3)




#g.toggle_pressure(pressure_box)
#LED_Harvard_connectors(valve='3',nozzle='C',height=0.05,speed=20,dwell=0.2,pressure=1.5,wire='second')
#g.toggle_pressure(pressure_box)



#g.toggle_pressure(pressure_box)
#LED_Harvard_connectors(valve='3',nozzle='C',height=0.05,speed=20,dwell=0.2,pressure=1.5,wire='third')
#g.toggle_pressure(pressure_box)

g.toggle_pressure(pressure_box)




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
