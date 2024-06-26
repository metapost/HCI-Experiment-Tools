# app version
# v1.1, fix bug, fix the missing of speech value. 20230218

# Created by haipeng.wang@gmail.com
# template version
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
fname = "demographic_saydo.txt"

# texts = ["Ease of use",
#          "Fluidity", 
#          "Ease of learning"]

## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = '# ' + 'uid ' + 'gender ' + 'age ' + 'sight ' + 'handedness ' + 'experience-display ' + 'experience-gesture ' + 'experience-speech ' + 'experience-silentSpeech'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    user_id = app.getSpinBox("User ID")
        
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(user_id) + ' '
    write_string += app.getRadioButton("gender") + ' '
    write_string += str(int(app.getEntry("age"))) + ' '
    write_string += app.getRadioButton("sight") + ' '
    write_string += app.getRadioButton("handedness") + ' '
    write_string += app.getRadioButton("display") + ' '
    write_string += app.getRadioButton("gesture") + ' '
    write_string += app.getRadioButton("speech") + ' '
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
app.addLabelSpinBoxRange("User ID", 1, 100, 0, 0)
app.addHorizontalSeparator(1, 0, 3)

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
app.addRadioButton("sight", "good", row="previous", column=1)
app.addRadioButton("sight", "good at distant of 5 meters", row="previous", column=2)

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

app.addLabel("Your prior experience with Gesture Interaction: ", column=0)
app.addRadioButton("gesture", "Daily", row="previous", column=1)
app.addRadioButton("gesture", "Weekly", row="previous", column=2)
app.addRadioButton("gesture", "Monthly", row="previous", column=3)
app.addRadioButton("gesture", "Yearly", row="previous", column=4)
app.addRadioButton("gesture", "Never", row="previous", column=5)

app.addLabel("Your prior experience with Speech Interaction: ", column=0)
app.addRadioButton("speech", "Daily", row="previous", column=1)
app.addRadioButton("speech", "Weekly", row="previous", column=2)
app.addRadioButton("speech", "Monthly", row="previous", column=3)
app.addRadioButton("speech", "Yearly", row="previous", column=4)
app.addRadioButton("speech", "Never", row="previous", column=5)

app.addLabel("Your prior experience with Silent Speech Interaction: ", column=0)
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


