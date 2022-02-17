#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import, division


from psychopy import gui, visual, core, data, event, logging, clock, colors
import numpy as np  
from numpy.random import random, choice as randchoice
import os 
import sys  
import random
import copy

# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath("/Users/udeozormi/Desktop/reinstatementParty1/Replay_VScode.py"))

# Store info about the experiment session
psychopyVersion = '2021.2.3'
expName = 'motorReplay' 
expInfo = {'participant': '', 'session': '001'}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion


#Save filename
filename = _thisDir + '/replay_data/' + expInfo['participant'] + "_" + expName + "_" + expInfo['date']
print(filename)
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/udeozormi/Desktop/reinstatementParty1/',
    savePickle=True, saveWideText=True,
    dataFileName=filename)

# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# Setup the Window
width = 2560
height = 1600
win = visual.Window(
    size=(width, height), fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='pix')
    
#store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess


# ======================================================= CREATE OBJECT CLASS AND IMPORTANT FUNCTIONS ==================================================================

#Objects Class
class Objects:
    def __init__(self,number):
        self.number = number
        self.name = ""
        self.descriptors = []

    def add_descriptor(self, descriptor):
        self.descriptors.append(descriptor)

    def pickDescriptors(self):

        bank = []
        for obj in all_objects:
            if self.number != obj.number:
                falseObj = obj
                bank = bank + falseObj.descriptors
        targets = random.sample(self.descriptors, 2) #pick two targets

        #pick one distractor and make sure it is not also a descriptor for the active object
        distractor = ''
        while True:
            distractor = random.choice(bank)
            if distractor not in self.descriptors:
                break 
            
        descriptors = random.sample((targets + [distractor]), 3) #add them to a single list and shuffle them
        print("true object descriptors -----> " + str(self.descriptors))
        print("descriptors shown --------> " + str(descriptors) + "\n")
        return descriptors

#returns a dictionary of 3 objects in each of the 3 conditions - see only, see+touch, and touch only
def assign_objects(objects):

    objects = random.sample(objects,len(objects)) #Shuffle the objects list

    names = ["Hebba", "Ahpop", "Dabu", "Ornik", "Vistur", "Glebin", "Bydar", "Quexer", "Shrilem"] #initialize object names

    assignments = {"see":[],"see & touch":[],"touch":[]}   #initialize conditions dictionary

    #assign each object a name and to a condition
    for obj in objects:
        name = random.choice(names)
        obj.name = name
        names.remove(name)
    
    assignments["see"] = objects[:3]
    assignments["see & touch"] = objects[3:6]
    assignments["touch"] = objects[6:]

    return assignments

#used to print object assignments on the screen
def printNamesInOrder(objectDict):
    names = []
    objects = np.concatenate(list(objectDict.values()))
    for obj in objects:
        names.append((obj.number, obj.name))
    return names

#assigns descriptors (from familiarization) to original objects, not the copy
def addToRealObj(obj_copy, desc):
    for obj in all_objects:
        if obj_copy.number == obj.number:
            obj.add_descriptor(desc)
            print(obj.name, obj.descriptors)

    return 

#create objects
obj_01 = Objects(1)
obj_02 = Objects(2)
obj_03 = Objects(3)
obj_04 = Objects(4)
obj_05 = Objects(5)
obj_06 = Objects(6)
obj_07 = Objects(7)
obj_08 = Objects(8)
obj_09 = Objects(9)

all_objects = [obj_01, obj_02, obj_03, obj_04, obj_05, obj_06, obj_07, obj_08, obj_09]

#put objects in a condition
assignments = assign_objects(all_objects)
thisExp.addData('Object Name Pairs', str(printNamesInOrder(assignments)).lower())
thisExp.nextEntry()

# ================================================================================== INITIALIZATIONS ==============================================================================
#Initialize intro screens    
introText = visual.TextStim(win, text = 'Welcome! Please hang tight as your experimenter organizes the objects for you', 
                                            units = 'pix', font='Arial', pos=(0, 150), height= 50, wrapWidth=None, ori=0, 
                                            color='white', colorSpace='rgb', opacity=1)

