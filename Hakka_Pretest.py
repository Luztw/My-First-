#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.83.03), 2016_01_18_1539
If you publish work using this script please cite the relevant PsychoPy publications
  Peirce, JW (2007) PsychoPy - Psychophysics software in Python. Journal of Neuroscience Methods, 162(1-2), 8-13.
  Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy. Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import division  # so that 1/3=0.333 instead of 1/3=0
from psychopy import locale_setup, visual, core, data, event, logging, sound, gui
from psychopy.constants import *  # things like STARTED, FINISHED
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import sin, cos, tan, log, log10, pi, average, sqrt, std, deg2rad, rad2deg, linspace, asarray
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys # to get file system encoding

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = u'\u0048\u0061\u006b\u006b\u0061\u005f\u0050\u0072\u0065\u0074\u0065\u0073\u0074'  # from the Builder filename that created this script
expInfo = {u'session': u'001', u'participant': u'',u'hand': u'',u'impaired': u'N',u'PoB': u'',u'age': u'',u'gender': u'001'}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False: core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + 'data/%s_%s_%s' %(expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=None,
    savePickle=True, saveWideText=True,
    dataFileName=filename)
#save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

# Setup the Window
win = visual.Window(size=(1280, 1024), fullscr=False, screen=0, allowGUI=False, allowStencil=False,
    monitor='testMonitor', color=[1.000,1.000,1.000], colorSpace='rgb',
    blendMode='avg', useFBO=True,
    )
# store frame rate of monitor if we can measure it successfully
expInfo['frameRate']=win.getActualFrameRate()
if expInfo['frameRate']!=None:
    frameDur = 1.0/round(expInfo['frameRate'])
else:
    frameDur = 1.0/60.0 # couldn't get a reliable measure so guess

# Initialize components for Routine "Intro"
IntroClock = core.Clock()
text = visual.TextStim(win=win, ori=0, name='text',
    text=u'\u5728\u672c\u5be6\u9a57\u4e2d\uff0c\u60a8\u5c07\u6703\u807d\u5230\u4e00\u7cfb\u5217\u7684\u55ae\u8a5e\n\u8acb\u5224\u65b7\u8a72\u55ae\u8a5e\u662f\u4e0d\u662f\u771f\u7684\u5ba2\u8a9e\u5b57\n\u82e5\u4e0d\u662f\u5ba2\u8a9e\u5b57\uff0c\u8acb\u6309\u0053\uff0c\u82e5\u662f\u5ba2\u8a9e\u5b57\n\u8acb\u6309L\u4e26\u8f38\u5165\u8a72\u5b57\u3002\n\u6309\u7a7a\u767d\u9375\u9032\u5165\u7df4\u7fd2\u984c',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=u'black', colorSpace='rgb', opacity=1,
    depth=-1.0)

# Initialize components for Routine "pre_trial"
pre_trialClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'\u8acb\u4ed4\u7d30\u8046\u807d',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Sound_Prac"
Sound_PracClock = core.Clock()
sound_1 = sound.Sound('A', secs=-1)
sound_1.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'S=\u4e0d\u662f\u5ba2\u8a9e  L=\u662f\u570b\u8a9e',    font=u'Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "PreFormal"
PreFormalClock = core.Clock()
text_5 = visual.TextStim(win=win, ori=0, name='text_5',
    text=u'\u7df4\u7fd2\u7d50\u675f\uff0c\u8acb\u6309\u7a7a\u767d\u9375\u9032\u5165\u6b63\u5f0f\u5be6\u9a57',    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "pre_trial"
pre_trialClock = core.Clock()
text_2 = visual.TextStim(win=win, ori=0, name='text_2',
    text=u'\u8acb\u4ed4\u7d30\u8046\u807d',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Initialize components for Routine "Sound"
SoundClock = core.Clock()
sound_2 = sound.Sound('A', secs=-1)
sound_2.setVolume(1)

# Initialize components for Routine "trial"
trialClock = core.Clock()
text_3 = visual.TextStim(win=win, ori=0, name='text_3',
    text=u'S=\u4e0d\u662f\u5ba2\u8a9e  L=\u662f\u5ba2\u8a9e',    font=u'Arial',
    pos=[0, -0.2], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)
text_4 = visual.TextStim(win=win, ori=0, name='text_4',
    text='default text',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=-2.0)

# Initialize components for Routine "End"
EndClock = core.Clock()
EndText = visual.TextStim(win=win, ori=0, name='EndText',
    text=u'\u5be6\u9a57\u7d50\u675f\uff0c\u8b1d\u8b1d\u53c3\u8207\uff01',    font='Arial',
    pos=[0, 0], height=0.1, wrapWidth=None,
    color=[-1.000,-1.000,-1.000], colorSpace='rgb', opacity=1,
    depth=0.0)

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

#------Prepare to start Routine "Intro"-------
t = 0
IntroClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_2 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_2.status = NOT_STARTED
# keep track of which components have finished
IntroComponents = []
IntroComponents.append(key_resp_2)
IntroComponents.append(text)
for thisComponent in IntroComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "Intro"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = IntroClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *key_resp_2* updates
    if t >= 0.0 and key_resp_2.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_2.tStart = t  # underestimates by a little under one frame
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_2.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_2.keys = theseKeys[-1]  # just the last key pressed
            key_resp_2.rt = key_resp_2.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # *text* updates
    if t >= 0.0 and text.status == NOT_STARTED:
        # keep track of start time/frame for later
        text.tStart = t  # underestimates by a little under one frame
        text.frameNStart = frameN  # exact frame index
        text.setAutoDraw(True)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in IntroComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "Intro"-------
for thisComponent in IntroComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
   key_resp_2.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.nextEntry()
# the Routine "Intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials_2 = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions(u'practiceList.xlsx'),
    seed=None, name='trials_2')#u'practiceList.xlsx'
thisExp.addLoop(trials_2)  # add the loop to the experiment
thisTrial_2 = trials_2.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial_2.rgb)
if thisTrial_2 != None:
    for paramName in thisTrial_2.keys():
        exec(paramName + '= thisTrial_2.' + paramName)

