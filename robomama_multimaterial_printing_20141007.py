from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator


#Location of written GCode file generated from this script
outfile = r"C:\Users\Lewis Group\Documents\GitHub\aerotech_automation\alexs_print.pgm"

#List of axes used for printing - comment out the axes not being used
AXES_USED = ['A',
         #   'B',
           # 'C', 
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
        'origin': (140,100),
        'size': 'auto',
        'profile': True,
        'profile-spacing': (40,40),
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
cant_y_translate = 2.5
#Defining positions of all 16 cantilevers as the top left (first 8 sensors) or bottom left (last 8 sensors) corner of cantilever, offest from extra and inset
cantilever_position = ((11.93, 33.9 + cant_y_translate), (17.68, 33.9+ cant_y_translate), (25.43, 33.9+ cant_y_translate), (31.18, 33.9+ cant_y_translate), (38.93, 33.9+ cant_y_translate), (44.68, 33.9+ cant_y_translate), (52.43, 33.9+ cant_y_translate), (58.18, 33.9+ cant_y_translate),
                       (11.93, 15.55 - cant_y_translate), (17.68, 15.55 - cant_y_translate), (25.43, 15.55 - cant_y_translate), (31.18, 15.55 - cant_y_translate), (38.93, 15.55 - cant_y_translate), (44.68, 15.55 - cant_y_translate), (52.43, 15.55 - cant_y_translate), (58.18, 15.55 - cant_y_translate))

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
           
wire_height=(0.03,)*8#(0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04, 0.04,
            # 0.03, 0.03, 0.03, 0.03, 0.02, 0.02, 0.02, 0.02)
wire_pressure=(5.5,)*8#(23,)*16#(7.8,)*8#(68,)*16+(68,)*4+(68,)*4

wire_speed = (7.5,)*8#+(4,)*4+(3.75,)*4+(4,)*4 #(2, 2, 2, 2, 2, 2, 2, 2,
            #2, 2, 2, 2, 2, 2, 2, 2)
                
                                                       #(7,3) (6,5)                                       

insulating_meand_spacing_top = 0.21
insulating_meand_spacing_bot = 0.21

insulating_height_top = (0.045,)*16
insulating_height_bot = (0.015,)*16

insulating_pressure_top = (3.5,)*16
insulating_pressure_bot = (3.5,)*16
                                        
insulating_speed_top = (15,)*16
insulating_speed_bot = (15,)*16



 
              
align_top_pressure=(17,)*16
top_over=(0.06,)*4+(0.07,)*4+(0.080,)*4+(0.090,)*4
top_height=(0.710,)*16 
top_speed=(3,)*16



cantilever_width = 3.5
cantilever_bending_length = 5.5
cantilever_length = cantilever_bending_length + cant_y_translate

trans_speed = 40


cover_pressure=(15,)*8
#
inset=(cantilever_width-wire_width)/2


#######SILVER TPU?
#electrode_height=0.150
#electrode_pressure = 6

##############TRAVIS"S INKS
electrode_height=0.190
electrode_pressure = 10






#ORIGIN OF PRINTING AREA IS DEFINED AS BOTTOM LEFT CORNER OF SUBSTRATE (glass 2"x3")

zA  = zB = zC = zD =0

pressure_box = 4       # COM port of pressure box    

silver_pressure = 20        #pressure for Ag-TPU syringe

tpu_pressure = 0.3           #pressure for TPU syringe

pressure_250 = 17        #pressure for Ag-TPU syringe (250 micron tip)
silver_pressure_50 = 25        #pressure for Ag-TPU syringe (50 micron tip)
silver_pressure_100 = 0.3               #pressure for Ag-TPU syringe (100 micron tip)
silver_pressure_30 = 5               #pressure for Ag-TPU syringe (30 micron tip)



tpu_pressure = 4.5           #pressure for TPU syringe

pdms_pressure = 27            #pressure for PDMS syringe

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

    

#coordinates of the center of all contact pads, in a dummy die starting in LL corner 
#and going clockwise 24 pads, 6 on each side

pyramid_positions=((0,0),(0,19.4-6),(0,38.8-12),(-19.4+6,19.4-6),(19.4-6,19.4-6))

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
    for i in range(1,8,2):
        g.feed(15)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1]-y_inset -0.5)
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=-(cantilever_length-y_inset), spacing=over,
                        z=height, tail = 1, clip_direction = '-y', speed=trace_speed, 
                        orientation = 'y', nozzle = nozzle, valve = None)
    
    for i in range(9,16,2):
        
        g.feed(15)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] +0.5 + y_inset)
        g.move(x=-overhang)
        meander_2tails(x=(cantilever_width + 2*overhang), y=(cantilever_length - y_inset), spacing=over, 
                    z=height, tail = 1, clip_direction = '+y', speed=trace_speed, 
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
    print length
    print y_move
    print 'length_ymove'
    g.feed(speed)
    g.abs_move(**{nozzle:z})
    g.move(x=tail)
    g.move(y=y_move)    
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=-y_move)
    space = cantilever_position[1][0] - cantilever_position[0][0]
    g.move(x=(space-width))
    g.move(y=y_move)
    g.arc(x = width, y=0, direction = arc_direction , radius = (width/2))
    g.move(y=-y_move)
    g.move(x=tail)

   
   

