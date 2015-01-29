from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\cell_printing_out.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = ['A',
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
        'origin': (150,150),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (40,40),
    },
    'slide2': {
        'origin': (150,87),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (40,40),
    },
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
cant_y_translate = 2.5
#Defining positions of all 16 cantilevers as the top left (first 8 sensors) or bottom left (last 8 sensors) corner of cantilever, offest from extra and inset
#cantilever_position = ((11.93, 33.9 + cant_y_translate), (17.68, 33.9+ cant_y_translate), (25.43, 33.9+ cant_y_translate), (31.18, 33.9+ cant_y_translate), (38.93, 33.9+ cant_y_translate), (44.68, 33.9+ cant_y_translate), (52.43, 33.9+ cant_y_translate), (58.18, 33.9+ cant_y_translate),
#                       (11.93, 15.55 - cant_y_translate), (17.68, 15.55 - cant_y_translate), (25.43, 15.55 - cant_y_translate), (31.18, 15.55 - cant_y_translate), (38.93, 15.55 - cant_y_translate), (44.68, 15.55 - cant_y_translate), (52.43, 15.55 - cant_y_translate), (58.18, 15.55 - cant_y_translate))

cantilever_position = ((11.93+0.75, 33.9 + cant_y_translate), (17.68-0.75, 33.9+ cant_y_translate), (25.43+0.75, 33.9+ cant_y_translate), (31.18-0.75, 33.9+ cant_y_translate), (38.93+0.75, 33.9+ cant_y_translate), (44.68-0.75, 33.9+ cant_y_translate), (52.43+0.75, 33.9+ cant_y_translate), (58.18-0.75, 33.9+ cant_y_translate),
                       (11.93+0.75, 15.55 - cant_y_translate), (17.68-0.75, 15.55 - cant_y_translate), (25.43+0.75, 15.55 - cant_y_translate), (31.18-0.75, 15.55 - cant_y_translate), (38.93+0.75, 15.55 - cant_y_translate), (44.68-0.75, 15.55 - cant_y_translate), (52.43+0.75, 15.55 - cant_y_translate), (58.18-0.75, 15.55 - cant_y_translate))



#Defining positions of 24 pins, 12 on top (4 overlapping) and 12 on bottom (4 overlapping)
pin_position = ((6.6, 47.56), (12.6, 47.56), (12.6, 47.56), (18.6, 47.56), (24.6, 47.56), (30.6, 47.56), (30.6, 47.56), (36.6, 47.56),
                (42.6, 47.56), (48.6, 47.56), (48.6, 47.56), (54.6, 47.56), (60.6, 47.56), (66.6, 47.56), (66.6, 47.56), (72.6, 47.56),
                (3, 3), (9, 3), (9, 3), (15, 3), (21, 3), (27, 3), (27, 3),
                (33, 3), (39, 3), (45, 3), (45, 3), (51, 3), (57, 3), (63, 3), (63, 3), (69, 3))

#Defining positions of wells as the bottom left corner (top 4) and the top left corner (bottom 4) of the square trace


well_position = ((10.5, 25.245), (24, 25.245), (37.5, 25.245), (51, 25.245), 
                       (10.5, 24.245), (24, 24.245), (37.5, 24.245), (51, 24.245))
#((10.5, 26.045), (24, 26.045), (37.5, 26.045), (51, 26.045), 
#                       (10.5, 25.045), (24, 25.045), (37.5, 25.045), (51, 25.045))

pressure_box = 4       # COM port of pressure box    

tail = 1.5          # first distance of wire before cantilever position and after

extra = 0#1.5      # distance from cantilever position to top wire line

wire_width = 1.55       # distance from center of each wire trace to its paired wire - width of sensor
        
wire_height=(0.035,)*8

wire_pressure=(7,)*8

wire_speed = (10,)*8
                
                
                ####printed top slide at 25um, but wires did that weird dragging thing on only half of each cantilever######
                ######printed bottom slide at 35um, looked fine.....print at this height from now on!!!!!!!!######
                                                                                            

insulating_meand_spacing_top = 0.13
insulating_meand_spacing_bot = 0.13

insulating_height_top = (0.025,)*16 
insulating_height_bot = (0.015,)*16

insulating_pressure_top = (3.5,)*16
insulating_pressure_bot = (3.5,)*16
                                        
insulating_speed_top = (15,)*16
insulating_speed_bot = (15,)*16

