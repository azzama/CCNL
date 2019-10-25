/********************** 
 * Stressexpday1 Test *
 **********************/

import { PsychoJS } from 'https://pavlovia.org/lib/core.js';
import * as core from 'https://pavlovia.org/lib/core.js';
import { TrialHandler } from 'https://pavlovia.org/lib/data.js';
import { Scheduler } from 'https://pavlovia.org/lib/util.js';
import * as util from 'https://pavlovia.org/lib/util.js';
import * as visual from 'https://pavlovia.org/lib/visual.js';
import { Sound } from 'https://pavlovia.org/lib/sound.js';

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
let expName = 'StressExpDay1';  // from the Builder filename that created this script
let expInfo = {'participant': '', 'session': '001'};

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
flowScheduler.add(WelcomeScreenRoutineBegin);
flowScheduler.add(WelcomeScreenRoutineEachFrame);
flowScheduler.add(WelcomeScreenRoutineEnd);
const PracticeBlockLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(PracticeBlockLoopLoopBegin, PracticeBlockLoopLoopScheduler);
flowScheduler.add(PracticeBlockLoopLoopScheduler);
flowScheduler.add(PracticeBlockLoopLoopEnd);
flowScheduler.add(BlockIntroRoutineBegin);
flowScheduler.add(BlockIntroRoutineEachFrame);
flowScheduler.add(BlockIntroRoutineEnd);
const Block1LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Block1LoopLoopBegin, Block1LoopLoopScheduler);
flowScheduler.add(Block1LoopLoopScheduler);
flowScheduler.add(Block1LoopLoopEnd);
flowScheduler.add(BlockIntroRoutineBegin);
flowScheduler.add(BlockIntroRoutineEachFrame);
flowScheduler.add(BlockIntroRoutineEnd);
const Block2LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Block2LoopLoopBegin, Block2LoopLoopScheduler);
flowScheduler.add(Block2LoopLoopScheduler);
flowScheduler.add(Block2LoopLoopEnd);
flowScheduler.add(BlockIntroRoutineBegin);
flowScheduler.add(BlockIntroRoutineEachFrame);
flowScheduler.add(BlockIntroRoutineEnd);
const Block3LoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(Block3LoopLoopBegin, Block3LoopLoopScheduler);
flowScheduler.add(Block3LoopLoopScheduler);
flowScheduler.add(Block3LoopLoopEnd);
flowScheduler.add(PreBaselineBreakRoutineBegin);
flowScheduler.add(PreBaselineBreakRoutineEachFrame);
flowScheduler.add(PreBaselineBreakRoutineEnd);
const BaselineLoopLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(BaselineLoopLoopBegin, BaselineLoopLoopScheduler);
flowScheduler.add(BaselineLoopLoopScheduler);
flowScheduler.add(BaselineLoopLoopEnd);
flowScheduler.add(EndScreenRoutineBegin);
flowScheduler.add(EndScreenRoutineEachFrame);
flowScheduler.add(EndScreenRoutineEnd);
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({expName, expInfo});

