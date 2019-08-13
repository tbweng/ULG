#!/usr/bin/env python

# Paradigm for PEER calibration                                               #
#                                                                             #
###############################################################################


############################
#  Import various modules  #
############################
from VisionEgg import *
start_default_logging(); watch_exceptions()

from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation, FunctionController
from VisionEgg.Textures import *
from VisionEgg.MoreStimuli import *
from VisionEgg.Text import *
from VisionEgg.ResponseControl import *
from VisionEgg.DaqKeyboard import *

import Image, ImageDraw
import OpenGL.GL as gl
import sys

## FLAGS (for debugging) 
SHOW_PDIGM=0       # display all fixation dots (requires peer_calibration.png)
LBLS_WRITE=0       # write coordinates of fixation dots to file

## DEFINE
nSamples = 27      # CAN NOT BE CHANGED WITHOUT OTHER MODIFICATIONS !
sampleDuration = 4 # duration of each sample being displayed in seconds

pdigm_image='peer_calibration.png'

if LBLS_WRITE == 1: 
  lbls_ver=open('lbls_peer_ver.1D', 'w');
  lbls_hor=open('lbls_peer_hor.1D', 'w');

# screen = get_default_screen()
screen = VisionEgg.Core.Screen(size=(1440,900))
screen.parameters.bgcolor = (0,0,0)

scrn_x=screen.size[0];
scrn_y=screen.size[1];
scrn_x_half=int(scrn_x/2);
scrn_y_half=int(scrn_y/2);

#max_x = 0.85
#min_x = 0.15
#center_x = (max_x-min_x)/2+min_x
#unit_x = (max_x-min_x)/20
#shift_x = 0

#max_y = 0.90
#min_y = 0.10
#center_y = (max_y-min_y)/2+min_y
#unit_y = (max_y-min_y)/20
#shift_y = 0.05


max_x = 0.95
min_x = 0.05
shift_x = 0.0
center_x = (max_x-min_x)/2+min_x
unit_x = (max_x-min_x)/20


max_y = 0.90
min_y = 0.10
shift_y = 0.0
center_y = (max_y-min_y)/2+min_y
unit_y = (max_y-min_y)/20


# vector defining horizontal position for each sample
pos_x = [ min_x, 
          center_x,
          max_x,
          min_x, 
          center_x,
          max_x,
          min_x,
          center_x,
          max_x,

          unit_x*2+min_x, 
          unit_x*18+min_x,
          min_x,
          max_x,
          center_x,
          min_x,
          max_x,
          unit_x*2+min_x,
          unit_x*18+min_x,
          
          unit_x*7+min_x,
          unit_x*13+min_x,
          unit_x*3+min_x,
          unit_x*17+min_x,
          center_x,
          unit_x*3+min_x,
          unit_x*17+min_x,
          unit_x*7+min_x,
          unit_x*13+min_x ]

for i, value in enumerate(pos_x):
  pos_x[i]=value+shift_x

# vector defining vertical position for each sample
pos_y = [ min_y,
          min_y,
          min_y,
          center_y,
          center_y,
          center_y,
          max_y,
          max_y,
          max_y,

          min_y,
          min_y,
          unit_y*2+min_y,
          unit_y*2+min_y,
          center_y,
          unit_y*18+min_y,
          unit_y*18+min_y,
          max_y,
          max_y,
          
          unit_y*3+min_y,
          unit_y*3+min_y,
          unit_y*7+min_y,
          unit_y*7+min_y,
          center_y,
          unit_y*13+min_y,
          unit_y*13+min_y,
          unit_y*17+min_y,
          unit_y*17+min_y]

for i, value in enumerate(pos_y):
  pos_y[i]=value+shift_y

order = [ 4, 17,  1, 14, 15,  6, 23, 25, 11, 
         16, 9,  2, 18,  0,  8, 26, 21, 10, 
         13, 20, 7, 12, 19,  3,  5, 22, 24 ]
     
#order = [  0,  1,  2,  3,  4,  5,  6,  7,  8, 
#           9, 10, 11, 12, 13, 14, 15, 16, 17, 
#          18, 19, 20, 21, 22, 23, 24, 25, 26 ]



texta = Text(text="Stay focused on the",
            color=(1.0,1.0,1.0),
            position=(scrn_x_half, scrn_y_half + 60),
            font_size=60,
            anchor='center')

textb = Text(text="white fixation circle",
            color=(1.0,1.0,1.0),
            position=(scrn_x_half,scrn_y_half),
            font_size=60,
            anchor='center')

