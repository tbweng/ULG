#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.0.7),
    on Tue Apr 23 14:29:54 2019
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


# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)

# Store info about the experiment session
psychopyVersion = '3.0.7'
expName = 'MID'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001', 'PracticeRT': '.5', 'Trial Order': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion


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

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/tbw665/Box/CNL_LabFiles/Longitudinal Study/MIDtask/MID.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1920, 1080], fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

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
jitter=''
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
probeDur = float(expInfo['PracticeRT'])
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

msg=''
respCheck=''
msgEarnings =''
TrackEarnings = 0

# "TrialCondition": [TrialType, TrialEarning_corr, TrialEarning_incorr, TrialEarning_msg, CorrectMessage, IncorrectMessage, CueImage, ProbeImage]
cond_dict = {
    "LgReward": [1, 5, 0, 5, "You won", "You did not win", WinProbe.bmp, WinBig.bmp],
    "SmallReward": [2, .2, 0, .2, "You won", "You did not win", WinProbe.bmp, WinSmall.bmp],
    "LgPun": [4, 0, -5, 5, "You did not lose", "You lost", LoseProbe.bmp, LoseBig.bmp],
    "SmallPun": [5, 0, -.2, .2, "You did not lose", "You lost", LoseProbe.bmp, LoseSmall.bmp],
    "Triangle": [3, 0, 0, 0, "You did not win or lose anything!", "You did not win or lose anything!", NeutralProbe.bmp, Neutral.bmp],
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
Run = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=[1, 2],
    seed=None, name='Run')
thisExp.addLoop(Run)  # add the loop to the experiment
thisRun = Run.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
if thisRun != None:
    for paramName in thisRun:
        exec('{} = thisRun[paramName]'.format(paramName))

