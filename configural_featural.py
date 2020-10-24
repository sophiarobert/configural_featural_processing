#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Sat Oct 24 16:14:20 2020
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from __future__ import absolute_import, division

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock
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
psychopyVersion = '2020.2.4'
expName = 'configural_featural'  # from the Builder filename that created this script
expInfo = {'participant': 'SR', 'design': '1'}
dlg = gui.DlgFromDict(dictionary=expInfo, sort_keys=False, title=expName)
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
    originPath='/Users/sophia/Documents/PycharmProjects/Configural_Featural_Study/configural_featural.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.DEBUG)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(
    size=[1792, 1120], fullscr=True, screen=0, 
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

# Initialize components for Routine "screen_scale"
screen_scaleClock = core.Clock()
from numpy.random import permutation
oldt=0
x_size=8.560
y_size=5.398
screen_height=0

if win.units=='norm':
    x_scale=.05
    y_scale=.1
    dbase = .0001
    unittext=' norm units'
    vsize=2
elif win.units=='pix':
    x_scale=60
    y_scale=40
    dbase = .1
    unittext=' pixels'
    vsize=win.size[1]
else:
    x_scale=.05
    y_scale=.05
    dbase = .0001
    unittext=' height units'
    vsize=1

# h = tan(degrees = 2) x (distance = 49.53)
height = 3.459
width = 3.459
text_top = visual.TextStim(win=win, name='text_top',
    text='Resize this image to match the size of a credit card with arrow keys',
    font='Arial',
    pos=(0, 0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-3.0);
text_bottom = visual.TextStim(win=win, name='text_bottom',
    text='Press Space when you’re finished',
    font='Arial',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-4.0);
ccimage = visual.ImageStim(
    win=win,
    name='ccimage', 
    image='bankcard.png', mask=None,
    ori=0, pos=(0, 0), size=(x_size*x_scale, y_size*y_scale),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-5.0)

# Initialize components for Routine "startInstruct"
startInstructClock = core.Clock()

# Initialize components for Routine "instrBlock1"
instrBlock1Clock = core.Clock()

# Initialize components for Routine "target_img"
target_imgClock = core.Clock()
target_image = visual.ImageStim(
    win=win,
    name='target_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "probe_img"
probe_imgClock = core.Clock()
probe_image = visual.ImageStim(
    win=win,
    name='probe_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)

# Initialize components for Routine "trial_resp"
trial_respClock = core.Clock()
key_resp = keyboard.Keyboard()

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "screen_scale"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
screen_scaleComponents = [text_top, text_bottom, ccimage]
for thisComponent in screen_scaleComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
screen_scaleClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "screen_scale"-------
while continueRoutine:
    # get current time
    t = screen_scaleClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=screen_scaleClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    keys=event.getKeys()
    
    if len(keys):
        if t-oldt<.5:
            dscale=5*dbase
            oldt=t
        else:
            dscale=dbase
            oldt=t
        if 'space' in keys:
            continueRoutine=False
        elif 'up' in keys:
            y_scale=round((y_scale+dscale)*10000)/10000
        elif 'down' in keys:
            y_scale=round((y_scale-dscale)*10000)/10000
        elif 'left' in keys:
            x_scale=round((x_scale-dscale)*10000)/10000
        elif 'right' in keys:
            x_scale=round((x_scale+dscale)*10000)/10000
        screen_height=round(vsize*10/y_scale)/10
        ccimage.size=[x_size*x_scale, y_size*y_scale]
        
    
    # *text_top* updates
    if text_top.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_top.frameNStart = frameN  # exact frame index
        text_top.tStart = t  # local t and not account for scr refresh
        text_top.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_top, 'tStartRefresh')  # time at next scr refresh
        text_top.setAutoDraw(True)
    
    # *text_bottom* updates
    if text_bottom.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_bottom.frameNStart = frameN  # exact frame index
        text_bottom.tStart = t  # local t and not account for scr refresh
        text_bottom.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_bottom, 'tStartRefresh')  # time at next scr refresh
        text_bottom.setAutoDraw(True)
    
    # *ccimage* updates
    if ccimage.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        ccimage.frameNStart = frameN  # exact frame index
        ccimage.tStart = t  # local t and not account for scr refresh
        ccimage.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(ccimage, 'tStartRefresh')  # time at next scr refresh
        ccimage.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in screen_scaleComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "screen_scale"-------
for thisComponent in screen_scaleComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('X Scale',x_scale)
thisExp.addData('Y Scale',y_scale)

thisExp.addData('text_top.started', text_top.tStartRefresh)
thisExp.addData('text_top.stopped', text_top.tStopRefresh)
thisExp.addData('text_bottom.started', text_bottom.tStartRefresh)
thisExp.addData('text_bottom.stopped', text_bottom.tStopRefresh)
thisExp.addData('ccimage.started', ccimage.tStartRefresh)
thisExp.addData('ccimage.stopped', ccimage.tStopRefresh)
# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "startInstruct"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
startInstructComponents = []
for thisComponent in startInstructComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
startInstructClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "startInstruct"-------
while continueRoutine:
    # get current time
    t = startInstructClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=startInstructClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in startInstructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "startInstruct"-------
for thisComponent in startInstructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "startInstruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
blocks = data.TrialHandler(nReps=1, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('Designs/design1.csv'),
    seed=None, name='blocks')
thisExp.addLoop(blocks)  # add the loop to the experiment
thisBlock = blocks.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
if thisBlock != None:
    for paramName in thisBlock:
        exec('{} = thisBlock[paramName]'.format(paramName))

for thisBlock in blocks:
    currentLoop = blocks
    # abbreviate parameter names if possible (e.g. rgb = thisBlock.rgb)
    if thisBlock != None:
        for paramName in thisBlock:
            exec('{} = thisBlock[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "instrBlock1"-------
    continueRoutine = True
    # update component parameters for each repeat
    if Block_type == 'conf_face':
        paths = ['Stimuli/edmd.png', 'Stimuli/eimd.png', 'Stimuli/eomu.png', 'Stimuli/eumu.png']
    elif Block_type == 'conf_haus':
        paths =  ['Stimuli/H-8sim0.png', 'Stimuli/H-8sim1.png', 'Stimuli/H-8sim2.png', 'Stimuli/H-8sim3.png']
    elif Block_type == 'feat_face':
        paths =  ['Stimuli/f15.png', 'Stimuli/f24.png', 'Stimuli/f131.png', 'Stimuli/f142.png']
    elif Block_type == 'feat_haus':
        paths = ['Stimuli/H5sim0.png', 'Stimuli/H6sim0.png', 'Stimuli/H7sim0.png', 'Stimuli/H8sim0.png']
    
    trial_order = np.concatenate((permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]), permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6])))
    trial_order = np.round(trial_order / 6 - 0.1)
    trialSame = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
    trialDiff = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
    diffTrial = list(range(12))
    shuffle(diffTrial)
    
    sameTrialid = 0
    diffTrialid = 0
    trialID = -1;
    rand_start = shuffle([0,1]);
    fix_color = fix_color_options[rand_start[0]];
    fixs_shuffled = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    shuffle(fixs_shuffled)
    fix_switch = [0,0,fixs_shuffled,0,0]
    
    # keep track of which components have finished
    instrBlock1Components = []
    for thisComponent in instrBlock1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrBlock1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrBlock1"-------
    while continueRoutine:
        # get current time
        t = instrBlock1Clock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrBlock1Clock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrBlock1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrBlock1"-------
    for thisComponent in instrBlock1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instrBlock1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=[None],
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
        
        # ------Prepare to start Routine "target_img"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        trialID = trialID + 1
        if trial_order[trialID]==1:
            target = paths[trialSame[sameTrialid]]
            probe = paths[trialSame[sameTrialid]]
            sameTrialid += 1
        elif trial_order[trialID]==0:
            img_pair = trialDiff[diffTrial[diffTrialid]]
            target = paths[img_pair[0]]
            probe = paths[img_pair[1]]
            diffTrialid += 1
        target_image.setSize((width*x_scale,height*y_scale))
        target_image.setImage(target)
        # keep track of which components have finished
        target_imgComponents = [target_image]
        for thisComponent in target_imgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        target_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "target_img"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = target_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=target_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *target_image* updates
            if target_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                target_image.frameNStart = frameN  # exact frame index
                target_image.tStart = t  # local t and not account for scr refresh
                target_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(target_image, 'tStartRefresh')  # time at next scr refresh
                target_image.setAutoDraw(True)
            if target_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > target_image.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    target_image.tStop = t  # not accounting for scr refresh
                    target_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(target_image, 'tStopRefresh')  # time at next scr refresh
                    target_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in target_imgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "target_img"-------
        for thisComponent in target_imgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('target_image.started', target_image.tStartRefresh)
        trials.addData('target_image.stopped', target_image.tStopRefresh)
        
        # ------Prepare to start Routine "probe_img"-------
        continueRoutine = True
        routineTimer.add(0.800000)
        # update component parameters for each repeat
        probe_image.setSize((width*x_scale,height*y_scale))
        probe_image.setImage(probe)
        # keep track of which components have finished
        probe_imgComponents = [probe_image]
        for thisComponent in probe_imgComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        probe_imgClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "probe_img"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = probe_imgClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=probe_imgClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *probe_image* updates
            if probe_image.status == NOT_STARTED and tThisFlip >= 0.3-frameTolerance:
                # keep track of start time/frame for later
                probe_image.frameNStart = frameN  # exact frame index
                probe_image.tStart = t  # local t and not account for scr refresh
                probe_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_image, 'tStartRefresh')  # time at next scr refresh
                probe_image.setAutoDraw(True)
            if probe_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_image.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_image.tStop = t  # not accounting for scr refresh
                    probe_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probe_image, 'tStopRefresh')  # time at next scr refresh
                    probe_image.setAutoDraw(False)
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in probe_imgComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "probe_img"-------
        for thisComponent in probe_imgComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        trials.addData('probe_image.started', probe_image.tStartRefresh)
        trials.addData('probe_image.stopped', probe_image.tStopRefresh)
        
        # ------Prepare to start Routine "trial_resp"-------
        continueRoutine = True
        # update component parameters for each repeat
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        trial_respComponents = [key_resp]
        for thisComponent in trial_respComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        trial_respClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "trial_resp"-------
        while continueRoutine:
            # get current time
            t = trial_respClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=trial_respClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *key_resp* updates
            waitOnFlip = False
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['y', 'n', 'left', 'right', 'space'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trial_respComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "trial_resp"-------
        for thisComponent in trial_respComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        trials.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        trials.addData('key_resp.started', key_resp.tStartRefresh)
        trials.addData('key_resp.stopped', key_resp.tStopRefresh)
        # the Routine "trial_resp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed 1 repeats of 'trials'
    
# completed 1 repeats of 'blocks'


# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