if SHOW_PDIGM:
  txtr_image = Texture(pdigm_image)
  image = TextureStimulus(texture=txtr_image,
              size = (scrn_x, scrn_y),
              internal_format = gl.GL_RGBA,
              max_alpha = 1.0,
              position = (scrn_x_half,scrn_y_half),
              anchor='center')


# Create a Viewport instance
viewportIntro = Viewport(screen=screen, stimuli=[texta,textb])


fixation = FilledCircle(
  anchor   = 'center',
  position = (scrn_x*pos_x[0], scrn_y*pos_y[0]),
  radius   = 5.0,
  color    = (255, 255, 255) 
)

if SHOW_PDIGM:
  viewport = Viewport(screen=screen,
                    stimuli=[image, fixation])
else:
  viewport = Viewport(screen=screen,
                    stimuli=[fixation])


p = Presentation(
    go_duration=(nSamples*sampleDuration,'seconds'),
    trigger_go_if_armed=0, # don't wait for trigger
    viewports=[viewport,viewportIntro])


# variabels for magnify fixation
next_sample_time=0 
max_radius=20.0
min_radius=5.0
blend_time=0.4
prev_time=0
radius=min_radius

# get first sample location
tmp_o = order.pop(0)
tmp_x = pos_x.pop(tmp_o)
tmp_y = pos_y.pop(tmp_o)
pos_x.insert(tmp_o,tmp_x)
pos_y.insert(tmp_o,tmp_y)
order.append(tmp_o)

if LBLS_WRITE == 1:
  lbls_ver.write("%6.2f\n" %(float(scrn_y*tmp_y)));
  lbls_hor.write("%6.2f\n" %(float(scrn_x*tmp_x)));

# main function
def getState(t):
    global next_sample_time
    global scrn_x, scrn_y
    global tmp_x, tmp_y
    global radius, min_radius, max_radius
    global prev_time
    
    curr_sample_time = int(t/sampleDuration) #bcount
    #print 't=%f radius=%f' %(t, radius)

    if curr_sample_time > next_sample_time:
        next_sample_time = curr_sample_time
        radius = max_radius
        prev_time = t
        
        tmp_o = order.pop(0)
        tmp_x = pos_x.pop(tmp_o)
        tmp_y = pos_y.pop(tmp_o)
        pos_x.insert(tmp_o,tmp_x)
        pos_y.insert(tmp_o,tmp_y)
        order.append(tmp_o)
        
        #print tmp_o, tmp_x
        if LBLS_WRITE == 1:
          lbls_ver.write("%6.2f\n" %(float(scrn_y*tmp_y)));
          lbls_hor.write("%6.2f\n" %(float(scrn_x*tmp_x)));

    if radius != min_radius:
      radius = max_radius - (max_radius - min_radius)/blend_time * (t-prev_time)
      if radius <= min_radius:
        radius = min_radius
    
    return( scrn_x*tmp_x, scrn_y*tmp_y)


def keydown(event):
  if event.key == pygame.locals.K_ESCAPE:  # Quit presentation 'p' with esc press
    p.parameters.go_duration = (0, 'frames')

def getImageRadius(t):
  global radius
  return(radius)

#######################
#  Define controllers #
#######################
stimulus_on_controller = ConstantController(during_go_value=1,between_go_value=0)
stimulus_off_controller = ConstantController(during_go_value=0,between_go_value=1)
trigger_in_controller = KeyboardTriggerInController(pygame.locals.K_5)

p.add_controller(p,'trigger_go_if_armed',trigger_in_controller)

p.add_controller(texta,'on', stimulus_off_controller )
p.add_controller(textb,'on', stimulus_off_controller )
p.add_controller(fixation,'on', stimulus_on_controller )

if SHOW_PDIGM:
  p.add_controller(image,'on', stimulus_on_controller)

#############################################################
#  Connect the controllers with the variables they control  #
#############################################################
p.add_controller(fixation,'position', FunctionController(during_go_func=getState))
p.add_controller(fixation,'radius', FunctionController(during_go_func=getImageRadius))
p.parameters.handle_event_callbacks = [(pygame.locals.KEYDOWN, keydown)]

#######################
#  Run the stimulus!  #
#######################
#p.export_movie_go(frames_per_sec=0.5,filename_base='movie/frame')
p.go()


if LBLS_WRITE == 1:
  lbls_ver.close
  lbls_hor.close
