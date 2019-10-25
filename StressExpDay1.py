#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v3.1.5),
    on October 24, 2019, at 21:49
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
expName = 'StressExpDay1'  # from the Builder filename that created this script
expInfo = {'participant': '', 'session': '001'}
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
    originPath='C:\\Users\\amiracle\\Desktop\\CCNL\\StressExpDay1\\StressExpDay1.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=(1024, 768), fullscr=True, screen=0, 
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

# Initialize components for Routine "WelcomeScreen"
WelcomeScreenClock = core.Clock()
textWelcome = visual.TextStim(win=win, name='textWelcome',
    text='Thank you for your participation. For this task, you are going to be shown some words paired with images. You will be asked to remember the words and images later, so please pay attention to them. You will also be asked to determine whether you have been shown the current word displayed previously. To respond, you will answer "yes" with the \'y\' key or "no" with the \'n\' key using your keyboard. It is important you respond correctly. You may enter the correct key only once. You are going to be able to practice a few times before the real experiment begins. You will get a few one-minute breaks throughout the task, and after the breaks are over, the task will start again automatically. When you are ready, press the space bar to begin.',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "PracticeBlock"
PracticeBlockClock = core.Clock()
practiceTrialImage = visual.ImageStim(
    win=win,
    name='practiceTrialImage', 
    image='images/UCI.jpg', mask=None,
    ori=0, pos=(0, 0.2), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
practiceTrials = visual.TextStim(win=win, name='practiceTrials',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CoverTaskQ = visual.TextStim(win=win, name='CoverTaskQ',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_answer_PB = visual.TextStim(win=win, name='key_answer_PB',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIimage = visual.ImageStim(
    win=win,
    name='ISIimage', 
    image='images/isi.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "BlockIntro"
BlockIntroClock = core.Clock()
TextBlockIntro = visual.TextStim(win=win, name='TextBlockIntro',
    text='Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block1"
Block1Clock = core.Clock()
Block1Image = visual.ImageStim(
    win=win,
    name='Block1Image', 
    image='images/Bedroom.png', mask=None,
    ori=0, pos=(0, 0.2), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Block1Trials = visual.TextStim(win=win, name='Block1Trials',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CoverTaskQ_2 = visual.TextStim(win=win, name='CoverTaskQ_2',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_answer_B1 = visual.TextStim(win=win, name='key_answer_B1',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIimage = visual.ImageStim(
    win=win,
    name='ISIimage', 
    image='images/isi.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "BlockIntro"
BlockIntroClock = core.Clock()
TextBlockIntro = visual.TextStim(win=win, name='TextBlockIntro',
    text='Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block2"
Block2Clock = core.Clock()
Block2Image = visual.ImageStim(
    win=win,
    name='Block2Image', 
    image='images/Kitchen.png', mask=None,
    ori=0, pos=(0, 0.2), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Block2Trials = visual.TextStim(win=win, name='Block2Trials',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CoverTaskQ_3 = visual.TextStim(win=win, name='CoverTaskQ_3',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_answer_B2 = visual.TextStim(win=win, name='key_answer_B2',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIimage = visual.ImageStim(
    win=win,
    name='ISIimage', 
    image='images/isi.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "BlockIntro"
BlockIntroClock = core.Clock()
TextBlockIntro = visual.TextStim(win=win, name='TextBlockIntro',
    text='Please take a one minute break before continuing. The experiment will start again automatically after the break is over.\n\n',
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "Block3"
Block3Clock = core.Clock()
Block3Image = visual.ImageStim(
    win=win,
    name='Block3Image', 
    image='images/Livingroom.png', mask=None,
    ori=0, pos=(0, 0.2), size=(0.4, 0.4),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)
Block3trials = visual.TextStim(win=win, name='Block3trials',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
CoverTaskQ_4 = visual.TextStim(win=win, name='CoverTaskQ_4',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);
key_answer_B3 = visual.TextStim(win=win, name='key_answer_B3',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIimage = visual.ImageStim(
    win=win,
    name='ISIimage', 
    image='images/isi.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "PreBaselineBreak"
PreBaselineBreakClock = core.Clock()
PreBaselineText = visual.TextStim(win=win, name='PreBaselineText',
    text="Please take a two minute break. After two minutes, the experiment will continue. In the next part of this task, you will be asked if you recognize words you may have seen before. You will respond with either the 'y' key for yes, and the 'n' key for no. ",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Initialize components for Routine "BaselineTest"
BaselineTestClock = core.Clock()
BaselineTestTrials = visual.TextStim(win=win, name='BaselineTestTrials',
    text='default text',
    font='Arial',
    pos=(0, -0.1), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
CoverTaskQ_5 = visual.TextStim(win=win, name='CoverTaskQ_5',
    text='default text',
    font='Arial',
    pos=(0, -0.4), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_answer_BT = visual.TextStim(win=win, name='key_answer_BT',
    text='default text',
    font='Arial',
    pos=(0,-0.45), height=0.02, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);

# Initialize components for Routine "ISI"
ISIClock = core.Clock()
ISIimage = visual.ImageStim(
    win=win,
    name='ISIimage', 
    image='images/isi.png', mask=None,
    ori=0, pos=(0, 0), size=(0.2, 0.2),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=128, interpolate=True, depth=0.0)

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
textEndScreen = visual.TextStim(win=win, name='textEndScreen',
    text="Congratulations on completing today's session. You may now close the window. ",
    font='Arial',
    pos=(0, 0), height=0.04, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "WelcomeScreen"-------
t = 0
WelcomeScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyWelcome = keyboard.Keyboard()
# keep track of which components have finished
WelcomeScreenComponents = [textWelcome, keyWelcome]
for thisComponent in WelcomeScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "WelcomeScreen"-------
while continueRoutine:
    # get current time
    t = WelcomeScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textWelcome* updates
    if t >= 0.0 and textWelcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        textWelcome.tStart = t  # not accounting for scr refresh
        textWelcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(textWelcome, 'tStartRefresh')  # time at next scr refresh
        textWelcome.setAutoDraw(True)
    
    # *keyWelcome* updates
    if t >= 1 and keyWelcome.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyWelcome.tStart = t  # not accounting for scr refresh
        keyWelcome.frameNStart = frameN  # exact frame index
        win.timeOnFlip(keyWelcome, 'tStartRefresh')  # time at next scr refresh
        keyWelcome.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(keyWelcome.clock.reset)  # t=0 on next screen flip
        keyWelcome.clearEvents(eventType='keyboard')
    if keyWelcome.status == STARTED:
        theseKeys = keyWelcome.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWelcome.keys = theseKeys.name  # just the last key pressed
            keyWelcome.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in WelcomeScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "WelcomeScreen"-------
for thisComponent in WelcomeScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textWelcome.started', textWelcome.tStartRefresh)
thisExp.addData('textWelcome.stopped', textWelcome.tStopRefresh)
# check responses
if keyWelcome.keys in ['', [], None]:  # No response was made
    keyWelcome.keys = None
thisExp.addData('keyWelcome.keys',keyWelcome.keys)
if keyWelcome.keys != None:  # we had a response
    thisExp.addData('keyWelcome.rt', keyWelcome.rt)
thisExp.addData('keyWelcome.started', keyWelcome.tStartRefresh)
thisExp.addData('keyWelcome.stopped', keyWelcome.tStopRefresh)
thisExp.nextEntry()
# the Routine "WelcomeScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
PracticeBlockLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StressWordLists.xlsx', selection='0:8'),
    seed=None, name='PracticeBlockLoop')
thisExp.addLoop(PracticeBlockLoop)  # add the loop to the experiment
thisPracticeBlockLoop = PracticeBlockLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPracticeBlockLoop.rgb)
if thisPracticeBlockLoop != None:
    for paramName in thisPracticeBlockLoop:
        exec('{} = thisPracticeBlockLoop[paramName]'.format(paramName))

for thisPracticeBlockLoop in PracticeBlockLoop:
    currentLoop = PracticeBlockLoop
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeBlockLoop.rgb)
    if thisPracticeBlockLoop != None:
        for paramName in thisPracticeBlockLoop:
            exec('{} = thisPracticeBlockLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "PracticeBlock"-------
    t = 0
    PracticeBlockClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    practiceTrials.setText(WordStim)
    CoverTaskQ.setText('Have you seen this word before?')
    key_resp_PB = keyboard.Keyboard()
    # keep track of which components have finished
    PracticeBlockComponents = [practiceTrialImage, practiceTrials, CoverTaskQ, key_resp_PB, key_answer_PB]
    for thisComponent in PracticeBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "PracticeBlock"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = PracticeBlockClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *practiceTrialImage* updates
        if t >= 0.0 and practiceTrialImage.status == NOT_STARTED:
            # keep track of start time/frame for later
            practiceTrialImage.tStart = t  # not accounting for scr refresh
            practiceTrialImage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(practiceTrialImage, 'tStartRefresh')  # time at next scr refresh
            practiceTrialImage.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practiceTrialImage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            practiceTrialImage.tStop = t  # not accounting for scr refresh
            practiceTrialImage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practiceTrialImage, 'tStopRefresh')  # time at next scr refresh
            practiceTrialImage.setAutoDraw(False)
        
        # *practiceTrials* updates
        if t >= 0.0 and practiceTrials.status == NOT_STARTED:
            # keep track of start time/frame for later
            practiceTrials.tStart = t  # not accounting for scr refresh
            practiceTrials.frameNStart = frameN  # exact frame index
            win.timeOnFlip(practiceTrials, 'tStartRefresh')  # time at next scr refresh
            practiceTrials.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if practiceTrials.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            practiceTrials.tStop = t  # not accounting for scr refresh
            practiceTrials.frameNStop = frameN  # exact frame index
            win.timeOnFlip(practiceTrials, 'tStopRefresh')  # time at next scr refresh
            practiceTrials.setAutoDraw(False)
        
        # *CoverTaskQ* updates
        if t >= 0.0 and CoverTaskQ.status == NOT_STARTED:
            # keep track of start time/frame for later
            CoverTaskQ.tStart = t  # not accounting for scr refresh
            CoverTaskQ.frameNStart = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ, 'tStartRefresh')  # time at next scr refresh
            CoverTaskQ.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CoverTaskQ.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            CoverTaskQ.tStop = t  # not accounting for scr refresh
            CoverTaskQ.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ, 'tStopRefresh')  # time at next scr refresh
            CoverTaskQ.setAutoDraw(False)
        
        # *key_resp_PB* updates
        if t >= 0.0 and key_resp_PB.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_PB.tStart = t  # not accounting for scr refresh
            key_resp_PB.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_PB, 'tStartRefresh')  # time at next scr refresh
            key_resp_PB.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_PB.clock.reset)  # t=0 on next screen flip
            key_resp_PB.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_PB.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_PB.tStop = t  # not accounting for scr refresh
            key_resp_PB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_PB, 'tStopRefresh')  # time at next scr refresh
            key_resp_PB.status = FINISHED
        if key_resp_PB.status == STARTED:
            theseKeys = key_resp_PB.getKeys(keyList=['n', 'y'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_PB.keys == []:  # then this was the first keypress
                    key_resp_PB.keys = theseKeys.name  # just the first key pressed
                    key_resp_PB.rt = theseKeys.rt
        
        # *key_answer_PB* updates
        if t >= 0.0 and key_answer_PB.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer_PB.tStart = t  # not accounting for scr refresh
            key_answer_PB.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_answer_PB, 'tStartRefresh')  # time at next scr refresh
            key_answer_PB.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_answer_PB.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_answer_PB.tStop = t  # not accounting for scr refresh
            key_answer_PB.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_answer_PB, 'tStopRefresh')  # time at next scr refresh
            key_answer_PB.setAutoDraw(False)
        if key_answer_PB.status == STARTED:  # only update if drawing
            key_answer_PB.setText(key_resp_PB.keys, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in PracticeBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "PracticeBlock"-------
    for thisComponent in PracticeBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeBlockLoop.addData('practiceTrialImage.started', practiceTrialImage.tStartRefresh)
    PracticeBlockLoop.addData('practiceTrialImage.stopped', practiceTrialImage.tStopRefresh)
    PracticeBlockLoop.addData('practiceTrials.started', practiceTrials.tStartRefresh)
    PracticeBlockLoop.addData('practiceTrials.stopped', practiceTrials.tStopRefresh)
    PracticeBlockLoop.addData('CoverTaskQ.started', CoverTaskQ.tStartRefresh)
    PracticeBlockLoop.addData('CoverTaskQ.stopped', CoverTaskQ.tStopRefresh)
    # check responses
    if key_resp_PB.keys in ['', [], None]:  # No response was made
        key_resp_PB.keys = None
    PracticeBlockLoop.addData('key_resp_PB.keys',key_resp_PB.keys)
    if key_resp_PB.keys != None:  # we had a response
        PracticeBlockLoop.addData('key_resp_PB.rt', key_resp_PB.rt)
    PracticeBlockLoop.addData('key_resp_PB.started', key_resp_PB.tStartRefresh)
    PracticeBlockLoop.addData('key_resp_PB.stopped', key_resp_PB.tStopRefresh)
    PracticeBlockLoop.addData('key_answer_PB.started', key_answer_PB.tStartRefresh)
    PracticeBlockLoop.addData('key_answer_PB.stopped', key_answer_PB.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIimage]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIimage* updates
        if t >= 0.0 and ISIimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISIimage.tStart = t  # not accounting for scr refresh
            ISIimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStartRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISIimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISIimage.tStop = t  # not accounting for scr refresh
            ISIimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStopRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    PracticeBlockLoop.addData('ISIimage.started', ISIimage.tStartRefresh)
    PracticeBlockLoop.addData('ISIimage.stopped', ISIimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'PracticeBlockLoop'


# ------Prepare to start Routine "BlockIntro"-------
t = 0
BlockIntroClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
# keep track of which components have finished
BlockIntroComponents = [TextBlockIntro]
for thisComponent in BlockIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "BlockIntro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlockIntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextBlockIntro* updates
    if t >= 0.0 and TextBlockIntro.status == NOT_STARTED:
        # keep track of start time/frame for later
        TextBlockIntro.tStart = t  # not accounting for scr refresh
        TextBlockIntro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStartRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(True)
    frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TextBlockIntro.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        TextBlockIntro.tStop = t  # not accounting for scr refresh
        TextBlockIntro.frameNStop = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStopRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlockIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BlockIntro"-------
for thisComponent in BlockIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TextBlockIntro.started', TextBlockIntro.tStartRefresh)
thisExp.addData('TextBlockIntro.stopped', TextBlockIntro.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Block1Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StressWordLists.xlsx', selection='8:20'),
    seed=None, name='Block1Loop')
thisExp.addLoop(Block1Loop)  # add the loop to the experiment
thisBlock1Loop = Block1Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock1Loop.rgb)
if thisBlock1Loop != None:
    for paramName in thisBlock1Loop:
        exec('{} = thisBlock1Loop[paramName]'.format(paramName))

for thisBlock1Loop in Block1Loop:
    currentLoop = Block1Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock1Loop.rgb)
    if thisBlock1Loop != None:
        for paramName in thisBlock1Loop:
            exec('{} = thisBlock1Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block1"-------
    t = 0
    Block1Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Block1Trials.setText(WordStim)
    CoverTaskQ_2.setText('Have you seen this word before?')
    key_resp_B1 = keyboard.Keyboard()
    # keep track of which components have finished
    Block1Components = [Block1Image, Block1Trials, CoverTaskQ_2, key_resp_B1, key_answer_B1]
    for thisComponent in Block1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block1"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block1Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block1Image* updates
        if t >= 0.0 and Block1Image.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block1Image.tStart = t  # not accounting for scr refresh
            Block1Image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block1Image, 'tStartRefresh')  # time at next scr refresh
            Block1Image.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block1Image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block1Image.tStop = t  # not accounting for scr refresh
            Block1Image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block1Image, 'tStopRefresh')  # time at next scr refresh
            Block1Image.setAutoDraw(False)
        
        # *Block1Trials* updates
        if t >= 0.0 and Block1Trials.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block1Trials.tStart = t  # not accounting for scr refresh
            Block1Trials.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block1Trials, 'tStartRefresh')  # time at next scr refresh
            Block1Trials.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block1Trials.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block1Trials.tStop = t  # not accounting for scr refresh
            Block1Trials.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block1Trials, 'tStopRefresh')  # time at next scr refresh
            Block1Trials.setAutoDraw(False)
        
        # *CoverTaskQ_2* updates
        if t >= 0.0 and CoverTaskQ_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            CoverTaskQ_2.tStart = t  # not accounting for scr refresh
            CoverTaskQ_2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_2, 'tStartRefresh')  # time at next scr refresh
            CoverTaskQ_2.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CoverTaskQ_2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            CoverTaskQ_2.tStop = t  # not accounting for scr refresh
            CoverTaskQ_2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_2, 'tStopRefresh')  # time at next scr refresh
            CoverTaskQ_2.setAutoDraw(False)
        
        # *key_resp_B1* updates
        if t >= 0.0 and key_resp_B1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_B1.tStart = t  # not accounting for scr refresh
            key_resp_B1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_B1, 'tStartRefresh')  # time at next scr refresh
            key_resp_B1.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_B1.clock.reset)  # t=0 on next screen flip
            key_resp_B1.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_B1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_B1.tStop = t  # not accounting for scr refresh
            key_resp_B1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_B1, 'tStopRefresh')  # time at next scr refresh
            key_resp_B1.status = FINISHED
        if key_resp_B1.status == STARTED:
            theseKeys = key_resp_B1.getKeys(keyList=['n', 'y'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_B1.keys == []:  # then this was the first keypress
                    key_resp_B1.keys = theseKeys.name  # just the first key pressed
                    key_resp_B1.rt = theseKeys.rt
        
        # *key_answer_B1* updates
        if t >= 0.0 and key_answer_B1.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer_B1.tStart = t  # not accounting for scr refresh
            key_answer_B1.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_answer_B1, 'tStartRefresh')  # time at next scr refresh
            key_answer_B1.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_answer_B1.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_answer_B1.tStop = t  # not accounting for scr refresh
            key_answer_B1.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_answer_B1, 'tStopRefresh')  # time at next scr refresh
            key_answer_B1.setAutoDraw(False)
        if key_answer_B1.status == STARTED:  # only update if drawing
            key_answer_B1.setText(key_resp_B1.keys, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block1"-------
    for thisComponent in Block1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1Loop.addData('Block1Image.started', Block1Image.tStartRefresh)
    Block1Loop.addData('Block1Image.stopped', Block1Image.tStopRefresh)
    Block1Loop.addData('Block1Trials.started', Block1Trials.tStartRefresh)
    Block1Loop.addData('Block1Trials.stopped', Block1Trials.tStopRefresh)
    Block1Loop.addData('CoverTaskQ_2.started', CoverTaskQ_2.tStartRefresh)
    Block1Loop.addData('CoverTaskQ_2.stopped', CoverTaskQ_2.tStopRefresh)
    # check responses
    if key_resp_B1.keys in ['', [], None]:  # No response was made
        key_resp_B1.keys = None
    Block1Loop.addData('key_resp_B1.keys',key_resp_B1.keys)
    if key_resp_B1.keys != None:  # we had a response
        Block1Loop.addData('key_resp_B1.rt', key_resp_B1.rt)
    Block1Loop.addData('key_resp_B1.started', key_resp_B1.tStartRefresh)
    Block1Loop.addData('key_resp_B1.stopped', key_resp_B1.tStopRefresh)
    Block1Loop.addData('key_answer_B1.started', key_answer_B1.tStartRefresh)
    Block1Loop.addData('key_answer_B1.stopped', key_answer_B1.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIimage]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIimage* updates
        if t >= 0.0 and ISIimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISIimage.tStart = t  # not accounting for scr refresh
            ISIimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStartRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISIimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISIimage.tStop = t  # not accounting for scr refresh
            ISIimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStopRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block1Loop.addData('ISIimage.started', ISIimage.tStartRefresh)
    Block1Loop.addData('ISIimage.stopped', ISIimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block1Loop'


# ------Prepare to start Routine "BlockIntro"-------
t = 0
BlockIntroClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
# keep track of which components have finished
BlockIntroComponents = [TextBlockIntro]
for thisComponent in BlockIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "BlockIntro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlockIntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextBlockIntro* updates
    if t >= 0.0 and TextBlockIntro.status == NOT_STARTED:
        # keep track of start time/frame for later
        TextBlockIntro.tStart = t  # not accounting for scr refresh
        TextBlockIntro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStartRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(True)
    frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TextBlockIntro.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        TextBlockIntro.tStop = t  # not accounting for scr refresh
        TextBlockIntro.frameNStop = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStopRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlockIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BlockIntro"-------
for thisComponent in BlockIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TextBlockIntro.started', TextBlockIntro.tStartRefresh)
thisExp.addData('TextBlockIntro.stopped', TextBlockIntro.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Block2Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StressWordLists.xlsx', selection='93:103'),
    seed=None, name='Block2Loop')
thisExp.addLoop(Block2Loop)  # add the loop to the experiment
thisBlock2Loop = Block2Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock2Loop.rgb)
if thisBlock2Loop != None:
    for paramName in thisBlock2Loop:
        exec('{} = thisBlock2Loop[paramName]'.format(paramName))

for thisBlock2Loop in Block2Loop:
    currentLoop = Block2Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock2Loop.rgb)
    if thisBlock2Loop != None:
        for paramName in thisBlock2Loop:
            exec('{} = thisBlock2Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block2"-------
    t = 0
    Block2Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Block2Trials.setText(WordStim)
    CoverTaskQ_3.setText('Have you seen this word before?')
    key_resp_B2 = keyboard.Keyboard()
    # keep track of which components have finished
    Block2Components = [Block2Image, Block2Trials, CoverTaskQ_3, key_resp_B2, key_answer_B2]
    for thisComponent in Block2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block2"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block2Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block2Image* updates
        if t >= 0.0 and Block2Image.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block2Image.tStart = t  # not accounting for scr refresh
            Block2Image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block2Image, 'tStartRefresh')  # time at next scr refresh
            Block2Image.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block2Image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block2Image.tStop = t  # not accounting for scr refresh
            Block2Image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block2Image, 'tStopRefresh')  # time at next scr refresh
            Block2Image.setAutoDraw(False)
        
        # *Block2Trials* updates
        if t >= 0.0 and Block2Trials.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block2Trials.tStart = t  # not accounting for scr refresh
            Block2Trials.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block2Trials, 'tStartRefresh')  # time at next scr refresh
            Block2Trials.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block2Trials.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block2Trials.tStop = t  # not accounting for scr refresh
            Block2Trials.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block2Trials, 'tStopRefresh')  # time at next scr refresh
            Block2Trials.setAutoDraw(False)
        
        # *CoverTaskQ_3* updates
        if t >= 0.0 and CoverTaskQ_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            CoverTaskQ_3.tStart = t  # not accounting for scr refresh
            CoverTaskQ_3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_3, 'tStartRefresh')  # time at next scr refresh
            CoverTaskQ_3.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CoverTaskQ_3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            CoverTaskQ_3.tStop = t  # not accounting for scr refresh
            CoverTaskQ_3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_3, 'tStopRefresh')  # time at next scr refresh
            CoverTaskQ_3.setAutoDraw(False)
        
        # *key_resp_B2* updates
        if t >= 0.0 and key_resp_B2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_B2.tStart = t  # not accounting for scr refresh
            key_resp_B2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_B2, 'tStartRefresh')  # time at next scr refresh
            key_resp_B2.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_B2.clock.reset)  # t=0 on next screen flip
            key_resp_B2.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_B2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_B2.tStop = t  # not accounting for scr refresh
            key_resp_B2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_B2, 'tStopRefresh')  # time at next scr refresh
            key_resp_B2.status = FINISHED
        if key_resp_B2.status == STARTED:
            theseKeys = key_resp_B2.getKeys(keyList=['n', 'y'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_B2.keys == []:  # then this was the first keypress
                    key_resp_B2.keys = theseKeys.name  # just the first key pressed
                    key_resp_B2.rt = theseKeys.rt
        
        # *key_answer_B2* updates
        if t >= 0.0 and key_answer_B2.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer_B2.tStart = t  # not accounting for scr refresh
            key_answer_B2.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_answer_B2, 'tStartRefresh')  # time at next scr refresh
            key_answer_B2.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_answer_B2.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_answer_B2.tStop = t  # not accounting for scr refresh
            key_answer_B2.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_answer_B2, 'tStopRefresh')  # time at next scr refresh
            key_answer_B2.setAutoDraw(False)
        if key_answer_B2.status == STARTED:  # only update if drawing
            key_answer_B2.setText(key_resp_B2.keys, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block2"-------
    for thisComponent in Block2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block2Loop.addData('Block2Image.started', Block2Image.tStartRefresh)
    Block2Loop.addData('Block2Image.stopped', Block2Image.tStopRefresh)
    Block2Loop.addData('Block2Trials.started', Block2Trials.tStartRefresh)
    Block2Loop.addData('Block2Trials.stopped', Block2Trials.tStopRefresh)
    Block2Loop.addData('CoverTaskQ_3.started', CoverTaskQ_3.tStartRefresh)
    Block2Loop.addData('CoverTaskQ_3.stopped', CoverTaskQ_3.tStopRefresh)
    # check responses
    if key_resp_B2.keys in ['', [], None]:  # No response was made
        key_resp_B2.keys = None
    Block2Loop.addData('key_resp_B2.keys',key_resp_B2.keys)
    if key_resp_B2.keys != None:  # we had a response
        Block2Loop.addData('key_resp_B2.rt', key_resp_B2.rt)
    Block2Loop.addData('key_resp_B2.started', key_resp_B2.tStartRefresh)
    Block2Loop.addData('key_resp_B2.stopped', key_resp_B2.tStopRefresh)
    Block2Loop.addData('key_answer_B2.started', key_answer_B2.tStartRefresh)
    Block2Loop.addData('key_answer_B2.stopped', key_answer_B2.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIimage]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIimage* updates
        if t >= 0.0 and ISIimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISIimage.tStart = t  # not accounting for scr refresh
            ISIimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStartRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISIimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISIimage.tStop = t  # not accounting for scr refresh
            ISIimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStopRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block2Loop.addData('ISIimage.started', ISIimage.tStartRefresh)
    Block2Loop.addData('ISIimage.stopped', ISIimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block2Loop'


# ------Prepare to start Routine "BlockIntro"-------
t = 0
BlockIntroClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(60.000000)
# update component parameters for each repeat
# keep track of which components have finished
BlockIntroComponents = [TextBlockIntro]
for thisComponent in BlockIntroComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "BlockIntro"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = BlockIntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *TextBlockIntro* updates
    if t >= 0.0 and TextBlockIntro.status == NOT_STARTED:
        # keep track of start time/frame for later
        TextBlockIntro.tStart = t  # not accounting for scr refresh
        TextBlockIntro.frameNStart = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStartRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(True)
    frameRemains = 0.0 + 60- win.monitorFramePeriod * 0.75  # most of one frame period left
    if TextBlockIntro.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        TextBlockIntro.tStop = t  # not accounting for scr refresh
        TextBlockIntro.frameNStop = frameN  # exact frame index
        win.timeOnFlip(TextBlockIntro, 'tStopRefresh')  # time at next scr refresh
        TextBlockIntro.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in BlockIntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "BlockIntro"-------
for thisComponent in BlockIntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('TextBlockIntro.started', TextBlockIntro.tStartRefresh)
thisExp.addData('TextBlockIntro.stopped', TextBlockIntro.tStopRefresh)

# set up handler to look after randomisation of conditions etc
Block3Loop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StressWordLists.xlsx', selection='176:184'),
    seed=None, name='Block3Loop')
thisExp.addLoop(Block3Loop)  # add the loop to the experiment
thisBlock3Loop = Block3Loop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock3Loop.rgb)
if thisBlock3Loop != None:
    for paramName in thisBlock3Loop:
        exec('{} = thisBlock3Loop[paramName]'.format(paramName))

for thisBlock3Loop in Block3Loop:
    currentLoop = Block3Loop
    # abbreviate parameter names if possible (e.g. rgb = thisBlock3Loop.rgb)
    if thisBlock3Loop != None:
        for paramName in thisBlock3Loop:
            exec('{} = thisBlock3Loop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "Block3"-------
    t = 0
    Block3Clock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    Block3trials.setText(WordStim)
    CoverTaskQ_4.setText('Have you seen this word before?')
    key_resp_B3 = keyboard.Keyboard()
    # keep track of which components have finished
    Block3Components = [Block3Image, Block3trials, CoverTaskQ_4, key_resp_B3, key_answer_B3]
    for thisComponent in Block3Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "Block3"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = Block3Clock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Block3Image* updates
        if t >= 0.0 and Block3Image.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block3Image.tStart = t  # not accounting for scr refresh
            Block3Image.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block3Image, 'tStartRefresh')  # time at next scr refresh
            Block3Image.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block3Image.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block3Image.tStop = t  # not accounting for scr refresh
            Block3Image.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block3Image, 'tStopRefresh')  # time at next scr refresh
            Block3Image.setAutoDraw(False)
        
        # *Block3trials* updates
        if t >= 0.0 and Block3trials.status == NOT_STARTED:
            # keep track of start time/frame for later
            Block3trials.tStart = t  # not accounting for scr refresh
            Block3trials.frameNStart = frameN  # exact frame index
            win.timeOnFlip(Block3trials, 'tStartRefresh')  # time at next scr refresh
            Block3trials.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if Block3trials.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            Block3trials.tStop = t  # not accounting for scr refresh
            Block3trials.frameNStop = frameN  # exact frame index
            win.timeOnFlip(Block3trials, 'tStopRefresh')  # time at next scr refresh
            Block3trials.setAutoDraw(False)
        
        # *CoverTaskQ_4* updates
        if t >= 0.0 and CoverTaskQ_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            CoverTaskQ_4.tStart = t  # not accounting for scr refresh
            CoverTaskQ_4.frameNStart = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_4, 'tStartRefresh')  # time at next scr refresh
            CoverTaskQ_4.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CoverTaskQ_4.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            CoverTaskQ_4.tStop = t  # not accounting for scr refresh
            CoverTaskQ_4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_4, 'tStopRefresh')  # time at next scr refresh
            CoverTaskQ_4.setAutoDraw(False)
        
        # *key_resp_B3* updates
        if t >= 0.0 and key_resp_B3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_B3.tStart = t  # not accounting for scr refresh
            key_resp_B3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_B3, 'tStartRefresh')  # time at next scr refresh
            key_resp_B3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_B3.clock.reset)  # t=0 on next screen flip
            key_resp_B3.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_B3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_B3.tStop = t  # not accounting for scr refresh
            key_resp_B3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_B3, 'tStopRefresh')  # time at next scr refresh
            key_resp_B3.status = FINISHED
        if key_resp_B3.status == STARTED:
            theseKeys = key_resp_B3.getKeys(keyList=['n', 'y'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_B3.keys == []:  # then this was the first keypress
                    key_resp_B3.keys = theseKeys.name  # just the first key pressed
                    key_resp_B3.rt = theseKeys.rt
        
        # *key_answer_B3* updates
        if t >= 0.0 and key_answer_B3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer_B3.tStart = t  # not accounting for scr refresh
            key_answer_B3.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_answer_B3, 'tStartRefresh')  # time at next scr refresh
            key_answer_B3.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_answer_B3.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_answer_B3.tStop = t  # not accounting for scr refresh
            key_answer_B3.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_answer_B3, 'tStopRefresh')  # time at next scr refresh
            key_answer_B3.setAutoDraw(False)
        if key_answer_B3.status == STARTED:  # only update if drawing
            key_answer_B3.setText(key_resp_B3.keys, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Block3Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "Block3"-------
    for thisComponent in Block3Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block3Loop.addData('Block3Image.started', Block3Image.tStartRefresh)
    Block3Loop.addData('Block3Image.stopped', Block3Image.tStopRefresh)
    Block3Loop.addData('Block3trials.started', Block3trials.tStartRefresh)
    Block3Loop.addData('Block3trials.stopped', Block3trials.tStopRefresh)
    Block3Loop.addData('CoverTaskQ_4.started', CoverTaskQ_4.tStartRefresh)
    Block3Loop.addData('CoverTaskQ_4.stopped', CoverTaskQ_4.tStopRefresh)
    # check responses
    if key_resp_B3.keys in ['', [], None]:  # No response was made
        key_resp_B3.keys = None
    Block3Loop.addData('key_resp_B3.keys',key_resp_B3.keys)
    if key_resp_B3.keys != None:  # we had a response
        Block3Loop.addData('key_resp_B3.rt', key_resp_B3.rt)
    Block3Loop.addData('key_resp_B3.started', key_resp_B3.tStartRefresh)
    Block3Loop.addData('key_resp_B3.stopped', key_resp_B3.tStopRefresh)
    Block3Loop.addData('key_answer_B3.started', key_answer_B3.tStartRefresh)
    Block3Loop.addData('key_answer_B3.stopped', key_answer_B3.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIimage]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIimage* updates
        if t >= 0.0 and ISIimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISIimage.tStart = t  # not accounting for scr refresh
            ISIimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStartRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISIimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISIimage.tStop = t  # not accounting for scr refresh
            ISIimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStopRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    Block3Loop.addData('ISIimage.started', ISIimage.tStartRefresh)
    Block3Loop.addData('ISIimage.stopped', ISIimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'Block3Loop'


# ------Prepare to start Routine "PreBaselineBreak"-------
t = 0
PreBaselineBreakClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(120.000000)
# update component parameters for each repeat
# keep track of which components have finished
PreBaselineBreakComponents = [PreBaselineText]
for thisComponent in PreBaselineBreakComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "PreBaselineBreak"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = PreBaselineBreakClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *PreBaselineText* updates
    if t >= 0.0 and PreBaselineText.status == NOT_STARTED:
        # keep track of start time/frame for later
        PreBaselineText.tStart = t  # not accounting for scr refresh
        PreBaselineText.frameNStart = frameN  # exact frame index
        win.timeOnFlip(PreBaselineText, 'tStartRefresh')  # time at next scr refresh
        PreBaselineText.setAutoDraw(True)
    frameRemains = 0.0 + 120- win.monitorFramePeriod * 0.75  # most of one frame period left
    if PreBaselineText.status == STARTED and t >= frameRemains:
        # keep track of stop time/frame for later
        PreBaselineText.tStop = t  # not accounting for scr refresh
        PreBaselineText.frameNStop = frameN  # exact frame index
        win.timeOnFlip(PreBaselineText, 'tStopRefresh')  # time at next scr refresh
        PreBaselineText.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreBaselineBreakComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "PreBaselineBreak"-------
for thisComponent in PreBaselineBreakComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('PreBaselineText.started', PreBaselineText.tStartRefresh)
thisExp.addData('PreBaselineText.stopped', PreBaselineText.tStopRefresh)

# set up handler to look after randomisation of conditions etc
BaselineLoop = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('StressWordLists.xlsx', selection='44:55'),
    seed=None, name='BaselineLoop')
thisExp.addLoop(BaselineLoop)  # add the loop to the experiment
thisBaselineLoop = BaselineLoop.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBaselineLoop.rgb)
if thisBaselineLoop != None:
    for paramName in thisBaselineLoop:
        exec('{} = thisBaselineLoop[paramName]'.format(paramName))