def print_all_wires_no_stop(valve, nozzle):
    width = wire_width
    inset = (cantilever_width-width)/2
    g.feed(20)
    g.abs_move(*cantilever_position[0])#cantilever_position[0][0]
    g.move(x=(-tail+inset), y=extra)
    g.abs_move(**{nozzle:wire_height[0]})
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.feed(8)
    g.set_pressure(pressure_box, wire_pressure[0])
    for i in range(0,8,2):
        j=i/2
        g.abs_move(cantilever_position[i][0]+(-tail+inset), y = cantilever_position[i][1]+extra)
        print_wires_no_stop(z=wire_height[j], speed=wire_speed[j], extra = extra,
            tail = 1.5, width = 1.55, length=(cantilever_length - 0.75), valve = valve, nozzle = nozzle, clip_direction = '+y', k=j, arc_direction = 'CCW')
    g.set_valve(num = valve, value = 0)
    g.feed(20)       
    g.abs_move(**{nozzle:20})
    
    g.abs_move(*cantilever_position[8])
    g.set_pressure(pressure_box, wire_pressure[0])
    g.move(x=(-tail+inset), y=extra)
    g.abs_move(**{nozzle:wire_height[4]})
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.feed(8)        
    for i in range(8,16,2):
        j=i/2
        g.abs_move(cantilever_position[i][0]+(-tail+inset), y = cantilever_position[i][1]-extra)
        print_wires_no_stop(z=wire_height[j], speed=wire_speed[j], extra = extra, 
            tail = 1.5, width = 1.55, length=-(cantilever_length - 0.75), valve = valve, nozzle = nozzle, clip_direction = '-y', k=j, arc_direction = 'CW')
    g.set_valve(num = valve, value = 0)
    g.feed(20)          
    g.abs_move(**{nozzle:50})  

def meander_tops(x, y, start, spacing, z, speed, nozzle, clip_direction, valve, orientation = 'y'):   
    g.feed(15)
    g.abs_move(**{nozzle:z})
    g.feed(speed)
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.meander(x=x, y=y, spacing=spacing, orientation = 'y', tail = False, start=start)
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction=clip_direction, height=5) 


