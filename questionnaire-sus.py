# app version
# v?, date

# Created by haipeng.wang@gmail.com
# a custom questionnaire for SUS system usability scales, all are 5-point Likert scale.
# ref1: SUS
# ref2: Laxmi Pandey, Ahmed Sabbir Arif. 2024. MELDER: The Design and Evaluation of a Real-time Silent Speech Recognizer for Mobile Devices. In Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems (CHI 2024). ACM, New York, NY, USA
# template version
# v1.0, 20240402

# You MUST customize the "header" info before using the scale.

import os
from appJar import gui

## data file.
fname = "questionnaire-sus.txt"

## Texts for the individual questionnaire items
# texts = ["易用性的程度",
#          "交互的流畅性"]

# texts = ["Ease of use",
#          "Fluidity", 
#          "Ease of learning"]

texts = [
    "The technique was fast", # speed
    "The technique was accurate", # accuracy
    "The feedback method used in the technique was effective and useful", # effectiveness
    "I think that I would like to use this system frequently", # willingness-to-use 
    "I thought the system was easy to use", # ease-of-use
    "I would imagine that most people would learn to use this system very quickly", # learnability
    "I felt very confident using the system", # confidence
    "I think the system will be private and secure when using in public places" # privacy and security
    ]


## an unbiased question example.
# How easy or difficult was it for you to...? [Very difficult, Difficult, Neutral, Easy, Very easy]

## Labels on the left and right sides of the scale
# left_labels = ["Very Low", "Very Low", "Strongly Disagree", "Very Unlikely", "Perfect"]
# right_labels = ["Very High", "Very High", "Strongly Agree", "Very Likely", "Failure"]

left_labels = ["Strongly Disagree", "Strongly Disagree", "Strongly Disagree", "Strongly Disagree", "Strongly Disagree", "Strongly Disagree", "Strongly Disagree", "Strongly Disagree"]
right_labels = ["Strongly Agree", "Strongly Agree", "Strongly Agree", "Strongly Agree", "Strongly Agree", "Strongly Agree", "Strongly Agree", "Strongly Agree"]


## Labels of the Conditions to be chosen from
conditions = ["pop", "pull", "auto"]

## Experiments to be chosen from
# experiments = ["Experiment 1", "Experiment 2"]
experiments = ["2"]

# block number
blocks = ["0", "1", "2", "3"]


## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = 'experiment ' + 'pid ' + 'condition ' + 'block ' + 'speed ' + 'accuracy ' + 'effectiveness ' + 'willingness-to-use ' + 'ease-of-use ' + 'learnability ' + 'confidence ' + 'privacy-security'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    experiment = app.getOptionBox("Experiment")
    pid = app.getSpinBox("PID")
    condition = app.getOptionBox("Condition")
    block = app.getOptionBox("Block")
    
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(experiment) + ' '
    write_string += str(pid) + ' '
    write_string += str(condition) + ' '
    write_string += str(block)

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

app.addLabelOptionBox("Experiment", experiments, 0, 0)
app.addLabelSpinBoxRange("PID", 1, 100, 0, 1)
app.addLabelOptionBox("Block", blocks, 0, 2)
app.addLabelOptionBox("Condition", conditions, 0, 3)
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

    app.setScaleRange("q" + str(i), 1, 5, 3)
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


