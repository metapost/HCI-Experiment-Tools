# app version
# v1.1, 20230302. fixed bug of conditions.
# v1.0, 20230218.
#
# Created by haipeng.wang@gmail.com
# template version
# v1.0, 20221211

# You MUST customize the "header" and left and right labels set before using the scales.

import os
from appJar import gui

## data file.
fname = "questionnaire-g2g-studyIII-2.1.txt"

## Texts for the individual questionnaire items
# texts = ["易用性的程度",
#         "交互的流畅性"]

texts = ["Ease of use individually(个人使用的易用性)",
         "Ease of collaboration with others(多人协作的易用性)",
         "Perceived accuracy(感受到的准确度)",
         "Perceived speed(感受到的速度)",
         "Privacy concerns(隐私保护程度)"]



## an unbiased question example.
# How easy or difficult was it for you to...? [Very difficult, Difficult, Neutral, Easy, Very easy]

## Labels on the left and right sides of the scale
# left_labels = ["Very Low", "Very Low", "Strongly Disagree", "Very Unlikely", "Perfect"]
# right_labels = ["Very High", "Very High", "Strongly Agree", "Very Likely", "Failure"]
left_labels = ["非常困难", "非常困难", "非常不准确", "非常慢", "很低"]
right_labels = ["非常容易", "非常容易", "非常准确", "非常快", "很高"]


## Labels of the Conditions to be chosen from
# conditions = ["pop", "pull", "auto"]
conditions = ["cross-device", "large-display"]

## Experiments to be chosen from
# experiments = ["Experiment 1", "Experiment 2"]
# experiments = ["2"]

# block number
# blocks = ["0", "1", "2", "3"]


## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        # header = '# ' + 'uid ' + 'condition ' + 'block ' + 'ease-of-use ' + 'ease-of-collaboration ' + 'ease-of-access ' + 'privacy-concerns'
        header = '# ' + 'uid ' + 'condition ' + 'ease-of-use ' + 'ease-of-collaboration ' + 'percevied-accuracy ' + 'percevied-speed ' + 'privacy'         
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    user_id = app.getSpinBox("User ID")
    condition = app.getOptionBox("Condition")

    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(user_id) + ' '
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

app.addLabelSpinBoxRange("User ID", 1, 100, 0, 0)
app.addLabelOptionBox("Condition", conditions, 0, 1)
app.addHorizontalSeparator(2, 0, 3)

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