insulating_dwell = 0.5

 
 #**** both top of bottom slide 1 TPU cover, bottom of bottom slide 2 TPU cover****# 
 
 
              
align_top_pressure=(10,)*16

top_over=(0.06,)*16 #spacing
top_height=(0.09,)*16 
top_speed=(3,)*16

 
  #**** printed at 60um spacing ***#
 #printed at 90um height, mannually adjusted down to ~82um (zeroing is off so this is not accurate)
 

cantilever_width = 2.9
cantilever_bending_length = 5.5
cantilever_length = cantilever_bending_length + cant_y_translate

trans_speed = 40


cover_pressure=(15,)*8
#
inset=(cantilever_width-wire_width)/2


########SILVER TPU: (85wt% of solid) Ag (2-4um covered) in 30%wt TPU 35A in DMF
#electrode_height=0.075
#electrode_pressure = 4

#############TRAVIS"S INK
electrode_height=0.130
electrode_pressure = 8
electrode_speed = 8


############################## VARIABLE TRASH ###########################

#
#cell_groove_height=(0.022,)*15
#
#cell_groove_pressure=(18.2,)*15
#               
#cell_groove_speed=(4,)*15
#
#cell_groove_spacing=(0.04, 0.030, 0.040, 0.060, 0.070, 0.080, 0.040, 0.050, 0.060, 0.070, 0.080, 0.040, 0.050, 0.060, 0.070, 0.080)
#

base_height=(0.015,)*16#(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
             #0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)
base_pressure=(2,2.3,2.6,2.9,3.2,3.5,3.8,4.1,)*2#(5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2)*2#(6.2,)*8+(6.1,)*8#
               
base_speed=(4,)*16#(5, 5, 5, 5, 5, 5, 5, 5,
            #5, 5, 5, 5, 5, 5, 5, 5)
base_height=(0.02,)*15 #(0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01,
             #0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)

base_pressure=(11.5,)*15 #(5.5, 5.6, 5.7, 5.8, 5.9, 6.0, 6.1, 6.2)*2#(6.2,)*8+(6.1,)*8#
               
base_speed=(4,)*15

base_spacing = 0.3875

############################## VARIABLE TRASH ###########################



############### END OF VARIABLE AND PARAMTER DEFINITIONS ###############


############################# FUNCTION DEFINITIONS ###########################


def set_home_in_z():
    g.write('POSOFFSET CLEAR A B C D')
    g.feed(25)
    g.abs_move(A=-2, B=-2, C=-2, D=-2)
    g.set_home(A=(-zA -2), B=(-zB -2), C = (-zC - 2), D=(-zD - 2))
    
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

def meander_2tails(x, y, z, spacing, orientation, tail, speed, clip_direction, nozzle, valve, dwell = 0.5):
    g.feed(15)
    g.move(x=-tail)
    g.abs_move(**{nozzle:z})
    g.feed(3)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=tail)
    g.feed(speed)
    g.meander(x=x, y=y, spacing=spacing, orientation='y', tail = False)
    #g.move(x=tail)
    if valve is not None:
        g.set_valve(num = valve, value = 0)
        
    g.dwell(0.3)
    g.clip(axis=nozzle, direction=clip_direction, height=5)
    #g.move(A=3)

def meander_nostop(x, y, spacing, orientation, speed):
    #g.feed(speed)
    temp_y_pos = g.current_position['y']
    g.meander(x=x, y=y, spacing=spacing, orientation='y', tail = False)
    new_y_pos = g.current_position['y']
    if abs(new_y_pos - temp_y_pos)> 0.1:
        msg = 'Your meander ends at the wrong Y position, dummy'
        raise RuntimeError(msg)
         

            
def test_print():    
    g.set_pressure(pressure_box, 1)
    g.toggle_pressure(pressure_box)
    g.feed(4)
    g.set_valve(num = 0, value = 1)
    g.dwell(0.5)
    g.meander(x=10, y=15, spacing=2, orientation = 'y', tail = False)
    g.set_valve(num = 0, value = 1)
    g.toggle_pressure(pressure_box)

    