pressSpace = visual.TextStim(win, text = 'Press Space to Continue', 
units = 'pix', font='Arial', pos=(0, -300), height= 25, wrapWidth=None, ori=0, 
                                            color='white', colorSpace='rgb', opacity=1)

accuracyScreen = visual.TextStim(win, text = "", 
                                            units = 'pix', font='Arial', pos=(0,0), height= 40, wrapWidth=None, ori=0, 
                                            color='white', colorSpace='rgb', opacity=1)                                            
                                                                                        
#Initialize Counter
countdownClock = core.Clock()
count = visual.TextStim(win=win, text = 'mynamejeff', name='count',
    font='Arial', units = "pix",
    pos=(0, 0), height=50, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)
                                            
#Initialize Familiarizarion
exploreClock = core.Clock()
exploreObject = visual.TextStim(win=win, name='ObjectName',
    font='Arial', units = "pix",
    pos=(0, 100), height=20, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)
    
#Initialize descriptor recall trials    
descriptorRecallClock = core.Clock()
descriptor1 = visual.TextStim(win=win, name='Descriptor1',
    font='Arial', units = "pix",
    pos=(500, 200), height=75, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0) 
descriptor2 = visual.TextStim(win=win, name='Descriptor1',
    font='Arial', units = "pix",
    pos=(500, 0), height=75, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0) 
descriptor3 = visual.TextStim(win=win, name='Descriptor1',
    font='Arial', units = "pix",
    pos=(500, -200), height=75, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0) 
objectName = visual.TextStim(win=win, name='ObjectName',
    font='Arial', units = "pix",
    pos=(-200, 0), height=100, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)
    
#Initialize free recall trials
freeRecallClock = core.Clock()
recallObject = visual.TextStim(win=win, name='ObjectName',
    font='Arial', units = "pix",
    pos=(0, 0), height=120, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0)

#  =================================================================================================================================================================================

#  PREPARE FAMILIARIZARION

#Build copy of original dictionary to manipulate
assignmentsCopy = copy.deepcopy(assignments)

#Run main intro 
objectNamePairs = printNamesInOrder(assignments)[1:-1]
print(objectNamePairs)
while True:
    introText.draw()
    if event.getKeys(keyList = 'space'):
        break
    if event.getKeys(keyList = 'escape'):
        core.quit()
    win.flip()


# ======================================================================= STARTING FAMILIARIZATION =======================================================================

