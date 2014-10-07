#---------------ROBOMAMA MULTIMATERIAL PRINTING------------------#

from mecode import G
import numpy as np
from aerotech_automator import AerotechAutomator

#Location of written GCode file generated from this script

outfile = r"C:\Users\Lewis Group\Desktop\Valentine\MY_PRINT_NOT_YOURS.pgm"


#List of axes used for printing - comment out the axes not being used
AXES_USED = ['A',
            'B',
           # 'C', 
          #  'D'
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
        'origin': (204.47,127.68),    # <- double check location of substrtate#
        'size': 'auto',
        'profile': True,
        'profile-spacing': (50,50),
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
    print_lines=True,
    aerotech_include=False,
    )

#---------------- VARIABLE AND PARAMTER DEFINITIONS ----------------#


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


#-------------------- FUNCTION DEFINITIONS -------------------------#
    
def set_home_in_z():
    g.write('POSOFFSET CLEAR A B C D')
    g.feed(25)
    g.abs_move(A=-2, B=-2, C=-2, D=-2)
    g.set_home(A=(-zA -2), B=(-zB -2), C = (-zC - 2), D=(-zD - 2))

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





def MGH_sensor(nozzle):
    g.set_pressure(pressure_box, electrode_pressure)
    g.abs_move(**{nozzle:electrode_height})
    g.set_valve(num = valve, value = 1)
    g.dwell(0.25)
    g.set_home(x=0,y=0)
    g.abs_move(x=1,y=9)
    g.move(z=-5)
    g.meander(x=10,y=10,spacing=0.3,start='UL')
    g.move(z=5)
    g.abs_move(x=1,y=7)
    g.move(z=-5)
    g.meander(x=10,y=10,spacing=0.3,start='UL')
    g.move(z=5)
    g.abs_move(x=1,y=5)
    g.move(z=-5)
    g.meander(x=10,y=10,spacing=0.3,start='UL')
    g.move(z=5)
    g.abs_move(x=1,y=7)
    g.move(z=-5)
    g.meander(x=10,y=10,spacing=0.3,start='UL')
    g.move(z=5)







#---------------- PRINTING - ALL FUNCTIONS CALLED HERE --------------------#



#------------------PRINT ME SOME SACRIFICIAL LAYERS

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



def print_silver_electrodes(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, silver_pressure)   
    g.feed(15)
    g.abs_move(x=3,y=24)
    pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=3,y=3,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    
   # g.abs_move(x=3,y=18)
   # g.abs_move(**{nozzle:height})
   # g.set_valve(num = valve, value = 1)
   # g.dwell(dwell)
   # g.feed(speed)
   # g.meander(x=3,y=3,spacing=0.19,start='UL')
   # g.set_valve(num = valve, value = 0)
   # g.feed(15)
   # g.clip(axis=nozzle, height=5)
   #
   # g.abs_move(x=3,y=12)
   # g.abs_move(**{nozzle:height})
   # g.set_valve(num = valve, value = 1)
   # g.dwell(dwell)
   # g.feed(speed)
   # g.meander(x=3,y=3,spacing=0.19,start='UL')
   # g.set_valve(num = valve, value = 0)
   # g.feed(15)
   # g.clip(axis=nozzle, height=5)
   #
   # g.abs_move(x=3,y=6)
   # g.abs_move(**{nozzle:height})
   # g.set_valve(num = valve, value = 1)
   # g.dwell(dwell)
   # g.feed(speed)
   # g.meander(x=3,y=3,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
   # g.feed(15)
   # g.clip(axis=nozzle, height=5)   
    g.abs_move(**{nozzle:30})

    
    