def print_sacrificial(trace_speed, height, over, nozzle, overhang = 0, y_inset = cant_y_translate):
    g.feed(40)
    g.abs_move(5, 40)
    g.feed(10)
    g.abs_move(**{nozzle:height})
    g.feed(trace_speed)
    g.move(y=-20)
    g.abs_move(**{nozzle:6})
    
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1]-y_inset -0.5)
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=-(cantilever_length-y_inset), spacing=over,
                        z=height, tail = 0.5, clip_direction = '-y', speed=trace_speed, 
                        orientation = 'y', nozzle = nozzle, valve = None)
    
    for i in range(9,16,2):
        
        g.feed(15)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] +0.5 + y_inset)
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=(cantilever_length - y_inset), spacing=over, 
                    z=height, tail = 0.5, clip_direction = '+y', speed=trace_speed, 
                    orientation = 'y', nozzle = nozzle, valve = None)
    g.feed(20)
    g.abs_move(**{nozzle:50})
    

def print_wires(z, speed, extra, tail, width, length, valve, nozzle, clip_direction, arc_direction, k):
    inset= (cantilever_width-width)/2
    #inset = 0.875
    g.feed(15)
    g.move(x=(-tail+inset), y=extra)
    g.feed(15)
    g.abs_move(**{nozzle:z})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.move(x=tail)
    g.move(y=-(length+extra))
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    #g.move(x=width)
    g.move(y=(length+extra))
    space = cantilever_position[1][0] - cantilever_position[0][0]
    g.move(x=(space-width))
    g.move(y=-(length+extra))
    #g.move(x=width)
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=(length+extra))
    g.move(x=tail)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, direction=clip_direction, height=3)
    g.abs_move(**{nozzle:20})

def print_wires_no_stop(z, speed, extra, tail, width, length, valve, nozzle, clip_direction, arc_direction, k):
  
    if length > 0:
        y_move = -(length + extra - (width/2))
    else:
        y_move = (-length + extra - (width/2))
        extra = -extra
    #print length
    #print y_move
    #print 'length_ymove'
    g.feed(speed)
    g.abs_move(**{nozzle:z})
    g.move(x=tail)
    g.move(y=y_move)    
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=-y_move)
    space = cantilever_position[1][0] - cantilever_position[0][0]
    print space-width
    g.move(x=(space-width))
    
    g.move(y=y_move)
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=-y_move)
    g.move(x=tail)

   
   

def print_all_wires_no_stop(valve, nozzle,initial_dwell):
    width = wire_width
    inset = (cantilever_width-width)/2
    g.set_pressure(pressure_box, wire_pressure[0])
    
    ######test circle#####
    g.feed(20)
    g.abs_move(4, 20)
    g.abs_move(**{nozzle:wire_height[0]})
    g.feed(wire_speed[0])
    g.set_valve(num = valve, value = 1)
    g.dwell(initial_dwell)
    g.arc(x=1.5,y=0.0001,radius=-3)
    g.abs_move(**{nozzle:3})
    g.feed(15)
    
    
    
    
    g.abs_move(*cantilever_position[0])
    g.set_pressure(pressure_box, wire_pressure[0])
    g.move(x=(-tail+inset), y=extra)
    g.abs_move(**{nozzle:wire_height[0]})
    g.feed(8)
    for i in range(0,8,2):
        j=i/2
        g.abs_move(cantilever_position[i][0]+(-tail+inset), y = cantilever_position[i][1]+extra)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        print_wires_no_stop(z=wire_height[j], speed=wire_speed[j], extra = extra,
            tail = 1.5, width = 1.55, length=(cantilever_length - 0.75), valve = valve, nozzle = nozzle, clip_direction = '+y', k=j, arc_direction = 'CCW')
        g.set_valve(num = valve, value = 0)
        g.move(x=1.5,**{nozzle:2})
        if i==6:
            print ''
        else:
            g.move(x=1.5,**{nozzle:-2})


    g.set_valve(num = valve, value = 0)
    g.feed(20)       
    g.abs_move(**{nozzle:20})
    
    g.abs_move(*cantilever_position[8])
    g.set_pressure(pressure_box, wire_pressure[0])
    g.move(x=(-tail+inset), y=extra)
    g.abs_move(**{nozzle:wire_height[4]})
    g.set_valve(num = valve, value = 1)
    g.feed(8)  
          
    for i in range(8,16,2):
        j=i/2
        g.abs_move(cantilever_position[i][0]+(-tail+inset), y = cantilever_position[i][1]-extra)
        g.feed(8)
        if valve is not None:
            g.set_valve(num = valve, value = 1)        
        print_wires_no_stop(z=wire_height[j], speed=wire_speed[j], extra = extra, 
            tail = 1.5, width = 1.55, length=-(cantilever_length - 0.75), valve = valve, nozzle = nozzle, clip_direction = '-y', k=j, arc_direction = 'CW')
        g.set_valve(num = valve, value = 0)
        g.move(x=1.5,**{nozzle:2})
        if i==14:
            print ''
        else:
            g.move(x=1.5,**{nozzle:-2})
        

    g.set_valve(num = valve, value = 0)
    g.feed(20)          
    g.abs_move(**{nozzle:50})  

