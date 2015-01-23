
############### VARIABLE AND PARAMTER DEFINITIONS ###############

#ORIGIN OF PRINTING AREA IS DEFINED AS BOTTOM LEFT CORNER OF SUBSTRATE (glass 2"x3")

zA  = zB = zC = zD =0
cant_y_translate = 2.5
#Defining positions of all 16 cantilevers as the top left (first 8 sensors) or bottom left (last 8 sensors) corner of cantilever, offest from extra and inset
cantilever_position = ((11.93, 33.9 + cant_y_translate), (17.68, 33.9+ cant_y_translate), (25.43, 33.9+ cant_y_translate), (31.18, 33.9+ cant_y_translate), (38.93, 33.9+ cant_y_translate), (44.68, 33.9+ cant_y_translate), (52.43, 33.9+ cant_y_translate), (58.18, 33.9+ cant_y_translate),
                       (11.93, 15.55 - cant_y_translate), (17.68, 15.55 - cant_y_translate), (25.43, 15.55 - cant_y_translate), (31.18, 15.55 - cant_y_translate), (38.93, 15.55 - cant_y_translate), (44.68, 15.55 - cant_y_translate), (52.43, 15.55 - cant_y_translate), (58.18, 15.55 - cant_y_translate))

#cantilever_position = ((11.93, 33.9 + cant_y_translate), (17.68-2, 33.9+ cant_y_translate), (25.43, 33.9+ cant_y_translate), (31.18-2, 33.9+ cant_y_translate), (38.93, 33.9+ cant_y_translate), (44.68-2, 33.9+ cant_y_translate), (52.43, 33.9+ cant_y_translate), (58.18-2, 33.9+ cant_y_translate),
#                       (11.93, 15.55 - cant_y_translate), (17.68, 15.55 - cant_y_translate), (25.43, 15.55 - cant_y_translate), (31.18, 15.55 - cant_y_translate), (38.93, 15.55 - cant_y_translate), (44.68, 15.55 - cant_y_translate), (52.43, 15.55 - cant_y_translate), (58.18, 15.55 - cant_y_translate))



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
        
wire_height=(0.025,)*8

wire_pressure=(7.5,)*8

wire_speed = (10,)*8
                
                                                                                            

insulating_meand_spacing_top = 0.13
insulating_meand_spacing_bot = 0.13

insulating_height_top = (0.025,)*16
insulating_height_bot = (0.015,)*16

insulating_pressure_top = (3.5,)*16
insulating_pressure_bot = (3.5,)*16
                                        
insulating_speed_top = (15,)*16
insulating_speed_bot = (15,)*16

insulating_dwell = 0.5

 
              
align_top_pressure=(10,)*16
top_over=(0.04,0.08,0.05,0.1,0.06,0.12,0.07,0.14,)*2
top_height=(0.05,)*16 
top_speed=(3,)*16



cantilever_width = 3.5
cantilever_bending_length = 5.5
cantilever_length = cantilever_bending_length + cant_y_translate

trans_speed = 40


cover_pressure=(15,)*8
#
inset=(cantilever_width-wire_width)/2


########SILVER TPU: (85wt% of solid) Ag (2-4um covered) in 30%wt TPU 35A in DMF
#electrode_height=0.075
#electrode_pressure = 4

#############TRAVIS"S INKS
electrode_height=0.130
electrode_pressure = 7
electrode_speed = 8

