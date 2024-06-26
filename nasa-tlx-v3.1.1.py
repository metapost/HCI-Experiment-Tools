# App version
# v1.0, MM DD, YYYY

# Template version
# Modified by haipeng.wang@gmail.com
# v3.1.1, 20230627, reset block number to 0 and 3, and discarded number 1 and 2.
# v3.1, 20230625, add all labels of six subscales to the header.
# v3.0, 20230508, add a major function to plot current data for current pid, this helps finding interesting things for following interview.
# v2.1, 20230505, changed uid to pid.
# v2.0, 20230316, added logic control, all scales will be disabled after click submit, set block will enable scales.
# v1.4, 20230228, remove the sharp number symbol from the header.
# v1.3.1, 20230228, marginally tiny improvement, add a head note.
# v1.3, 20230216, minor improvement, remove the experiment variable.
# v1.2, 20221211, minor improvement.
# v1.1, 20221211, added block, check file exists or not, added button of exit.
# v1.0, 20221210


## only collect tlx after block3. tlx after block0 is a practice.

# You MUST customize the "header" info before using the scale.
# You MUST need to set manually the block number which will be plot.

#!/usr/bin/python3

## install: pip3 install appjar
import os
import matplotlib.pyplot as plt
from appJar import gui

## data file.
fname = "nasa-rawtlx-results-g2g-IV-v1.0.txt"


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
         "体力需求    -    完成任务的体力需求(例如：拖拽、旋转、控制等)",
         "时限需求    -    完成任务的速率或节奏，即时间紧迫感",
         "自我表现    -    对完成任务中自我表现的满意程度，对任务完成水平的自我评价",
         "努力程度    -    完成任务所付出的努力",
         "受挫感    -    完成任务中感到的沮丧、烦躁、压力大和愤怒等"]

## Labels on the left and right sides of the scale
#left_labels = ["Very Low", "Very Low", "Very Low", "Perfect", "Very Low", "Very Low"]
#right_labels = ["Very High", "Very High", "Very High", "Failure", "Very High", "Very High"]
left_labels = ["非常低", "非常低", "非常低", "完美", "非常低", "非常低"]
right_labels = ["非常高", "非常高", "非常高", "失败", "非常高", "非常高"]


## Labels of the Conditions to be chosen from
conditions = ["?", "C1", "C2"] # Condition template, reserve the "?".

# block number, only perform tlx after block3, practice tlx after block0, but data should be discarded.
blocks = ["?", "0", "3"] # "-" is default value, and it let user must choose a number before go ahead.

# init config for app
def init_app():
    for scale in app.getAllScales():
        app.disableScale(scale) # disable all scales, let user set block number firstly.

## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = 'pid ' + 'condition ' + 'block ' + 'mental ' + 'physical ' + 'temporal ' + 'performance ' + 'effort ' + 'frustration'
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


# Define a function to show the plot
def show_plot(tab):
    # data convert
    import csv

    fn = 'nasa-rawtlx-results-g2g-IV-v1.0'

    # Open the input file for reading
    with open(fn+ '.txt', 'r') as input_file:
        # Read the contents of the file and split each line by commas
        lines = [line.strip().split(' ') for line in input_file.readlines()]

    # Open the output file for writing as a CSV file
    with open(fn + '.csv', 'w', newline='') as output_file:
        # Create a CSV writer object and write the data to the file
        writer = csv.writer(output_file)
        writer.writerows(lines)

    # print('Data written to .csv file')


    # plot
    import pandas as pd
    import numpy as np

    df = pd.read_csv(fn + '.csv')
    # print(df)

    # define the pid to select rows
    # define block id to select rows
    # define the dv to select columns
    pid = int(app.getSpinBox("User ID"))
    bid = 3 # only need rows with block id==3
    dv = ['mental', 'physical', 'temporal', 'performance', 'effort', 'frustration']

    # Select specific rows of pid and block id
    df = df.loc[df['pid'] == pid]
    df = df.loc[df['block'] == bid]
    # print(df)

    # Select specific columns by name
    columns_to_select = ['condition', 'mental', 'physical', 'temporal', 'performance', 'effort', 'frustration']
    df = df[columns_to_select]
    # print(df)

    # Create the bar chart
    num_dv = len(dv)
    num_condition = len(df['condition'])

    fig, ax = plt.subplots()
    width = 0.8 / num_dv # number of dv

    for i, var in enumerate(dv):
        x = np.arange(num_condition) + i * width # 2 conditions
        ax.bar(x, df[var], width=width, label=var)

    # Set axis labels and title
    # ax.set_xlabel('Conditions')
    # ax.set_ylabel('Scale')
    ax.set_title('User' + str(pid) + ': Raw TLX')

    # Set the x-tick labels
    ax.set_xticks(np.arange(num_condition) + 0.4) # set the number of conditions
    # ax.set_xticklabels(['Condition 1', 'Condition 2'])
    ax.set_xticklabels(df['condition'])

    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()


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
app.addButton("Plot", show_plot, 4*len(texts) + 1 + 3, 0)
app.addButton("Submit", on_submit, 4*len(texts) + 1 + 3, 1)
app.addButton("Exit", on_exit, 4*len(texts) + 1 + 3, 3)
app.setStartFunction(init_app)

app.go()