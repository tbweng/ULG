#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on Wed Apr 17 15:04:56 2019
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, sound, gui, visual, core, data, event, logging, clock
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
import csv


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'stopSignal'  # from the Builder filename that created this script

test_dlg = gui.Dlg(title='Stop Signal Task')
test_dlg.addField('Participant ID')
test_dlg.addField('Trial Order', choices=['1','2','3','4','5','6','7','8','9','10','11','12','practice'])
test_dlg.addField('Handedness', choices=['R','L'])
input_data = test_dlg.show()
expInfo = {'participant': input_data[0], 'trial_order': input_data[1], 'handedness': input_data[2]}
if test_dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion
print(input_data)

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/utbrainstudy/ULG/fMRI-tasks/SST/stopSignal_updated.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1440, 900], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True)
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

#method to write to csv after each trial
def writeTrialtoFile(trial_type, arrow, correct_response, ssd, iti, response_key, response_acc, response_rt, soa, end_fixation_duration):
    dir = 'data'
    if not os.path.isdir(dir):
        os.makedirs(dir)
    file_name = dir+os.path.sep + expInfo['participant'].zfill(3) +'_'+ expName +'_backup-'+ expInfo['date'] + '.csv'

    with open(file_name, 'a') as save_file:
        file_writer = csv.writer(save_file, delimiter=',')
        if os.stat(file_name).st_size == 0:
            file_writer.writerow(('trial_type', 'arrow_1', 'corrAns', 'ss_delay', 'iti_duration', 'key_response.keys', 'key_response.corr', 'key_response.rt', 'SOA', 'run_fixation_duration', 'participant', 'trial_order', 'handedness'))
        file_writer.writerow((trial_type, arrow, correct_response, ssd, iti, response_key, response_acc, response_rt, soa, end_fixation_duration, expInfo['participant'], expInfo['trial_order'], expInfo['handedness']))

