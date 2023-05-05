# App version
# v1.0, May 5, 2023

# Template version
# Modified by haipeng.wang@gmail.com
# v2.1, 20230505, changed uid to pid.
# v2.0, 20230316, added logic control, all scales will be disabled after click submit, set block will enable scales.
# v1.4, 20230228, remove the sharp number symbol from the header.
# v1.3.1, 20230228, marginally tiny improvement, add a head note.
# v1.3, 20230216, minor improvement, remove the experiment variable.
# v1.2, 20221211, minor improvement.
# v1.1, 20221211, added block, check file exists or not, added button of exit.
# v1.0, 20221210

# You MUST customize the "header" info before using the scale.

#!/usr/bin/python3

## install: pip3 install appjar
import os
from appJar import gui

## data file.
fname = "nasa-rawtlx-results-ccl-v2.txt"


## Texts for the individual questionnaire items
#texts = ["Mental Demand    -    How mentally demanding was the task?",
         # "Physical Demand    -    How physically demanding was the task?",
         # "Temporal Demand    -    How hurried or rushed was the pace of the task?",
         # "Performance    -    How successful were you in accomplishing what you were asked to do?",
         # "Effort    -    How hard did you have to work to accomplish your level of performance?",
         # "Frustration    -    How insecure, discouraged, irritated, stressed and annoyed were you?"]

#texts = ["脑力需求    -    How mentally demanding was the task?",
         #"体力需求    -    How physically demanding was the task?",
         # "时限需求    -    How hurried or rushed was the pace of the task?",
         # "自我表现    -    How successful were you in accomplishing what you were asked to do?",
         # "努力程度    -    How hard did you have to work to accomplish your level of performance?",
         # "受挫感    -    How insecure, discouraged, irritated, stressed and annoyed were you?"]

texts = ["脑力需求    -    完成任务的脑力需求(例如：思考、决定、记忆、观察和搜索等)",
         # "体力需求    -    完成任务的体力需求(例如：拖拽、旋转、控制等)",
         # "时限需求    -    完成任务的速率或节奏，即时间紧迫感",
         "自我表现    -    对完成任务中自我表现的满意程度，对任务完成水平的自我评价",
         "努力程度    -    完成任务所付出的努力",
         "受挫感    -    完成任务中感到的沮丧、烦躁、压力大和愤怒等"]

## Labels on the left and right sides of the scale
#left_labels = ["Very Low", "Very Low", "Very Low", "Perfect", "Very Low", "Very Low"]
#right_labels = ["Very High", "Very High", "Very High", "Failure", "Very High", "Very High"]
left_labels = ["非常低", "完美", "非常低", "非常低"]
right_labels = ["非常高", "失败", "非常高", "非常高"]


## Labels of the Conditions to be chosen from
conditions = ["?", "Cross-Language", "Auto", "Auto-Cross-Language"]

## Experiments to be chosen from
# experiments = ["Experiment 1", "Experiment 2"]
# experiments = ["2"]

# block number
# blocks = ["0", "1", "2", "3"]
blocks = ["?", "0", "3"] # "-" is default value, and it let user must choose a number before go ahead.

# init config for app
def init_app():
    for scale in app.getAllScales():
        app.disableScale(scale) # disable all scales, let user set block number firstly.

## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = 'pid ' + 'condition ' + 'block ' + 'mental ' + 'performance ' + 'effort ' + 'frustration'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    user_id = app.getSpinBox("User ID")
    condition = app.getOptionBox("Condition")
    block = app.getOptionBox("Block")
    
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(user_id) + ' '
    write_string += str(condition) + ' '
    write_string += str(block)

    for i in range(len(texts)):
        write_string += ' ' + str(app.getScale("q" + str(i)) * 5)

    file_handle.write(write_string + '\n')
    file_handle.close()
    
    app.infoBox("RawTLX Input", "Input successfully.")
    print("The results were written successfully.")
        
    # reset block to - (NA)
    app.setOptionBox('Block', '?')

    # disabled all scales
    for scale in app.getAllScales():
        app.disableScale(scale)

def on_exit():
    app.stop()

def on_block_change(option):
        for scale in app.getAllScales():
            app.enableScale(scale)


## Main entry point
app = gui()
# app.showSplash("NASA RawTLX", fill='red', stripe='black', fg='white', font=44)
app.setTitle("NASA-RawTLX")
app.setSize(1000, 700)
app.setFont(size=16, weight="bold")

app.addLabelSpinBoxRange("User ID", 1, 100, 0, 0)
app.addLabelOptionBox("Condition", conditions, 0, 1)
app.addLabelOptionBox("Block", blocks, 0, 2)
app.setOptionBoxChangeFunction("Block", on_block_change)
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

    app.setScaleRange("q" + str(i), 0, 20, 10)
    app.setScaleIncrement("q" + str(i), 1)
    app.showScaleIntervals("q" + str(i), 1)
    app.showScaleValue("q" + str(i), show=True)

    app.setSticky("we")
    app.addLabel("ticks_q" + str(i), "||", 4*i + 2 + 3, 1)
    app.addHorizontalSeparator(4*i + 3 + 3, 0, 4)

app.setSticky("we")
app.addButton("Submit", on_submit, 4*len(texts) + 1 + 3, 1)
app.addButton("Exit", on_exit, 4*len(texts) + 1 + 3, 3)
app.setStartFunction(init_app)

app.go()