def meander_tops(x, y, start, spacing, z, speed, nozzle, clip_direction, valve, orientation = 'y'):   
    g.feed(10)
    g.abs_move(**{nozzle:z})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    #g.dwell(0.25)
    g.meander(x=x, y=y, spacing=spacing, orientation = orientation, tail = False, start=start)
    g.move(**{nozzle:0.1})
    #g.clip(axis=nozzle, direction=clip_direction, height=5) 


def print_all_aligned_tops(nozzle, valve):
    g.set_pressure(pressure_box, align_top_pressure[1])
    pressure_purge(delay = 1.5)
    y_translation = cant_y_translate
    
    #test_line
    g.abs_move(x=5.3,y=7)
    g.set_pressure(pressure_box, align_top_pressure[0])
    g.abs_move(**{nozzle:top_height[0]})
    g.feed(top_speed[0])
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.move(y=30)
    g.set_valve(num = valve, value = 0)
    g.move(**{nozzle:0.100})

    for i in range(1,8,2):
        g.feed(5)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] - y_translation +0.5)
        g.move(x=-0.15)
        g.set_pressure(pressure_box, align_top_pressure[i])
        #pressure_purge(delay = 0.1)
        meander_tops(x=(cantilever_width + 0.15), y=cantilever_length - y_translation +0.5, start='UL', spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)
    
    g.set_valve(num = valve, value = 0)

    g.move(x=4)
    g.move(y=-10) ## this is the movement from end of top row to start of bottom row, without turning off pressure, traveling between the two rows
    g.move(x=-50)
    
    
    for i in range (9,16,2):
        g.feed(5)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] + y_translation -0.5)
        g.move(x=-0.15)
        g.set_pressure(pressure_box, align_top_pressure[i])
        #pressure_purge(delay = 0.1)
        meander_tops(x=(cantilever_width + 0.15), y=cantilever_length - y_translation +0.5, start='LL',spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)
    
    g.set_valve(num = valve, value = 0)
#

def print_all_wires(valve, nozzle):
    
    for i in range(0,8,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = 1.5, tail = 1.5, width = 1.55, length=5.2, valve = valve, nozzle = nozzle, clip_direction = '+y', k=j, arc_direction = 'CCW')
        g.feed(30)
        g.abs_move(**{nozzle:60})
        g.dwell(1)   
    
    for i in range(8,16,2):
        g.feed(15)
        j=i/2
        g.abs_move(*cantilever_position[i])
        g.set_pressure(pressure_box, wire_pressure[j])
        print_wires(z=wire_height[j], speed=wire_speed[j], extra = -1.5, tail = 1.5, width = 1.55, length=-5.2, valve = valve, nozzle = nozzle, clip_direction = '-y', k=j, arc_direction = 'CW')
        g.feed(30)
        g.abs_move(**{nozzle:60})
        g.dwell(1)

def print_cover(z, height, length, over, speed, pressure, start, valve = 1):
    g.feed(speed)    
    g.set_pressure(com_port=pressure_box, value=pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.8)
    g.meander(x=length, y=height, spacing = over, start=start, orientation = 'x')
    g.set_valve(num = valve, value = 0)          

def print_all_covers(nozzle = 'A', valve = 0):
    for i in range(0,4):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] + 14))
        g.move(x=0.5, y=-0.5)
        g.abs_move(**{nozzle:0.23})
        print_cover(z=0.3, height=4.9, length = 11.5, over = 0.40, speed = 12, pressure = cover_pressure[i], start='UL',valve = valve)
        g.clip(axis=nozzle, direction='-y', height=5)

    
    
    for i in range(4,8):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] -14))
        g.move(x=0.5, y=0.5)
        g.abs_move(**{nozzle:0.23})
        print_cover(z=0.3, height=4.9, length = 11.5, over = 0.41, speed = 12, pressure = cover_pressure[i], start='LL', valve = valve)
        g.clip(axis=nozzle, direction='+y', height=5)
                          