# Initialize components for Routine "instructions"
instructionsClock = core.Clock()
right_handed_instructions = visual.ImageStim(
    win=win,
    name='right_handed_instructions', 
    image='sst_images/Instructions_Scanner_RightHanded.bmp', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
left_handed_instructions = visual.ImageStim(
    win=win,
    name='left_handed_instructions', 
    image='sst_images/Instructions_Scanner_LeftHanded.bmp', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "scanTrigger"
scanTriggerClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Waiting for scanner trigger...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0,
    color='white', colorSpace='rgb', opacity=1,
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "trial_start"
trial_startClock = core.Clock()
arrow_key = visual.ImageStim(
    win=win,
    name='arrow_key', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.8, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
stop_arrow = visual.ImageStim(
    win=win,
    name='stop_arrow', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.7, 2.0),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)
# Set experiment start values for variable component trial_t
trial_t = ''
trial_tContainer = []
SSD = 0.050
right_left_arrow_duration = 1.000
stop_signal_duration = 0.300
leftover_fixation = 1.0
show_stop_signal = False

# Initialize components for Routine "iti"
itiClock = core.Clock()
fixation_cross = visual.TextStim(win=win, name='fixation_cross',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "run_end"
run_endClock = core.Clock()
final_fixation_cross = visual.TextStim(win=win, name='final_fixation_cross',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
runs = data.TrialHandler(nReps=2, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='runs')
thisExp.addLoop(runs)  # add the loop to the experiment
thisRun = runs.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in runs:
    currentLoop = runs
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
            
    # ------Prepare to start Routine "instructions"-------
    t = 0
    instructionsClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    start_key = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructionsComponents = [right_handed_instructions, left_handed_instructions, start_key]
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instructions"-------
    while continueRoutine:
        # get current time
        t = instructionsClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *right_handed_instructions* updates
        if (expInfo['handedness'] == 'R') and right_handed_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            right_handed_instructions.tStart = t
            right_handed_instructions.frameNStart = frameN  # exact frame index
            right_handed_instructions.setAutoDraw(True)
        
        # *left_handed_instructions* updates
        if (expInfo['handedness'] == 'L') and left_handed_instructions.status == NOT_STARTED:
            # keep track of start time/frame for later
            left_handed_instructions.tStart = t
            left_handed_instructions.frameNStart = frameN  # exact frame index
            left_handed_instructions.setAutoDraw(True)
        
        # *start_key* updates
        if t >= 0.0 and start_key.status == NOT_STARTED:
            # keep track of start time/frame for later
            start_key.tStart = t
            start_key.frameNStart = frameN  # exact frame index
            start_key.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if start_key.status == STARTED:
            theseKeys = event.getKeys(keyList=['space'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructionsComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instructions"-------
    for thisComponent in instructionsComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instructions" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()

    # ------Prepare to start Routine "scanTrigger"-------
    t = 0
    scanTriggerClock.reset()  # clock
    frameN = -1
    if(expInfo['trial_order'] != 'practice'):
        continueRoutine = True
    else:
        continueRoutine = False
    # update component parameters for each repeat
    scanTriggerKey = event.BuilderKeyResponse()
    # keep track of which components have finished
    scanTriggerComponents = [text_2, scanTriggerKey]
    for thisComponent in scanTriggerComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED

    # -------Start Routine "scanTrigger"-------
    while continueRoutine:
        # get current time
        t = scanTriggerClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame

        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)

        # *scanTriggerKey* updates
        if t >= 0.0 and scanTriggerKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            scanTriggerKey.tStart = t
            scanTriggerKey.frameNStart = frameN  # exact frame index
            scanTriggerKey.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if scanTriggerKey.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space','5'])

            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                # a response ends the routine
                continueRoutine = False

        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in scanTriggerComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished

        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()

    # -------Ending Routine "scanTrigger"-------
    for thisComponent in scanTriggerComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "scanTrigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()


    # set up handler to look after randomisation of conditions etc
    if(expInfo['trial_order'] == 'practice'):
        trial_order = 'sst_trial_order_practice.csv'
    else:  
        if(runs.nRemaining == 1):
            trial_order = 'sst_trial_order_'+expInfo['trial_order']+'A.csv'
        elif(runs.nRemaining == 0):
            trial_order = 'sst_trial_order_'+expInfo['trial_order']+'B.csv'
        
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(trial_order),
        seed=None, name='trials')
        
    thisExp.addLoop(trials)  # add the loop to the experiment
    thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    for thisTrial in trials:
        currentLoop = trials
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                exec('{} = thisTrial[paramName]'.format(paramName))
        
        # ------Prepare to start Routine "trial_start"-------
        t = 0
        trial_startClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        arrow_key.setImage(arrow_1)
        stop_arrow.setImage(arrow_2)
        key_response = event.BuilderKeyResponse()
        trial_t = trial_type  # Set routine start values for trial_t
        iti_duration = jitter/1000 # Set routine start values for iti_duration
        show_stop_signal = False
        
        if(trial_t == 'stop'):
            right_left_arrow_duration = SSD
        elif(trial_t == 'go'):
            right_left_arrow_duration = 1.000
         
        if(trial_t == 'stop' and SSD > 0.700):
            stop_signal_duration = 1.000 - SSD
            
        # keep track of which components have finished
        trial_startComponents = [arrow_key, stop_arrow, key_response, trial_t]
        for thisComponent in trial_startComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial_start"-------
        while continueRoutine:
            # get current time
            t = trial_startClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *arrow_key* updates
            if t >= 0.0 and arrow_key.status == NOT_STARTED:
                # keep track of start time/frame for later
                arrow_key.tStart = t
                arrow_key.frameNStart = frameN  # exact frame index
                arrow_key.setAutoDraw(True)
            frameRemains = 0.0 + right_left_arrow_duration- win.monitorFramePeriod * 0.75  # most of one frame period left
            if arrow_key.status == STARTED and t >= frameRemains:
                arrow_key.setAutoDraw(False)
            
            # *stop_arrow* updates
            if (show_stop_signal) and stop_arrow.status == NOT_STARTED:
                # keep track of start time/frame for later
                stop_arrow.tStart = t
                stop_arrow.frameNStart = frameN  # exact frame index
                stop_arrow.setAutoDraw(True)
            if stop_arrow.status == STARTED and t >= (stop_arrow.tStart + stop_signal_duration):
                stop_arrow.setAutoDraw(False)
            
            # *key_response* updates
            if t >= 0 and key_response.status == NOT_STARTED:
                # keep track of start time/frame for later
                key_response.tStart = t
                key_response.frameNStart = frameN  # exact frame index
                key_response.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if key_response.status == STARTED and t >= frameRemains:
                key_response.status = FINISHED
            if key_response.status == STARTED:
                theseKeys = event.getKeys(keyList=['1', '2'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    if key_response.keys == []:  # then this was the first keypress
                        key_response.keys = theseKeys[0]  # just the first key pressed
                        key_response.rt = key_response.clock.getTime()
                        # was this 'correct'?
                        if (key_response.keys == str(corrAns)) or (key_response.keys == corrAns):
                            key_response.corr = 1
                        else:
                            key_response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
            if(trial_t == 'stop' and arrow_key.status == FINISHED):
                show_stop_signal = True
            if(trial_t == 'stop' and stop_arrow.status == FINISHED):
                continueRoutine = False
            if(trial_t == 'go' and key_response.status == FINISHED and key_response.keys == []):
                continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_startComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_start"-------
        for thisComponent in trial_startComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_response.keys in ['', [], None]:  # No response was made
            key_response.keys=None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               key_response.corr = 1;  # correct non-response
            else:
               key_response.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_response.keys',key_response.keys)
        trials.addData('key_response.corr', key_response.corr)
        if key_response.keys != None:  # we had a response
            trials.addData('key_response.rt', key_response.rt)
        thisExp.addData('trial_t.routineEndVal', trial_t)  # Save end routine value
        if(not key_response.keys):
            leftover_fixation = 0.0
        if(trial_t == 'stop'):
            if(key_response.corr == 1 and SSD > 0 and SSD < 0.900):
                SSD = SSD + 0.050
            elif(key_response.corr != 1 and SSD > 0):
                SSD = SSD - 0.050
            elif(SSD == 0.050 or SSD == 0.900):
                SSD = SSD
        trials.addData('ss_delay', SSD)
        trials.addData('iti_duration', iti_duration)
        # the Routine "trial_start" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "iti"-------
        t = 0
        itiClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        fixation_cross.setText('+')
        if(trial_t == 'stop' and key_response.corr == 1):
            leftover_fixation = 1.0 - stop_signal_duration - right_left_arrow_duration
        elif(trial_t == 'stop' and key_response.corr != 1):
            leftover_fixation = 1.0 - key_response.rt
        elif(trial_t == 'go' and not key_response.keys):
            leftover_fixation = 0.0
        elif(trial_t == 'go' and key_response.keys):
            leftover_fixation = 1.0 - key_response.rt
        holder = 0
        soa = 0
        if(trial_t == 'go'):
            if(key_response.keys):
                holder = key_response.rt
            else:
                holder = right_left_arrow_duration
            print(iti_duration + leftover_fixation + holder)
            soa = iti_duration + leftover_fixation + holder
        elif(trial_t == 'stop'):
            print(iti_duration+leftover_fixation+right_left_arrow_duration+stop_signal_duration)
            soa = iti_duration + leftover_fixation + right_left_arrow_duration + stop_signal_duration
        trials.addData('SOA', soa)
        # keep track of which components have finished
        itiComponents = [fixation_cross]
        for thisComponent in itiComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        writeTrialtoFile(trial_t, arrow_1, str(corrAns), SSD, iti_duration, key_response.keys, key_response.corr, key_response.rt, soa, None)
        # -------Start Routine "iti"-------
        while continueRoutine:
            # get current time
            t = itiClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation_cross* updates
            if t >= 0 and fixation_cross.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation_cross.tStart = t
                fixation_cross.frameNStart = frameN  # exact frame index
                fixation_cross.setAutoDraw(True)
            frameRemains = 0 + iti_duration+leftover_fixation- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation_cross.status == STARTED and t >= frameRemains:
                fixation_cross.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in itiComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "iti"-------
        for thisComponent in itiComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "iti" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        #repeat trial if stop trial and response given during SSD
        
        
    # completed 1 repeats of 'trials'
    
    writeTrialtoFile('run_end', '', '', '', '', '', '', '', '', run_end_fixation)
    # ------Prepare to start Routine "run_end"-------
    t = 0
    run_endClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(run_end_fixation/1000)
    # update component parameters for each repeat
    # keep track of which components have finished
    run_endComponents = [final_fixation_cross]
    for thisComponent in run_endComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "run_end"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = run_endClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *final_fixation_cross* updates
        if t >= 0 and final_fixation_cross.status == NOT_STARTED:
            # keep track of start time/frame for later
            final_fixation_cross.tStart = t
            final_fixation_cross.frameNStart = frameN  # exact frame index
            final_fixation_cross.setAutoDraw(True)
        frameRemains = 0 + (run_end_fixation/1000)- win.monitorFramePeriod * 0.75  # most of one frame period left
        if final_fixation_cross.status == STARTED and t >= frameRemains:
            final_fixation_cross.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in run_endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "run_end"-------
    for thisComponent in run_endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    # the Routine "run_end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 2 repeats of 'runs'

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