var frameDur;
function updateInfo() {
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '3.1.5';

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

var WelcomeScreenClock;
var textWelcome;
var PracticeBlockClock;
var practiceTrialImage;
var practiceTrials;
var CoverTaskQ;
var key_answer_PB;
var ISIClock;
var ISIimage;
var BlockIntroClock;
var TextBlockIntro;
var Block1Clock;
var Block1Image;
var Block1Trials;
var CoverTaskQ_2;
var key_answer_B1;
var Block2Clock;
var Block2Image;
var Block2Trials;
var CoverTaskQ_3;
var key_answer_B2;
var Block3Clock;
var Block3Image;
var Block3trials;
var CoverTaskQ_4;
var key_answer_B3;
var PreBaselineBreakClock;
var PreBaselineText;
var BaselineTestClock;
var BaselineTestTrials;
var CoverTaskQ_5;
var key_answer_BT;
var EndScreenClock;
var textEndScreen;
var globalClock;
var routineTimer;
function experimentInit() {
  // Initialize components for Routine "WelcomeScreen"
  WelcomeScreenClock = new util.Clock();
  textWelcome = new visual.TextStim({
    win: psychoJS.window,
    name: 'textWelcome',
    text: 'Thank you for your participation. For this task, you are going to be shown some words paired with images. You will be asked to remember the words and images later, so please pay attention to them. You will also be asked to determine whether you have been shown the current word displayed previously. To respond, you will answer "yes" with the \'y\' key or "no" with the \'n\' key using your keyboard. It is important you respond correctly. You may enter the correct key only once. You are going to be able to practice a few times before the real experiment begins. You will get a few one-minute breaks throughout the task, and after the breaks are over, the task will start again automatically. When you are ready, press the space bar to begin.',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "PracticeBlock"
  PracticeBlockClock = new util.Clock();
  practiceTrialImage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'practiceTrialImage', units : undefined, 
    image : 'images/UCI.jpg', mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  practiceTrials = new visual.TextStim({
    win: psychoJS.window,
    name: 'practiceTrials',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CoverTaskQ = new visual.TextStim({
    win: psychoJS.window,
    name: 'CoverTaskQ',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_answer_PB = new visual.TextStim({
    win: psychoJS.window,
    name: 'key_answer_PB',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISIimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ISIimage', units : undefined, 
    image : 'images/isi.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "BlockIntro"
  BlockIntroClock = new util.Clock();
  TextBlockIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'TextBlockIntro',
    text: 'Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Block1"
  Block1Clock = new util.Clock();
  Block1Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Block1Image', units : undefined, 
    image : 'images/Bedroom.png', mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Block1Trials = new visual.TextStim({
    win: psychoJS.window,
    name: 'Block1Trials',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CoverTaskQ_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'CoverTaskQ_2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_answer_B1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'key_answer_B1',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISIimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ISIimage', units : undefined, 
    image : 'images/isi.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "BlockIntro"
  BlockIntroClock = new util.Clock();
  TextBlockIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'TextBlockIntro',
    text: 'Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Block2"
  Block2Clock = new util.Clock();
  Block2Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Block2Image', units : undefined, 
    image : 'images/Kitchen.png', mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Block2Trials = new visual.TextStim({
    win: psychoJS.window,
    name: 'Block2Trials',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CoverTaskQ_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'CoverTaskQ_3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_answer_B2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'key_answer_B2',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISIimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ISIimage', units : undefined, 
    image : 'images/isi.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "BlockIntro"
  BlockIntroClock = new util.Clock();
  TextBlockIntro = new visual.TextStim({
    win: psychoJS.window,
    name: 'TextBlockIntro',
    text: 'Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "Block3"
  Block3Clock = new util.Clock();
  Block3Image = new visual.ImageStim({
    win : psychoJS.window,
    name : 'Block3Image', units : undefined, 
    image : 'images/Livingroom.png', mask : undefined,
    ori : 0, pos : [0, 0.2], size : [0.4, 0.4],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  Block3trials = new visual.TextStim({
    win: psychoJS.window,
    name: 'Block3trials',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  CoverTaskQ_4 = new visual.TextStim({
    win: psychoJS.window,
    name: 'CoverTaskQ_4',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -2.0 
  });
  
  key_answer_B3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'key_answer_B3',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -4.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISIimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ISIimage', units : undefined, 
    image : 'images/isi.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "PreBaselineBreak"
  PreBaselineBreakClock = new util.Clock();
  PreBaselineText = new visual.TextStim({
    win: psychoJS.window,
    name: 'PreBaselineText',
    text: "Please take a two minute break. After two minutes, the experiment will continue. In the next part of this task, you will be asked if you recognize words you may have seen before. You will respond with either the 'y' key for yes, and the 'n' key for no. ",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Initialize components for Routine "BaselineTest"
  BaselineTestClock = new util.Clock();
  BaselineTestTrials = new visual.TextStim({
    win: psychoJS.window,
    name: 'BaselineTestTrials',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.1)], height: 0.1,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  CoverTaskQ_5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'CoverTaskQ_5',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.4)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -1.0 
  });
  
  key_answer_BT = new visual.TextStim({
    win: psychoJS.window,
    name: 'key_answer_BT',
    text: 'default text',
    font: 'Arial',
    units : undefined, 
    pos: [0, (- 0.45)], height: 0.02,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: -3.0 
  });
  
  // Initialize components for Routine "ISI"
  ISIClock = new util.Clock();
  ISIimage = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ISIimage', units : undefined, 
    image : 'images/isi.png', mask : undefined,
    ori : 0, pos : [0, 0], size : [0.2, 0.2],
    color : new util.Color([1, 1, 1]), opacity : 1,
    flipHoriz : false, flipVert : false,
    texRes : 128, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "EndScreen"
  EndScreenClock = new util.Clock();
  textEndScreen = new visual.TextStim({
    win: psychoJS.window,
    name: 'textEndScreen',
    text: "Congratulations on completing today's session. You may now close the window. ",
    font: 'Arial',
    units : undefined, 
    pos: [0, 0], height: 0.04,  wrapWidth: undefined, ori: 0,
    color: new util.Color('white'),  opacity: 1,
    depth: 0.0 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}

var t;
var frameN;
var keyWelcome;
var WelcomeScreenComponents;
function WelcomeScreenRoutineBegin() {
  //------Prepare to start Routine 'WelcomeScreen'-------
  t = 0;
  WelcomeScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keyWelcome = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  WelcomeScreenComponents = [];
  WelcomeScreenComponents.push(textWelcome);
  WelcomeScreenComponents.push(keyWelcome);
  
  for (const thisComponent of WelcomeScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var continueRoutine;
function WelcomeScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'WelcomeScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = WelcomeScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textWelcome* updates
  if (t >= 0.0 && textWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textWelcome.tStart = t;  // (not accounting for frame time here)
    textWelcome.frameNStart = frameN;  // exact frame index
    textWelcome.setAutoDraw(true);
  }

  
  // *keyWelcome* updates
  if (t >= 1 && keyWelcome.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWelcome.tStart = t;  // (not accounting for frame time here)
    keyWelcome.frameNStart = frameN;  // exact frame index
    keyWelcome.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWelcome.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keyWelcome.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWelcome.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      keyWelcome.rt = keyWelcome.clock.getTime();
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
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of WelcomeScreenComponents)
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


function WelcomeScreenRoutineEnd() {
  //------Ending Routine 'WelcomeScreen'-------
  for (const thisComponent of WelcomeScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (keyWelcome.keys === undefined || keyWelcome.keys.length === 0) {    // No response was made
      keyWelcome.keys = undefined;
  }
  
  psychoJS.experiment.addData('keyWelcome.keys', keyWelcome.keys);
  if (typeof keyWelcome.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('keyWelcome.rt', keyWelcome.rt);
      routineTimer.reset();
      }
  
  // the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}

var PracticeBlockLoop;
var currentLoop;
function PracticeBlockLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  PracticeBlockLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'StressWordLists.xlsx', '0:8'),
    seed: undefined, name: 'PracticeBlockLoop'});
  psychoJS.experiment.addLoop(PracticeBlockLoop); // add the loop to the experiment
  currentLoop = PracticeBlockLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisPracticeBlockLoop of PracticeBlockLoop) {
    thisScheduler.add(importConditions(PracticeBlockLoop));
    thisScheduler.add(PracticeBlockRoutineBegin);
    thisScheduler.add(PracticeBlockRoutineEachFrame);
    thisScheduler.add(PracticeBlockRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisPracticeBlockLoop));
  }

  return Scheduler.Event.NEXT;
}


function PracticeBlockLoopLoopEnd() {
  psychoJS.experiment.removeLoop(PracticeBlockLoop);

  return Scheduler.Event.NEXT;
}

var Block1Loop;
function Block1LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Block1Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'StressWordLists.xlsx', '8:92'),
    seed: undefined, name: 'Block1Loop'});
  psychoJS.experiment.addLoop(Block1Loop); // add the loop to the experiment
  currentLoop = Block1Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock1Loop of Block1Loop) {
    thisScheduler.add(importConditions(Block1Loop));
    thisScheduler.add(Block1RoutineBegin);
    thisScheduler.add(Block1RoutineEachFrame);
    thisScheduler.add(Block1RoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBlock1Loop));
  }

  return Scheduler.Event.NEXT;
}


function Block1LoopLoopEnd() {
  psychoJS.experiment.removeLoop(Block1Loop);

  return Scheduler.Event.NEXT;
}

var Block2Loop;
function Block2LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Block2Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'StressWordLists.xlsx', '92:176'),
    seed: undefined, name: 'Block2Loop'});
  psychoJS.experiment.addLoop(Block2Loop); // add the loop to the experiment
  currentLoop = Block2Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock2Loop of Block2Loop) {
    thisScheduler.add(importConditions(Block2Loop));
    thisScheduler.add(Block2RoutineBegin);
    thisScheduler.add(Block2RoutineEachFrame);
    thisScheduler.add(Block2RoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBlock2Loop));
  }

  return Scheduler.Event.NEXT;
}


function Block2LoopLoopEnd() {
  psychoJS.experiment.removeLoop(Block2Loop);

  return Scheduler.Event.NEXT;
}

var Block3Loop;
function Block3LoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  Block3Loop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'StressWordLists.xlsx', '176:260'),
    seed: undefined, name: 'Block3Loop'});
  psychoJS.experiment.addLoop(Block3Loop); // add the loop to the experiment
  currentLoop = Block3Loop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBlock3Loop of Block3Loop) {
    thisScheduler.add(importConditions(Block3Loop));
    thisScheduler.add(Block3RoutineBegin);
    thisScheduler.add(Block3RoutineEachFrame);
    thisScheduler.add(Block3RoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBlock3Loop));
  }

  return Scheduler.Event.NEXT;
}