def stacked_rectangle(x, y, layer_height, layers, nozzle = 'A'):
    
    for i in range(layers):
        g.move(x=x)
        g.move(y=-y)
        g.move(x=-x)
        g.move(y=y)
        g.move(**{nozzle:layer_height})

def print_single_well(x, y, layer_height, layers, speed, pressure, filament = 1, valve = 0, nozzle = 'A'):
    g.feed(speed)
    g.set_pressure(com_port = pressure_box, value = pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    stacked_rectangle(x=x, y=y, layer_height = layer_height, layers = layers, nozzle = nozzle)
    g.set_valve(num=valve, value = 0)

def print_ID(pressure,speed,nozzle,valve,dwell):
    g.feed(15)
    g.abs_move(x=3,y=5)
    g.abs_move(**{nozzle:0.35})
    g.feed(speed)
    g.set_pressure(com_port = pressure_box, value = pressure)
    pressure_purge(delay = 1)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.move(x=2)
    g.move(x=-2,y=2)
    g.move(y=-2)
    g.feed(15)
    g.clip(axis=nozzle, direction='+y', height=10)
    
def print_all_single_wells(layer_height, layer_increments, total_increments, pressure, speed, nozzle, valve):
    #
    for i in range(0,4):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.35})
        print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
        g.clip(axis=nozzle, direction='+y', height=3)
    
    for i in range(4,8):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.35})
        print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
        g.clip(axis=nozzle, direction='-y', height=3)
     
    count = 0
    repeats = (total_increments)-1     
    
    
    for i in range(repeats-1):
        
        count = count + layer_increments
        for i in range(0,4):
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:0.15+count*layer_height})
            print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
            g.clip(axis=nozzle, direction='+y', height=3)
       
        for i in range(4,8):      
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:0.15+count*layer_height})
            print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
            g.clip(axis=nozzle, direction='-y', height=3)

def print_insulating_layer(nozzle, valve, TorB):
    if TorB == 'T':
        speed = insulating_speed_top
        height = insulating_height_top[0]
        pressure = insulating_pressure_top
        spacing = insulating_meand_spacing_top 
        y_translation = cant_y_translate
        dwell=1.5
        
    else:
        speed = insulating_speed_bot
        height = insulating_height_bot[0]
        pressure = insulating_pressure_bot
        spacing = insulating_meand_spacing_bot
        y_translation = 0
        dwell=1.8
    
    g.feed(25)
    g.set_pressure(pressure_box, pressure[1])             
    pressure_purge(delay = 0.5)
    g.abs_move(x=cantilever_position[0][0]-3, y=cantilever_position[0][1] - y_translation)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)

    for i in range(0,8):
        g.abs_move(cantilever_position[i][0], cantilever_position[i][1] - y_translation)
        if valve is not None:
            g.set_valve(num = valve, value = 1)
        g.dwell(insulating_dwell)
        g.feed(speed[0])
        meander_nostop(x=cantilever_width, y=-(cantilever_length - y_translation), spacing=spacing, orientation = 'y', speed=speed[i])            
        g.set_valve(num = valve, value = 0)
         
    g.move(x=3)
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
    
    g.feed(25)
    g.set_pressure(pressure_box, pressure[1])             
    pressure_purge(delay = 0.5)
    g.abs_move(x=cantilever_position[8][0]-3, y=cantilever_position[8][1] - y_translation)
    g.abs_move(**{nozzle:height})
    
    for i in range(8,16):
        g.abs_move(cantilever_position[i][0], cantilever_position[i][1] + y_translation)
        if valve is not None:
            g.set_valve(num = valve, value = 1)        
        g.dwell(insulating_dwell)
        g.feed(speed[0])
        meander_nostop(x=cantilever_width, y=cantilever_length - y_translation, spacing=spacing, orientation = 'y', speed=speed[i])
        g.set_valve(num = valve, value = 0)

    g.move(x=3)
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)