#run familiarization trials
for trial in range(27):

    #check if any of our conditions have gone through all 3 objects. If so, delete the entire condition so it is not randomly chosen later
    condition_to_remove = None
    for condition in assignmentsCopy:
        # print(condition, len(assignmentsCopy[condition]))
        if len(assignmentsCopy[condition]) == 0:
            condition_to_remove = condition

    if condition_to_remove != None:
        assignmentsCopy.pop(condition_to_remove)

    #if all of the conditions have been completed, refill dictionary for next run
    if len(assignmentsCopy) == 0:
        assignmentsCopy = copy.deepcopy(assignments)


    #------------------SET UP TRIAL---------------------------

    condition = random.choice(list(assignmentsCopy.keys()))  #randomly choose a condition
    obj = random.choice(assignmentsCopy[condition])   #Randomly choose an object from that condition
    assignmentsCopy[condition].remove(obj)    #Remove that object from our condition so it is not chosen again in this run
    exploreObject.setText(condition + " " + obj.name)   #Set text to show on the screen
    exploreObject.setHeight(60)    #Set size of text

    #Initialize gui for object description
    descriptorGui = gui.Dlg(title = obj.name)
    descriptorGui.addField("Descriptor for " + obj.name)

    #draw trial info screen
    while True:
        exploreObject.draw()
        pressSpace.draw()
        win.flip()
        if event.getKeys(keyList = 'space'):
            break
        if event.getKeys(keyList = 'escape'):
            core.quit()
            
    # set countdown timers
    routineTimer.reset()
    routineTimer.add(6.000000)
    countdownClock.reset()  # t0 is time of first possible flip
    
    #run Countdown
    while routineTimer.getTime() > 0:
        t = countdownClock.getTime()
        count.setText(str((int(5-t+1)))) #display time remaining

        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()
        
        if t >= 0:
            count.draw()
            
        if t > 5:
            break
        win.flip()

    #set trial timers
    routineTimer.reset()
    routineTimer.add(21.00000)
    exploreClock.reset()  # t0 is time of first possible flip
    
    #show only the name during exploration
    exploreObject.setText(obj.name)    #set text to name of object only
    exploreObject.setHeight(120)  #resize text

    #------------------RUN EXPLORATION TRIAL---------------------

    while routineTimer.getTime() > 0:
        t = exploreClock.getTime()

        #check force quit
        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()

        #draw object name for 5 seconds, then hide it for 10s, and show for another 5 seconds
        if t <= 5 or t >= 15:
            exploreObject.draw()
        if t > 20:
            break
        win.flip()

    descriptorGui.show() #ask for one descriptor after exploration

    #assign the provided descriptor to the obj in lowercase
    descriptor = descriptorGui.data[0].lower() 
    addToRealObj(obj, descriptor) #add descriptor to the real objects (not the copy)

    #Save data
    thisExp.addData('object' , obj.number)
    thisExp.addData('descriptor', descriptor)

    thisExp.nextEntry()

# ======================================================================= ENDING FAMILIARZATION ==========================================================================

#  PREPARE DESCRIPTOR RECALL

#build a copy of the all_objects list to manipulate
all_objects_copy = copy.deepcopy(all_objects)

#Move counter
count.setPos((200, 0))

#initialize tracker for trials answered correctly
total_correct = 0

#show intro screen
introText.setText("We will now begin the descriptor recall task. \n \n \n Please tell your experimenter when you are ready to continue!")
while True:
    introText.draw()
    win.flip()
    if event.getKeys(keyList = 'space'):
        break
    if event.getKeys(keyList = 'escape'):
        core.quit()

# ======================================================================= STARTING DESRCIPTOR RECALL =======================================================================

#run descriptor recall trials
for trial in range(27):


    #refill object list when it becomes empty (every 9 trials)
    if len(all_objects_copy) == 0:
        all_objects_copy = copy.deepcopy(all_objects)
        total_correct = 0 #reset counter after every 9 trials

    #------------------SET UP TRIAL---------------------------

    obj = random.choice(all_objects_copy)  #randomly choose an object
    all_objects_copy.remove(obj)   #remove object so it is not chosen again 

    trialDescriptors = obj.pickDescriptors() #run fucntion to pick the 3 descriptor options for this trial (one of them is a distractor)
    descriptor1.setText(trialDescriptors[0])
    descriptor2.setText(trialDescriptors[1])
    descriptor3.setText(trialDescriptors[2])
    objectName.setText(obj.name)  #set the text for the trial object

    #Initialize gui for object description
    responseGui = gui.Dlg(title = obj.name)
    responseGui.addField("Which descriptor does not match " + obj.name + "?")

    # set countdown timers
    routineTimer.reset()
    routineTimer.add(4.000000)
    countdownClock.reset(0)  # t0 is time of first possible flip
    
    #run Countdown
    while routineTimer.getTime() > 0:
        t = countdownClock.getTime()
        count.setText(str((int(3-t+1)))) #display time remaining

        #check esc
        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()
        
        if t >= 0:
            count.draw()
            objectName.draw()
            
        if t > 3:
            break
        win.flip()
        
    #set timers
    routineTimer.reset()
    routineTimer.add(12.00000)
    descriptorRecallClock.reset(0)  # t0 is time of first possible flip

    #-------------RUN DESCRIPTOR RECALL TRIAL----------------------

    while routineTimer.getTime() > 0:
        t = descriptorRecallClock.getTime()

        #check esc
        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()

        #draw object name for 3 seconds, then hide it for 5s, and show for another 3 seconds
        if t <= 3 or t >= 8:
            objectName.draw()
            descriptor1.draw()
            descriptor2.draw()
            descriptor3.draw()

        if t > 11:
            break
        win.flip()

    #ask participant to choose after 11 seconds
    responseGui.show()
    response = responseGui.data[0].lower()

    #if participant chose correctly, tally and mark log sheet - 0 incorrect, 1 correct
    if response not in obj.descriptors:
        total_correct += 1
        thisExp.addData('correct', 1)
    else: thisExp.addData('correct', 0)
    
    #if you have cycled through 9 objects, save run accuracy and 
    if (trial+1) % 9 == 0:
        accuracy  = round(total_correct/9 *100 , 2)
        accuracyScreen.setText("Your accuracy for this run is " + str(accuracy) + "%!")
        thisExp.addData('run_accuracy' , accuracy)
        while True:
            accuracyScreen.draw()
            pressSpace.draw()
            if event.getKeys(keyList = 'space'):
                break
            if event.getKeys(keyList = 'escape'):
                core.quit()
            win.flip()

    #Save other trial data
    thisExp.addData('object_dr' , obj.number) 
    thisExp.addData('descriptor_options' , (obj.descriptors, trialDescriptors)) 
    thisExp.addData('response', response)

    thisExp.nextEntry()