def print_all_aligned_tops(nozzle, valve):
    g.set_pressure(pressure_box, align_top_pressure[1])
    pressure_purge(delay = 1.5)
    y_translation = cant_y_translate
    #for i in range(1,8,2):
    #    g.feed(15)
    #    g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] - y_translation +0.5)
    #    g.move(x=-0.1)
    #    g.set_pressure(pressure_box, align_top_pressure[i])
    #    pressure_purge(delay = 0.5)
    #    meander_tops(x=(cantilever_width + 0.1), y=cantilever_length - y_translation +0.5, start='UL', spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)
    
    for i in range(9,16,2):
        g.feed(15)
        g.abs_move(x=cantilever_position[i][0], y=cantilever_position[i][1] + y_translation -0.5)
        g.move(x=-0.1)
        g.set_pressure(pressure_box, align_top_pressure[i])
        pressure_purge(delay = 0.5)
        meander_tops(x=(cantilever_width + 0.1), y=cantilever_length - y_translation +0.5, start='LL',spacing=top_over[i], z=top_height[i], speed=top_speed[i], orientation = 'y', nozzle = nozzle, clip_direction = '+y', valve = valve)


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
    g.dwell(0.25)
    g.meander(x=length, y=height, spacing = over, start=start, orientation = 'x')
    g.set_valve(num = valve, value = 0)          

def print_all_covers(nozzle = 'A', valve = 0):
    for i in range(0,4):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] + 14))
        g.move(x=0.5, y=-0.5)
        g.abs_move(**{nozzle:0.23})
        print_cover(z=0.3, height=4.9, length = 11.5, over = 0.41, speed = 8, pressure = cover_pressure[i], start='UL',valve = valve)
        g.clip(axis=nozzle, direction='-y', height=5)

    
    
    for i in range(4,8):
        
        g.feed(15)
        g.abs_move(x=well_position[i][0], y=(well_position[i][1] -14))
        g.move(x=0.5, y=0.5)
        g.abs_move(**{nozzle:0.23})
        print_cover(z=0.3, height=4.9, length = 11.5, over = 0.41, speed = 8, pressure = cover_pressure[i], start='LL', valve = valve)
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


def print_all_single_wells(layer_height, layer_increments, total_increments, pressure, speed, nozzle, valve):
    
    for i in range(0,4):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.15})
        print_single_well(x = 12.5, y = -14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
        g.clip(axis=nozzle, direction='+y', height=3)
        #g.move(A=3)
    
    for i in range(4,8):      
        g.feed(15)
        g.abs_move(*well_position[i])
        g.abs_move(**{nozzle:0.15})
        print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
        g.clip(axis=nozzle, direction='-y', height=3)
        #g.move(A=3) 
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
            #g.move(A=3)
        for i in range(4,8):      
            g.feed(15)
            g.abs_move(*well_position[i])
            g.abs_move(**{nozzle:0.15+count*layer_height})
            print_single_well(x = 12.5, y = 14, layer_height = layer_height ,  layers = layer_increments, speed = speed, pressure = pressure, filament = 1, valve = valve, nozzle = nozzle)
            g.clip(axis=nozzle, direction='-y', height=3)

def print_insulating_layer(nozzle, valve, TorB):
    dwell = 0.2
    if TorB == 'T':
        speed = insulating_speed_top
        height = insulating_height_top[0]
        pressure = insulating_pressure_top
        spacing = insulating_meand_spacing_top 
        y_translation = cant_y_translate
        
    else:
        speed = insulating_speed_bot
        height = insulating_height_bot[0]
        pressure = insulating_pressure_bot
        spacing = insulating_meand_spacing_bot
        y_translation = 0
    
    g.feed(25)
    g.set_pressure(pressure_box, pressure[1])             
    pressure_purge(delay = 0.5)
    g.abs_move(cantilever_position[0][0]-3, cantilever_position[0][1] - y_translation)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed[0])

    for i in range(0,8):
        g.abs_move(cantilever_position[i][0], cantilever_position[i][1] - y_translation)
        meander_nostop(x=cantilever_width, y=-(cantilever_length - y_translation), spacing=spacing, orientation = 'y', speed=speed[i])            
                    
    g.move(x=3)
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
    
    g.abs_move(cantilever_position[8][0]-3, cantilever_position[8][1] + y_translation)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed[0])       
   
    for i in range(8,16):
        g.abs_move(cantilever_position[i][0], cantilever_position[i][1] + y_translation)
        meander_nostop(x=cantilever_width, y=cantilever_length - y_translation, spacing=spacing, orientation = 'y', speed=speed[i])

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
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]-extra + silver_inset))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset), y=(cantilever_position[j][1]+extra - silver_inset))
            g.move(x=-0.5)
            g.abs_move(*pin_position[i])
            g.move(x=0.6)
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
            g.feed(5)
            if  i>15:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]-extra + silver_inset))
            else:
                g.abs_move(x=(cantilever_position[j][0] + inset + wire_width), y=(cantilever_position[j][1]+extra - silver_inset))
            g.move(x=0.5)
            g.abs_move(*pin_position[i]) 
            g.move(x=0.6)
            g.arc(x=0,y=0.00001,radius=-0.6)
            g.set_valve(num = valve, value = 0)
            g.clip(axis=nozzle, direction=myclip, height=5)