def print_electrodes(valve, nozzle):
    silver_inset = 0.75
    for i in range(0,32):
        j=(i/2)
        if i<16:
            myclip='-y'
        else:
            myclip='+y'
        if i%2==0:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(**{nozzle:electrode_height})
            g.set_valve(num = valve, value = 1)
            g.dwell(0.25)
            g.feed(electrode_speed)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]-extra + silver_inset))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]+extra - silver_inset))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i])
            g.move(x=1)
            g.arc(x=0,y=0.00001,radius=-1)
            g.move(x=-0.4)
            g.arc(x=0,y=0.00001,radius=-0.6)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, direction=myclip, height=5)
        else:
            g.feed(15)
            g.abs_move(*pin_position[i]) 
            g.set_pressure(pressure_box, electrode_pressure)
            g.abs_move(**{nozzle:electrode_height})
            g.set_valve(num = valve, value = 1)
            g.dwell(0.25)
            g.feed(electrode_speed)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]-extra + silver_inset))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]+extra - silver_inset))
            g.move(x=0.5)
            g.abs_move(*pin_position[i]) 
            g.move(x=1)
            g.arc(x=0,y=0.00001,radius=-1)
            g.move(x=-0.4)
            g.arc(x=0,y=0.00001,radius=-0.6)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, direction=myclip, height=5)




#################################### END OF FUNCTION DEFINITIONS #######################################



#################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
reference_nozzle = 'A'
automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")

#active_slide = 'slide1'
#z_ref = -88.0601
###
active_slide = 'slide2'
z_ref = -80.93123
#automator.substrate_origins[active_slide]['A'][2]#-81.24665 #slide2
#automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
g.write("POSOFFSET CLEAR X Y U A B C D")

  

substrate_dif = automator.substrate_origins[active_slide][reference_nozzle][2] - z_ref

if 'A' in AXES_USED:
    zA = automator.substrate_origins[active_slide]['A'][2] - substrate_dif
if 'B' in AXES_USED:
    zB = automator.substrate_origins[active_slide]['B'][2] - substrate_dif
if 'C' in AXES_USED:
    zC = automator.substrate_origins[active_slide]['C'][2] - substrate_dif
if 'D' in AXES_USED:
    zD = automator.substrate_origins[active_slide]['D'][2] - substrate_dif    

 
#
###########PRINT ME SOME SACRIFICIAL LAYERS
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0] - 1.7, y=automator.substrate_origins[active_slide]['A'][1] - 1)
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ac')
#g.set_home(x=0, y=0)
#
#print_sacrificial(trace_speed = 5, height = -0.050, over = 0.75, nozzle = 'C', overhang = 0)

  
####PRINT ME SOME INSULATING LAYERS ON BOTTOM
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0).
#
#
#g.toggle_pressure(pressure_box)   
##pressure_clear(dwell_time = 1, pressure = 10, valve = 1) 
#
#print_insulating_layer(valve='1',nozzle='A',TorB='B')
#g.toggle_pressure(pressure_box)




#
# 
########PRINT ME SOME WIRES
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##pressure_clear(dwell_time = 1, pressure = 30, valve = 3)
#print_all_wires_no_stop(valve='2',nozzle='B',initial_dwell=0.2)
#g.toggle_pressure(pressure_box)

#
##
#######PRINT ME SOME INSULATING LAYERS ON TOP
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##pressure_clear(dwell_time = 4, pressure = 30, valve = 1)
#print_insulating_layer(valve='1',nozzle='A',TorB='T')
#g.toggle_pressure(pressure_box)



##########PRINT ME SOME SILVER ELECTRODES
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
##g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
##pressure_clear(dwell_time = 8, pressure = 40, valve = 4)
#print_electrodes(valve='1',nozzle='A')
#g.toggle_pressure(pressure_box)


##
##########PRINT ME SOME PDMS MICROGROOVES
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
#print_all_aligned_tops(valve='2',nozzle='B')
#g.toggle_pressure(pressure_box)
###########
###

###
##########PRINT ME SOME PDMS COVERS AND WELLS
set_home_in_z()
g.abs_move(x=automator.substrate_origins[active_slide]['A'][0]- 1.7, y=automator.substrate_origins[active_slide]['A'][1]- 2)
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####

g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ac')
g.set_home(x=0, y=0)
#
g.toggle_pressure(pressure_box)
#pressure_clear(dwell_time = 1, pressure = 40, valve = 1)
print_all_covers(nozzle = 'C', valve = 3)
print_all_single_wells(layer_height = 0.35, layer_increments=5, total_increments=6, pressure=35, speed=22, nozzle = 'C', valve = 3)
#print_ID(pressure=24,speed=25,nozzle='C',valve=3,dwell=0.4)
g.toggle_pressure(pressure_box)

g.teardown()


