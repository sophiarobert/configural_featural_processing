#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2020.2.4),
    on Tue Nov  3 17:20:20 2020
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
expInfo = {'participant': '', 'design': '1', 'position': '2'}
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
from numpy.random import shuffle
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
height = 1.7296
width = 1.7296
width3deg = 2.5958
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

# Initialize components for Routine "prePrac1"
prePrac1Clock = core.Clock()
prePrac1 = 'Designs/prac_instr1.png'

prePracTargetImg1 = 'Stimuli/dory1.png'
prePracProbeImg1 = 'Stimuli/dory2.png'

if int(expInfo['position']) == 0:
    xPosition = 0
elif int(expInfo['position']) == 2:
    xPosition = (width3deg*x_scale)
elif int(expInfo['position']) == 1:
    xPosition = -(width3deg*x_scale)
elif int(expInfo['position']) == '3':
    xPosition = width3deg*x_scale
prac_instr1 = visual.ImageStim(
    win=win,
    name='prac_instr1', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_9 = keyboard.Keyboard()

# Initialize components for Routine "prePrac1_1"
prePrac1_1Clock = core.Clock()
image_6 = visual.ImageStim(
    win=win,
    name='image_6', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
text_8 = visual.TextStim(win=win, name='text_8',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_7 = visual.ImageStim(
    win=win,
    name='image_7', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "prePrac2"
prePrac2Clock = core.Clock()
if int(expInfo['design']) < 5:
    prePrac2 = 'Designs/prac_instr2_1234.png'
    prePrac1Corr = 'j'
elif int(expInfo['design']) > 4:
    prePrac2 = 'Designs/prac_instr2_5678.png'
    prePrac1Corr = 'f'

prePracTargetImg2 = 'Stimuli/nemo2.png'
prePracProbeImg2 = 'Stimuli/nemo2.png'

prac_instr2 = visual.ImageStim(
    win=win,
    name='prac_instr2', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
prePrac1Resp = keyboard.Keyboard()

# Initialize components for Routine "prePrac3"
prePrac3Clock = core.Clock()
prac_instr3_feedback = visual.ImageStim(
    win=win,
    name='prac_instr3_feedback', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_11 = keyboard.Keyboard()

# Initialize components for Routine "prePrac3_2"
prePrac3_2Clock = core.Clock()
image_8 = visual.ImageStim(
    win=win,
    name='image_8', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
text_9 = visual.TextStim(win=win, name='text_9',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
image_9 = visual.ImageStim(
    win=win,
    name='image_9', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)

# Initialize components for Routine "prePrac4"
prePrac4Clock = core.Clock()
if int(expInfo['design']) < 5:
    prePrac4 = 'Designs/prac_instr4_1234.png'
    prePrac2Corr = 'f'
    prePracFix = 'space'
elif int(expInfo['design']) > 4:
    prePrac4 = 'Designs/prac_instr4_5678.png'
    prePrac2Corr = 'j'
    prePracFix = 'space'
prac_instr4 = visual.ImageStim(
    win=win,
    name='prac_instr4', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_10 = keyboard.Keyboard()
key_resp_13 = keyboard.Keyboard()

# Initialize components for Routine "prePrac5"
prePrac5Clock = core.Clock()
if int(expInfo['design']) < 5:
    prePrac5 = 'Designs/prac_instr5_1234.png'
elif int(expInfo['design']) > 4:
    prePrac5 = 'Designs/prac_instr5_5678.png'
prac_instr5 = visual.ImageStim(
    win=win,
    name='prac_instr5', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "prac_instructions"
prac_instructionsClock = core.Clock()
pracCorr=''
corrFix =''
pTrial = 0
pfix_color_options = ['white','black']

prac_paths=''
samepTrials=''
diffpTrials=''
prac_paths = ['Stimuli/dory1.png','Stimuli/dory2.png','Stimuli/nemo1.jpg','Stimuli/nemo2.png']
sameCount = 0
diffCount = 0
samepTrials = [0,1,2,3,1,3]
shuffle(samepTrials)
diffpTrials = [[0,1],[1,0],[0,1],[2,3],[3,2],[2,3]]
shuffle(diffpTrials)
ptrial_order = [0,0,0,0,0,0,1,1,1,1,1,1]
shuffle(ptrial_order)

corrpFix =''
samePTrialid = 0
diffPTrialid = 0
numPTrials = 12
pfixs_shuffled1 = [1,0,0,0]
pfixs_shuffled2 = [1,0,0,1]
shuffle(pfixs_shuffled1)
shuffle(pfixs_shuffled2)
pfix_switch = [0,0]+pfixs_shuffled1+pfixs_shuffled2+[0,0]
side_same_prac = [0,0,0,1,1,1]
side_diff_prac = [0,0,0,1,1,1]



# Initialize components for Routine "prac_target"
prac_targetClock = core.Clock()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
text_6 = visual.TextStim(win=win, name='text_6',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "prac_probe"
prac_probeClock = core.Clock()
image_2 = visual.ImageStim(
    win=win,
    name='image_2', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=0.0)
text_7 = visual.TextStim(win=win, name='text_7',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
prac_resp = keyboard.Keyboard()
prac_fix_resp = keyboard.Keyboard()

# Initialize components for Routine "prac_feedback"
prac_feedbackClock = core.Clock()
image_3 = visual.ImageStim(
    win=win,
    name='image_3', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
feedback_msg = visual.TextStim(win=win, name='feedback_msg',
    text='default text',
    font='Arial',
    pos=(0, -0.25), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "startInstruct"
startInstructClock = core.Clock()
fix_color_options = ["white","black"];

if int(expInfo['design']) == 1:
    design_file = 'Designs/design1.csv'
elif int(expInfo['design']) == 2:
    design_file = 'Designs/design2.csv'
elif int(expInfo['design']) == 3:
    design_file = 'Designs/design3.csv'
elif int(expInfo['design']) == 4:
    design_file = 'Designs/design4.csv'
elif int(expInfo['design']) == 5:
    design_file = 'Designs/design5.csv'
elif int(expInfo['design']) == 6:
    design_file = 'Designs/design6.csv'
elif int(expInfo['design']) == 7:
    design_file = 'Designs/design7.csv'
elif int(expInfo['design']) == 8:
    design_file = 'Designs/design8.csv'
text_3 = visual.TextStim(win=win, name='text_3',
    text='Now you are ready to play the game!\n\nYou will be doing the same thing you just practiced, but with faces and houses.\n\nPress <SPACE> to see the instructions!',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "instrBlock"
instrBlockClock = core.Clock()
instructions_image = visual.ImageStim(
    win=win,
    name='instructions_image', 
    image='sin', mask=None,
    ori=0, pos=(0, 0), size=(0.75*1.5, 0.75),
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-1.0)
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "target_img"
target_imgClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
target_image = visual.ImageStim(
    win=win,
    name='target_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
key_resp_3 = keyboard.Keyboard()

# Initialize components for Routine "ISI_fix"
ISI_fixClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()

# Initialize components for Routine "probe_img"
probe_imgClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=-1.0);
probe_image = visual.ImageStim(
    win=win,
    name='probe_image', 
    image='sin', mask=None,
    ori=0, pos=[0,0], size=1.0,
    color=[1,1,1], colorSpace='rgb', opacity=1,
    flipHoriz=False, flipVert=False,
    texRes=512, interpolate=True, depth=-2.0)
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "trial_resp"
trial_respClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
good_job = visual.TextStim(win=win, name='good_job',
    text='Great Job!\n\nPress <SPACE> to keep going!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);
key_resp_8 = keyboard.Keyboard()

# Initialize components for Routine "EndScreen"
EndScreenClock = core.Clock()
allDone = visual.TextStim(win=win, name='allDone',
    text='You are all done. Thank you!',
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='black', colorSpace='rgb', opacity=1, 
    languageStyle='LTR',
    depth=0.0);

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

# the Routine "screen_scale" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prePrac1"-------
continueRoutine = True
# update component parameters for each repeat
prac_instr1.setImage(prePrac1)
key_resp_9.keys = []
key_resp_9.rt = []
_key_resp_9_allKeys = []
# keep track of which components have finished
prePrac1Components = [prac_instr1, key_resp_9]
for thisComponent in prePrac1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac1"-------
while continueRoutine:
    # get current time
    t = prePrac1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr1* updates
    if prac_instr1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr1.frameNStart = frameN  # exact frame index
        prac_instr1.tStart = t  # local t and not account for scr refresh
        prac_instr1.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr1, 'tStartRefresh')  # time at next scr refresh
        prac_instr1.setAutoDraw(True)
    
    # *key_resp_9* updates
    waitOnFlip = False
    if key_resp_9.status == NOT_STARTED and tThisFlip >= 2-frameTolerance:
        # keep track of start time/frame for later
        key_resp_9.frameNStart = frameN  # exact frame index
        key_resp_9.tStart = t  # local t and not account for scr refresh
        key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
        key_resp_9.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_9.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_9.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_9_allKeys.extend(theseKeys)
        if len(_key_resp_9_allKeys):
            key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
            key_resp_9.rt = _key_resp_9_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac1"-------
for thisComponent in prePrac1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prePrac1" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prePrac1_1"-------
continueRoutine = True
routineTimer.add(0.700000)
# update component parameters for each repeat
image_6.setPos((xPosition, 0))
image_6.setSize((width*x_scale,height*y_scale))
image_6.setImage(prePracTargetImg1)
image_7.setPos((xPosition, 0))
image_7.setSize((width*x_scale,height*y_scale))
image_7.setImage(prePracProbeImg1)
# keep track of which components have finished
prePrac1_1Components = [image_6, text_8, image_7]
for thisComponent in prePrac1_1Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac1_1Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac1_1"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prePrac1_1Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac1_1Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_6* updates
    if image_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_6.frameNStart = frameN  # exact frame index
        image_6.tStart = t  # local t and not account for scr refresh
        image_6.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_6, 'tStartRefresh')  # time at next scr refresh
        image_6.setAutoDraw(True)
    if image_6.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_6.tStartRefresh + 0.2-frameTolerance:
            # keep track of stop time/frame for later
            image_6.tStop = t  # not accounting for scr refresh
            image_6.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_6, 'tStopRefresh')  # time at next scr refresh
            image_6.setAutoDraw(False)
    
    # *text_8* updates
    if text_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_8.frameNStart = frameN  # exact frame index
        text_8.tStart = t  # local t and not account for scr refresh
        text_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
        text_8.setAutoDraw(True)
    if text_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_8.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            text_8.tStop = t  # not accounting for scr refresh
            text_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
            text_8.setAutoDraw(False)
    
    # *image_7* updates
    if image_7.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        image_7.frameNStart = frameN  # exact frame index
        image_7.tStart = t  # local t and not account for scr refresh
        image_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_7, 'tStartRefresh')  # time at next scr refresh
        image_7.setAutoDraw(True)
    if image_7.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_7.tStartRefresh + 0.2-frameTolerance:
            # keep track of stop time/frame for later
            image_7.tStop = t  # not accounting for scr refresh
            image_7.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_7, 'tStopRefresh')  # time at next scr refresh
            image_7.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac1_1Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac1_1"-------
for thisComponent in prePrac1_1Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_6.started', image_6.tStartRefresh)
thisExp.addData('image_6.stopped', image_6.tStopRefresh)
thisExp.addData('text_8.started', text_8.tStartRefresh)
thisExp.addData('text_8.stopped', text_8.tStopRefresh)
thisExp.addData('image_7.started', image_7.tStartRefresh)
thisExp.addData('image_7.stopped', image_7.tStopRefresh)

# ------Prepare to start Routine "prePrac2"-------
continueRoutine = True
# update component parameters for each repeat
prac_instr2.setImage(prePrac2)
prePrac1Resp.keys = []
prePrac1Resp.rt = []
_prePrac1Resp_allKeys = []
# keep track of which components have finished
prePrac2Components = [prac_instr2, prePrac1Resp]
for thisComponent in prePrac2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac2"-------
while continueRoutine:
    # get current time
    t = prePrac2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr2* updates
    if prac_instr2.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        prac_instr2.frameNStart = frameN  # exact frame index
        prac_instr2.tStart = t  # local t and not account for scr refresh
        prac_instr2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr2, 'tStartRefresh')  # time at next scr refresh
        prac_instr2.setAutoDraw(True)
    
    # *prePrac1Resp* updates
    waitOnFlip = False
    if prePrac1Resp.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        prePrac1Resp.frameNStart = frameN  # exact frame index
        prePrac1Resp.tStart = t  # local t and not account for scr refresh
        prePrac1Resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prePrac1Resp, 'tStartRefresh')  # time at next scr refresh
        prePrac1Resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(prePrac1Resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(prePrac1Resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if prePrac1Resp.status == STARTED and not waitOnFlip:
        theseKeys = prePrac1Resp.getKeys(keyList=['f', 'j'], waitRelease=False)
        _prePrac1Resp_allKeys.extend(theseKeys)
        if len(_prePrac1Resp_allKeys):
            prePrac1Resp.keys = _prePrac1Resp_allKeys[-1].name  # just the last key pressed
            prePrac1Resp.rt = _prePrac1Resp_allKeys[-1].rt
            # was this correct?
            if (prePrac1Resp.keys == str(prePrac1Corr)) or (prePrac1Resp.keys == prePrac1Corr):
                prePrac1Resp.corr = 1
            else:
                prePrac1Resp.corr = 0
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac2"-------
for thisComponent in prePrac2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_instr2.started', prac_instr2.tStartRefresh)
thisExp.addData('prac_instr2.stopped', prac_instr2.tStopRefresh)
# check responses
if prePrac1Resp.keys in ['', [], None]:  # No response was made
    prePrac1Resp.keys = None
    # was no response the correct answer?!
    if str(prePrac1Corr).lower() == 'none':
       prePrac1Resp.corr = 1;  # correct non-response
    else:
       prePrac1Resp.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('prePrac1Resp.keys',prePrac1Resp.keys)
thisExp.addData('prePrac1Resp.corr', prePrac1Resp.corr)
if prePrac1Resp.keys != None:  # we had a response
    thisExp.addData('prePrac1Resp.rt', prePrac1Resp.rt)
thisExp.addData('prePrac1Resp.started', prePrac1Resp.tStartRefresh)
thisExp.addData('prePrac1Resp.stopped', prePrac1Resp.tStopRefresh)
thisExp.nextEntry()
# the Routine "prePrac2" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prePrac3"-------
continueRoutine = True
# update component parameters for each repeat
if prePrac1Resp.keys == prePrac1Corr:
    prePrac3 = 'Designs/prac_instr3_corr.png'
elif prePrac1Resp.keys != prePrac1Corr:
    prePrac3 = 'Designs/prac_instr3_wrong.png'

if int(expInfo['position']) == 0:
    xPosition = 0
elif int(expInfo['position']) == 2:
    xPosition = -(width*x_scale)
elif int(expInfo['position']) == 1:
    xPosition = -(width*x_scale)
elif int(expInfo['position']) == '3':
    xPosition = width*x_scale
prac_instr3_feedback.setImage(prePrac3)
key_resp_11.keys = []
key_resp_11.rt = []
_key_resp_11_allKeys = []
# keep track of which components have finished
prePrac3Components = [prac_instr3_feedback, key_resp_11]
for thisComponent in prePrac3Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac3Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac3"-------
while continueRoutine:
    # get current time
    t = prePrac3Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac3Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr3_feedback* updates
    if prac_instr3_feedback.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr3_feedback.frameNStart = frameN  # exact frame index
        prac_instr3_feedback.tStart = t  # local t and not account for scr refresh
        prac_instr3_feedback.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr3_feedback, 'tStartRefresh')  # time at next scr refresh
        prac_instr3_feedback.setAutoDraw(True)
    
    # *key_resp_11* updates
    waitOnFlip = False
    if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_11.frameNStart = frameN  # exact frame index
        key_resp_11.tStart = t  # local t and not account for scr refresh
        key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
        key_resp_11.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_11.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_11.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_11_allKeys.extend(theseKeys)
        if len(_key_resp_11_allKeys):
            key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
            key_resp_11.rt = _key_resp_11_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac3Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac3"-------
for thisComponent in prePrac3Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prePrac3" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prePrac3_2"-------
continueRoutine = True
routineTimer.add(0.700000)
# update component parameters for each repeat
image_8.setPos((xPosition, 0))
image_8.setSize((width*x_scale,height*y_scale))
image_8.setImage(prePracTargetImg2)
image_9.setPos((xPosition, 0))
image_9.setSize((width*x_scale,height*y_scale))
image_9.setImage(prePracProbeImg2)
# keep track of which components have finished
prePrac3_2Components = [image_8, text_9, image_9]
for thisComponent in prePrac3_2Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac3_2Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac3_2"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prePrac3_2Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac3_2Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *image_8* updates
    if image_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image_8.frameNStart = frameN  # exact frame index
        image_8.tStart = t  # local t and not account for scr refresh
        image_8.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_8, 'tStartRefresh')  # time at next scr refresh
        image_8.setAutoDraw(True)
    if image_8.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_8.tStartRefresh + 0.2-frameTolerance:
            # keep track of stop time/frame for later
            image_8.tStop = t  # not accounting for scr refresh
            image_8.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_8, 'tStopRefresh')  # time at next scr refresh
            image_8.setAutoDraw(False)
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 0.7-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # *image_9* updates
    if image_9.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
        # keep track of start time/frame for later
        image_9.frameNStart = frameN  # exact frame index
        image_9.tStart = t  # local t and not account for scr refresh
        image_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image_9, 'tStartRefresh')  # time at next scr refresh
        image_9.setAutoDraw(True)
    if image_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > image_9.tStartRefresh + 0.2-frameTolerance:
            # keep track of stop time/frame for later
            image_9.tStop = t  # not accounting for scr refresh
            image_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(image_9, 'tStopRefresh')  # time at next scr refresh
            image_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac3_2Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac3_2"-------
for thisComponent in prePrac3_2Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('image_8.started', image_8.tStartRefresh)
thisExp.addData('image_8.stopped', image_8.tStopRefresh)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)
thisExp.addData('image_9.started', image_9.tStartRefresh)
thisExp.addData('image_9.stopped', image_9.tStopRefresh)

# ------Prepare to start Routine "prePrac4"-------
continueRoutine = True
routineTimer.add(9.000000)
# update component parameters for each repeat
prac_instr4.setImage(prePrac4)
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
key_resp_13.keys = []
key_resp_13.rt = []
_key_resp_13_allKeys = []
# keep track of which components have finished
prePrac4Components = [prac_instr4, key_resp_10, key_resp_13]
for thisComponent in prePrac4Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac4Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac4"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = prePrac4Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac4Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr4* updates
    if prac_instr4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr4.frameNStart = frameN  # exact frame index
        prac_instr4.tStart = t  # local t and not account for scr refresh
        prac_instr4.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr4, 'tStartRefresh')  # time at next scr refresh
        prac_instr4.setAutoDraw(True)
    if prac_instr4.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > prac_instr4.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            prac_instr4.tStop = t  # not accounting for scr refresh
            prac_instr4.frameNStop = frameN  # exact frame index
            win.timeOnFlip(prac_instr4, 'tStopRefresh')  # time at next scr refresh
            prac_instr4.setAutoDraw(False)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_10.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_10.tStop = t  # not accounting for scr refresh
            key_resp_10.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_10, 'tStopRefresh')  # time at next scr refresh
            key_resp_10.status = FINISHED
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # was this correct?
            if (key_resp_10.keys == str(prePracFix)) or (key_resp_10.keys == prePracFix):
                key_resp_10.corr = 1
            else:
                key_resp_10.corr = 0
    
    # *key_resp_13* updates
    waitOnFlip = False
    if key_resp_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_13.frameNStart = frameN  # exact frame index
        key_resp_13.tStart = t  # local t and not account for scr refresh
        key_resp_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_13, 'tStartRefresh')  # time at next scr refresh
        key_resp_13.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_13.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_13.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_13.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > key_resp_13.tStartRefresh + 9-frameTolerance:
            # keep track of stop time/frame for later
            key_resp_13.tStop = t  # not accounting for scr refresh
            key_resp_13.frameNStop = frameN  # exact frame index
            win.timeOnFlip(key_resp_13, 'tStopRefresh')  # time at next scr refresh
            key_resp_13.status = FINISHED
    if key_resp_13.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_13.getKeys(keyList=['f', 'j'], waitRelease=False)
        _key_resp_13_allKeys.extend(theseKeys)
        if len(_key_resp_13_allKeys):
            key_resp_13.keys = _key_resp_13_allKeys[-1].name  # just the last key pressed
            key_resp_13.rt = _key_resp_13_allKeys[-1].rt
            # was this correct?
            if (key_resp_13.keys == str(prePrac2Corr)) or (key_resp_13.keys == prePrac2Corr):
                key_resp_13.corr = 1
            else:
                key_resp_13.corr = 0
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac4Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac4"-------
for thisComponent in prePrac4Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('prac_instr4.started', prac_instr4.tStartRefresh)
thisExp.addData('prac_instr4.stopped', prac_instr4.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
    # was no response the correct answer?!
    if str(prePracFix).lower() == 'none':
       key_resp_10.corr = 1;  # correct non-response
    else:
       key_resp_10.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
thisExp.addData('key_resp_10.corr', key_resp_10.corr)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.nextEntry()
# check responses
if key_resp_13.keys in ['', [], None]:  # No response was made
    key_resp_13.keys = None
    # was no response the correct answer?!
    if str(prePrac2Corr).lower() == 'none':
       key_resp_13.corr = 1;  # correct non-response
    else:
       key_resp_13.corr = 0;  # failed to respond (incorrectly)
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_13.keys',key_resp_13.keys)
thisExp.addData('key_resp_13.corr', key_resp_13.corr)
if key_resp_13.keys != None:  # we had a response
    thisExp.addData('key_resp_13.rt', key_resp_13.rt)
thisExp.addData('key_resp_13.started', key_resp_13.tStartRefresh)
thisExp.addData('key_resp_13.stopped', key_resp_13.tStopRefresh)
thisExp.nextEntry()

# ------Prepare to start Routine "prePrac5"-------
continueRoutine = True
# update component parameters for each repeat
prac_instr5.setImage(prePrac5)
key_resp_12.keys = []
key_resp_12.rt = []
_key_resp_12_allKeys = []
# keep track of which components have finished
prePrac5Components = [prac_instr5, key_resp_12]
for thisComponent in prePrac5Components:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prePrac5Clock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prePrac5"-------
while continueRoutine:
    # get current time
    t = prePrac5Clock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prePrac5Clock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *prac_instr5* updates
    if prac_instr5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        prac_instr5.frameNStart = frameN  # exact frame index
        prac_instr5.tStart = t  # local t and not account for scr refresh
        prac_instr5.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(prac_instr5, 'tStartRefresh')  # time at next scr refresh
        prac_instr5.setAutoDraw(True)
    
    # *key_resp_12* updates
    waitOnFlip = False
    if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_12.frameNStart = frameN  # exact frame index
        key_resp_12.tStart = t  # local t and not account for scr refresh
        key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
        key_resp_12.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_12.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_12_allKeys.extend(theseKeys)
        if len(_key_resp_12_allKeys):
            key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
            key_resp_12.rt = _key_resp_12_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in prePrac5Components:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prePrac5"-------
for thisComponent in prePrac5Components:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prePrac5" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "prac_instructions"-------
continueRoutine = True
# update component parameters for each repeat
rand_Pstart = [0,1]
shuffle(rand_Pstart)
pfix_color = pfix_color_options[rand_Pstart[0]]
# keep track of which components have finished
prac_instructionsComponents = []
for thisComponent in prac_instructionsComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
prac_instructionsClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "prac_instructions"-------
while continueRoutine:
    # get current time
    t = prac_instructionsClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=prac_instructionsClock)
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
    for thisComponent in prac_instructionsComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "prac_instructions"-------
for thisComponent in prac_instructionsComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "prac_instructions" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
pTrials = data.TrialHandler(nReps=numPTrials, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=[None],
    seed=None, name='pTrials')
thisExp.addLoop(pTrials)  # add the loop to the experiment
thisPTrial = pTrials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPTrial.rgb)
if thisPTrial != None:
    for paramName in thisPTrial:
        exec('{} = thisPTrial[paramName]'.format(paramName))

for thisPTrial in pTrials:
    currentLoop = pTrials
    # abbreviate parameter names if possible (e.g. rgb = thisPTrial.rgb)
    if thisPTrial != None:
        for paramName in thisPTrial:
            exec('{} = thisPTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "prac_target"-------
    continueRoutine = True
    routineTimer.add(0.300000)
    # update component parameters for each repeat
    xPosition =''
    if pfix_switch[pTrial] == 1:
        corrPfix = 'space'
        if pfix_color == "white":
            pfix_color = pfix_color_options[1]
        else:
            pfix_color = pfix_color_options[0]
    else:
        pfix_color = pfix_color
        corrPfix = None
    
    if ptrial_order[pTrial] == 0:
        prac_target = prac_paths[samepTrials[sameCount]]
        prac_probe = prac_paths[samepTrials[sameCount]]
        if int(expInfo['design']) < 5:
            pracCorr = 'f'
        elif int(expInfo['design']) > 4:
            pracCorr = 'j'
        sameCount = sameCount + 1
    elif ptrial_order[pTrial] == 1:
        prac_target = prac_paths[diffpTrials[diffCount][0]]
        prac_probe = prac_paths[diffpTrials[diffCount][1]]
        if int(expInfo['design']) < 5:
            pracCorr = 'j'
        elif int(expInfo['design']) > 4:
            pracCorr = 'f'
        print(pracCorr)
        diffCount = diffCount + 1
    else:
        print('What is going on')
    
    if int(expInfo['position']) == 0:
        xPosition = 0
    elif int(expInfo['position']) == 2:
        if ptrial_order[pTrial]==1:
            if side_same_prac[samePTrialid] == 1: #left
                xPosition = -(width3deg*x_scale)
            elif side_same_prac[samePTrialid] == 0: #right
                xPosition = width3deg*x_scale
            samePTrialid += 1
        elif ptrial_order[pTrial]==0:
            if side_diff_prac[diffPTrialid] == 1: #left
                xPosition = -(width3deg*x_scale)
            elif side_diff_prac[diffPTrialid] == 0: #right
                xPosition = width3deg*x_scale
            diffPTrialid += 1
    elif int(expInfo['position']) == 1:
        xPosition = -(width3deg*x_scale)
    elif int(expInfo['position']) == '3':
        xPosition = width3deg*x_scale
    
    thisExp.addData('pfix_switches', pfix_switch[pTrial])
    thisExp.addData('Pside', xPosition)
    thisExp.addData('ptrial_type1S0D',ptrial_order[pTrial])
    thisExp.addData('ptarget',prac_target)
    thisExp.addData('pprobe',prac_probe)
    image.setPos((xPosition, 0))
    image.setSize((width*x_scale,height*y_scale))
    image.setImage(prac_target)
    text_6.setColor(pfix_color, colorSpace='rgb')
    # keep track of which components have finished
    prac_targetComponents = [image, text_6]
    for thisComponent in prac_targetComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_targetClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_target"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prac_targetClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_targetClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image* updates
        if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image.frameNStart = frameN  # exact frame index
            image.tStart = t  # local t and not account for scr refresh
            image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
            image.setAutoDraw(True)
        if image.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image.tStop = t  # not accounting for scr refresh
                image.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image, 'tStopRefresh')  # time at next scr refresh
                image.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 0.3-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_targetComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_target"-------
    for thisComponent in prac_targetComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pTrials.addData('image.started', image.tStartRefresh)
    pTrials.addData('image.stopped', image.tStopRefresh)
    pTrials.addData('text_6.started', text_6.tStartRefresh)
    pTrials.addData('text_6.stopped', text_6.tStopRefresh)
    
    # ------Prepare to start Routine "prac_probe"-------
    continueRoutine = True
    routineTimer.add(4.200000)
    # update component parameters for each repeat
    image_2.setPos((xPosition, 0))
    image_2.setSize((width*x_scale,height*y_scale))
    image_2.setImage(prac_probe)
    text_7.setColor(pfix_color, colorSpace='rgb')
    prac_resp.keys = []
    prac_resp.rt = []
    _prac_resp_allKeys = []
    prac_fix_resp.keys = []
    prac_fix_resp.rt = []
    _prac_fix_resp_allKeys = []
    # keep track of which components have finished
    prac_probeComponents = [image_2, text_7, prac_resp, prac_fix_resp]
    for thisComponent in prac_probeComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_probeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_probe"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prac_probeClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_probeClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_2* updates
        if image_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_2.frameNStart = frameN  # exact frame index
            image_2.tStart = t  # local t and not account for scr refresh
            image_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_2, 'tStartRefresh')  # time at next scr refresh
            image_2.setAutoDraw(True)
        if image_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_2.tStartRefresh + 0.2-frameTolerance:
                # keep track of stop time/frame for later
                image_2.tStop = t  # not accounting for scr refresh
                image_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_2, 'tStopRefresh')  # time at next scr refresh
                image_2.setAutoDraw(False)
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 4.2-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *prac_resp* updates
        waitOnFlip = False
        if prac_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            prac_resp.frameNStart = frameN  # exact frame index
            prac_resp.tStart = t  # local t and not account for scr refresh
            prac_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_resp, 'tStartRefresh')  # time at next scr refresh
            prac_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                prac_resp.tStop = t  # not accounting for scr refresh
                prac_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prac_resp, 'tStopRefresh')  # time at next scr refresh
                prac_resp.status = FINISHED
        if prac_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
            _prac_resp_allKeys.extend(theseKeys)
            if len(_prac_resp_allKeys):
                prac_resp.keys = _prac_resp_allKeys[-1].name  # just the last key pressed
                prac_resp.rt = _prac_resp_allKeys[-1].rt
                # was this correct?
                if (prac_resp.keys == str(pracCorr)) or (prac_resp.keys == pracCorr):
                    prac_resp.corr = 1
                else:
                    prac_resp.corr = 0
        
        # *prac_fix_resp* updates
        waitOnFlip = False
        if prac_fix_resp.status == NOT_STARTED and tThisFlip >= 0.2-frameTolerance:
            # keep track of start time/frame for later
            prac_fix_resp.frameNStart = frameN  # exact frame index
            prac_fix_resp.tStart = t  # local t and not account for scr refresh
            prac_fix_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(prac_fix_resp, 'tStartRefresh')  # time at next scr refresh
            prac_fix_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(prac_fix_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(prac_fix_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if prac_fix_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > prac_fix_resp.tStartRefresh + 4-frameTolerance:
                # keep track of stop time/frame for later
                prac_fix_resp.tStop = t  # not accounting for scr refresh
                prac_fix_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(prac_fix_resp, 'tStopRefresh')  # time at next scr refresh
                prac_fix_resp.status = FINISHED
        if prac_fix_resp.status == STARTED and not waitOnFlip:
            theseKeys = prac_fix_resp.getKeys(keyList=['space'], waitRelease=False)
            _prac_fix_resp_allKeys.extend(theseKeys)
            if len(_prac_fix_resp_allKeys):
                prac_fix_resp.keys = _prac_fix_resp_allKeys[-1].name  # just the last key pressed
                prac_fix_resp.rt = _prac_fix_resp_allKeys[-1].rt
                # was this correct?
                if (prac_fix_resp.keys == str(corrPfix)) or (prac_fix_resp.keys == corrPfix):
                    prac_fix_resp.corr = 1
                else:
                    prac_fix_resp.corr = 0
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_probeComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_probe"-------
    for thisComponent in prac_probeComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pTrials.addData('image_2.started', image_2.tStartRefresh)
    pTrials.addData('image_2.stopped', image_2.tStopRefresh)
    pTrials.addData('text_7.started', text_7.tStartRefresh)
    pTrials.addData('text_7.stopped', text_7.tStopRefresh)
    # check responses
    if prac_resp.keys in ['', [], None]:  # No response was made
        prac_resp.keys = None
        # was no response the correct answer?!
        if str(pracCorr).lower() == 'none':
           prac_resp.corr = 1;  # correct non-response
        else:
           prac_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for pTrials (TrialHandler)
    pTrials.addData('prac_resp.keys',prac_resp.keys)
    pTrials.addData('prac_resp.corr', prac_resp.corr)
    if prac_resp.keys != None:  # we had a response
        pTrials.addData('prac_resp.rt', prac_resp.rt)
    pTrials.addData('prac_resp.started', prac_resp.tStartRefresh)
    pTrials.addData('prac_resp.stopped', prac_resp.tStopRefresh)
    # check responses
    if prac_fix_resp.keys in ['', [], None]:  # No response was made
        prac_fix_resp.keys = None
        # was no response the correct answer?!
        if str(corrPfix).lower() == 'none':
           prac_fix_resp.corr = 1;  # correct non-response
        else:
           prac_fix_resp.corr = 0;  # failed to respond (incorrectly)
    # store data for pTrials (TrialHandler)
    pTrials.addData('prac_fix_resp.keys',prac_fix_resp.keys)
    pTrials.addData('prac_fix_resp.corr', prac_fix_resp.corr)
    if prac_fix_resp.keys != None:  # we had a response
        pTrials.addData('prac_fix_resp.rt', prac_fix_resp.rt)
    pTrials.addData('prac_fix_resp.started', prac_fix_resp.tStartRefresh)
    pTrials.addData('prac_fix_resp.stopped', prac_fix_resp.tStopRefresh)
    
    # ------Prepare to start Routine "prac_feedback"-------
    continueRoutine = True
    routineTimer.add(2.000000)
    # update component parameters for each repeat
    feedIM =''
    if prac_resp.keys == pracCorr: 
        if prac_fix_resp.keys == corrPfix:
            feedIM = 'Stimuli/greenCheck.png'
            prac_msg = 'Well done!'
        elif prac_fix_resp.keys != corrPfix:
            feedIM = 'Stimuli/redWrong.png'
            prac_msg = 'Oops, your picture response was right but the cross response was wrong.'
    elif prac_resp.keys != pracCorr:
        if prac_fix_resp.keys == corrPfix:
            feedIM = 'Stimuli/redWrong.png'
            prac_msg = 'Oops, your cross response was right but the picture response was wrong.'
        elif prac_fix_resp.keys != corrPfix:
            feedIM = 'Stimuli/redWrong.png'
            prac_msg = 'Oops, both responses were wrong.'
    
    print(prac_resp.keys)
    print(prac_fix_resp.keys)
    print(prac_msg)
    image_3.setImage(feedIM)
    feedback_msg.setText(prac_msg)
    # keep track of which components have finished
    prac_feedbackComponents = [image_3, feedback_msg]
    for thisComponent in prac_feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    prac_feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "prac_feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = prac_feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=prac_feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *image_3* updates
        if image_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            image_3.frameNStart = frameN  # exact frame index
            image_3.tStart = t  # local t and not account for scr refresh
            image_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(image_3, 'tStartRefresh')  # time at next scr refresh
            image_3.setAutoDraw(True)
        if image_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > image_3.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                image_3.tStop = t  # not accounting for scr refresh
                image_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(image_3, 'tStopRefresh')  # time at next scr refresh
                image_3.setAutoDraw(False)
        
        # *feedback_msg* updates
        if feedback_msg.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            feedback_msg.frameNStart = frameN  # exact frame index
            feedback_msg.tStart = t  # local t and not account for scr refresh
            feedback_msg.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(feedback_msg, 'tStartRefresh')  # time at next scr refresh
            feedback_msg.setAutoDraw(True)
        if feedback_msg.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > feedback_msg.tStartRefresh + 2-frameTolerance:
                # keep track of stop time/frame for later
                feedback_msg.tStop = t  # not accounting for scr refresh
                feedback_msg.frameNStop = frameN  # exact frame index
                win.timeOnFlip(feedback_msg, 'tStopRefresh')  # time at next scr refresh
                feedback_msg.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in prac_feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "prac_feedback"-------
    for thisComponent in prac_feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    pTrial = pTrial + 1
    pTrials.addData('image_3.started', image_3.tStartRefresh)
    pTrials.addData('image_3.stopped', image_3.tStopRefresh)
    pTrials.addData('feedback_msg.started', feedback_msg.tStartRefresh)
    pTrials.addData('feedback_msg.stopped', feedback_msg.tStopRefresh)
    thisExp.nextEntry()
    
# completed numPTrials repeats of 'pTrials'


# ------Prepare to start Routine "startInstruct"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
startInstructComponents = [text_3, key_resp_7]
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
    
    # *text_3* updates
    if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_3.frameNStart = frameN  # exact frame index
        text_3.tStart = t  # local t and not account for scr refresh
        text_3.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
        text_3.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
blocks = data.TrialHandler(nReps=2, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(design_file),
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
    
    # ------Prepare to start Routine "instrBlock"-------
    continueRoutine = True
    # update component parameters for each repeat
    img_size =''
    if Block_type == 'conf_face':
        img_size = (width*x_scale,height*y_scale)
        paths = ['Stimuli/edmd.png', 'Stimuli/eimd.png', 'Stimuli/eomu.png', 'Stimuli/eumu.png']
        if int(expInfo['design']) < 5:
            instruction_img = 'Designs/instructions_face_1234.png'
        else:
            instruction_img = 'Designs/instructions_face_5678.png'
    elif Block_type == 'conf_haus':
        img_size = (width*x_scale,height*y_scale)
        paths =  ['Stimuli/H-8sim0.png', 'Stimuli/H-8sim1.png', 'Stimuli/H-8sim2.png', 'Stimuli/H-8sim3.png']
        if int(expInfo['design']) < 5:
            instruction_img = 'Designs/instructions_haus_1234.png'
        else:
            instruction_img = 'Designs/instructions_haus_5678.png'
    elif Block_type == 'feat_face':
        img_size = (width*x_scale,height*y_scale)
        paths =  ['Stimuli/f15.png', 'Stimuli/f24.png', 'Stimuli/f131.png', 'Stimuli/f142.png']
        if int(expInfo['design']) < 5:
            instruction_img = 'Designs/instructions_face_1234.png'
        else:
            instruction_img = 'Designs/instructions_face_5678.png'
    elif Block_type == 'feat_haus':
        img_size = (width*x_scale,height*y_scale)
        paths = ['Stimuli/H5sim0.png', 'Stimuli/H6sim0.png', 'Stimuli/H7sim0.png', 'Stimuli/H8sim0.png']
        if int(expInfo['design']) < 5:
            instruction_img = 'Designs/instructions_haus_1234.png'
        else:
            instruction_img = 'Designs/instructions_haus_5678.png'
    
    sameTrialid = -1
    diffTrialid = -1
    sameTrial_left_id = -1
    diffTrial_left_id = -1
    sameTrial_right_id = -1
    diffTrial_right_id = -1
    trialID = -1;
    rand_start = [0,1]
    shuffle(rand_start)
    fix_color = fix_color_options[rand_start[0]]
    
    if int(expInfo['position']) == 2:
        trial_order = np.concatenate((permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6])))
        trial_order = np.round(trial_order / 6 - 0.1)
        trialSame_left = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
        trialDiff_left = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
        trialSame_right = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
        trialDiff_right = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
        diffTrial_left = list(range(12))
        shuffle(diffTrial_left)
        diffTrial_right = list(range(12))
        shuffle(diffTrial_right)
        numTrials = 48
        fixs_shuffled = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]
        shuffle(fixs_shuffled)
        fix_switch = [0,0]+fixs_shuffled+[0,0]
        side_same = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
        side_diff = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
        shuffle(side_same)
        shuffle(side_diff)
    elif int(expInfo['position']) == 1:
        trial_order = np.concatenate((permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6])))
        trial_order = np.round(trial_order / 6 - 0.1)
        trialSame = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
        trialDiff = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
        diffTrial = list(range(12))
        shuffle(diffTrial)
        numTrials = 24
        fixs_shuffled = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(fixs_shuffled)
        fix_switch = [0,0]+fixs_shuffled+[0,0]
    #    side = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    elif int(expInfo['position']) == 3:
        trial_order = np.concatenate((permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6]),permutation([1, 2, 3, 4, 5, 6])))
        trial_order = np.round(trial_order / 6 - 0.1)
        trialSame = np.concatenate((permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3]),permutation([0, 1, 2, 3])))
        trialDiff = np.array([(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (1, 0), (2, 3), (2, 0), (2, 1),(3, 0), (3, 1), (3, 2)])
        diffTrial = list(range(12))
        shuffle(diffTrial)
        numTrials = 24
        fixs_shuffled = [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        shuffle(fixs_shuffled)
        fix_switch = [0,0]+fixs_shuffled+[0,0]
    #    side = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    
    
    instructions_image.setImage(instruction_img)
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # keep track of which components have finished
    instrBlockComponents = [instructions_image, key_resp_2]
    for thisComponent in instrBlockComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    instrBlockClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "instrBlock"-------
    while continueRoutine:
        # get current time
        t = instrBlockClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=instrBlockClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instructions_image* updates
        if instructions_image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instructions_image.frameNStart = frameN  # exact frame index
            instructions_image.tStart = t  # local t and not account for scr refresh
            instructions_image.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instructions_image, 'tStartRefresh')  # time at next scr refresh
            instructions_image.setAutoDraw(True)
        
        # *key_resp_2* updates
        waitOnFlip = False
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 1-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instrBlockComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "instrBlock"-------
    for thisComponent in instrBlockComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # the Routine "instrBlock" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=numTrials, method='sequential', 
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
        img_pair = 0
        target = 0
        probe = 0
        corr = 0
        trialID = trialID + 1
        
        if fix_switch[trialID] == 1:
            if fix_color == "white":
                fix_color = fix_color_options[1]
            else:
                fix_color = fix_color_options[0]
        
        if int(expInfo['position']) == 0:
            xPosition = 0
        elif int(expInfo['position']) == 2:
            if trial_order[trialID]==1:
                sameTrialid += 1
                if side_same[sameTrialid] == 1: #left
                    xPosition = -(width*x_scale)
                    sameTrial_left_id += 1
                    print('left same ID: ' + str(sameTrial_left_id))
                    target = paths[trialSame_left[sameTrial_left_id]]
                    probe = paths[trialSame_left[sameTrial_left_id]]
                    if int(expInfo['design']) < 5:
                        corr = 'f'
                    elif int(expInfo['design']) > 4:
                        corr = 'j'
                elif side_same[sameTrialid] == 0: #right
                    xPosition = width*x_scale
                    sameTrial_right_id += 1
                    print('right same ID: ' + str(sameTrial_right_id))
                    target = paths[trialSame_right[sameTrial_right_id]]
                    probe = paths[trialSame_right[sameTrial_right_id]]
                    if int(expInfo['design']) < 5:
                        corr = 'f'
                    elif int(expInfo['design']) > 4:
                        corr = 'j'
            elif trial_order[trialID]==0:
                diffTrialid += 1
                if side_diff[diffTrialid] == 1: #left
                    xPosition = -(width*x_scale)
                    diffTrial_left_id += 1
                    print('left diff ID: ' + str(diffTrial_left_id))
                    img_pair = trialDiff_left[diffTrial_left[diffTrial_left_id]]
                    target = paths[img_pair[0]]
                    probe = paths[img_pair[1]]
                    if int(expInfo['design']) < 5:
                        corr = 'j'
                    elif int(expInfo['design']) > 4:
                        corr = 'f'
                elif side_diff[diffTrialid] == 0: #right
                    xPosition = width*x_scale
                    diffTrial_right_id += 1
                    print('right diff ID: ' + str(diffTrial_right_id))
                    img_pair = trialDiff_right[diffTrial_right[diffTrial_right_id]]
                    target = paths[img_pair[0]]
                    probe = paths[img_pair[1]]
                    if int(expInfo['design']) < 5:
                        corr = 'j'
                    elif int(expInfo['design']) > 4:
                        corr = 'f'
        elif int(expInfo['position']) == 1:
            xPosition = -(width*x_scale)
            if trial_order[trialID]==1:
                sameTrialid += 1
                target = paths[trialSame[sameTrialid]]
                probe = paths[trialSame[sameTrialid]]
                if int(expInfo['design']) < 5:
                    corr = 'f'
                elif int(expInfo['design']) > 4:
                    corr = 'j'
            elif trial_order[trialID]==0:
                diffTrialid += 1
                img_pair = trialDiff[diffTrial[diffTrialid]]
                target = paths[img_pair[0]]
                probe = paths[img_pair[1]]
                if int(expInfo['design']) < 5:
                    corr = 'j'
                elif int(expInfo['design']) > 4:
                    corr = 'f'
        elif expInfo['position'] == '3':
            xPosition = width*x_scale
            if trial_order[trialID]==1:
                sameTrialid += 1
                target = paths[trialSame[sameTrialid]]
                probe = paths[trialSame[sameTrialid]]
                if int(expInfo['design']) < 5:
                    corr = 'f'
                elif int(expInfo['design']) > 4:
                    corr = 'j'
            elif trial_order[trialID]==0:
                diffTrialid += 1
                img_pair = trialDiff[diffTrial[diffTrialid]]
                target = paths[img_pair[0]]
                probe = paths[img_pair[1]]
                if int(expInfo['design']) < 5:
                    corr = 'j'
                elif int(expInfo['design']) > 4:
                    corr = 'f'
        
        thisExp.addData('fix_switches', fix_switch[trialID])
        thisExp.addData('side', xPosition)
        thisExp.addData('trial_type1S0D',trial_order[trialID])
        thisExp.addData('target',target)
        thisExp.addData('probe',probe)
        text_4.setColor(fix_color, colorSpace='rgb')
        target_image.setPos((xPosition, 0))
        target_image.setSize(img_size)
        target_image.setImage(target)
        key_resp_3.keys = []
        key_resp_3.rt = []
        _key_resp_3_allKeys = []
        # keep track of which components have finished
        target_imgComponents = [text_4, target_image, key_resp_3]
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
            
            # *text_4* updates
            if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_4.frameNStart = frameN  # exact frame index
                text_4.tStart = t  # local t and not account for scr refresh
                text_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
                text_4.setAutoDraw(True)
            if text_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_4.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_4.tStop = t  # not accounting for scr refresh
                    text_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                    text_4.setAutoDraw(False)
            
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
            
            # *key_resp_3* updates
            waitOnFlip = False
            if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_3.frameNStart = frameN  # exact frame index
                key_resp_3.tStart = t  # local t and not account for scr refresh
                key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
                key_resp_3.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_3.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_3.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_3.tStop = t  # not accounting for scr refresh
                    key_resp_3.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                    key_resp_3.status = FINISHED
            if key_resp_3.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_3.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_3_allKeys.extend(theseKeys)
                if len(_key_resp_3_allKeys):
                    key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                    key_resp_3.rt = _key_resp_3_allKeys[-1].rt
            
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
        # check responses
        if key_resp_3.keys in ['', [], None]:  # No response was made
            key_resp_3.keys = None
        trials.addData('key_resp_3.keys',key_resp_3.keys)
        if key_resp_3.keys != None:  # we had a response
            trials.addData('key_resp_3.rt', key_resp_3.rt)
        
        # ------Prepare to start Routine "ISI_fix"-------
        continueRoutine = True
        routineTimer.add(0.300000)
        # update component parameters for each repeat
        text.setColor(fix_color, colorSpace='rgb')
        key_resp_4.keys = []
        key_resp_4.rt = []
        _key_resp_4_allKeys = []
        # keep track of which components have finished
        ISI_fixComponents = [text, key_resp_4]
        for thisComponent in ISI_fixComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        ISI_fixClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
        frameN = -1
        
        # -------Run Routine "ISI_fix"-------
        while continueRoutine and routineTimer.getTime() > 0:
            # get current time
            t = ISI_fixClock.getTime()
            tThisFlip = win.getFutureFlipTime(clock=ISI_fixClock)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *text* updates
            if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                text.setAutoDraw(True)
            if text.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text, 'tStopRefresh')  # time at next scr refresh
                    text.setAutoDraw(False)
            
            # *key_resp_4* updates
            waitOnFlip = False
            if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_4.frameNStart = frameN  # exact frame index
                key_resp_4.tStart = t  # local t and not account for scr refresh
                key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
                key_resp_4.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_4.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_4.tStartRefresh + 0.3-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_4.tStop = t  # not accounting for scr refresh
                    key_resp_4.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                    key_resp_4.status = FINISHED
            if key_resp_4.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_4.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_4_allKeys.extend(theseKeys)
                if len(_key_resp_4_allKeys):
                    key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                    key_resp_4.rt = _key_resp_4_allKeys[-1].rt
            
            # check for quit (typically the Esc key)
            if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
                core.quit()
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ISI_fixComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # -------Ending Routine "ISI_fix"-------
        for thisComponent in ISI_fixComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        # check responses
        if key_resp_4.keys in ['', [], None]:  # No response was made
            key_resp_4.keys = None
        trials.addData('key_resp_4.keys',key_resp_4.keys)
        if key_resp_4.keys != None:  # we had a response
            trials.addData('key_resp_4.rt', key_resp_4.rt)
        
        # ------Prepare to start Routine "probe_img"-------
        continueRoutine = True
        routineTimer.add(0.200000)
        # update component parameters for each repeat
        text_5.setColor(fix_color, colorSpace='rgb')
        probe_image.setPos((xPosition, 0))
        probe_image.setSize(img_size)
        probe_image.setImage(probe)
        key_resp_5.keys = []
        key_resp_5.rt = []
        _key_resp_5_allKeys = []
        # keep track of which components have finished
        probe_imgComponents = [text_5, probe_image, key_resp_5]
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
            
            # *text_5* updates
            if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_5.frameNStart = frameN  # exact frame index
                text_5.tStart = t  # local t and not account for scr refresh
                text_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
                text_5.setAutoDraw(True)
            if text_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    text_5.tStop = t  # not accounting for scr refresh
                    text_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(text_5, 'tStopRefresh')  # time at next scr refresh
                    text_5.setAutoDraw(False)
            
            # *probe_image* updates
            if probe_image.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                probe_image.frameNStart = frameN  # exact frame index
                probe_image.tStart = t  # local t and not account for scr refresh
                probe_image.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(probe_image, 'tStartRefresh')  # time at next scr refresh
                probe_image.setAutoDraw(True)
            if probe_image.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > probe_image.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    probe_image.tStop = t  # not accounting for scr refresh
                    probe_image.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(probe_image, 'tStopRefresh')  # time at next scr refresh
                    probe_image.setAutoDraw(False)
            
            # *key_resp_5* updates
            waitOnFlip = False
            if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_5.frameNStart = frameN  # exact frame index
                key_resp_5.tStart = t  # local t and not account for scr refresh
                key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
                key_resp_5.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_5.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > key_resp_5.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    key_resp_5.tStop = t  # not accounting for scr refresh
                    key_resp_5.frameNStop = frameN  # exact frame index
                    win.timeOnFlip(key_resp_5, 'tStopRefresh')  # time at next scr refresh
                    key_resp_5.status = FINISHED
            if key_resp_5.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_5_allKeys.extend(theseKeys)
                if len(_key_resp_5_allKeys):
                    key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                    key_resp_5.rt = _key_resp_5_allKeys[-1].rt
            
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
        # check responses
        if key_resp_5.keys in ['', [], None]:  # No response was made
            key_resp_5.keys = None
        trials.addData('key_resp_5.keys',key_resp_5.keys)
        if key_resp_5.keys != None:  # we had a response
            trials.addData('key_resp_5.rt', key_resp_5.rt)
        
        # ------Prepare to start Routine "trial_resp"-------
        continueRoutine = True
        # update component parameters for each repeat
        text_2.setColor(fix_color, colorSpace='rgb')
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        key_resp_6.keys = []
        key_resp_6.rt = []
        _key_resp_6_allKeys = []
        # keep track of which components have finished
        trial_respComponents = [text_2, key_resp, key_resp_6]
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
            
            # *text_2* updates
            if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_2.frameNStart = frameN  # exact frame index
                text_2.tStart = t  # local t and not account for scr refresh
                text_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
                text_2.setAutoDraw(True)
            
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
                theseKeys = key_resp.getKeys(keyList=['f', 'j'], waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    # was this correct?
                    if (key_resp.keys == str(corr)) or (key_resp.keys == corr):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *key_resp_6* updates
            waitOnFlip = False
            if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                key_resp_6.frameNStart = frameN  # exact frame index
                key_resp_6.tStart = t  # local t and not account for scr refresh
                key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
                key_resp_6.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp_6.status == STARTED and not waitOnFlip:
                theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
                _key_resp_6_allKeys.extend(theseKeys)
                if len(_key_resp_6_allKeys):
                    key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                    key_resp_6.rt = _key_resp_6_allKeys[-1].rt
            
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
            # was no response the correct answer?!
            if str(corr).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for trials (TrialHandler)
        trials.addData('key_resp.keys',key_resp.keys)
        trials.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            trials.addData('key_resp.rt', key_resp.rt)
        # check responses
        if key_resp_6.keys in ['', [], None]:  # No response was made
            key_resp_6.keys = None
        trials.addData('key_resp_6.keys',key_resp_6.keys)
        if key_resp_6.keys != None:  # we had a response
            trials.addData('key_resp_6.rt', key_resp_6.rt)
        trials.addData('key_resp_6.started', key_resp_6.tStartRefresh)
        trials.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
        # the Routine "trial_resp" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
    # completed numTrials repeats of 'trials'
    
    
    # ------Prepare to start Routine "feedback"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    # keep track of which components have finished
    feedbackComponents = [good_job, key_resp_8]
    for thisComponent in feedbackComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "feedback"-------
    while continueRoutine:
        # get current time
        t = feedbackClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *good_job* updates
        if good_job.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            good_job.frameNStart = frameN  # exact frame index
            good_job.tStart = t  # local t and not account for scr refresh
            good_job.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(good_job, 'tStartRefresh')  # time at next scr refresh
            good_job.setAutoDraw(True)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 2 repeats of 'blocks'


# ------Prepare to start Routine "EndScreen"-------
continueRoutine = True
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndScreenComponents = [allDone]
for thisComponent in EndScreenComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
EndScreenClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "EndScreen"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndScreenClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=EndScreenClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *allDone* updates
    if allDone.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        allDone.frameNStart = frameN  # exact frame index
        allDone.tStart = t  # local t and not account for scr refresh
        allDone.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(allDone, 'tStartRefresh')  # time at next scr refresh
        allDone.setAutoDraw(True)
    if allDone.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > allDone.tStartRefresh + 1.0-frameTolerance:
            # keep track of stop time/frame for later
            allDone.tStop = t  # not accounting for scr refresh
            allDone.frameNStop = frameN  # exact frame index
            win.timeOnFlip(allDone, 'tStopRefresh')  # time at next scr refresh
            allDone.setAutoDraw(False)
    
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
thisExp.addData('allDone.started', allDone.tStartRefresh)
thisExp.addData('allDone.stopped', allDone.tStopRefresh)

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
