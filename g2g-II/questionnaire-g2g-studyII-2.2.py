# Created by haipeng.wang@gmail.com
# v1.0, 20221211

# You MUST customize the "header" and left and right labels set before using the scale.

import os
from appJar import gui

## data file.
fname = "questionnaire-g2gII-2.2.txt"

## Called when the submit button is clicked
def on_submit():
    if not os.path.exists(fname):
        # define header of log file.
        header = '# ' + 'uid ' + 'preferred'
        file_handle = open(fname, "a")
        file_handle.write(header + '\n')
        file_handle.close()        
        
    user_id = app.getSpinBox("User ID")
    preferred = app.getRadioButton("preferred")
        
    file_handle = open(fname, "a")

    write_string = ''
    write_string += str(user_id) + ' '
    write_string += str(preferred)
        
    file_handle.write(write_string + '\n')
    file_handle.close()
    
    app.infoBox("Questionnaire Input", "Input successfully.")

def on_exit():
    app.stop()


## Main entry point
app = gui()
# app.showSplash("Questionnaire", fill='red', stripe='black', fg='white', font=44)
app.setTitle("Questionnaire")
app.setSize(1000, 300)
app.setFont(size=16, weight="bold")

app.addLabelSpinBoxRange("User ID", 1, 100, row=0, column=0)

app.addHorizontalSeparator(colspan=2)
app.addLabel("Which of the methods was preferred: ", row=app.getRow())
app.addRadioButton("preferred", "Seated Horizontal phone on Table", row="previous", column=1)
app.addRadioButton("preferred", "Seated Vertical phone on Table", column=1)
app.addRadioButton("preferred", "Seated Vertical phone Hold in Hand", column=1)
app.addRadioButton("preferred", "Standing Vertical phone Hold in Hand", column=1)
app.addRadioButton("preferred", "Walking Vertical phone Hold in Hand", column=1)

app.setSticky("we")
app.addButton("Exit", func=on_exit, row=app.getRow(), column=0)
app.addButton("Submit", func=on_submit, row="previous", column=1, colspan=2)

app.go()


