from mecode import G
import numpy as np

outfile = r"/Volumes/jlewis/User Files/Valentine/AFRL/my_print.pgm"


g=G(
    direct_write=False,
    #outfile=outfile,
    #header=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterheader.txt",
    #footer=r"/Users/alex/alexvalentine/AFRL-printing/mymegacasterfooter.txt",
    print_lines=True,
    aerotech_include=False,
)


pressure_box = 16  #megacaster pressure box com port

pressure = 55    #pressure needed for AG-TPU ink with 100um nozzle + high pressure adapter

#def square_base(length, height, connections, layer_height, theta = 45):
#    base_extra = height/np.tan(theta)  # x component of slope
#
#    base_length = length + 2*base_extra
#    
#    layers = height/layer_height
#    layers = int(round(layers))
#    
#    for i in range(layers):
#        if i==0:
#            g.meader(base_length, base_length, spacing=0.1,start='UL')
#            g.move(x = , y = , z = height)
#        elif i%2==1:
#            
#        else:
            

pad_positions=((0.1,0.38+0.28*0),(.1,0.38+0.28*1),(.1,0.38+0.28*2),(.1,0.38+0.28*3),(.1,0.38+0.28*4),(.1,0.38+0.28*5),
(0.38+0.28*0,2.06),(0.38+0.28*1,2.06),(0.38+0.28*2,2.06),(0.38+0.28*3,2.06),(0.38+0.28*4,2.06),(0.38+0.28*5,2.06),
(2.06,0.38+0.28*5),(2.06,0.38+0.28*4),(2.06,0.38+0.28*3),(2.06,0.38+0.28*2),(2.06,0.38+0.28*1),(2.06,0.38+0.28*0),
(0.38+0.28*5,0.1),(0.38+0.28*4,0.1),(0.38+0.28*3,0.1),(0.38+0.28*2,0.1),(0.38+0.28*1,0.1),(0.38+0.28*0,0.1))

#coordinates of the center of all contact pads, starting in LL corner and going clockwise
#24 pads, 6 on each side


ATMEGA328_pad_positions = (

((0.2,7.3),(0.2,6.5),(0.2,5.7),(0.2,4.9),(0.2,4.1),(0.2,3.3),(0.2,2.5),(0.2,1.7)),
((1.7,0.2),(2.5,0.2),(3.3,0.2),(4.1,0.2),(4.9,0.2),(5.7,0.2),(6.5,0.2),(7.3,0.2)),
((8.8,1.7),(8.8,2.5),(8.8,3.3),(8.8,4.1),(8.8,4.9),(8.8,5.7),(8.8,6.5),(8.8,7.3)),
((7.3,8.8),(6.5,8.8),(5.7,8.8),(4.9,8.8),(4.1,8.8),(3.3,8.8),(2.5,8.8),(1.7,8.8))

)



