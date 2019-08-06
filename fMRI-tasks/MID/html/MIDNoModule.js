/************ 
 * Mid Test *
 ************/

// init psychoJS:
var psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0, 0, 0]),
  units: 'height'
});

// store info about the experiment session:
let expName = 'MID';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001', 'PracticeRT': '200'};

// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instructRoutineBegin);
flowScheduler.add(instructRoutineEachFrame);
flowScheduler.add(instructRoutineEnd);
flowScheduler.add(scanTriggerRoutineBegin);
flowScheduler.add(scanTriggerRoutineEachFrame);
flowScheduler.add(scanTriggerRoutineEnd);
flowScheduler.add(PrepTimeRoutineBegin);
flowScheduler.add(PrepTimeRoutineEachFrame);
flowScheduler.add(PrepTimeRoutineEnd);
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin, trialsLoopScheduler);
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);
flowScheduler.add(waitRoutineBegin);
flowScheduler.add(waitRoutineEachFrame);
flowScheduler.add(waitRoutineEnd);
flowScheduler.add(DisplayMoneyRoutineBegin);
flowScheduler.add(DisplayMoneyRoutineEachFrame);
flowScheduler.add(DisplayMoneyRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({configURL: 'config.json', expInfo: expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.0.7';

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0/Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0/60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  
  return Scheduler.Event.NEXT;
}

var instructClock;
var instructFig;
var scanTriggerClock;
var text_2;
var PrepTimeClock;
var PrepFixation;
var cueClock;
var cueImage;
var fixation_2Clock;
var fixation;
var trialClock;
var Target;
var feedbackClock;
var feedbackMsg;
var CalculateRTClock;
var waitClock;
var polygon;
var DisplayMoneyClock;
var text;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "instruct"
  instructClock = new util.Clock();
  instructFig = new visual.ImageStim({
    win : psychoJS.window,
    name : 'instructFig', units : undefined, 
    image : 'images/MID_instructions.bmp', mask : undefined,
    ori : 0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "scanTrigger"
  scanTriggerClock = new util.Clock();
  text_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'text_2',
    text: 'Waiting for scanner trigger...',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PrepTime"
  PrepTimeClock = new util.Clock();
  PrepFixation = new visual.Rect ({
    win: psychoJS.window, name: 'PrepFixation',
    units: psychoJS.window.units,
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1.0, interpolate: true,
  });
  
  // Initialize components for Routine "cue"
  cueClock = new util.Clock();
  cueImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'cueImage', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "fixation_2"
  fixation_2Clock = new util.Clock();
  fixation = new visual.Rect ({
    win: psychoJS.window, name: 'fixation',
    units: psychoJS.window.units,
    width: [0.05, 0.05][0], height: [0.05, 0.05][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1.0, interpolate: true,
  });
  
  // Initialize components for Routine "trial"
  trialClock = new util.Clock();
  Target = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Target', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0, pos : [0, 0], size : [1.3, 1],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : -1.0 
  });
  // Initialize components for Routine "feedback"
  feedbackClock = new util.Clock();
  feedbackMsg = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedbackMsg',
    text: 'default text',
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: 2, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Initialize components for Routine "CalculateRT"
  CalculateRTClock = new util.Clock();
  // Initialize components for Routine "wait"
  waitClock = new util.Clock();
  polygon = new visual.Rect ({
    win: psychoJS.window, name: 'polygon',
    units: psychoJS.window.units,
    width: [0.5, 0.5][0], height: [0.5, 0.5][1],
    ori: 0, pos: [0, 0],
    lineWidth: 1, lineColor: new util.Color([1, 1, 1]),
    fillColor: new util.Color([1, 1, 1]),
    opacity: 1, depth: -1.0, interpolate: true,
  });
  
  // Initialize components for Routine "DisplayMoney"
  DisplayMoneyClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: msgEarnings,
    font: 'Arial',
    pos: [0, 0], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var ready;
var instructComponents;
function instructRoutineBegin() {
  //------Prepare to start Routine 'instruct'-------
  t = 0;
  instructClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  ready = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  instructComponents = [];
  instructComponents.push(instructFig);
  instructComponents.push(ready);
  
  for (const thisComponent of instructComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function instructRoutineEachFrame() {
  //------Loop for each frame of Routine 'instruct'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = instructClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *instructFig* updates
  if (t >= 0.0 && instructFig.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    instructFig.tStart = t;  // (not accounting for frame time here)
    instructFig.frameNStart = frameN;  // exact frame index
    instructFig.setAutoDraw(true);
  }

  
  // *ready* updates
  if (t >= 0.0 && ready.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ready.tStart = t;  // (not accounting for frame time here)
    ready.frameNStart = frameN;  // exact frame index
    ready.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (ready.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['y', 'n', 'left', 'right', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of instructComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function instructRoutineEnd() {
  //------Ending Routine 'instruct'-------
  for (const thisComponent of instructComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "instruct" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var scanTriggerKey;
var scanTriggerComponents;
function scanTriggerRoutineBegin() {
  //------Prepare to start Routine 'scanTrigger'-------
  t = 0;
  scanTriggerClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  scanTriggerKey = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  scanTriggerComponents = [];
  scanTriggerComponents.push(text_2);
  scanTriggerComponents.push(scanTriggerKey);
  
  for (const thisComponent of scanTriggerComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function scanTriggerRoutineEachFrame() {
  //------Loop for each frame of Routine 'scanTrigger'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = scanTriggerClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text_2* updates
  if (t >= 0.0 && text_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text_2.tStart = t;  // (not accounting for frame time here)
    text_2.frameNStart = frameN;  // exact frame index
    text_2.setAutoDraw(true);
  }

  
  // *scanTriggerKey* updates
  if (t >= 0.0 && scanTriggerKey.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    scanTriggerKey.tStart = t;  // (not accounting for frame time here)
    scanTriggerKey.frameNStart = frameN;  // exact frame index
    scanTriggerKey.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (scanTriggerKey.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['y', 'n', 'left', 'right', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      // a response ends the routine
      continueRoutine = false;
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of scanTriggerComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function scanTriggerRoutineEnd() {
  //------Ending Routine 'scanTrigger'-------
  for (const thisComponent of scanTriggerComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "scanTrigger" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var PrepTimeComponents;
function PrepTimeRoutineBegin() {
  //------Prepare to start Routine 'PrepTime'-------
  t = 0;
  PrepTimeClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  PrepTimeComponents = [];
  PrepTimeComponents.push(PrepFixation);
  
  for (const thisComponent of PrepTimeComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function PrepTimeRoutineEachFrame() {
  //------Loop for each frame of Routine 'PrepTime'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PrepTimeClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *PrepFixation* updates
  if (t >= 0.0 && PrepFixation.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    PrepFixation.tStart = t;  // (not accounting for frame time here)
    PrepFixation.frameNStart = frameN;  // exact frame index
    PrepFixation.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (PrepFixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    PrepFixation.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of PrepTimeComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function PrepTimeRoutineEnd() {
  //------Ending Routine 'PrepTime'-------
  for (const thisComponent of PrepTimeComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var trials;
function trialsLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  trials = new TrialHandler({
    psychoJS,
    nReps: 10, method: TrialHandler.Method.RANDOM,
    extraInfo: expInfo, originPath: undefined,
    trialList: 'MID_trials.xlsx',
    seed: undefined, name: 'trials'});
  psychoJS.experiment.addLoop(trials); // add the loop to the experiment

  // Schedule all the trials in the trialList:
  for (const thisTrial of trials) {
    thisScheduler.add(importConditions(trials));
    thisScheduler.add(cueRoutineBegin);
    thisScheduler.add(cueRoutineEachFrame);
    thisScheduler.add(cueRoutineEnd);
    thisScheduler.add(fixation_2RoutineBegin);
    thisScheduler.add(fixation_2RoutineEachFrame);
    thisScheduler.add(fixation_2RoutineEnd);
    thisScheduler.add(trialRoutineBegin);
    thisScheduler.add(trialRoutineEachFrame);
    thisScheduler.add(trialRoutineEnd);
    thisScheduler.add(feedbackRoutineBegin);
    thisScheduler.add(feedbackRoutineEachFrame);
    thisScheduler.add(feedbackRoutineEnd);
    thisScheduler.add(CalculateRTRoutineBegin);
    thisScheduler.add(CalculateRTRoutineEachFrame);
    thisScheduler.add(CalculateRTRoutineEnd);
    thisScheduler.add(endLoopIteration(thisTrial));
  }

  return Scheduler.Event.NEXT;
}


function trialsLoopEnd() {
  psychoJS.experiment.removeLoop(trials);

  return Scheduler.Event.NEXT;
}

var cueComponents;
function cueRoutineBegin() {
  //------Prepare to start Routine 'cue'-------
  t = 0;
  cueClock.reset(); // clock
  frameN = -1;
  routineTimer.add(2.000000);
  // update component parameters for each repeat
  cueImage.setImage(cue);
  // keep track of which components have finished
  cueComponents = [];
  cueComponents.push(cueImage);
  
  for (const thisComponent of cueComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function cueRoutineEachFrame() {
  //------Loop for each frame of Routine 'cue'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = cueClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *cueImage* updates
  if (t >= 0.0 && cueImage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    cueImage.tStart = t;  // (not accounting for frame time here)
    cueImage.frameNStart = frameN;  // exact frame index
    cueImage.setAutoDraw(true);
  }

  frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (cueImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    cueImage.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of cueComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function cueRoutineEnd() {
  //------Ending Routine 'cue'-------
  for (const thisComponent of cueComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var fixationResp;
var fixation_2Components;
function fixation_2RoutineBegin() {
  //------Prepare to start Routine 'fixation_2'-------
  t = 0;
  fixation_2Clock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  fixationResp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  fixation_2Components = [];
  fixation_2Components.push(fixation);
  fixation_2Components.push(fixationResp);
  
  for (const thisComponent of fixation_2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function fixation_2RoutineEachFrame() {
  //------Loop for each frame of Routine 'fixation_2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = fixation_2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *fixation* updates
  if (t >= 0.0 && fixation.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixation.tStart = t;  // (not accounting for frame time here)
    fixation.frameNStart = frameN;  // exact frame index
    fixation.setAutoDraw(true);
  }

  frameRemains = 0.0 + jitter - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixation.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixation.setAutoDraw(false);
  }
  
  // *fixationResp* updates
  if (t >= 0.0 && fixationResp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    fixationResp.tStart = t;  // (not accounting for frame time here)
    fixationResp.frameNStart = frameN;  // exact frame index
    fixationResp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { fixationResp.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + jitter - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (fixationResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    fixationResp.status = PsychoJS.Status.FINISHED;
  }

  if (fixationResp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['y', 'n', 'left', 'right', 'space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      fixationResp.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      fixationResp.rt = fixationResp.clock.getTime();
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of fixation_2Components)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function fixation_2RoutineEnd() {
  //------Ending Routine 'fixation_2'-------
  for (const thisComponent of fixation_2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (fixationResp.keys === undefined || fixationResp.keys.length === 0) {    // No response was made
      fixationResp.keys = undefined;
  }
  
  psychoJS.experiment.addData('fixationResp.keys', fixationResp.keys);
  if (typeof fixationResp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('fixationResp.rt', fixationResp.rt);
      }
  
  // the Routine "fixation_2" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var probeResp;
var trialComponents;
function trialRoutineBegin() {
  //------Prepare to start Routine 'trial'-------
  t = 0;
  trialClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  Target.setImage(probe);
  probeResp = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  trialComponents = [];
  trialComponents.push(Target);
  trialComponents.push(probeResp);
  
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function trialRoutineEachFrame() {
  //------Loop for each frame of Routine 'trial'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = trialClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Target* updates
  if (t >= 0.0 && Target.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Target.tStart = t;  // (not accounting for frame time here)
    Target.frameNStart = frameN;  // exact frame index
    Target.setAutoDraw(true);
  }

  frameRemains = 0.0 + jitterTarget - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Target.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Target.setAutoDraw(false);
  }
  
  // *probeResp* updates
  if (t >= 0.0 && probeResp.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    probeResp.tStart = t;  // (not accounting for frame time here)
    probeResp.frameNStart = frameN;  // exact frame index
    probeResp.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { probeResp.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + jitterTarget - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (probeResp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    probeResp.status = PsychoJS.Status.FINISHED;
  }

  if (probeResp.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      probeResp.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      probeResp.rt = probeResp.clock.getTime();
      // was this 'correct'?
      if (probeResp.keys == 'space') {
          probeResp.corr = 1;
      } else {
          probeResp.corr = 0;
      }
    }
  }
  
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of trialComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function trialRoutineEnd() {
  //------Ending Routine 'trial'-------
  for (const thisComponent of trialComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (probeResp.keys === undefined || probeResp.keys.length === 0) {    // No response was made
      probeResp.keys = undefined;
  }
  
  // was no response the correct answer?!
  if (probeResp.keys === undefined) {
    if (['None','none',undefined].includes('space')) {
       probeResp.corr = 1  // correct non-response
    } else {
       probeResp.corr = 0  // failed to respond (incorrectly)
    }
  }
  // store data for thisExp (ExperimentHandler)
  psychoJS.experiment.addData('probeResp.keys', probeResp.keys);
  psychoJS.experiment.addData('probeResp.corr', probeResp.corr);
  if (typeof probeResp.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('probeResp.rt', probeResp.rt);
      }
  
  // the Routine "trial" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var feedbackComponents;
function feedbackRoutineBegin() {
  //------Prepare to start Routine 'feedback'-------
  t = 0;
  feedbackClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  feedbackMsg.setText(((((respCheck + '\n\n') + msg) + '\n\nTotal Earnings:') + msgEarnings));
  // keep track of which components have finished
  feedbackComponents = [];
  feedbackComponents.push(feedbackMsg);
  
  for (const thisComponent of feedbackComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function feedbackRoutineEachFrame() {
  //------Loop for each frame of Routine 'feedback'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = feedbackClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *feedbackMsg* updates
  if (t >= 0.0 && feedbackMsg.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    feedbackMsg.tStart = t;  // (not accounting for frame time here)
    feedbackMsg.frameNStart = frameN;  // exact frame index
    feedbackMsg.setAutoDraw(true);
  }

  frameRemains = 0.0 + feedbackDur - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (feedbackMsg.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    feedbackMsg.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of feedbackComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function feedbackRoutineEnd() {
  //------Ending Routine 'feedback'-------
  for (const thisComponent of feedbackComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "feedback" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var CalculateRTComponents;
function CalculateRTRoutineBegin() {
  //------Prepare to start Routine 'CalculateRT'-------
  t = 0;
  CalculateRTClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  // keep track of which components have finished
  CalculateRTComponents = [];
  
  for (const thisComponent of CalculateRTComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function CalculateRTRoutineEachFrame() {
  //------Loop for each frame of Routine 'CalculateRT'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = CalculateRTClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of CalculateRTComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function CalculateRTRoutineEnd() {
  //------Ending Routine 'CalculateRT'-------
  for (const thisComponent of CalculateRTComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  // the Routine "CalculateRT" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var waitComponents;
function waitRoutineBegin() {
  //------Prepare to start Routine 'wait'-------
  t = 0;
  waitClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  waitComponents = [];
  waitComponents.push(polygon);
  
  for (const thisComponent of waitComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function waitRoutineEachFrame() {
  //------Loop for each frame of Routine 'wait'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = waitClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *polygon* updates
  if (t >= 0.0 && polygon.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    polygon.tStart = t;  // (not accounting for frame time here)
    polygon.frameNStart = frameN;  // exact frame index
    polygon.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (polygon.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    polygon.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of waitComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function waitRoutineEnd() {
  //------Ending Routine 'wait'-------
  for (const thisComponent of waitComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var DisplayMoneyComponents;
function DisplayMoneyRoutineBegin() {
  //------Prepare to start Routine 'DisplayMoney'-------
  t = 0;
  DisplayMoneyClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  DisplayMoneyComponents = [];
  DisplayMoneyComponents.push(text);
  
  for (const thisComponent of DisplayMoneyComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function DisplayMoneyRoutineEachFrame() {
  //------Loop for each frame of Routine 'DisplayMoney'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = DisplayMoneyClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *text* updates
  if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    text.tStart = t;  // (not accounting for frame time here)
    text.frameNStart = frameN;  // exact frame index
    text.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    text.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;// reverts to True if at least one component still running
  for (const thisComponent of DisplayMoneyComponents)
    if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
      continueRoutine = true;
      break;
    }
  
  // refresh the screen if continuing
  if (continueRoutine && routineTimer.getTime() > 0) {
    return Scheduler.Event.FLIP_REPEAT;
  }
  else {
    return Scheduler.Event.NEXT;
  }
}


function DisplayMoneyRoutineEnd() {
  //------Ending Routine 'DisplayMoney'-------
  for (const thisComponent of DisplayMoneyComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisTrial) {
  // ------Prepare for next entry------
  return function () {
    if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
      psychoJS.experiment.nextEntry();
    }
  return Scheduler.Event.NEXT;
  };
}


function importConditions(loop) {
  const trialIndex = loop.getTrialIndex();
  return function () {
    loop.setTrialIndex(trialIndex);
    psychoJS.importAttributes(loop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


function quitPsychoJS(message, isCompleted) {
  psychoJS.window.close();
  psychoJS.quit({message, isCompleted});

  return Scheduler.Event.QUIT;
}