for thisTrial_2 in trials_2:
    currentLoop = trials_2
    # abbreviate parameter names if possible (e.g. rgb = thisTrial_2.rgb)
    if thisTrial_2 != None:
        for paramName in thisTrial_2.keys():
            exec(paramName + '= thisTrial_2.' + paramName)
    
    #------Prepare to start Routine "pre_trial"-------
    responseDLG = gui.Dlg(title = 'Test', pos = (400, 418))
    responseDLG.addField('', width = 45, lines = 4, multiLineText = True)
    t = 0
    pre_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pre_trialComponents = []
    pre_trialComponents.append(text_2)
    for thisComponent in pre_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pre_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pre_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if text_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pre_trial"-------
    for thisComponent in pre_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Sound_Prac"-------
    t = 0
    Sound_PracClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sound_1.setSound(Item_Practice, secs=-1)
    # keep track of which components have finished
    Sound_PracComponents = []
    Sound_PracComponents.append(sound_1)
    for thisComponent in Sound_PracComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Sound_Prac"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = Sound_PracClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_1
        if t >= 0.0 and sound_1.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_1.tStart = t  # underestimates by a little under one frame
            sound_1.frameNStart = frameN  # exact frame index
            sound_1.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Sound_PracComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED  or t<sound_1.getDuration()+0.5:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Sound_Prac"-------
    for thisComponent in Sound_PracComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_1.stop() #ensure sound has stopped at end of routine
    # the Routine "Sound_Prac" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    text_4.setText(u'\u8acb\u56de\u7b54')
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text_3)
    trialComponents.append(key_resp_3)
    trialComponents.append(text_4)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                #Show the dialogue box when pressing "c"
                if key_resp_3.keys == "l":
                    #And show the mouse cursor to click the buttons on the box
                    event.Mouse(visible=True)
                    responseDLG.show()
                    if responseDLG.OK:
                        trials_2.addData('comments', responseDLG.data)
                    else:
                        trials_2.addData('comments', None)
                    #hide the cursor again afterwards
                    event.Mouse(visible = False)
                else:
                    trials_2.addData('comments', None)
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for trials_2 (TrialHandler)
    trials_2.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials_2.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials_2'


#------Prepare to start Routine "PreFormal"-------
t = 0
PreFormalClock.reset()  # clock 
frameN = -1
# update component parameters for each repeat
key_resp_4 = event.BuilderKeyResponse()  # create an object of type KeyResponse
key_resp_4.status = NOT_STARTED
# keep track of which components have finished
PreFormalComponents = []
PreFormalComponents.append(text_5)
PreFormalComponents.append(key_resp_4)
for thisComponent in PreFormalComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "PreFormal"-------
continueRoutine = True
while continueRoutine:
    # get current time
    t = PreFormalClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_5* updates
    if t >= 0.0 and text_5.status == NOT_STARTED:
        # keep track of start time/frame for later
        text_5.tStart = t  # underestimates by a little under one frame
        text_5.frameNStart = frameN  # exact frame index
        text_5.setAutoDraw(True)
    
    # *key_resp_4* updates
    if t >= 0.0 and key_resp_4.status == NOT_STARTED:
        # keep track of start time/frame for later
        key_resp_4.tStart = t  # underestimates by a little under one frame
        key_resp_4.frameNStart = frameN  # exact frame index
        key_resp_4.status = STARTED
        # keyboard checking is just starting
        win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
        event.clearEvents(eventType='keyboard')
    if key_resp_4.status == STARTED:
        theseKeys = event.getKeys(keyList=['space'])
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            key_resp_4.keys = theseKeys[-1]  # just the last key pressed
            key_resp_4.rt = key_resp_4.clock.getTime()
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in PreFormalComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "PreFormal"-------
for thisComponent in PreFormalComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# check responses
if key_resp_4.keys in ['', [], None]:  # No response was made
   key_resp_4.keys=None