def print_die(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=32,y=13)
    g.set_home(x=0,y=0)
    pressure_purge(delay = 2)
    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.abs_move(**{nozzle:5})
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.abs_move(**{nozzle:height})
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                if j==0:
                    g.dwell(1.7)
                else:
                    g.dwell(dwell)
                g.feed(speed)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.075,y=-0.075)
                if j<3:
                    g.move(y=pad_positions[j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.075,y=0.075)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.075,y=0.075)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')
            else:
                g.abs_move(**{nozzle:5})
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.abs_move(**{nozzle:height})
                if valve is not None:
                    g.set_valve(num = valve, value = 1)
                g.dwell(dwell)
                g.feed(speed)
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.075,y=-0.075)
                if j<3:
                    g.move(y=-(pad_positions[j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.075,y=0.075)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.075,y=0.075)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')

def print_die_wiring(valve,nozzle,height,speed,dwell,pressure):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    pressure_purge(delay = 2)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.move(x=(j+1)-3,y=-3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                else:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.move(x=(j+1)-3,y=3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.move(x=-3,y=(j+1)-3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                else:
                    g.abs_move(**{nozzle:5})
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.abs_move(**{nozzle:height})
                    if valve is not None:
                        g.set_valve(num = valve, value = 1)
                    g.dwell(dwell)
                    g.feed(speed)
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)
                    else:
                        g.move(x=3,y=(j+1)-3)
                        g.set_valve(num = valve, value = 0)
                        g.feed(15)
                        g.clip(axis=nozzle, height=5)


def pyramids():

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[2][0],y=pyramid_positions[2][1])
    g.move(z=-3)
    
    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)
    
    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)
    g.abs_move(x=pyramid_positions[4][0],y=pyramid_positions[4][1])
    g.move(z=-3)

    for i in np.arange(10):
        if i%2==0:
            start1='LL'
            num=-1            
        else:
            start1='UR'
            num=1
        g.meander(4.4-(i*0.2),4.4-(i*0.2),0.1,start=start1)
        g.move(x=0.1*num,y=0.1*num,z=0.1)

    g.move(x=-3.6,y=3.4,z=2)

def serp_wires_pyramids():
    g.abs_move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[3][0],y=pyramid_positions[3][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)

    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=1.55,y=3.2)
    g.move(z=-2.05)
    g.move(y=0.3)
    g.move(y=0.95,z=-0.95)
    
    g.move(y=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=0.4,radius=-0.3,direction=dir)
    g.move(y=0.45)
    g.move(y=0.95,z=0.95)
    g.move(y=0.3)
    g.move(z=2.05)
   
    g.move(x=1.3)
    g.move(z=-2.05)
    g.move(y=-0.3)
    g.move(y=-0.95,z=-0.95)
    
    g.move(y=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0,y=-0.4,radius=-0.3,direction=dir)
    g.move(y=-0.45)
    g.move(y=-0.95,z=0.95)
    g.move(y=-0.3)
    g.move(z=2.05)


    g.abs_move(x=pyramid_positions[1][0],y=pyramid_positions[1][1])
    g.move(x=3.2,y=1.55)
    g.move(z=-2.05)

    g.move(x=0.3)
    g.move(x=0.95,z=-0.95)

    g.move(x=0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=0.45)
    g.move(x=0.95,z=0.95)
    g.move(x=0.3)
    g.move(z=2.05)
   
    g.move(y=1.3)
    g.move(z=-2.05)
    g.move(x=-0.3)
    g.move(x=-0.95,z=-0.95)
    
    g.move(x=-0.45)
    
    for i in np.arange(20):
        if i%2==0:
            dir='CW'
        else:
            dir='CCW'
        g.arc(x=-0.4,y=0,radius=-0.3,direction=dir)
    g.move(x=-0.45)
    g.move(x=-0.95,z=0.95)
    g.move(x=-0.3)
    g.move(z=2.05)



    g.move(x=20,y=20)