def first_print():

    #11 layers - 1 base + 10 notched
    #g.move(5)
    
    
    g.feed(3)
    
    #base layer (1)
    g.meander(4.4,4.4,0.1)
    
    #next layer (2)
    g.move(-0.1,-0.1,0.08)
    
    #second layer fill (2)
    g.meander(4.2,4.1,0.1,start="UR")
    
    
    #first line of notches (2)
    g.move(y=-0.1)
    g.move(-1.4)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.4)
    
    #next layer (3)
    g.move(0.1,0.1,0.08)
    
    #second line of notches (3)
    g.move(1.3)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.3)
    g.move(y=0.1)
    
    #third layer fill (3)
    g.meander(4,3.9,0.1,start="LR")
    
    #next layer (4)
    g.move(-0.1,-0.1,0.08)
    
    #fourth layer fill (4)
    g.meander(3.8,3.7,0.1,start="UR")
    
    #third line notches (4)
    g.move(y=-0.1)
    g.move(-1.2)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.2)
    
    #next layer (5)
    g.move(0.1,0.1,0.08)
    
    #fourth line notches (5)
    
    g.move(1.1)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.1)
    g.move(y=0.1)
    
    #fifth layer fill (5)
    g.meander(3.6,3.5,0.1,start="LR")
    
    #next layer (6)
    g.move(-0.1,-0.1,0.08)
    
    #sixth layer fill (6)
    g.meander(3.4,3.3,0.1,start="UR")
    
    #fifth line notches (6)
    g.move(y=-0.1)
    g.move(-1)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1)
    
    #next layer (7)
    g.move(0.1,0.1,0.08)
    
    #sixth line notches (7)
    g.move(0.9)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.9)
    g.move(y=0.1)
    
    #seventh layer fill
    g.meander(3.2,3.1,0.1,start="LR")
    
    #next layer (8)
    g.move(-0.1,-0.1,0.08)
    
    #eigth layer fill
    g.meander(3,2.9,0.1,start="UR")
    
    #seventh line notches
    g.move(y=-0.1)
    g.move(-0.8)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-0.8)
    
    #next line (9)
    g.move(0.1,0.1,0.08)
    
    #eigth line notches (9)
    g.move(0.7)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.7)
    g.move(y=0.1)
    
    #ninth layer fill (9)
    g.meander(2.8,2.7,0.1,start="LR")
    
    #next line (10)
    g.move(-0.1,-0.1,0.08)
    
    #tenth layer fill (10)
    g.meander(2.6,2.5,0.1,start="UR")
    
    #ninth line notches (10)
    g.move(y=-0.1)
    g.move(-0.6)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-1.0)
    g.move(y=0.1)
    g.move(-0.2)
    g.move(y=-0.1)
    g.move(-0.6)
    
    #next line (11)
    g.move(0.1,0.1,0.08)
    
    #tenth line notches(11)
    g.move(0.5)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(1.0)
    g.move(y=0.1)
    g.move(0.2)
    g.move(y=-0.1)
    g.move(0.5)
    g.move(y=0.1)
    
    #eleventh layer fill
    g.meander(2.4,2.3,0.1,start="LR")

    #g.move(3,3,3)

   
      
         
def MGH_print():
    #----print 4 electrodes 
    #g.set_home(x=0,y=0)
    #g.abs_move(x=3,y=24)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=18)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=12)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=3,y=6)
    #g.move(z=-5)
    #g.meander(x=3,y=3,spacing=0.3,start='UL')
    #g.move(z=5)
    #g.abs_move(x=0,y=0)

    #----print TPU around electrodes
    #g.move(z=-5)
    #g.meander(x=30,y=3,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(x=-3)
    #g.move(y=0.3)
    #g.meander(x=27,y=2.1,spacing=0.3,start='LL')
    #g.move(y=0.3)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=12.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=15.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=18.3)
    #g.move(z=-5)
    #g.meander(x=27,y=2.4,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=21.)
    #g.move(z=-5)
    #g.meander(x=24,y=3,spacing=0.3,start='LR')
    #g.move(z=5)
    #g.abs_move(x=30,y=24.3)
    #g.move(z=-5)
    #g.meander(x=27,y=3,spacing=0.3,start='LR')
    #g.move(x=-0.3)
    #g.meander(x=2.7,y=24,spacing=0.3,start='UR',orientation='y')
    #g.move(z=5)

    #----print leads
#    g.abs_move(x=4.5,y=22.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#    
#    g.abs_move(x=4.5,y=16.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=-1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=10.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=1.75)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)
#
#    g.abs_move(x=4.5,y=4.5)
#    g.move(z=-4.7)
#    g.move(x=6)
#    g.move(x=3,y=5.5)
#    g.move(y=0.5)
#    g.meander(x=2,y=1,spacing=0.3,start='UL')
#    g.move(z=4.7)


    #----print TPU cover
    g.abs_move(x=0,y=0)
    g.move(z=-4.4)
    g.meander(x=30,y=9.2,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.3)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=2.1)
    g.move(y=0.3)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LR')
    g.move(z=4.4)
    g.move(x=-15.5,y=0.3)
    g.move(z=-4.4)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(x=-13.4,y=0.2)
    g.move(z=-4.4)
    g.meander(x=15.5,y=0.8,spacing=0.3,start='LL')
    g.move(y=0.3)
    g.meander(x=13.4,y=1,spacing=0.3,start='LL')
    g.move(x=-13.4)
    g.meander(x=30,y=10,spacing=0.3,start='LL')
    g.move(z=4.4)
    g.move(y=-10.3)
    g.move(z=-4.4)
    g.meander(x=14.5,y=8,spacing=0.3,start='UR')
    

    g.move(z=3)