for thisRun in Run:
    currentLoop = Run
    # abbreviate parameter names if possible (e.g. rgb = thisRun.rgb)
    if thisRun != None:
        for paramName in thisRun:
            exec('{} = thisRun[paramName]'.format(paramName))
    
    
    TrialOrder = TrialOrders[expInfo['Trial Order']][Run] + ".csv"
    print(TrialOrder)
    # ------Prepare to start Routine "instruct"-------
    t = 0
    instructClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    ready = event.BuilderKeyResponse()
    # keep track of which components have finished
    instructComponents = [instructFig, ready]
    for thisComponent in instructComponents:
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
            instructFig.tStart = t
            instructFig.frameNStart = frameN  # exact frame index
            instructFig.setAutoDraw(True)
        
        # *ready* updates
        if t >= 0.0 and ready.status == NOT_STARTED:
            # keep track of start time/frame for later
            ready.tStart = t
            ready.frameNStart = frameN  # exact frame index
            ready.status = STARTED
            # keyboard checking is just starting
            event.clearEvents(eventType='keyboard')
        if ready.status == STARTED:
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
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
    # the Routine "instruct" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "scanTrigger"-------
    t = 0
    scanTriggerClock.reset()  # clock
    frameN = -1
    continueRoutine = True
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
            theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
            
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
            PrepFixation.tStart = t
            PrepFixation.frameNStart = frameN  # exact frame index
            PrepFixation.setAutoDraw(True)
        frameRemains = 0.0 + 2- win.monitorFramePeriod * 0.75  # most of one frame period left
        if PrepFixation.status == STARTED and t >= frameRemains:
            PrepFixation.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
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
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=None, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('TimeVersion1.xlsx'),
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
        cueImage.setImage(cue)
        # keep track of which components have finished
        cueComponents = [cueImage]
        for thisComponent in cueComponents:
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
                cueImage.tStart = t
                cueImage.frameNStart = frameN  # exact frame index
                cueImage.setAutoDraw(True)
            frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
            if cueImage.status == STARTED and t >= frameRemains:
                cueImage.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        # ------Prepare to start Routine "fixation_2"-------
        t = 0
        fixation_2Clock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        jitter = np.random.uniform(low = 1.5, high = 4)
        jitter = round(jitter, 3)
        thisExp.addData('jitter', jitter)
        fixationResp = event.BuilderKeyResponse()
        # keep track of which components have finished
        fixation_2Components = [fixation, fixationResp]
        for thisComponent in fixation_2Components:
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
                fixation.tStart = t
                fixation.frameNStart = frameN  # exact frame index
                fixation.setAutoDraw(True)
            frameRemains = 0.0 + jitter- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixation.status == STARTED and t >= frameRemains:
                fixation.setAutoDraw(False)
            
            # *fixationResp* updates
            if t >= 0.0 and fixationResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                fixationResp.tStart = t
                fixationResp.frameNStart = frameN  # exact frame index
                fixationResp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(fixationResp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + jitter- win.monitorFramePeriod * 0.75  # most of one frame period left
            if fixationResp.status == STARTED and t >= frameRemains:
                fixationResp.status = FINISHED
            if fixationResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['y', 'n', 'left', 'right', 'space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    fixationResp.keys = theseKeys[-1]  # just the last key pressed
                    fixationResp.rt = fixationResp.clock.getTime()
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        # check responses
        if fixationResp.keys in ['', [], None]:  # No response was made
            fixationResp.keys=None
        trials.addData('fixationResp.keys',fixationResp.keys)
        if fixationResp.keys != None:  # we had a response
            trials.addData('fixationResp.rt', fixationResp.rt)
        # the Routine "fixation_2" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "trial"-------
        t = 0
        trialClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        print("probeDur is:", probeDur)
        
        jitterTarget = np.random.uniform(low = .15, high = .5)
        jitterTarget = round(jitterTarget, 3)
        thisExp.addData('jitterTarget', jitterTarget)
        
        feedbackDur = 2 - probeDur
        
        
        Target.setImage(probe)
        probeResp = event.BuilderKeyResponse()
        # keep track of which components have finished
        trialComponents = [Target, probeResp]
        for thisComponent in trialComponents:
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
                Target.tStart = t
                Target.frameNStart = frameN  # exact frame index
                Target.setAutoDraw(True)
            frameRemains = 0.0 + probeDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if Target.status == STARTED and t >= frameRemains:
                Target.setAutoDraw(False)
            
            # *probeResp* updates
            if t >= 0.0 and probeResp.status == NOT_STARTED:
                # keep track of start time/frame for later
                probeResp.tStart = t
                probeResp.frameNStart = frameN  # exact frame index
                probeResp.status = STARTED
                # keyboard checking is just starting
                win.callOnFlip(probeResp.clock.reset)  # t=0 on next screen flip
                event.clearEvents(eventType='keyboard')
            frameRemains = 0.0 + probeDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if probeResp.status == STARTED and t >= frameRemains:
                probeResp.status = FINISHED
            if probeResp.status == STARTED:
                theseKeys = event.getKeys(keyList=['space'])
                
                # check for quit:
                if "escape" in theseKeys:
                    endExpNow = True
                if len(theseKeys) > 0:  # at least one key was pressed
                    probeResp.keys = theseKeys[-1]  # just the last key pressed
                    probeResp.rt = probeResp.clock.getTime()
                    # was this 'correct'?
                    if (probeResp.keys == str('space')) or (probeResp.keys == 'space'):
                        probeResp.corr = 1
                    else:
                        probeResp.corr = 0
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
        thisExp.addData('feedbackDur', feedbackDur)
        thisExp.addData('rt_list', rt_list)
        thisExp.addData('Trial counter', Trials)
        
        
            
        # check responses
        if probeResp.keys in ['', [], None]:  # No response was made
            probeResp.keys=None
            # was no response the correct answer?!
            if str('space').lower() == 'none':
               probeResp.corr = 1;  # correct non-response
            else:
               probeResp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('probeResp.keys',probeResp.keys)
        trials.addData('probeResp.corr', probeResp.corr)
        if probeResp.keys != None:  # we had a response
            trials.addData('probeResp.rt', probeResp.rt)
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "feedback"-------
        t = 0
        feedbackClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        TrialType = cond_dict[condition][0]
        
        n_correct = n_correct + probeResp.corr
        percentacc = n_correct/Trials*100
        
        print(percentacc)
        
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
        
                print("Adjusting RT...")
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
        
        
            
        # if condition == "WinBig":
        #     TrialEarning = 5
        #     if probeResp.corr == 1:
        #         msg = "You won $%.2f!" % TrialEarning
        #     else:
        #         msg = "You did not win $%.2f!" % TrialEarning
        #         TrialEarning = 0
        # elif condition == "WinSmall":
        #     TrialEarning = .2
        #     if probeResp.corr == 1:
        #         msg = "You won $%.2f!" % TrialEarning
        #     else:
        #         msg = "You did not win $%.2f!" % TrialEarning
        #         TrialEarning = 0
        # elif condition == "LoseBig":
        #     TrialEarning = 5
        #     if probeResp.corr == 1:
        #         msg = "You did not lose $%.2f!" % TrialEarning
        #     else:
        #         msg = "You lost $%.2f!" % TrialEarning
        #         TrialEarning = -5
        # elif condition == "LoseSmall":
        #     TrialEarning = .2
        #     if probeResp.corr == 1:
        #         msg = "You did not lose $%.2f!" % TrialEarning
        #     else:
        #         msg = "You lost $%.2f!" % TrialEarning
        #         TrialEarning = -.2
        # else:
        #     msg = "You did not win or lose anything!"
        #     TrialEarning = 0    
        
        
        if fixationResp.keys != None:
            respCheck = "You pressed too soon!"
            probeResp.corr == 0 # override probe response since subject pressed too soon
        elif probeResp.keys == 'space':
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
        feedbackMsg.setText(respCheck + '\n\n' + msg + '\n\n' + msgEarnings)
        # keep track of which components have finished
        feedbackComponents = [feedbackMsg]
        for thisComponent in feedbackComponents:
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
                feedbackMsg.tStart = t
                feedbackMsg.frameNStart = frameN  # exact frame index
                feedbackMsg.setAutoDraw(True)
            frameRemains = 0.0 + feedbackDur- win.monitorFramePeriod * 0.75  # most of one frame period left
            if feedbackMsg.status == STARTED and t >= frameRemains:
                feedbackMsg.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        thisExp.addData('percentacc', percentacc)
        thisExp.addData('meanrt', meanrt)
        
        
        #tmp
        thisExp.addData('UserAcc', UserAcc)
        thisExp.addData('Acc', Acc)
        thisExp.addData('AdjTrial', AdjTrial)
        thisExp.addData('AdjTrialInc', AdjTrialInc)
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # ------Prepare to start Routine "calcRT"-------
        t = 0
        calcRTClock.reset()  # clock
        frameN = -1
        continueRoutine = True
        # update component parameters for each repeat
        # keep track of which components have finished
        calcRTComponents = []
        for thisComponent in calcRTComponents:
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        
        # -------Start Routine "calcRT"-------
        while continueRoutine:
            # get current time
            t = calcRTClock.getTime()
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # check for quit (typically the Esc key)
            if endExpNow or event.getKeys(keyList=["escape"]):
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
        
    # completed  repeats of 'trials'
    
    thisExp.nextEntry()
    
# completed 2 repeats of 'Run'


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
        polygon.tStart = t
        polygon.frameNStart = frameN  # exact frame index
        polygon.setAutoDraw(True)
    frameRemains = 0.0 + 5- win.monitorFramePeriod * 0.75  # most of one frame period left
    if polygon.status == STARTED and t >= frameRemains:
        polygon.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
        text.tStart = t
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if text.status == STARTED and t >= frameRemains:
        text.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
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
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
