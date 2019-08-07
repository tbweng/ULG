#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on Wed Aug  7 12:21:19 2019
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

from psychopy.hardware import keyboard

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.1.5'
expName = 'MID'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'practiceRT': '.5', 'trial Order': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/utbrainstudy/ULG/fMRI-tasks/MID/MID_lastrun.py',
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
    winType='pyglet', allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard()

# Initialize components for Routine "instruct"
instructClock = core.Clock()
instructFig = visual.ImageStim(
    win=win,
    name='instructFig', 
    image='images/MID_instructions.bmp', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "scanTrigger"
scanTriggerClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Waiting for scanner trigger...',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PrepTime"
PrepTimeClock = core.Clock()
PrepFixation = visual.ShapeStim(
    win=win, name='PrepFixation', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)
TrialOrders = {
1: ["TimeVersion5", "TimeVersion16"],
2: ["TimeVersion13", "TimeVersion1"],
3: ["TimeVersion9", "TimeVersion14"],
4: ["TimeVersion15", "TimeVersion12"],
5: ["TimeVersion6", "TimeVersion5"],
6: ["TimeVersion8", "TimeVersion11"],
7: ["TimeVersion2", "TimeVersion9"],
8: ["TimeVersion3", "TimeVersion8"],
9: ["TimeVersion10", "TimeVersion2"],
10: ["TimeVersion7", "TimeVersion13"],
11: ["TimeVersion11", "TimeVersion7"],
12: ["TimeVersion4", "TimeVersion3"],
}


# Initialize components for Routine "cue"
cueClock = core.Clock()
cueImage = visual.ImageStim(
    win=win,
    name='cueImage', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "fixation_2"
fixation_2Clock = core.Clock()
# Fixation Dur is defined in the TimeVersion csv file
FixationDur=''
fixation = visual.ShapeStim(
    win=win, name='fixation', vertices='cross',
    size=(0.05, 0.05),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=-1.0, interpolate=True)

# Initialize components for Routine "trial"
trialClock = core.Clock()
rt_list = []
probeDur = float(expInfo['practiceRT'])
Trials = 0
Target = visual.ImageStim(
    win=win,
    name='Target', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(1.3, 1),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=-1.0)

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
UserAcc = []
NonNeutralTrialsNum = 0
AdjTrial = 0
AdjTrialInc = 3
AdjUserRT = probeDur
Acc = 0
meanrt = 0
percentacc = 0
n_correct = 0
UserPercentAcc = ''
prevAcc = ''
msg=''
respCheck=''
msgEarnings =''
TrackEarnings = 0

# "TrialCondition": [TrialType, TrialEarning_corr, TrialEarning_incorr, TrialEarning_msg, CorrectMessage, IncorrectMessage, CueImage, ProbeImage]
cond_dict = {
    "LgReward": [1, 5, 0, 5, "You won", "You did not win", 'WinProbe.bmp', 'WinBig.bmp'],
    "SmallReward": [2, .2, 0, .2, "You won", "You did not win", 'WinProbe.bmp', 'WinSmall.bmp'],
    "LgPun": [4, 0, -5, 5, "You did not lose", "You lost", 'LoseProbe.bmp', 'LoseBig.bmp'],
    "SmallPun": [5, 0, -.2, .2, "You did not lose", "You lost", 'LoseProbe.bmp', 'LoseSmall.bmp'],
    "Triangle": [3, 0, 0, 0, "You did not win or lose anything!", "You did not win or lose anything!", 'NeutralProbe.bmp', 'Neutral.bmp'],
}
feedbackMsg = visual.TextStim(win=win, name='feedbackMsg',
    text='default text',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=2, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "calcRT"
calcRTClock = core.Clock()
OverallRT=''

# Initialize components for Routine "wait"
waitClock = core.Clock()
polygon = visual.ShapeStim(
    win=win, name='polygon', vertices='cross',
    size=(0.5, 0.5),
    ori=0, pos=(0, 0),
    lineWidth=1, lineColor=[1,1,1], lineColorSpace='rgb',
    fillColor=[1,1,1], fillColorSpace='rgb',
    opacity=1, depth=0.0, interpolate=True)

# Initialize components for Routine "DisplayMoney"
DisplayMoneyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text=msgEarnings,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# set up handler to look after randomisation of conditions etc
run = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='run')
thisExp.addLoop(run)  # add the loop to the experiment
thisRun = run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in run:
    currentLoop = run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instruct"-------
    t = 0
    instructClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ready = keyboard.Keyboard()
    # keep track of which components have finished
    instructComponents = [instructFig, ready]
    for thisComponent in instructComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "instruct"-------
    while continueRoutine:
        # get current time
        t = instructClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructFig* updates
        if t >= 0.0 and instructFig.status == NOT_STARTED:
            # keep track of start time/frame for later
            instructFig.tStart = t  # not accounting for scr refresh
            instructFig.frameNStart = frameN  # exact frame index
            win.timeOnFlip(instructFig, 'tStartRefresh')  # time at next scr refresh
            instructFig.setAutoDraw(True)
        
        # *ready* updates
        if t >= 0.0 and ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready.tStart = t  # not accounting for scr refresh
            ready.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ready, 'tStartRefresh')  # time at next scr refresh
            ready.status = STARTED
            # keyboard checking is just starting
            ready.clearEvents(eventType='keyboard')
        if ready.status == STARTED:
            theseKeys = ready.getKeys(keyList=['1', '2'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instruct"-------
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('instructFig.started', instructFig.tStartRefresh)
    run.addData('instructFig.stopped', instructFig.tStopRefresh)
    # the Routine "instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "scanTrigger"-------
    t = 0
    scanTriggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    scanTriggerKey = keyboard.Keyboard()
    # keep track of which components have finished
    scanTriggerComponents = [text_2, scanTriggerKey]
    for thisComponent in scanTriggerComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
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
            text_2.tStart = t  # not accounting for scr refresh
            text_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
            text_2.setAutoDraw(True)
        
        # *scanTriggerKey* updates
        if t >= 0.0 and scanTriggerKey.status == NOT_STARTED:
            # keep track of start time/frame for later
            scanTriggerKey.tStart = t  # not accounting for scr refresh
            scanTriggerKey.frameNStart = frameN  # exact frame index
            win.timeOnFlip(scanTriggerKey, 'tStartRefresh')  # time at next scr refresh
            scanTriggerKey.status = STARTED
            # keyboard checking is just starting
            scanTriggerKey.clearEvents(eventType='keyboard')
        if scanTriggerKey.status == STARTED:
            theseKeys = scanTriggerKey.getKeys(keyList=['5'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
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
    run.addData('text_2.started', text_2.tStartRefresh)
    run.addData('text_2.stopped', text_2.tStopRefresh)
    # the Routine "scanTrigger" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "PrepTime"-------
    t = 0
    PrepTimeClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    PrepTimeComponents = [PrepFixation]
    for thisComponent in PrepTimeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PrepTime"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PrepTimeClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *PrepFixation* updates
        if t >= 0.0 and PrepFixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            PrepFixation.tStart = t  # not accounting for scr refresh
            PrepFixation.frameNStart = frameN  # exact frame index
            win.timeOnFlip(PrepFixation, 'tStartRefresh')  # time at next scr refresh
            PrepFixation.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PrepFixation.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            PrepFixation.tStop = t  # not accounting for scr refresh
            PrepFixation.frameNStop = frameN  # exact frame index
            win.timeOnFlip(PrepFixation, 'tStopRefresh')  # time at next scr refresh
            PrepFixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PrepTimeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PrepTime"-------
    for thisComponent in PrepTimeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    run.addData('PrepFixation.started', PrepFixation.tStartRefresh)
    run.addData('PrepFixation.stopped', PrepFixation.tStopRefresh)
    if run.nRemaining is 1:
        run=1
    elif run.nRemaining is 0:
        run=2
        
    TrialOrder = TrialOrders[float(expInfo['trial Order'])][run-1] + ".csv"
    print("trial order is: ", TrialOrder)
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions(TrialOrder),
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
        
        # ------Prepare to start Routine "cue"-------
        t = 0
        cueClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        routineTimer.add(2.000000)
        # update component parameters for each repeat
        cueImage.setImage('images/' + cond_dict[Condition][7])
        # keep track of which components have finished
        cueComponents = [cueImage]
        for thisComponent in cueComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "cue"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = cueClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cueImage* updates
            if t >= 0.0 and cueImage.status == NOT_STARTED:
                # keep track of start time/frame for later
                cueImage.tStart = t  # not accounting for scr refresh
                cueImage.frameNStart = frameN  # exact frame index
                win.timeOnFlip(cueImage, 'tStartRefresh')  # time at next scr refresh
                cueImage.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cueImage.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                cueImage.tStop = t  # not accounting for scr refresh
                cueImage.frameNStop = frameN  # exact frame index
                win.timeOnFlip(cueImage, 'tStopRefresh')  # time at next scr refresh
                cueImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in cueComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "cue"-------
        for thisComponent in cueComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('cueImage.started', cueImage.tStartRefresh)
        trials.addData('cueImage.stopped', cueImage.tStopRefresh)
        
        # ------Prepare to start Routine "fixation_2"-------
        t = 0
        fixation_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        fixationResp = keyboard.Keyboard()
        # keep track of which components have finished
        fixation_2Components = [fixation, fixationResp]
        for thisComponent in fixation_2Components:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "fixation_2"-------
        while continueRoutine:
            # get current time
            t = fixation_2Clock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *fixation* updates
            if t >= 0.0 and fixation.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixation.tStart = t  # not accounting for scr refresh
                fixation.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStartRefresh')  # time at next scr refresh
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + FixationDur/1000- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixation.tStop = t  # not accounting for scr refresh
                fixation.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixation, 'tStopRefresh')  # time at next scr refresh
                fixation.setAutoDraw(False)
            
            # *fixationResp* updates
            if t >= 0.0 and fixationResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationResp.tStart = t  # not accounting for scr refresh
                fixationResp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(fixationResp, 'tStartRefresh')  # time at next scr refresh
                fixationResp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(fixationResp.clock.reset)  # t=0 on next screen flip
                fixationResp.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + FixationDur/1000- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixationResp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                fixationResp.tStop = t  # not accounting for scr refresh
                fixationResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(fixationResp, 'tStopRefresh')  # time at next scr refresh
                fixationResp.status = FINISHED
            if fixationResp.status == STARTED:
                theseKeys = fixationResp.getKeys(keyList=['1', '2', 'space'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    fixationResp.keys = theseKeys.name  # just the last key pressed
                    fixationResp.rt = theseKeys.rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_2Components:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "fixation_2"-------
        for thisComponent in fixation_2Components:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('FixationDur', FixationDur/1000)
        trials.addData('fixation.started', fixation.tStartRefresh)
        trials.addData('fixation.stopped', fixation.tStopRefresh)
        # check responses
        if fixationResp.keys in ['', [], None]:  # No response was made
            fixationResp.keys = None
        trials.addData('fixationResp.keys',fixationResp.keys)
        if fixationResp.keys != None:  # we had a response
            trials.addData('fixationResp.rt', fixationResp.rt)
        trials.addData('fixationResp.started', fixationResp.tStartRefresh)
        trials.addData('fixationResp.stopped', fixationResp.tStopRefresh)
        # the Routine "fixation_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        feedbackDur = 2 - probeDur
        
        
        Target.setImage("images/" + cond_dict[Condition][6])
        probeResp = keyboard.Keyboard()
        # keep track of which components have finished
        trialComponents = [Target, probeResp]
        for thisComponent in trialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "trial"-------
        while continueRoutine:
            # get current time
            t = trialClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Target* updates
            if t >= 0.0 and Target.status == NOT_STARTED:
                # keep track of start time/frame for later
                Target.tStart = t  # not accounting for scr refresh
                Target.frameNStart = frameN  # exact frame index
                win.timeOnFlip(Target, 'tStartRefresh')  # time at next scr refresh
                Target.setAutoDraw(True)
            frameRemains = 0.0 + probeDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Target.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                Target.tStop = t  # not accounting for scr refresh
                Target.frameNStop = frameN  # exact frame index
                win.timeOnFlip(Target, 'tStopRefresh')  # time at next scr refresh
                Target.setAutoDraw(False)
            
            # *probeResp* updates
            if t >= 0.0 and probeResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                probeResp.tStart = t  # not accounting for scr refresh
                probeResp.frameNStart = frameN  # exact frame index
                win.timeOnFlip(probeResp, 'tStartRefresh')  # time at next scr refresh
                probeResp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(probeResp.clock.reset)  # t=0 on next screen flip
                probeResp.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + probeDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if probeResp.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                probeResp.tStop = t  # not accounting for scr refresh
                probeResp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(probeResp, 'tStopRefresh')  # time at next scr refresh
                probeResp.status = FINISHED
            if probeResp.status == STARTED:
                theseKeys = probeResp.getKeys(keyList=['1'], waitRelease=False)
                if len(theseKeys):
                    theseKeys = theseKeys[0]  # at least one key was pressed
                    
                    # check for quit:
                    if "escape" == theseKeys:
                        endExpNow = True
                    probeResp.keys = theseKeys.name  # just the last key pressed
                    probeResp.rt = theseKeys.rt
                    # was this 'correct'?
                    if (probeResp.keys == str('1')) or (probeResp.keys == '1'):
                        probeResp.corr = 1
                    else:
                        probeResp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial"-------
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        if probeResp.corr is 1:
           rt_list.append(probeResp.rt)
        
        # Trial counter
        Trials = Trials + 1
        
        #bthisExp.addData('probeDur', probeDur)
        thisExp.addData('feedbackDur', feedbackDur)
        thisExp.addData('rt_list', rt_list)
        thisExp.addData('Trial counter', Trials)
        
        
            
        trials.addData('Target.started', Target.tStartRefresh)
        trials.addData('Target.stopped', Target.tStopRefresh)
        # check responses
        if probeResp.keys in ['', [], None]:  # No response was made
            probeResp.keys = None
            # was no response the correct answer?!
            if str('1').lower() == 'none':
               probeResp.corr = 1;  # correct non-response
            else:
               probeResp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('probeResp.keys',probeResp.keys)
        trials.addData('probeResp.corr', probeResp.corr)
        if probeResp.keys != None:  # we had a response
            trials.addData('probeResp.rt', probeResp.rt)
        trials.addData('probeResp.started', probeResp.tStartRefresh)
        trials.addData('probeResp.stopped', probeResp.tStopRefresh)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        TrialType = cond_dict[Condition][0]
        
        n_correct = n_correct + probeResp.corr
        percentacc_total = n_correct/Trials*100
        
        print(percentacc_total)
        
        rt_array = np.array(rt_list)
        meanrt = rt_array.mean()
        
        
        if TrialType != 3:
            NonNeutralTrialsNum = NonNeutralTrialsNum + 1 # counter of non-neutral (incentivized) trials
        
            UserAcc.append(probeResp.corr)
            UserAcc_array = np.array(UserAcc)
           
        # The probe duration is adjusted every three trials starting at trial 7.
        # Acc is calculated using only non-neutral trial types.
        
        # the task difficulty is adjusted over the course of the task after every 
        # third incentivized trial based on the overall accuracy rate of the previous six trials
        
            if NonNeutralTrialsNum is AdjTrial + AdjTrialInc:
                UserPercentAcc = UserAcc_array.sum()/3*100
        
                if NonNeutralTrialsNum is 3:
                    Acc = UserPercentAcc
                else: 
                    Acc = (UserPercentAcc + prevAcc)/2
        
                AdjRTmsg="Adjusting RT..."
                print(AdjRTmsg)
                thisExp.addData('AdjRTmsg', AdjRTmsg)
                print("Acc: ", Acc)
                
                # adaptive RT adjustment
                if Acc < 5:
                    AdjUserRT = AdjUserRT + .070
                elif Acc < 15:
                    AdjUserRT = AdjUserRT + .060
                elif Acc < 25:
                    AdjUserRT = AdjUserRT + .050
                elif Acc < 35:
                    AdjUserRT = AdjUserRT + .040
                elif Acc < 45:
                    AdjUserRT = AdjUserRT + .030
                elif Acc < 55:
                    AdjUserRT = AdjUserRT + .020
                elif Acc > 95:
                    AdjUserRT = AdjUserRT - .050
                elif Acc > 85:
                    AdjUserRT = AdjUserRT - .040
                elif Acc > 75:
                    AdjUserRT = AdjUserRT - .030
                elif Acc > 65:
                    AdjUserRT = AdjUserRT - .020
        
                UserAcc = []
                prevAcc = UserPercentAcc
                print("prevAcc: ", prevAcc)
                print("previous RT was: ", probeDur)
                print("new RT is: ", AdjUserRT)
                
                AdjTrial = NonNeutralTrialsNum
                probeDur = AdjUserRT
        
        
        if meanrt > 0:
            meanrt = meanrt
        
        # ensure that probe dur is between 150ms and 500ms
        if probeDur > .5:
            probeDur = .5
            AdjUserRT = probeDur
        elif probeDur < .15:
            probeDur = .15
            AdjUserRT = probeDur
        
        if fixationResp.keys != None:
            respCheck = "You pressed too soon!"
            probeResp.corr == 0 # override probe response since subject pressed too soon
        elif probeResp.keys == '1':
            respCheck = "Correct Response!"
            
        else:
            respCheck = "You pressed too slow!"
        
        
        if Condition == "Triangle":
            msg = cond_dict[Condition][4]
            TrialEarning = 0
        elif probeResp.corr == 1:
            msg = cond_dict[Condition][4] + " $%.2f!" % cond_dict[Condition][3]
            TrialEarning = cond_dict[Condition][1]
        else:
            msg = cond_dict[Condition][5] + " $%.2f!" % cond_dict[Condition][3]
            TrialEarning = cond_dict[Condition][2]
        
        TrackEarnings = TrackEarnings + TrialEarning
        msgEarnings = "Total Earnings: $%.2f!" % TrackEarnings
        
        thisExp.addData('msg', msg)
        thisExp.addData('TrackEarnings', TrackEarnings)
        feedbackMsg.setText(respCheck + '\n\n' + msg)
        # keep track of which components have finished
        feedbackComponents = [feedbackMsg]
        for thisComponent in feedbackComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "feedback"-------
        while continueRoutine:
            # get current time
            t = feedbackClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedbackMsg* updates
            if t >= 0.0 and feedbackMsg.status == NOT_STARTED:
                # keep track of start time/frame for later
                feedbackMsg.tStart = t  # not accounting for scr refresh
                feedbackMsg.frameNStart = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStartRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + feedbackDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                # keep track of stop time/frame for later
                feedbackMsg.tStop = t  # not accounting for scr refresh
                feedbackMsg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedbackMsg, 'tStopRefresh')  # time at next scr refresh
                feedbackMsg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "feedback"-------
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('TrialType', TrialType)
        thisExp.addData('NonNeutralTrialsNum', NonNeutralTrialsNum)
        thisExp.addData('probeDur', probeDur)
        thisExp.addData('percentacc_total', percentacc_total)
        thisExp.addData('meanrt', meanrt)
        
        
        #tmp
        thisExp.addData('UserAcc', UserAcc)
        thisExp.addData('Acc', Acc)
        thisExp.addData('AdjTrial', AdjTrial)
        thisExp.addData('AdjTrialInc', AdjTrialInc)
        
        
        print("Trial Type: ", TrialType, ", UserPercentAcc: ", UserPercentAcc, ", Acc: ", Acc, ", prevAcc: ", prevAcc, ", probeAcc: ", probeResp.corr, "meanrt :", meanrt, ", NonNeutralTrialsNum", NonNeutralTrialsNum, ", Trials: ", Trials, ", probeResp.rt: ", probeResp.rt, ", AdjUserRT: ", AdjUserRT, ", probeDur: ", probeDur)
        
        
        trials.addData('feedbackMsg.started', feedbackMsg.tStartRefresh)
        trials.addData('feedbackMsg.stopped', feedbackMsg.tStopRefresh)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "calcRT"-------
        t = 0
        calcRTClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # Not sure purpose of OverallRT
        """
        if probeResp.keys is not None: 
            OverallRT = probeResp.rt
        
        elif len(TextDisplay1.RESP) > 0 Then
        
         OverallRT = c.GetAttrib("ProbeTime") + TextDisplay1.RT
        
        ElseIf Len(Feedback.RESP) > 0 Then
        
         C.SetAttrib "OverallRT", c.GetAttrib("ProbeTime") + TextDisplay1.Duration + Feedback.RT
        """
        # keep track of which components have finished
        calcRTComponents = []
        for thisComponent in calcRTComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "calcRT"-------
        while continueRoutine:
            # get current time
            t = calcRTClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in calcRTComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "calcRT"-------
        for thisComponent in calcRTComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # the Routine "calcRT" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 1 repeats of 'run'


# ------Prepare to start Routine "wait"-------
t = 0
waitClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(5.000000)
# update component parameters for each repeat
# keep track of which components have finished
waitComponents = [polygon]
for thisComponent in waitComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "wait"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = waitClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *polygon* updates
    if t >= 0.0 and polygon.status == NOT_STARTED:
        # keep track of start time/frame for later
        polygon.tStart = t  # not accounting for scr refresh
        polygon.frameNStart = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
        polygon.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        polygon.tStop = t  # not accounting for scr refresh
        polygon.frameNStop = frameN  # exact frame index
        win.timeOnFlip(polygon, 'tStopRefresh')  # time at next scr refresh
        polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in waitComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "wait"-------
for thisComponent in waitComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('polygon.started', polygon.tStartRefresh)
thisExp.addData('polygon.stopped', polygon.tStopRefresh)

# ------Prepare to start Routine "DisplayMoney"-------
t = 0
DisplayMoneyClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
msgEarnings = "You earned a total of: $%.2f!" % TrackEarnings

# keep track of which components have finished
DisplayMoneyComponents = [text]
for thisComponent in DisplayMoneyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "DisplayMoney"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = DisplayMoneyClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # not accounting for scr refresh
        text.frameNStart = frameN  # exact frame index
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        text.tStop = t  # not accounting for scr refresh
        text.frameNStop = frameN  # exact frame index
        win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in DisplayMoneyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "DisplayMoney"-------
for thisComponent in DisplayMoneyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