function Block3LoopLoopEnd() {
  psychoJS.experiment.removeLoop(Block3Loop);

  return Scheduler.Event.NEXT;
}

var BaselineLoop;
function BaselineLoopLoopBegin(thisScheduler) {
  // set up handler to look after randomisation of conditions etc
  BaselineLoop = new TrialHandler({
    psychoJS: psychoJS,
    nReps: 1, method: TrialHandler.Method.SEQUENTIAL,
    extraInfo: expInfo, originPath: undefined,
    trialList: TrialHandler.importConditions(psychoJS.serverManager, 'StressWordLists.xlsx', '44:55'),
    seed: undefined, name: 'BaselineLoop'});
  psychoJS.experiment.addLoop(BaselineLoop); // add the loop to the experiment
  currentLoop = BaselineLoop;  // we're now the current loop

  // Schedule all the trials in the trialList:
  for (const thisBaselineLoop of BaselineLoop) {
    thisScheduler.add(importConditions(BaselineLoop));
    thisScheduler.add(BaselineTestRoutineBegin);
    thisScheduler.add(BaselineTestRoutineEachFrame);
    thisScheduler.add(BaselineTestRoutineEnd);
    thisScheduler.add(ISIRoutineBegin);
    thisScheduler.add(ISIRoutineEachFrame);
    thisScheduler.add(ISIRoutineEnd);
    thisScheduler.add(endLoopIteration(thisScheduler, thisBaselineLoop));
  }

  return Scheduler.Event.NEXT;
}


