# App version
# v1.1, 20230424, reset all scales to default values as condition box changed values.
# v1.0, 20230421

# Created by haipeng.wang@gmail.com
# Template version
# v2.1, 20230424, reset all scales to default values as optionalbox of conditon changed values.
# v2.0, 20230319, added WTU, willingness-to-use is a measure of a user's attitude toward using a technique.
# v1.3, 20230309, change the UID to PID.
# v1.2, 20230222, added two scales and changed them to 7-Likert scales.
# v1.1, 20230221, added conditions.
# v1.0, 20221211

# You MUST customize the "header" and left and right labels set before using the scale.

import os
from appJar import gui

## data file.
fname = "questionnaire-g2g-cdgain.txt"

## Texts for the individual questionnaire items
# texts = ["易用性的程度",
#         "交互的流畅性"]

## While ease-of-use can contribute to willingness-to-use, they are not synonymous. 
# A system may be easy to use, but if it is not perceived as useful or relevant to the user's needs, they may not be willing to use it. 
# Conversely, a system may be perceived as difficult to use, but if the user sees significant benefits or value in using it, they may still be willing to use it.

texts = ["Ease of use(易用性)",
         "Ease of learning(易学性)",
         "Willingness-to-use(使用意愿)",
         "Perceived accuracy(感受到的准确度)",
         "Perceived speed(感受到的交互速度)"]         
         # "Ease of access", # for studyIII
         # "Privacy concerns"]

## an unbiased question example.
# How easy or difficult was it for you to...? [Very difficult, Difficult, Neutral, Easy, Very easy]

## Labels on the left and right sides of the scale
# left_labels = ["Very Low", "Very Low", "Strongly Disagree", "Very Unlikely", "Perfect"]
# right_labels = ["Very High", "Very High", "Strongly Agree", "Very Likely", "Failure"]
left_labels = ["非常困难", "非常困难", "非常不愿意", "非常不准确", "非常慢", "非常困难", "Very Low", "Very Bad"]
right_labels = ["非常容易", "非常容易", "非常愿意", "非常准确", "非常快", "非常容易", "Very High", "Very Good"]


## Labels of the Conditions to be chosen from
conditions = ["Constant", "Linear", "Nonlinear"]


## Experiments to be chosen from
# experiments = ["Experiment 1", "Experiment 2"]
# experiments = ["2"]

# block number
# blocks = ["0", "1", "2", "3"]

## call as condition optional box changed
## each time changed condition, reset all scales to default values.
def conditionChanged():
    for i, entry in enumerate(texts):
        # app.setScaleRange("q" + str(i), 1, 5, 4) # 7 scale range, 4 is default value.
        app.setScaleRange("q" + str(i), 1, 5, 3) # 5 scale range, 3 is default value.    


## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = 'pid ' + 'condition ' + 'ease-of-use ' + 'ease-of-leaning ' + 'WTU ' + 'percevied-accuracy ' + 'percevied-speed'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    pid = app.getSpinBox("PID")
    condition = app.getOptionBox("Condition")
    
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(pid) + ' '
    write_string += str(condition)

    for i in range(len(texts)):
        write_string += ' ' + str(app.getScale("q" + str(i)))

    file_handle.write(write_string + '\n')
    file_handle.close()
    
    app.infoBox("Questionnaire Input", "Input successfully.")

def on_exit():
    app.stop()


## Main entry point
app = gui()
# app.showSplash("Questionnaire", fill='red', stripe='black', fg='white', font=44)
app.setTitle("Questionnaire")
app.setSize(1000, 700)
app.setFont(size=16, weight="bold")

app.addLabelSpinBoxRange("PID", 1, 100, 0, 0)
app.addLabelOptionBox("Condition", conditions, 0, 1)
app.setOptionBoxChangeFunction("Condition", conditionChanged)
app.addHorizontalSeparator(2, 0, 4)

for i, entry in enumerate(texts):
    app.setSticky("we")
    app.addLabel("q" + str(i) + "_text", entry, 4*i + 3, 1)

    app.setSticky("e")
    app.addLabel("q" + str(i) + "_label_left", left_labels[i], 4*i + 1 + 3, 0)
    app.setSticky("we")
    app.addScale("q" + str(i), 4*i + 1 + 3, 1)
    app.setSticky("w")
    app.addLabel("q" + str(i) + "_label_right", right_labels[i], 4*i + 1 + 3, 2)

    # app.setScaleRange("q" + str(i), 1, 5, 4) # 7 scale range, 4 is default value.
    app.setScaleRange("q" + str(i), 1, 5, 3) # 5 scale range, 3 is default value.
    app.setScaleIncrement("q" + str(i), 1)
    app.showScaleIntervals("q" + str(i), 1)
    app.showScaleValue("q" + str(i), show=True)

    app.setSticky("we")
    app.addLabel("ticks_q" + str(i), "||", 4*i + 2 + 3, 1)
    app.addHorizontalSeparator(4*i + 3 + 3, 0, 4)

app.setSticky("we")
app.addButton("Submit", on_submit, 4*len(texts) + 1 + 3, 1)
app.addButton("Exit", on_exit, 4*len(texts) + 1 + 3, 3)

app.go()