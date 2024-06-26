# app version
# v1.0, fix bug. 2023mmdd

# Created by haipeng.wang@gmail.com
# template version
# v1.3, 20230309, change the UID to PID.
# v1.2, 20230228, remove the separator below uid widget.
# v1.1, 20230215, remove experiment and condition variables.
# v1.0, 20221212, full functions finshed.
# v0.1, 20221212

# requirements
# 1 gender, age, handedness, visual acuity, prior experience with techniques related to the research.
# please indicate your age:

# You MUST customize the filename and the "header" info before using the scale.

import os
from appJar import gui

## data filename.
fname = "demographic.txt"

# texts = ["Ease of use",
#          "Fluidity", 
#          "Ease of learning"]

## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = 'pid ' + 'gender ' + 'age ' + 'sight ' + 'handedness ' + 'experience-display ' + 'experience-gesture ' + 'experience-silentSpeech'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    pid = app.getSpinBox("PID")
        
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(pid) + ' '
    write_string += app.getRadioButton("gender") + ' '
    write_string += str(int(app.getEntry("age"))) + ' '
    write_string += app.getRadioButton("sight") + ' '
    write_string += app.getRadioButton("handedness") + ' '
    write_string += app.getRadioButton("display") + ' '
    write_string += app.getRadioButton("gesture") + ' '
    write_string += app.getRadioButton("silentSpeech")
    
    file_handle.write(write_string + '\n')
    file_handle.close()
    
    app.infoBox("Input", "Input successfully.")

def on_exit():
    app.stop()


## Main entry point
app = gui()
# app.showSplash("Questionnaire", fill='red', stripe='black', fg='white', font=44)
app.setTitle("Demographic")
app.setSize(1100, 700)
app.setFont(size=16, weight="bold")

app.setSticky("we")
app.addLabelSpinBoxRange("PID", 1, 100, 0, 0)

## Basic info of participants
app.startLabelFrame("Basic Info", colspan=6)
app.setSticky("w")
app.addLabel("genderLabel", "Your gender: ", column=0)
app.addRadioButton("gender", "Male", row="previous", column=1)
app.addRadioButton("gender", "Female", row="previous", column=2)

app.addLabel("Your age: ")
app.addNumericEntry("age", row="previous", column=1)
app.stopLabelFrame()

## Human Factors
app.startLabelFrame("Human Factors", colspan=6)
app.setSticky("w")
app.addLabel("Your corrected sight: ", column=0)
app.addRadioButton("sight", "My eyesight is GOOD up to 5 meters.", row="previous", column=1)
app.addRadioButton("sight", "My eyesight is BAD beyond 5 meters.", row="previous", column=2)

app.addLabel("Your handedness: ", column=0)
app.addRadioButton("handedness", "Right", row="previous", column=1)
app.addRadioButton("handedness", "Left", row="previous", column=2)
app.addRadioButton("handedness", "Both", row="previous", column=3)
app.stopLabelFrame()

## prior experience 
app.startLabelFrame("Prior Experience", colspan=6)
app.addLabel("Your prior experience with Large Displays: ", column=0)
app.addRadioButton("display", "Daily", row="previous", column=1)
app.addRadioButton("display", "Weekly", row="previous", column=2)
app.addRadioButton("display", "Monthly", row="previous", column=3)
app.addRadioButton("display", "Yearly", row="previous", column=4)
app.addRadioButton("display", "Never", row="previous", column=5)

app.addLabel("Your prior experience with gesture interaction: ", column=0)
app.addRadioButton("gesture", "Daily", row="previous", column=1)
app.addRadioButton("gesture", "Weekly", row="previous", column=2)
app.addRadioButton("gesture", "Monthly", row="previous", column=3)
app.addRadioButton("gesture", "Yearly", row="previous", column=4)
app.addRadioButton("gesture", "Never", row="previous", column=5)

app.addLabel("Your prior experience with silent speech interaction: ", column=0)
app.addRadioButton("silentSpeech", "Daily", row="previous", column=1)
app.addRadioButton("silentSpeech", "Weekly", row="previous", column=2)
app.addRadioButton("silentSpeech", "Monthly", row="previous", column=3)
app.addRadioButton("silentSpeech", "Yearly", row="previous", column=4)
app.addRadioButton("silentSpeech", "Never", row="previous", column=5)
app.stopLabelFrame()

app.setSticky("we")
row = app.getRow()
app.addButton("Exit", on_exit, column=0)
app.addButton("Submit", on_submit, row="previous", column=2)

app.go()