def print_tpu_base(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, tpu_pressure)   
    g.feed(15)
    g.abs_move(x=0,y=0)
    pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=30,y=3,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=24,y=3,spacing=0.3,start='LR')
    g.move(x=-3)
    g.move(y=0.3)
    g.meander(x=27,y=2.1,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=24,y=3,spacing=0.3,start='LR')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    
    g.abs_move(x=30,y=12.3)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    
    g.abs_move(x=30,y=15.)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=24,y=3,spacing=0.3,start='LR')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    
    g.abs_move(x=30,y=18.3)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)

    g.abs_move(x=30,y=21.)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=24,y=3,spacing=0.3,start='LR')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)

    g.abs_move(x=30,y=24.3)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=27,y=3,spacing=0.3,start='LR')
    g.move(x=-0.3)
    g.meander(x=2.7,y=24,spacing=0.3,start='UR',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    g.abs_move(**{nozzle:30})
    
    
def print_silver_wires(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, silver_pressure)   
    g.feed(15)
    g.abs_move(x=4.5,y=22.5)
    pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=6)
    g.move(x=3,y=-5.5)
    g.move(y=0.5)
    g.meander(x=2,y=1,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis='A', height=5, direction='+y')
    
      
    g.abs_move(x=4.5,y=16.5)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=6)
    g.move(x=3,y=-1.75)
    g.move(y=0.5)
    g.meander(x=2,y=1,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    
    g.abs_move(x=4.5,y=10.5)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=6)
    g.move(x=3,y=1.75)
    g.move(y=0.5)
    g.meander(x=2,y=1,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    

    g.abs_move(x=4.5,y=4.5)
    g.abs_move(**{nozzle:height})
    g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.move(x=6)
    g.move(x=3,y=5.5)
    g.move(y=0.5)
    g.meander(x=2,y=1,spacing=0.19,start='UL')
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=5)
    g.abs_move(**{nozzle:30})
    
def print_tpu_cover(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, tpu_pressure)   
    g.feed(15)
    g.abs_move(x=0,y=0)
    pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=30,y=27,spacing=0.3,start='LL',orientation='y')
    g.clip(axis=nozzle, height=5)
    g.abs_move(**{nozzle:30})

def print_pdms_cover(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, pdms_pressure)   
    g.feed(15)
    g.abs_move(x=0,y=0)
    pressure_purge(delay = 2)
    g.abs_move(**{nozzle:height})
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.feed(speed)
    g.meander(x=30,y=27,spacing=0.5,start='LL',orientation='y')
    g.clip(axis=nozzle, height=5)
    g.abs_move(**{nozzle:30})

def print_die(valve,nozzle,height,speed,dwell):
    g.set_pressure(pressure_box, silver_pressure_30)   
    g.feed(15)
    g.abs_move(x=0,y=0)
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
                g.move(x=0.075,y=0.075)
                g.rect(x=0.15,y=0.15,start='UR')
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=pad_positions[j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
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
                g.move(x=-0.05,y=-0.05)
                g.rect(x=0.05,y=0.05,start='UR')
                g.move(x=-0.025,y=-0.025)
                if j<3:
                    g.move(y=-(pad_positions[j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
                    g.set_valve(num = valve, value = 0)
                    g.feed(15)
                    g.clip(axis=nozzle, height=5, direction='-x')

def print_die_wiring():
    g.set_pressure(pressure_box, silver_pressure_50)   
    g.feed(15)
    g.abs_move(x=0,y=0)
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
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                    g.move(z=-0.5)
                    g.move(y=3)
                    if j<3:
                        g.move(x=-3/(j+1),y=3)
                    else:
                        g.move(x=(j+1)-3,y=3)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[j][0],y=pad_positions[j][1])
                    g.move(z=-0.5)
                    g.move(x=-3)
                    if j<3:
                        g.move(x=-3,y=-3/(j+1))
                    else:
                        g.move(x=-3,y=(j+1)-3)
                else:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[17-j][0],y=pad_positions[17-j][1])
                    g.move(z=-0.5)
                    g.move(x=3)
                    if j<3:
                        g.move(x=3,y=-3/(j+1))
                    else:
                        g.move(x=3,y=(j+1)-3)


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


    


def serpentine_encaps_pdms(nozzle,valve,pressure,speed,height):
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
    g.move(x=2)
    g.feed(speed/2)
    for i in np.arange(10):
        if i%2==0:
            direc='CW'
        else:
            direc='CCW'
        g.arc(y=0,x=2.5,radius=-1.7,direction=direc)
    g.feed(speed)
    g.move(x=2)
    g.move(y=6)
    g.meander(x=10,y=-12,spacing=0.35,start='LL',orientation='y')
    g.set_valve(num = valve, value = 0)
    g.clip(axis=nozzle, direction='-y', height=20)
      
def serpentine_encaps_wire(nozzle,valve,pressure,speed,height):    
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
    g.abs_move(x=10,y=10)
    g.abs_move(**{nozzle:height})  
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.feed(speed)
    g.dwell(0.3)
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



#---------------- PRINTING - ALL FUNCTIONS CALLED HERE --------------------#
reference_nozzle = 'A' 
z_ref = -81.352239
automator.load_state(r"C:\Users\Lewis Group\Desktop\Calibration\alignment_data.txt")
g.write("POSOFFSET CLEAR X Y U A B C D")

substrate_dif = automator.home_positions[reference_nozzle][2] - z_ref

if 'A' in AXES_USED:
    zA = automator.home_positions['A'][2] - substrate_dif
if 'B' in AXES_USED:
    zB = automator.home_positions['B'][2] - substrate_dif
if 'C' in AXES_USED:
    zC = automator.home_positions['C'][2] - substrate_dif
if 'D' in AXES_USED:
    zD = automator.home_positions['D'][2] - substrate_dif  
    
    
#------------------PRINT ME SILVER ELECTRODE PADS
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=-10, y=-10)
#
#g.toggle_pressure(pressure_box)   
#
#print_silver_electrodes(valve='1',nozzle='A',height=0.18,speed=6,dwell=1)
#
#g.toggle_pressure(pressure_box)


#------------------PRINT ME TPU BASE
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ab')
#g.set_home(x=-10, y=-10)
#
#g.toggle_pressure(pressure_box)   
#
#print_tpu_base(valve='2',nozzle='B',height=0.56,speed=20,dwell=0.6)
#
#g.toggle_pressure(pressure_box)


#------------------PRINT ME SILVER WIRES
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=-10, y=-10)
#
#g.toggle_pressure(pressure_box)   
#
#print_silver_wires(valve='1',nozzle='A',height=0.58,speed=4,dwell=1)
#
#g.toggle_pressure(pressure_box)


