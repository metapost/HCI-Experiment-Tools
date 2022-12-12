# Created by hapeng.wang@gmail.com
# v2.0, 20221212, added log file.
# v1.0, 20221212

# You MUST customize the "header" info before using the scale.

import os
import datetime
from appJar import gui

## data file.
fname = "procedure.log"

## Experiments to be chosen from
experiments = ["1", "2", "3"]

## Labels of the Conditions to be chosen from
conditions = ["pop", "pull", "auto"]

# block number
blocks = ["0", "1", "2", "3"]

def on_exit():
    app.stop()

def checked(cb):
    """print the checked time."""
    app.setCheckBoxText(cb, text = cb + ' | ' + str(datetime.datetime.now().strftime("%H:%M:%S")))
    file_handle = open(fname, "a")
    file_handle.write(cb + ' | ' + str(datetime.datetime.now().strftime("%H:%M:%S")) + '\n')
    file_handle.close()

## Main entry point
app = gui()
# app.showSplash("Procedure \n Guide and Track Experiment \n haipeng.wang at gmail", fill='red', stripe='black', fg='white', font=44)
app.setTitle("Pilot Study - Procedure Guide and Tracking")
app.setSize(1200, 700)
app.setFont(size=16, weight="bold")

## experiments basic settings
app.addLabelOptionBox("Experiment", experiments, 0, 0)
app.addLabelSpinBoxRange("User ID", 1, 100, 0, 1)
app.addLabelOptionBox("Block", blocks, 0, 2)
app.addLabelOptionBox("Condition", conditions, 0, 3)


app.startTabbedFrame("TabbedFrame", colspan=4)
app.setSticky("w")
app.setFont(20)

## preparation
app.startTab("0. Preparation")
app.addCheckBox("Video recorder: 1 primary + 1 backup")
app.addCheckBox("Audio recorder: 1 primary + 1 backup")
app.addCheckBox("TLX + Usability Questionnaires")
app.addCheckBox("Notification on Lab. door.")
app.stopTab()

## Pre-experiment
app.startTab("1. Pre-Experiment")
app.addCheckBox("Greetings users.")
app.addCheckBox("If you feel uncomfortable you can stop at any time during the study.")
app.addCheckBox("This is a study of system; we are not studying you.")
app.addCheckBox("Consent form.")
app.addCheckBox("Video/Audio recording only for research; \n Your privacy is our priority.", row="previous", column=1)
app.addCheckBox("Demographic")
app.addCheckBox("Instruction: play video.")
app.addCheckBox("Answer questions", row="previous", column=1)
app.addCheckBox("Practice: techniques trials + TLX & Survey")
app.addNamedCheckBox(name="Answer questions", title="Answer practice questions", row="previous", column=1)
app.addNamedCheckBox(name="Break", title="Break after practice")
app.stopTab()

## Main-experiment
app.startTab("2. Main-Experiment")
app.addCheckBox("Turn on video recorders.")
app.addCheckBox("to proceed as quickly and accurately as possible but at a pace that is comfortable.", colspan=4)
app.addCheckBox("Think Aloud (optional)")

app.addCheckBox("Block-0", column=0)
app.addNamedCheckBox(name="Trials \u00D7 2", title="trial-0", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-0", row="previous", column=2)
app.addNamedCheckBox(name="Break", title="break-0", row="previous", column=3)

app.addCheckBox("Block-1", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-1", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-1", row="previous", column=2)
app.addNamedCheckBox(name="Break", title="break-1", row="previous", column=3)

app.addCheckBox("Block-2", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-2", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-2", row="previous", column=2)
app.addNamedCheckBox(name="Break(must)", title="break-2", row="previous", column=3)

app.addCheckBox("Block-3", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-3", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-3", row="previous", column=2)
app.addNamedCheckBox(name="Break", title="break-3", row="previous", column=3)

app.stopTab()

## Post-experiment
app.startTab("3. Post-Experiment")
app.addCheckBox("Turn on audio recorders.")
app.addCheckBox("Interview:")
app.addCheckBox("closed questions.", row="previous", column=1)
app.addCheckBox("open questions.", row="previous", column=2)
app.addCheckBox("repeat and confirm.", row="previous", column=3) # repeat your understanding and confirm with users.
app.addCheckBox("Debrief")
app.addNamedCheckBox(name="Answer questions", title="Answer Debrief", row="previous", column=1)
app.addCheckBox("Maintain participants pool.")
app.addCheckBox("Thank you, good bye!")
app.stopTab()

app.stopTabbedFrame()

tk = app.getAllCheckBoxes().keys()
for i, entry in enumerate(tk):
    app.setCheckBoxChangeFunction(entry, checked)

app.setSticky("we")
row = app.getRow()
app.addButton("Exit", on_exit, row, 3)

app.go()