# ======================================================================== ENDING DESCRIPTOR RECALL ==========================================================================

#  PREPARE FREE RECALL

#build a copy of the all_objects list to manipulate
all_objects_copy = copy.deepcopy(all_objects)

#move and resize things
pressSpace.setPos((0,0))
pressSpace.setHeight(75)
count.setPos((0,0))

#show intro screen
introText.setText("We will now begin the free recall task. \n \n \n Please tell your experimenter when you are ready to continue!")
while True:
    introText.draw()
    if event.getKeys(keyList = 'space'):
        break
    if event.getKeys(keyList = 'escape'):
        core.quit()
    win.flip()

# ======================================================================= STARTING FREE RECALL ====================================================================================


#run free recall trials
for trial in range(27):

    #refill object list when it becomes empty
    if len(all_objects_copy) == 0:
        all_objects_copy = copy.deepcopy(all_objects)

    #------------------SET UP TRIAL---------------------------

    obj = random.choice(all_objects_copy)  #randomly choose an object
    all_objects_copy.remove(obj)   #remove object so it is not chosen again 
    recallObject.setText(obj.name) #set the name of the object to show

    #Draw continue screen
    while True:
            pressSpace.draw()
            if event.getKeys(keyList = 'space'):
                break
            if event.getKeys(keyList = 'escape'):
                core.quit()
            win.flip()

    # set countdown timers
    routineTimer.reset()
    routineTimer.add(4.000000)
    countdownClock.reset()
    
    #run Countdown
    while routineTimer.getTime() > 0:
        t = countdownClock.getTime()
        count.setText(str((int(3-t+1)))) #display time remaining
        
        #check esc
        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()
        
        if t >= 0:
            count.draw()
            
        if t > 3:
            break
        win.flip()
        
    #set timers
    routineTimer.reset()
    routineTimer.add(16.00000)
    freeRecallClock.reset()

    #---------------RUN FREE RECALL TRIAL--------------------------
    while routineTimer.getTime() > 0:
        t = freeRecallClock.getTime()

        #check esc
        forceQuit = event.getKeys(keyList=['escape'], modifiers=False, timeStamped=False) 
        if forceQuit:
            print("Experiment Terminated")
            core.quit()

        #show name and descriptors
        if t >= 0:
            recallObject.draw()

        if t > 15:
            break
        win.flip()

    #save data
    thisExp.addData('object_fr', obj.number)
    thisExp.nextEntry()
    
# ======================================================================= ENDING FREE RECALL ==========================================================================


print("experiment done")

    
    