# store data for thisExp (ExperimentHandler)
thisExp.addData('key_resp_4.keys',key_resp_4.keys)
if key_resp_4.keys != None:  # we had a response
    thisExp.addData('key_resp_4.rt', key_resp_4.rt)
thisExp.nextEntry()
# the Routine "PreFormal" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=1, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('stimuliList.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb=thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial.keys():
        exec(paramName + '= thisTrial.' + paramName)

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial.keys():
            exec(paramName + '= thisTrial.' + paramName)
    
    #------Prepare to start Routine "pre_trial"-------
    responseDLG = gui.Dlg(title = 'Test', pos = (400, 418))
    responseDLG.addField('', width = 45, lines = 4, multiLineText = True)
    t = 0
    pre_trialClock.reset()  # clock 
    frameN = -1
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    # keep track of which components have finished
    pre_trialComponents = []
    pre_trialComponents.append(text_2)
    for thisComponent in pre_trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "pre_trial"-------
    continueRoutine = True
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = pre_trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_2* updates
        if t >= 0.0 and text_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_2.tStart = t  # underestimates by a little under one frame
            text_2.frameNStart = frameN  # exact frame index
            text_2.setAutoDraw(True)
        if text_2.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
            text_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in pre_trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "pre_trial"-------
    for thisComponent in pre_trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    #------Prepare to start Routine "Sound"-------
    t = 0
    SoundClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    sound_2.setSound(Item_Formal, secs=-1)
    # keep track of which components have finished
    SoundComponents = []
    SoundComponents.append(sound_2)
    for thisComponent in SoundComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "Sound"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = SoundClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # start/stop sound_2
        if t >= 0.0 and sound_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            sound_2.tStart = t  # underestimates by a little under one frame
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.play()  # start the sound (it finishes automatically)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in SoundComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED or t<sound_2.getDuration()+0.5:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "Sound"-------
    for thisComponent in SoundComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    sound_2.stop() #ensure sound has stopped at end of routine
    # the Routine "Sound" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    #------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock 
    frameN = -1
    # update component parameters for each repeat
    key_resp_3 = event.BuilderKeyResponse()  # create an object of type KeyResponse
    key_resp_3.status = NOT_STARTED
    text_4.setText(u'\u8acb\u56de\u7b54')
    # keep track of which components have finished
    trialComponents = []
    trialComponents.append(text_3)
    trialComponents.append(key_resp_3)
    trialComponents.append(text_4)
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    #-------Start Routine "trial"-------
    continueRoutine = True
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if t >= 0.0 and text_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_3.tStart = t  # underestimates by a little under one frame
            text_3.frameNStart = frameN  # exact frame index
            text_3.setAutoDraw(True)
        
        # *key_resp_3* updates
        if t >= 0.0 and key_resp_3.status == NOT_STARTED:
            # keep track of start time/frame for later
            key_resp_3.tStart = t  # underestimates by a little under one frame
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if key_resp_3.status == STARTED:
            theseKeys = event.getKeys(keyList=['s', 'l'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                key_resp_3.keys = theseKeys[-1]  # just the last key pressed
                key_resp_3.rt = key_resp_3.clock.getTime()
                #Show the dialogue box when pressing "c"
                if key_resp_3.keys == "l":
                    #And show the mouse cursor to click the buttons on the box
                    event.Mouse(visible=True)
                    responseDLG.show()
                    if responseDLG.OK:
                        trials.addData('comments', responseDLG.data)
                    else:
                        trials.addData('comments', None)
                    #hide the cursor again afterwards
                    event.Mouse(visible = False)
                else:
                    trials.addData('comments', None)
                # a response ends the routine
                continueRoutine = False
        
        # *text_4* updates
        if t >= 0.0 and text_4.status == NOT_STARTED:
            # keep track of start time/frame for later
            text_4.tStart = t  # underestimates by a little under one frame
            text_4.frameNStart = frameN  # exact frame index
            text_4.setAutoDraw(True)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    #-------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
       key_resp_3.keys=None
    # store data for trials (TrialHandler)
    trials.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        trials.addData('key_resp_3.rt', key_resp_3.rt)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1 repeats of 'trials'


#------Prepare to start Routine "End"-------
t = 0
EndClock.reset()  # clock 
frameN = -1
routineTimer.add(1.000000)
# update component parameters for each repeat
# keep track of which components have finished
EndComponents = []
EndComponents.append(EndText)
for thisComponent in EndComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

#-------Start Routine "End"-------
continueRoutine = True
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = EndClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *EndText* updates
    if t >= 0.0 and EndText.status == NOT_STARTED:
        # keep track of start time/frame for later
        EndText.tStart = t  # underestimates by a little under one frame
        EndText.frameNStart = frameN  # exact frame index
        EndText.setAutoDraw(True)
    if EndText.status == STARTED and t >= (0.0 + (1.0-win.monitorFramePeriod*0.75)): #most of one frame period left
        EndText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in EndComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

#-------Ending Routine "End"-------
for thisComponent in EndComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
win.close()
core.quit()