#------------------PRINT ME TPU COVER

#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ac')
#g.set_home(x=0, y=0)
#
#print_sacrificial_rect(trace_speed = 5, height = -0.015, over = 0.75, nozzle = 'C', overhang = 0)

#nozzle_change(nozzles = 'ab')
#g.set_home(x=-10, y=-10)
#
#g.toggle_pressure(pressure_box)   
#
#print_tpu_cover(valve='2',nozzle='B',height=1.4,speed=15,dwell=0.6)
#
#g.toggle_pressure(pressure_box)


#------------------PRINT ME PDMS COVER
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=0, y=0)
#
#g.abs_move(x=0, y=0)
#nozzle_change(nozzles = 'ac')
#g.set_home(x=-10, y=-10)
#
#g.toggle_pressure(pressure_box)   
#
#print_pdms_cover(valve='3',nozzle='C',height=4,speed=10,dwell=1.2)
#
#g.toggle_pressure(pressure_box)

#------------------PRINT ME SILVER TPU DUMMY DIE
#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
#g.set_home(x=-10, y=-10)
##
###g.abs_move(x=0, y=0)
###nozzle_change(nozzles = 'ac')
###g.set_home(x=-10, y=-10)
##
#g.toggle_pressure(pressure_box)   
##
#print_die(valve='1',nozzle='A',height=0.008,speed=0.4,dwell=0.5)
##
#g.toggle_pressure(pressure_box)


#------------------PRINT ME ENCAPS SERPENTINE TEST (top)
set_home_in_z()
g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
###^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####


g.set_home(x=0, y=0)

g.abs_move(x=0, y=0)
nozzle_change(nozzles = 'ab')
g.set_home(x=0, y=0)

g.toggle_pressure(pressure_box)   
serpentine_encaps_pdms(nozzle='B',valve='2',pressure=20,speed=9,height=0.4)
g.toggle_pressure(pressure_box)

#------------------PRINT ME ENCAPS SERPENTINE TEST (wire)

#set_home_in_z()
#g.abs_move(x=automator.substrate_origins['slide1']['A'][0], y=automator.substrate_origins['slide1']['A'][1])
####^^^ ONLY RUN THIS LINE IF THIS IS THE FIRST MATERIAL TO BE PRINTED AFTER PROFILING#####
#
#
#g.set_home(x=0, y=0)
#
#
#g.toggle_pressure(pressure_box)   
#serpentine_encaps_wire(nozzle='A',valve='1',pressure=15,speed=4,height=0.05)
#
#g.view(backend='matplotlib')
#
g.teardown()