def SHORT_serpentine_encaps_pdms(nozzle,valve,pressure,speed,height):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=5,y=5)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(0.8)
    g.meander(x=10,y=12,spacing=0.35,start='LL',orientation='y')
    g.move(y=6)
    g.feed(speed/2)
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=2.5,y=0,radius=-1.7,direction=direc)
    g.move(x=2)
    g.feed(speed)
    g.move(y=6)
    g.meander(x=10,y=-12,spacing=0.35,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)


def LONG_serpentine_encaps_pdms(nozzle,valve,pressure,speed,height):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=5,y=5)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(0.8)
    g.meander(x=10,y=12,spacing=0.26,start='LL',orientation='y')
    g.move(y=6)
    g.feed(speed/1.6)
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.move(x=-2)
    g.feed(speed)
    g.move(y=6)
    g.meander(x=10,y=-12,spacing=0.25,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
      
def SHORT_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.3)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(x=2.5,y=0,radius=-1.7,direction=direc)
    g.move(x=5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)

def LONG_serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(1.7)
    g.meander(x=2,y=2,spacing=0.08,start='LL',orientation='y')
    g.move(y=1)
    g.move(x=5)
    g.abs_move(**{nozzle:height-0.04})  
    for i in np.arange(13):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=2.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=1.5,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=0,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-0.8,radius=-1.7,direction=direc)
    for i in np.arange(2):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=2.5,x=-1.5,radius=-1.7,direction=direc)
    for i in np.arange(4):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0.8,x=-2.5,radius=-1.7,direction=direc)
    for i in np.arange(13):
        if i%2==0:
            direc='CCW'
        else:
            direc='CW'
        g.arc(y=0,x=-2.5,radius=-1.7,direction=direc)
    g.abs_move(**{nozzle:height+0.04})  
    g.move(x=-5)
    g.move(y=-1)
    g.meander(x=2,y=2,spacing=0.08,start='LR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)







#################################### END OF FUNCTION DEFINITIONS #######################################



#################################### PRINTING - ALL FUNCTIONS CALLED HERE ############################
reference_nozzle = 'A'
active_slide = 'slide1'
z_ref = -88.11936
automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
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

##------------------PRINT ME ENCAPS SERPENTINE TEST (top)
set_home_in_z()
g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####


g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ab')
g.set_home(x=0, y=0)

g.toggle_pressure(pressure_box)
LONG_serpentine_encaps_pdms(nozzle='B',valve='2',pressure=22,speed=9,height=0.15+.24+.28)
g.toggle_pressure(pressure_box)

#------------------PRINT ME ENCAPS SERPENTINE TEST (wire)
#
set_home_in_z()
g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####


g.set_home(x=0, y=0)


g.toggle_pressure(pressure_box)   
LONG_serpentine_encaps_wire(nozzle='A',valve='1',pressure=30,speed=0.7,height=0.4-0.15+0.1)
g.toggle_pressure(pressure_box)


##------------------PRINT ME DIE AND WIRING
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
##g.abs_move(x=0, y=0)
##nozzle_change(nozzles = 'ab')
#g.set_home(x=0, y=0)
#
#g.toggle_pressure(pressure_box)
#print_die(valve='1',nozzle='A',height=0.015,speed=0.36,dwell=0.7,pressure=10)
#print_die_wiring(valve='1',nozzle='A',height=0.015,speed=0.6,dwell=0.7,pressure=16)
#
#g.toggle_pressure(pressure_box)


g.view(backend='matplotlib')

##
g.teardown()