def print_die():
    #g.abs_move(x=0,y=0)
    #g.abs_move(x=0.38,y=0.1)
    #g.move(x=0.1,y=0.1)
    #g.rect(x=0.2,y=0.2)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='LL',orientation='y')
    #g.move(x=-0.1) #x=380,y=200
    #
    #g.move(y=0.18) 
    #g.move(x=-0.18)
    #
    #g.move(y=0.1)
    #g.meander(x=0.2,y=0.2,spacing=0.05,start='UR',orientation='y')
    #g.clip(axis='z',direction='-x',height=1 )

    for i in np.arange(2):
        for j in np.arange(6):
            if i==0:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                g.move(z=-0.5)
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
                else:
                    g.move(y=pad_positions[12+j][1]-pad_positions[23-j][1])
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
            else:
                g.move(z=0.5)
                g.abs_move(x=pad_positions[6+j][0],y=pad_positions[6+j][1])
                g.move(z=-0.5)
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
                else:
                    g.move(y=-(pad_positions[12+j][1]-pad_positions[23-j][1]))
                    g.move(x=-(pad_positions[23-j][0]-pad_positions[12+j][0]))
                    g.move(x=0.025,y=0.025)
                    g.rect(x=0.05,y=0.05,start='UR')
                    g.move(x=0.05,y=0.05)
                    g.rect(x=0.15,y=0.15,start='UR')
                    g.move(x=-0.075,y=-0.075)
    g.move(z=0.5)
    
    
def print_die_wiring():
    g.move(z=-0.5)
    for i in np.arange(2):        
        for j in np.arange(6):
                if i==0:
                    g.move(z=0.5)
                    g.abs_move(x=pad_positions[23-j][0],y=pad_positions[23-j][1])
                    g.move(z=-0.5)
                    g.move(y=-3)
                    if j<3:
                        g.move(x=-3/(j+1),y=-3)
                    else:
                        g.move(x=(j+1)-3,y=-3)
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
    g.move(z=0.5)    
    
##third line of notches
#g.move(0.1,0.1,0.1)
#g.move(1)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1.0)
#g.move(y=0.1)
#g.move(0.2)
#g.move(y=-0.1)
#g.move(1)
#g.move(y=0.1)
#
##third layer of fill
#g.meander(4.,3.9,0.1,start="LR")
#
#g.move(-0.1,-0.1,0.1)
#
##fourth layer of fill
#g.meander(3.8,3.7,0.1,start="UR")
#



#g.move(-0.1,-0.1,0.1)
#g.meander(4.2,4.2,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(4,4,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.8,3.8,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.6,3.6,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.4,3.4,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(3.2,3.2,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(3.,3.,0.1,start='UR')
#g.move(0.1,0.1,0.1)
#g.meander(2.8,2.8,0.1)
#g.move(-0.1,-0.1,0.1)
#g.meander(2.6,2.6,0.1,start='UR')
#g.move(0.1,0.1,0.1)

#g.move(-1.1,-1.1,1)
#g.meander(2.4,2.4,0.1,start='UR')


#
#g.set_home(x=0, y=0, z=0)
##
#g.set_pressure(pressure_box, pressure)
#g.toggle_pressure(pressure_box)
#first_print()
#MGH_print()
#g.toggle_pressure(pressure_box)