function BaselineLoopLoopEnd() {
  psychoJS.experiment.removeLoop(BaselineLoop);

  return Scheduler.Event.NEXT;
}

var key_resp_PB;
var PracticeBlockComponents;
function PracticeBlockRoutineBegin() {
  //------Prepare to start Routine 'PracticeBlock'-------
  t = 0;
  PracticeBlockClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  practiceTrials.setText(WordStim);
  CoverTaskQ.setText('Have you seen this word before?');
  key_resp_PB = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  PracticeBlockComponents = [];
  PracticeBlockComponents.push(practiceTrialImage);
  PracticeBlockComponents.push(practiceTrials);
  PracticeBlockComponents.push(CoverTaskQ);
  PracticeBlockComponents.push(key_resp_PB);
  PracticeBlockComponents.push(key_answer_PB);
  
  for (const thisComponent of PracticeBlockComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}

var frameRemains;
function PracticeBlockRoutineEachFrame() {
  //------Loop for each frame of Routine 'PracticeBlock'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PracticeBlockClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *practiceTrialImage* updates
  if (t >= 0.0 && practiceTrialImage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    practiceTrialImage.tStart = t;  // (not accounting for frame time here)
    practiceTrialImage.frameNStart = frameN;  // exact frame index
    practiceTrialImage.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (practiceTrialImage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    practiceTrialImage.setAutoDraw(false);
  }
  
  // *practiceTrials* updates
  if (t >= 0.0 && practiceTrials.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    practiceTrials.tStart = t;  // (not accounting for frame time here)
    practiceTrials.frameNStart = frameN;  // exact frame index
    practiceTrials.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (practiceTrials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    practiceTrials.setAutoDraw(false);
  }
  
  // *CoverTaskQ* updates
  if (t >= 0.0 && CoverTaskQ.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    CoverTaskQ.tStart = t;  // (not accounting for frame time here)
    CoverTaskQ.frameNStart = frameN;  // exact frame index
    CoverTaskQ.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (CoverTaskQ.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    CoverTaskQ.setAutoDraw(false);
  }
  
  // *key_resp_PB* updates
  if (t >= 0.0 && key_resp_PB.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_PB.tStart = t;  // (not accounting for frame time here)
    key_resp_PB.frameNStart = frameN;  // exact frame index
    key_resp_PB.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_PB.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_PB.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_PB.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_PB.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'y']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_PB.keys.length === 0) {  // then this was the first keypress
        key_resp_PB.keys = theseKeys[0];  // just the first key pressed
        key_resp_PB.rt = key_resp_PB.clock.getTime();
      }
    }
  }
  
  
  // *key_answer_PB* updates
  if (t >= 0.0 && key_answer_PB.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_answer_PB.tStart = t;  // (not accounting for frame time here)
    key_answer_PB.frameNStart = frameN;  // exact frame index
    key_answer_PB.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_answer_PB.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_answer_PB.setAutoDraw(false);
  }
  
  if (key_answer_PB.status === PsychoJS.Status.STARTED){ // only update if being drawn
    key_answer_PB.setText(key_resp_PB.keys);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of PracticeBlockComponents)
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


function PracticeBlockRoutineEnd() {
  //------Ending Routine 'PracticeBlock'-------
  for (const thisComponent of PracticeBlockComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_PB.keys === undefined || key_resp_PB.keys.length === 0) {    // No response was made
      key_resp_PB.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_PB.keys', key_resp_PB.keys);
  if (typeof key_resp_PB.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_PB.rt', key_resp_PB.rt);
      }
  
  return Scheduler.Event.NEXT;
}

var ISIComponents;
function ISIRoutineBegin() {
  //------Prepare to start Routine 'ISI'-------
  t = 0;
  ISIClock.reset(); // clock
  frameN = -1;
  routineTimer.add(0.500000);
  // update component parameters for each repeat
  // keep track of which components have finished
  ISIComponents = [];
  ISIComponents.push(ISIimage);
  
  for (const thisComponent of ISIComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function ISIRoutineEachFrame() {
  //------Loop for each frame of Routine 'ISI'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = ISIClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *ISIimage* updates
  if (t >= 0.0 && ISIimage.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    ISIimage.tStart = t;  // (not accounting for frame time here)
    ISIimage.frameNStart = frameN;  // exact frame index
    ISIimage.setAutoDraw(true);
  }

  frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (ISIimage.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    ISIimage.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of ISIComponents)
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


function ISIRoutineEnd() {
  //------Ending Routine 'ISI'-------
  for (const thisComponent of ISIComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var BlockIntroComponents;
function BlockIntroRoutineBegin() {
  //------Prepare to start Routine 'BlockIntro'-------
  t = 0;
  BlockIntroClock.reset(); // clock
  frameN = -1;
  routineTimer.add(1.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  BlockIntroComponents = [];
  BlockIntroComponents.push(TextBlockIntro);
  
  for (const thisComponent of BlockIntroComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function BlockIntroRoutineEachFrame() {
  //------Loop for each frame of Routine 'BlockIntro'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = BlockIntroClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *TextBlockIntro* updates
  if (t >= 0.0 && TextBlockIntro.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    TextBlockIntro.tStart = t;  // (not accounting for frame time here)
    TextBlockIntro.frameNStart = frameN;  // exact frame index
    TextBlockIntro.setAutoDraw(true);
  }

  frameRemains = 0.0 + 1 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (TextBlockIntro.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    TextBlockIntro.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of BlockIntroComponents)
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


function BlockIntroRoutineEnd() {
  //------Ending Routine 'BlockIntro'-------
  for (const thisComponent of BlockIntroComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var key_resp_B1;
var Block1Components;
function Block1RoutineBegin() {
  //------Prepare to start Routine 'Block1'-------
  t = 0;
  Block1Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  Block1Trials.setText(WordStim);
  CoverTaskQ_2.setText('Have you seen this word before?');
  key_resp_B1 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Block1Components = [];
  Block1Components.push(Block1Image);
  Block1Components.push(Block1Trials);
  Block1Components.push(CoverTaskQ_2);
  Block1Components.push(key_resp_B1);
  Block1Components.push(key_answer_B1);
  
  for (const thisComponent of Block1Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Block1RoutineEachFrame() {
  //------Loop for each frame of Routine 'Block1'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Block1Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Block1Image* updates
  if (t >= 0.0 && Block1Image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block1Image.tStart = t;  // (not accounting for frame time here)
    Block1Image.frameNStart = frameN;  // exact frame index
    Block1Image.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block1Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block1Image.setAutoDraw(false);
  }
  
  // *Block1Trials* updates
  if (t >= 0.0 && Block1Trials.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block1Trials.tStart = t;  // (not accounting for frame time here)
    Block1Trials.frameNStart = frameN;  // exact frame index
    Block1Trials.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block1Trials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block1Trials.setAutoDraw(false);
  }
  
  // *CoverTaskQ_2* updates
  if (t >= 0.0 && CoverTaskQ_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    CoverTaskQ_2.tStart = t;  // (not accounting for frame time here)
    CoverTaskQ_2.frameNStart = frameN;  // exact frame index
    CoverTaskQ_2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (CoverTaskQ_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    CoverTaskQ_2.setAutoDraw(false);
  }
  
  // *key_resp_B1* updates
  if (t >= 0.0 && key_resp_B1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_B1.tStart = t;  // (not accounting for frame time here)
    key_resp_B1.frameNStart = frameN;  // exact frame index
    key_resp_B1.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_B1.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_B1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_B1.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_B1.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'y']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_B1.keys.length === 0) {  // then this was the first keypress
        key_resp_B1.keys = theseKeys[0];  // just the first key pressed
        key_resp_B1.rt = key_resp_B1.clock.getTime();
      }
    }
  }
  
  
  // *key_answer_B1* updates
  if (t >= 0.0 && key_answer_B1.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_answer_B1.tStart = t;  // (not accounting for frame time here)
    key_answer_B1.frameNStart = frameN;  // exact frame index
    key_answer_B1.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_answer_B1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_answer_B1.setAutoDraw(false);
  }
  
  if (key_answer_B1.status === PsychoJS.Status.STARTED){ // only update if being drawn
    key_answer_B1.setText(key_resp_B1.keys);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Block1Components)
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


function Block1RoutineEnd() {
  //------Ending Routine 'Block1'-------
  for (const thisComponent of Block1Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_B1.keys === undefined || key_resp_B1.keys.length === 0) {    // No response was made
      key_resp_B1.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_B1.keys', key_resp_B1.keys);
  if (typeof key_resp_B1.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_B1.rt', key_resp_B1.rt);
      }
  
  return Scheduler.Event.NEXT;
}

var key_resp_B2;
var Block2Components;
function Block2RoutineBegin() {
  //------Prepare to start Routine 'Block2'-------
  t = 0;
  Block2Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  Block2Trials.setText(WordStim);
  CoverTaskQ_3.setText('Have you seen this word before?');
  key_resp_B2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Block2Components = [];
  Block2Components.push(Block2Image);
  Block2Components.push(Block2Trials);
  Block2Components.push(CoverTaskQ_3);
  Block2Components.push(key_resp_B2);
  Block2Components.push(key_answer_B2);
  
  for (const thisComponent of Block2Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Block2RoutineEachFrame() {
  //------Loop for each frame of Routine 'Block2'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Block2Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Block2Image* updates
  if (t >= 0.0 && Block2Image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block2Image.tStart = t;  // (not accounting for frame time here)
    Block2Image.frameNStart = frameN;  // exact frame index
    Block2Image.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block2Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block2Image.setAutoDraw(false);
  }
  
  // *Block2Trials* updates
  if (t >= 0.0 && Block2Trials.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block2Trials.tStart = t;  // (not accounting for frame time here)
    Block2Trials.frameNStart = frameN;  // exact frame index
    Block2Trials.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block2Trials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block2Trials.setAutoDraw(false);
  }
  
  // *CoverTaskQ_3* updates
  if (t >= 0.0 && CoverTaskQ_3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    CoverTaskQ_3.tStart = t;  // (not accounting for frame time here)
    CoverTaskQ_3.frameNStart = frameN;  // exact frame index
    CoverTaskQ_3.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (CoverTaskQ_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    CoverTaskQ_3.setAutoDraw(false);
  }
  
  // *key_resp_B2* updates
  if (t >= 0.0 && key_resp_B2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_B2.tStart = t;  // (not accounting for frame time here)
    key_resp_B2.frameNStart = frameN;  // exact frame index
    key_resp_B2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_B2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_B2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_B2.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_B2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'y']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_B2.keys.length === 0) {  // then this was the first keypress
        key_resp_B2.keys = theseKeys[0];  // just the first key pressed
        key_resp_B2.rt = key_resp_B2.clock.getTime();
      }
    }
  }
  
  
  // *key_answer_B2* updates
  if (t >= 0.0 && key_answer_B2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_answer_B2.tStart = t;  // (not accounting for frame time here)
    key_answer_B2.frameNStart = frameN;  // exact frame index
    key_answer_B2.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_answer_B2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_answer_B2.setAutoDraw(false);
  }
  
  if (key_answer_B2.status === PsychoJS.Status.STARTED){ // only update if being drawn
    key_answer_B2.setText(key_resp_B2.keys);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Block2Components)
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


function Block2RoutineEnd() {
  //------Ending Routine 'Block2'-------
  for (const thisComponent of Block2Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_B2.keys === undefined || key_resp_B2.keys.length === 0) {    // No response was made
      key_resp_B2.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_B2.keys', key_resp_B2.keys);
  if (typeof key_resp_B2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_B2.rt', key_resp_B2.rt);
      }
  
  return Scheduler.Event.NEXT;
}

var key_resp_B3;
var Block3Components;
function Block3RoutineBegin() {
  //------Prepare to start Routine 'Block3'-------
  t = 0;
  Block3Clock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  Block3trials.setText(WordStim);
  CoverTaskQ_4.setText('Have you seen this word before?');
  key_resp_B3 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  Block3Components = [];
  Block3Components.push(Block3Image);
  Block3Components.push(Block3trials);
  Block3Components.push(CoverTaskQ_4);
  Block3Components.push(key_resp_B3);
  Block3Components.push(key_answer_B3);
  
  for (const thisComponent of Block3Components)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function Block3RoutineEachFrame() {
  //------Loop for each frame of Routine 'Block3'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = Block3Clock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *Block3Image* updates
  if (t >= 0.0 && Block3Image.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block3Image.tStart = t;  // (not accounting for frame time here)
    Block3Image.frameNStart = frameN;  // exact frame index
    Block3Image.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block3Image.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block3Image.setAutoDraw(false);
  }
  
  // *Block3trials* updates
  if (t >= 0.0 && Block3trials.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    Block3trials.tStart = t;  // (not accounting for frame time here)
    Block3trials.frameNStart = frameN;  // exact frame index
    Block3trials.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (Block3trials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    Block3trials.setAutoDraw(false);
  }
  
  // *CoverTaskQ_4* updates
  if (t >= 0.0 && CoverTaskQ_4.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    CoverTaskQ_4.tStart = t;  // (not accounting for frame time here)
    CoverTaskQ_4.frameNStart = frameN;  // exact frame index
    CoverTaskQ_4.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (CoverTaskQ_4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    CoverTaskQ_4.setAutoDraw(false);
  }
  
  // *key_resp_B3* updates
  if (t >= 0.0 && key_resp_B3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_B3.tStart = t;  // (not accounting for frame time here)
    key_resp_B3.frameNStart = frameN;  // exact frame index
    key_resp_B3.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_B3.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_B3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_B3.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_B3.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'y']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_B3.keys.length === 0) {  // then this was the first keypress
        key_resp_B3.keys = theseKeys[0];  // just the first key pressed
        key_resp_B3.rt = key_resp_B3.clock.getTime();
      }
    }
  }
  
  
  // *key_answer_B3* updates
  if (t >= 0.0 && key_answer_B3.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_answer_B3.tStart = t;  // (not accounting for frame time here)
    key_answer_B3.frameNStart = frameN;  // exact frame index
    key_answer_B3.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_answer_B3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_answer_B3.setAutoDraw(false);
  }
  
  if (key_answer_B3.status === PsychoJS.Status.STARTED){ // only update if being drawn
    key_answer_B3.setText(key_resp_B3.keys);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of Block3Components)
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


function Block3RoutineEnd() {
  //------Ending Routine 'Block3'-------
  for (const thisComponent of Block3Components) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_B3.keys === undefined || key_resp_B3.keys.length === 0) {    // No response was made
      key_resp_B3.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_B3.keys', key_resp_B3.keys);
  if (typeof key_resp_B3.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_B3.rt', key_resp_B3.rt);
      }
  
  return Scheduler.Event.NEXT;
}

var PreBaselineBreakComponents;
function PreBaselineBreakRoutineBegin() {
  //------Prepare to start Routine 'PreBaselineBreak'-------
  t = 0;
  PreBaselineBreakClock.reset(); // clock
  frameN = -1;
  routineTimer.add(5.000000);
  // update component parameters for each repeat
  // keep track of which components have finished
  PreBaselineBreakComponents = [];
  PreBaselineBreakComponents.push(PreBaselineText);
  
  for (const thisComponent of PreBaselineBreakComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function PreBaselineBreakRoutineEachFrame() {
  //------Loop for each frame of Routine 'PreBaselineBreak'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = PreBaselineBreakClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *PreBaselineText* updates
  if (t >= 0.0 && PreBaselineText.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    PreBaselineText.tStart = t;  // (not accounting for frame time here)
    PreBaselineText.frameNStart = frameN;  // exact frame index
    PreBaselineText.setAutoDraw(true);
  }

  frameRemains = 0.0 + 5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (PreBaselineText.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    PreBaselineText.setAutoDraw(false);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of PreBaselineBreakComponents)
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


function PreBaselineBreakRoutineEnd() {
  //------Ending Routine 'PreBaselineBreak'-------
  for (const thisComponent of PreBaselineBreakComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  return Scheduler.Event.NEXT;
}

var key_resp_BT;
var BaselineTestComponents;
function BaselineTestRoutineBegin() {
  //------Prepare to start Routine 'BaselineTest'-------
  t = 0;
  BaselineTestClock.reset(); // clock
  frameN = -1;
  routineTimer.add(3.000000);
  // update component parameters for each repeat
  BaselineTestTrials.setText(WordStim);
  CoverTaskQ_5.setText('Have you seen this word before?');
  key_resp_BT = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  BaselineTestComponents = [];
  BaselineTestComponents.push(BaselineTestTrials);
  BaselineTestComponents.push(CoverTaskQ_5);
  BaselineTestComponents.push(key_resp_BT);
  BaselineTestComponents.push(key_answer_BT);
  
  for (const thisComponent of BaselineTestComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function BaselineTestRoutineEachFrame() {
  //------Loop for each frame of Routine 'BaselineTest'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = BaselineTestClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *BaselineTestTrials* updates
  if (t >= 0.0 && BaselineTestTrials.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    BaselineTestTrials.tStart = t;  // (not accounting for frame time here)
    BaselineTestTrials.frameNStart = frameN;  // exact frame index
    BaselineTestTrials.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (BaselineTestTrials.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    BaselineTestTrials.setAutoDraw(false);
  }
  
  // *CoverTaskQ_5* updates
  if (t >= 0.0 && CoverTaskQ_5.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    CoverTaskQ_5.tStart = t;  // (not accounting for frame time here)
    CoverTaskQ_5.frameNStart = frameN;  // exact frame index
    CoverTaskQ_5.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (CoverTaskQ_5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    CoverTaskQ_5.setAutoDraw(false);
  }
  
  // *key_resp_BT* updates
  if (t >= 0.0 && key_resp_BT.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_resp_BT.tStart = t;  // (not accounting for frame time here)
    key_resp_BT.frameNStart = frameN;  // exact frame index
    key_resp_BT.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { key_resp_BT.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_resp_BT.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_resp_BT.status = PsychoJS.Status.FINISHED;
  }

  if (key_resp_BT.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['n', 'y']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      if (key_resp_BT.keys.length === 0) {  // then this was the first keypress
        key_resp_BT.keys = theseKeys[0];  // just the first key pressed
        key_resp_BT.rt = key_resp_BT.clock.getTime();
      }
    }
  }
  
  
  // *key_answer_BT* updates
  if (t >= 0.0 && key_answer_BT.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    key_answer_BT.tStart = t;  // (not accounting for frame time here)
    key_answer_BT.frameNStart = frameN;  // exact frame index
    key_answer_BT.setAutoDraw(true);
  }

  frameRemains = 0.0 + 3 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
  if (key_answer_BT.status === PsychoJS.Status.STARTED && t >= frameRemains) {
    key_answer_BT.setAutoDraw(false);
  }
  
  if (key_answer_BT.status === PsychoJS.Status.STARTED){ // only update if being drawn
    key_answer_BT.setText(key_resp_BT.keys);
  }
  // check for quit (typically the Esc key)
  if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
    return psychoJS.quit('The [Escape] key was pressed. Goodbye!', false);
  }
  
  // check if the Routine should terminate
  if (!continueRoutine) {  // a component has requested a forced-end of Routine
    return Scheduler.Event.NEXT;
  }
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of BaselineTestComponents)
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


function BaselineTestRoutineEnd() {
  //------Ending Routine 'BaselineTest'-------
  for (const thisComponent of BaselineTestComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (key_resp_BT.keys === undefined || key_resp_BT.keys.length === 0) {    // No response was made
      key_resp_BT.keys = undefined;
  }
  
  psychoJS.experiment.addData('key_resp_BT.keys', key_resp_BT.keys);
  if (typeof key_resp_BT.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('key_resp_BT.rt', key_resp_BT.rt);
      }
  
  return Scheduler.Event.NEXT;
}

var keyWelcome_2;
var EndScreenComponents;
function EndScreenRoutineBegin() {
  //------Prepare to start Routine 'EndScreen'-------
  t = 0;
  EndScreenClock.reset(); // clock
  frameN = -1;
  // update component parameters for each repeat
  keyWelcome_2 = new core.BuilderKeyResponse(psychoJS);
  
  // keep track of which components have finished
  EndScreenComponents = [];
  EndScreenComponents.push(textEndScreen);
  EndScreenComponents.push(keyWelcome_2);
  
  for (const thisComponent of EndScreenComponents)
    if ('status' in thisComponent)
      thisComponent.status = PsychoJS.Status.NOT_STARTED;
  
  return Scheduler.Event.NEXT;
}


function EndScreenRoutineEachFrame() {
  //------Loop for each frame of Routine 'EndScreen'-------
  let continueRoutine = true; // until we're told otherwise
  // get current time
  t = EndScreenClock.getTime();
  frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
  // update/draw components on each frame
  
  // *textEndScreen* updates
  if (t >= 0.0 && textEndScreen.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    textEndScreen.tStart = t;  // (not accounting for frame time here)
    textEndScreen.frameNStart = frameN;  // exact frame index
    textEndScreen.setAutoDraw(true);
  }

  
  // *keyWelcome_2* updates
  if (t >= 1 && keyWelcome_2.status === PsychoJS.Status.NOT_STARTED) {
    // keep track of start time/frame for later
    keyWelcome_2.tStart = t;  // (not accounting for frame time here)
    keyWelcome_2.frameNStart = frameN;  // exact frame index
    keyWelcome_2.status = PsychoJS.Status.STARTED;
    // keyboard checking is just starting
    psychoJS.window.callOnFlip(function() { keyWelcome_2.clock.reset(); }); // t = 0 on screen flip
    psychoJS.eventManager.clearEvents({eventType:'keyboard'});
  }

  if (keyWelcome_2.status === PsychoJS.Status.STARTED) {
    let theseKeys = psychoJS.eventManager.getKeys({keyList:['space']});
    
    // check for quit:
    if (theseKeys.indexOf('escape') > -1) {
      psychoJS.experiment.experimentEnded = true;
    }
    
    if (theseKeys.length > 0) {  // at least one key was pressed
      keyWelcome_2.keys = theseKeys[theseKeys.length-1];  // just the last key pressed
      keyWelcome_2.rt = keyWelcome_2.clock.getTime();
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
  
  continueRoutine = false;  // reverts to True if at least one component still running
  for (const thisComponent of EndScreenComponents)
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


function EndScreenRoutineEnd() {
  //------Ending Routine 'EndScreen'-------
  for (const thisComponent of EndScreenComponents) {
    if (typeof thisComponent.setAutoDraw === 'function') {
      thisComponent.setAutoDraw(false);
    }
  }
  
  // check responses
  if (keyWelcome_2.keys === undefined || keyWelcome_2.keys.length === 0) {    // No response was made
      keyWelcome_2.keys = undefined;
  }
  
  psychoJS.experiment.addData('keyWelcome_2.keys', keyWelcome_2.keys);
  if (typeof keyWelcome_2.keys !== 'undefined') {  // we had a response
      psychoJS.experiment.addData('keyWelcome_2.rt', keyWelcome_2.rt);
      routineTimer.reset();
      }
  
  // the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
  routineTimer.reset();
  
  return Scheduler.Event.NEXT;
}


function endLoopIteration(thisScheduler, thisTrial) {
  // ------Prepare for next entry------
  return function () {
    // ------Check if user ended loop early------
    if (currentLoop.finished) {
      // Check for and save orphaned data
      if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
        psychoJS.experiment.nextEntry();
      }
      thisScheduler.stop();
    } else if (typeof thisTrial === 'undefined' || !('isTrials' in thisTrial) || thisTrial.isTrials) {
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
  // Check for and save orphaned data
  if (Object.keys(psychoJS.experiment._thisEntry).length > 0) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});

  return Scheduler.Event.QUIT;
}
