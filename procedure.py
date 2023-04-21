# Created by haipeng.wang@gmail.com
# v4.5, 20230319, added enfored breaks between blocks to reduce the effect of fatigue.
# v4.4, 20230316, added an attention tab following main-experiment tab.
# v4.3, 20230309, change the UID to PID.
# v4.2, 20230303, added UID arrangements and Latin square enforcement.
# v4.1, 20230302, added reminder about how do interview and debrief.
# v4.0, 20230221, added a tab of appendix.
# v3.2, 20230221, added "please describe or label the technique?" and "Anything else want to say?" in post-experiment.
# v3.1, 20230218, added a new tab about post-study check.
# v3.0, 20230216, support changing the conditions during the pilot.
# v2.1, 20221212, minor improvement for preparation and intervew.
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

def on_exit():
    app.stop()

def checked(cb):
    """print the checked time."""
    app.setCheckBoxText(cb, text = cb + ' | ' + str(datetime.datetime.now().strftime("%H:%M:%S")))
    file_handle = open(fname, "a")
    file_handle.write(cb + ' | ' + str(datetime.datetime.now().strftime("%H:%M:%S")) + '\n')
    file_handle.close()

def conditionChanged():
    tmp_cond = app.getOptionBox("Condition")

    file_handle = open(fname, "a")
    file_handle.write('\n' + "condition: " + tmp_cond + '\n')
    file_handle.close()
    
    app.clearAllCheckBoxes()

## Main entry point
app = gui()
# app.showSplash("Procedure \n Guide and Track Experiment \n haipeng.wang at gmail", fill='red', stripe='black', fg='white', font=44)
app.setTitle("Pilot Study - Procedure Guide and Tracking")
app.setSize(1200, 700)
app.setFont(size=16, weight="bold")

## experiments basic settings
app.addLabelOptionBox("Experiment", experiments, 0, 0)
app.addLabelSpinBoxRange("User ID", 1, 100, 0, 1)

# app.addLabelOptionBox("Condition", conditions, 0, 2)
# app.setOptionBoxChangeFunction("Condition", conditionChanged)
# app.setStartFunction(conditionChanged)

app.startTabbedFrame("TabbedFrame", colspan=4)
app.setSticky("w")
app.setFont(20)

## preparation
app.startTab("0. Preparation")
app.addCheckBox("1 primary investigator; 2 assistants for video and interview respectively")
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
app.addCheckBox("PID arrangement")
app.addCheckBox("enforce Latin Square", row="previous", column=1)
app.addCheckBox("Demographic")
app.addCheckBox("Instruction: play video.")
app.addCheckBox("Answer questions", row="previous", column=1)
app.addCheckBox("Practice: Task + TLX & Survey (confirm TLX scores with users)")
app.addNamedCheckBox(name="Answer questions", title="Answer practice questions", row="previous", column=1)
app.addNamedCheckBox(name="Break", title="Break after practice")
app.stopTab()

## Main-experiment
app.startTab("2. Main-Experiment")
app.addLabelOptionBox("Condition", conditions, column=2)
app.setOptionBoxChangeFunction("Condition", conditionChanged)
# app.setStartFunction(conditionChanged)


app.addCheckBox("Turn on video recorders.")
app.addCheckBox("to proceed as quickly and accurately as possible but at a pace that is comfortable.", colspan=4)
app.addCheckBox("Think Aloud (optional)")

app.addCheckBox("Block-0", column=0)
app.addNamedCheckBox(name="Trials \u00D7 2", title="trial-0", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-0", row="previous", column=2)
app.addNamedCheckBox(name="Break(must)", title="break-0", row="previous", column=3)

app.addCheckBox("Block-1", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-1", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-1", row="previous", column=2)
app.addNamedCheckBox(name="Break(must)", title="break-1", row="previous", column=3)

app.addCheckBox("Block-2", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-2", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-2", row="previous", column=2)
app.addNamedCheckBox(name="Break(must)", title="break-2", row="previous", column=3)

app.addCheckBox("Block-3", column=0)
app.addNamedCheckBox(name="Trials \u00D7 3", title="trial-3", row="previous", column=1)
app.addNamedCheckBox(name="TLX + Q", title="survey-3", row="previous", column=2)
app.addNamedCheckBox(name="Break(must)", title="break-3", row="previous", column=3)

app.addLabel("Enforce break between blocks to reduce effects of fatigue.", colspan=2)

app.stopTab()

# Attention to the main-experiment
app.startTab("2.1 Attention")
app.addLabel("During Practice and Block-0:")
app.addCheckBox("Observe and give full guides to participants.")
app.addCheckBox("Keep eyes on participants.")
app.addLabel("During B1-B3:")
app.addCheckBox("No special emergent requests from users, no any saying, help from investigators.")
app.addCheckBox("Don't introduce systematic biases from investigators.")
app.stopTab()

## Post-experiment
app.startTab("3. Post-Experiment")
app.addCheckBox("User break.")
app.addCheckBox("Turn on audio recorders.")
app.addCheckBox("review survey to find questions for interview.", row="previous", column=1, colspan=2)
app.addCheckBox("Interview:")
app.addCheckBox("closed questions.", row="previous", column=1)
app.addCheckBox("How would you describe or label the technique?", row="previous", column=2)
app.addLabel("conversation, not just ask Q and get Answer.")
app.addCheckBox("open questions.", row="previous", column=1)
app.addCheckBox("What features you like or dislike? and Why?", row="previous", column=2)
app.addCheckBox("repeat and confirm.", column=1, colspan=2) # repeat your understanding and confirm with users.
app.addCheckBox("Debrief (Purpose and Benefits)")
app.addCheckBox("Anything else want to say?", row="previous", column=1)
app.addNamedCheckBox(name="Answer questions", title="Answer Debrief", row="previous", column=2)
app.addCheckBox("Maintain participants pool.")
app.addCheckBox("Thank you, good bye!")
app.stopTab()

# Post-study check
app.startTab("4. Post-study check")
app.addCheckBox("check TLX data, if it works correctly.")
app.addCheckBox("check questionnaire data, if it works correctly.")
app.addCheckBox("check study log data.")
app.stopTab()

# Appendix
app.startTab("5. Appendix")
app.addCheckBox("Video shows HOW users conduct an interactive behavior. For example, how make errors.")
app.addCheckBox("Interview finds WHY users have such interactive behavior.")
app.stopTab()

app.stopTabbedFrame()

tk = app.getAllCheckBoxes().keys()
for i, entry in enumerate(tk):
    app.setCheckBoxChangeFunction(entry, checked)

app.setSticky("we")
row = app.getRow()
app.addButton("Exit", on_exit, row, 3)

app.go()