def arduino_gen1(valve,nozzle,height,speed,dwell,pressure,testline,startx,starty):
    g.feed(25)
    g.set_pressure(pressure_box, pressure)
   
    #if testline == 'y':
    #    #########test line
    #    g.abs_move(x=2,y=3.5)
    #    #pressure_purge(delay = 2)
    #    g.abs_move(**{nozzle:height})
    #    if valve is not None:
    #        g.set_valve(num = valve, value = 1)
    #    g.dwell(dwell)
    #    g.feed(speed)
    #    g.move(x=15)
    #    g.feed(20)
    #    g.clip(axis=nozzle, height=2, direction='-x')
    #    #########test line
    

    g.write("POSOFFSET CLEAR X Y")    
    g.abs_move(x=startx,y=starty) ####bottom left corner of TPU square
    g.set_home(x=-6.5,y=-6.5)
    
        
    
    ###### RESET WIRE, PIN 29
    
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=-3,y=-3)
    g.move(x=-3)
    g.move(x=-0.3,**{nozzle:1})
    g.move(x=-0.3,**{nozzle:-1})
    g.abs_move(x = ATMEGA328_pad_positions[3][4][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][4][1])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')

    ###### VCC WIRE, PIN 4
    #
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height+0.04})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)
    g.move(x=-3,y=-3)
    g.move(x=-1,y=-1,**{nozzle:-0.04})    
    g.move(x=-4,y=-4)
    g.abs_move(y = ATMEGA328_pad_positions[0][3][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][3][0])
    g.move(x=-2)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    #
    ##### Rx WIRE, PIN 30
    #
    g.abs_move(x = ATMEGA328_pad_positions[3][5][0], y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.abs_move(y = ATMEGA328_pad_positions[3][5][1])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
    
    
    #### Tx WIRE, PIN 30
    
    g.abs_move(x=-4,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=3,y=-3)
    g.abs_move(x = ATMEGA328_pad_positions[3][6][0])
    g.abs_move(y = ATMEGA328_pad_positions[3][6][1])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+y')
    
    
    ##### GND WIRE (LED), PIN 17
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(x=-2)
    g.move(y=1)
    g.move(y=0.8,**{nozzle:1})
    g.move(y=0.8,**{nozzle:-1})
    g.move(y=1)
    g.move(y=0.3,**{nozzle:1})
    g.move(y=0.3,**{nozzle:-1})
    g.abs_move(y = ATMEGA328_pad_positions[2][0][1])
    g.abs_move(x = ATMEGA328_pad_positions[2][0][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='+x')
    

    ##### GND WIRE (cap, half of oscillator), PIN 20, 5, 7
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height+0.04})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(1,**{nozzle:-0.04})
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.abs_move(y = ATMEGA328_pad_positions[0][4][1])
    g.move(x=-10)
    g.move(x=-0.8,**{nozzle:1})
    g.move(x=-0.8,**{nozzle:-1})
    g.move(x=-1)
    g.move(y=-0.8)
    g.move(x=2.5)
    g.abs_move(y = ATMEGA328_pad_positions[0][6][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][6][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')


    ##### GND WIRE (other cap, other half of oscillator), PIN 8
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height+0.08})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-1.5,y=1.5)
    g.move(1,**{nozzle:-0.04})
    g.abs_move(y = ATMEGA328_pad_positions[2][4][1])
    g.move(x=-5)
    g.move(y=-2,**{nozzle:-0.04})
    g.move(x=-4)
    g.abs_move(x=-1,y=-1)
    g.move(x=-1)
    g.move(x=-0.8,**{nozzle:1})
    g.move(x=-0.8,**{nozzle:-1})
    g.move(x=-1)
    g.move(y=2.6)
    g.move(y=-0.8)
    g.move(x=4)
    g.abs_move(y = ATMEGA328_pad_positions[0][7][1])
    g.abs_move(x = ATMEGA328_pad_positions[0][7][0])
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')

    ##### Tx terminal

    g.abs_move(x=-4,y=13.5)
    g.abs_move(**{nozzle:height+0.09})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')


    ##### Rx terminal

    g.abs_move(x = ATMEGA328_pad_positions[3][5][0], y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')



    #### VCC terminal
    
    g.abs_move(x=13.5,y=13.5)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')
    
    
    ##### GND WIRE (LED), PIN 17
    
    g.abs_move(x=13.5,y=-4)
    g.abs_move(**{nozzle:height})
    g.feed(speed)
    if valve is not None:
        g.set_valve(num = valve, value = 1)
    g.dwell(dwell)  
    g.move(x=-0.75,y=-0.75)
    g.rect(x=1.5,y=1.5)
    g.set_valve(num = valve, value = 0)
    g.feed(15)
    g.clip(axis=nozzle, height=2,direction='-x')



arduino_gen1(valve='1',nozzle='z',height=0.05,speed=4,dwell=0.1,pressure=23,startx=420.766728,starty=108.626399,testline='y')



g.view(backend='matplotlib')

g.teardown()