for thisBaselineLoop in BaselineLoop:
    currentLoop = BaselineLoop
    # abbreviate parameter names if possible (e.g. rgb = thisBaselineLoop.rgb)
    if thisBaselineLoop != None:
        for paramName in thisBaselineLoop:
            exec('{} = thisBaselineLoop[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "BaselineTest"-------
    t = 0
    BaselineTestClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(3.000000)
    # update component parameters for each repeat
    BaselineTestTrials.setText(WordStim)
    CoverTaskQ_5.setText('Have you seen this word  before?')
    key_resp_BT = keyboard.Keyboard()
    # keep track of which components have finished
    BaselineTestComponents = [BaselineTestTrials, CoverTaskQ_5, key_resp_BT, key_answer_BT]
    for thisComponent in BaselineTestComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "BaselineTest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = BaselineTestClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *BaselineTestTrials* updates
        if t >= 0.0 and BaselineTestTrials.status == NOT_STARTED:
            # keep track of start time/frame for later
            BaselineTestTrials.tStart = t  # not accounting for scr refresh
            BaselineTestTrials.frameNStart = frameN  # exact frame index
            win.timeOnFlip(BaselineTestTrials, 'tStartRefresh')  # time at next scr refresh
            BaselineTestTrials.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if BaselineTestTrials.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            BaselineTestTrials.tStop = t  # not accounting for scr refresh
            BaselineTestTrials.frameNStop = frameN  # exact frame index
            win.timeOnFlip(BaselineTestTrials, 'tStopRefresh')  # time at next scr refresh
            BaselineTestTrials.setAutoDraw(False)
        
        # *CoverTaskQ_5* updates
        if t >= 0.0 and CoverTaskQ_5.status == NOT_STARTED:
            # keep track of start time/frame for later
            CoverTaskQ_5.tStart = t  # not accounting for scr refresh
            CoverTaskQ_5.frameNStart = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_5, 'tStartRefresh')  # time at next scr refresh
            CoverTaskQ_5.setAutoDraw(True)
        frameRemains = 0.0 + 3.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if CoverTaskQ_5.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            CoverTaskQ_5.tStop = t  # not accounting for scr refresh
            CoverTaskQ_5.frameNStop = frameN  # exact frame index
            win.timeOnFlip(CoverTaskQ_5, 'tStopRefresh')  # time at next scr refresh
            CoverTaskQ_5.setAutoDraw(False)
        
        # *key_resp_BT* updates
        if t >= 0.0 and key_resp_BT.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_BT.tStart = t  # not accounting for scr refresh
            key_resp_BT.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_resp_BT, 'tStartRefresh')  # time at next scr refresh
            key_resp_BT.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_BT.clock.reset)  # t=0 on next screen flip
            key_resp_BT.clearEvents(eventType='keyboard')
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_resp_BT.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_resp_BT.tStop = t  # not accounting for scr refresh
            key_resp_BT.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_BT, 'tStopRefresh')  # time at next scr refresh
            key_resp_BT.status = FINISHED
        if key_resp_BT.status == STARTED:
            theseKeys = key_resp_BT.getKeys(keyList=['n', 'y'], waitRelease=False)
            if len(theseKeys):
                theseKeys = theseKeys[0]  # at least one key was pressed
                
                # check for quit:
                if "escape" == theseKeys:
                    endExpNow = True
                if key_resp_BT.keys == []:  # then this was the first keypress
                    key_resp_BT.keys = theseKeys.name  # just the first key pressed
                    key_resp_BT.rt = theseKeys.rt
        
        # *key_answer_BT* updates
        if t >= 0.0 and key_answer_BT.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_answer_BT.tStart = t  # not accounting for scr refresh
            key_answer_BT.frameNStart = frameN  # exact frame index
            win.timeOnFlip(key_answer_BT, 'tStartRefresh')  # time at next scr refresh
            key_answer_BT.setAutoDraw(True)
        frameRemains = 0.0 + 3- win.monitorFramePeriod * 0.75  # most of one frame period left
        if key_answer_BT.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            key_answer_BT.tStop = t  # not accounting for scr refresh
            key_answer_BT.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_answer_BT, 'tStopRefresh')  # time at next scr refresh
            key_answer_BT.setAutoDraw(False)
        if key_answer_BT.status == STARTED:  # only update if drawing
            key_answer_BT.setText(key_resp_BT.keys, log=False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in BaselineTestComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "BaselineTest"-------
    for thisComponent in BaselineTestComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BaselineLoop.addData('BaselineTestTrials.started', BaselineTestTrials.tStartRefresh)
    BaselineLoop.addData('BaselineTestTrials.stopped', BaselineTestTrials.tStopRefresh)
    BaselineLoop.addData('CoverTaskQ_5.started', CoverTaskQ_5.tStartRefresh)
    BaselineLoop.addData('CoverTaskQ_5.stopped', CoverTaskQ_5.tStopRefresh)
    # check responses
    if key_resp_BT.keys in ['', [], None]:  # No response was made
        key_resp_BT.keys = None
    BaselineLoop.addData('key_resp_BT.keys',key_resp_BT.keys)
    if key_resp_BT.keys != None:  # we had a response
        BaselineLoop.addData('key_resp_BT.rt', key_resp_BT.rt)
    BaselineLoop.addData('key_resp_BT.started', key_resp_BT.tStartRefresh)
    BaselineLoop.addData('key_resp_BT.stopped', key_resp_BT.tStopRefresh)
    BaselineLoop.addData('key_answer_BT.started', key_answer_BT.tStartRefresh)
    BaselineLoop.addData('key_answer_BT.stopped', key_answer_BT.tStopRefresh)
    
    # ------Prepare to start Routine "ISI"-------
    t = 0
    ISIClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(0.500000)
    # update component parameters for each repeat
    # keep track of which components have finished
    ISIComponents = [ISIimage]
    for thisComponent in ISIComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "ISI"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = ISIClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *ISIimage* updates
        if t >= 0.0 and ISIimage.status == NOT_STARTED:
            # keep track of start time/frame for later
            ISIimage.tStart = t  # not accounting for scr refresh
            ISIimage.frameNStart = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStartRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if ISIimage.status == STARTED and t >= frameRemains:
            # keep track of stop time/frame for later
            ISIimage.tStop = t  # not accounting for scr refresh
            ISIimage.frameNStop = frameN  # exact frame index
            win.timeOnFlip(ISIimage, 'tStopRefresh')  # time at next scr refresh
            ISIimage.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in ISIComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "ISI"-------
    for thisComponent in ISIComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    BaselineLoop.addData('ISIimage.started', ISIimage.tStartRefresh)
    BaselineLoop.addData('ISIimage.stopped', ISIimage.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1 repeats of 'BaselineLoop'


# ------Prepare to start Routine "EndScreen"-------
t = 0
EndScreenClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
keyWelcome_2 = keyboard.Keyboard()
# keep track of which components have finished
EndScreenComponents = [textEndScreen, keyWelcome_2]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "EndScreen"-------
while continueRoutine:
    # get current time
    t = EndScreenClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *textEndScreen* updates
    if t >= 0.0 and textEndScreen.status == NOT_STARTED:
        # keep track of start time/frame for later
        textEndScreen.tStart = t  # not accounting for scr refresh
        textEndScreen.frameNStart = frameN  # exact frame index
        win.timeOnFlip(textEndScreen, 'tStartRefresh')  # time at next scr refresh
        textEndScreen.setAutoDraw(True)
    
    # *keyWelcome_2* updates
    if t >= 1 and keyWelcome_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        keyWelcome_2.tStart = t  # not accounting for scr refresh
        keyWelcome_2.frameNStart = frameN  # exact frame index
        win.timeOnFlip(keyWelcome_2, 'tStartRefresh')  # time at next scr refresh
        keyWelcome_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(keyWelcome_2.clock.reset)  # t=0 on next screen flip
        keyWelcome_2.clearEvents(eventType='keyboard')
    if keyWelcome_2.status == STARTED:
        theseKeys = keyWelcome_2.getKeys(keyList=['space'], waitRelease=False)
        if len(theseKeys):
            theseKeys = theseKeys[0]  # at least one key was pressed
            
            # check for quit:
            if "escape" == theseKeys:
                endExpNow = True
            keyWelcome_2.keys = theseKeys.name  # just the last key pressed
            keyWelcome_2.rt = theseKeys.rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndScreenComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "EndScreen"-------
for thisComponent in EndScreenComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('textEndScreen.started', textEndScreen.tStartRefresh)
thisExp.addData('textEndScreen.stopped', textEndScreen.tStopRefresh)
# check responses
if keyWelcome_2.keys in ['', [], None]:  # No response was made
    keyWelcome_2.keys = None
thisExp.addData('keyWelcome_2.keys',keyWelcome_2.keys)
if keyWelcome_2.keys != None:  # we had a response
    thisExp.addData('keyWelcome_2.rt', keyWelcome_2.rt)
thisExp.addData('keyWelcome_2.started', keyWelcome_2.tStartRefresh)
thisExp.addData('keyWelcome_2.stopped', keyWelcome_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "EndScreen" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
