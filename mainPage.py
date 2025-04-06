from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from main import linkage
from timetable import getDayFromIndex as day_name
from matplotlib import pyplot as plt
import numpy as np

subject_codes = {
    "Accounting": "ACCT", "Anthropology": "ANTH", "Art Studies (General)": "ARTS", "Asian Studies": "ASIA",
    "Astronomy": "ASTR", "Biology": "BIOL", "Chemistry": "CHEM", "Child & Youth Care": "CYC", "Chinese": "CHIN",
    "Community Health Promotion": "CHP", "Computer Science": "CSCI", "Creative Writing": "CREW", "Criminology": "CRIM",
    "Dental Hygiene": "DHYG", "Digital Media": "DMED", "Early Childhood Education and Care": "ECEC", "Economics": "ECON",
    "Education": "EDUC", "Education Assistant and Community Support": "EACS", "Engineering": "ENGR", "English": "ENGL",
    "Event Management": "EVNT", "Film Studies": "FILM", "Finance": "FIN", "Fisheries & Aquaculture": "FISH",
    "Forestry": "FRST", "Foundations for Success": "FFSU", "French": "FREN", "Geography": "GEOG", "Geology": "GEOL",
    "Global Studies": "GLST", "Graphic Arts": "GDAG", "Health Sciences & Human Services": "HSER", "History": "HIST",
    "Horticulture": "HORT", "Hospitality Management": "HOSP", "Human Services": "HSER", "Indigenous/Xwulmuxw Studies": "INDG",
    "Information Tech & Applied Systems": "ITAS", "Interdisciplinary Studies": "IDST", "Interior Design": "INTR",
    "Internship": "INTP", "Japanese": "JPNS", "Kinesiology": "KIN", "Law": "LAWW", "Liberal Studies": "LBST",
    "Linguistics": "LING", "Management": "MGMT", "Marketing": "MRKT", "Mathematics": "MATH", "Media Studies": "MDIA",
    "Music": "MUSC", "Nursing – Generic Baccalaureate": "NURS", "Philosophy": "PHIL", "Physical Education – se Kinesiology": "PHED",
    "Physics": "PHYS", "Political Studies": "POLI", "Practical Nursing": "PNUR", "Prior Learning Assessment": "PLAR",
    "Professional Indigenous Land Management": "PILM", "Psychology": "PSYC", "Quantitative Methods": "QUME",
    "Recreation & Sport Management": "RSM", "Religious Studies": "RLST", "Resource Management Officer": "RMOT",
    "Social Science Interdisciplinary": "SSID", "Social Service Worker": "SSWK", "Social Work": "SOWK", "Sociology": "SOCI",
    "Spanish": "SPAN", "Studies in Women and Gender": "SWAG", "Study Skills": "STSK", "Theatre": "THEA", "Tourism Management": "TRMT"
}

term_codes = {"Fall 2024" : "F2024", "Spring 2025" : "S2025", "Fall 2025" : "F2025", "Spring 2026" : "S2026"}
time_periods = ("30 minutes", "1 hour", "1.5 hours", "2 hours", "2.5 hours", "3 hours", "3.5 hours", "4 hours", "4.5 hours", "5 hours", "5.5 hours", "6 hours")

app = QApplication([])
mainPage = QWidget()
mainPage.setWindowTitle("Disgusting Soup")

# Widgets
comboBoxSubject = QComboBox()
comboBoxSubject.addItems(subject_codes.keys())

comboBoxTerm = QComboBox()
comboBoxTerm.addItems(term_codes.keys())

comboBoxTime = QComboBox()
comboBoxTime.addItems(time_periods)

subjectLabel = QLabel("Please, select the subject area")
subjectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

termLabel = QLabel("Please, select the term")
termLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

timeLabel = QLabel("Please, select the time period and days of the week you are available")
timeLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

submitButton = QPushButton("Submit")
quitButton = QPushButton("Quit")

checkBoxM = QCheckBox("Monday")
checkBoxT = QCheckBox("Tuesday")
checkBoxW = QCheckBox("Wednesday")
checkBoxTh = QCheckBox("Thursday")
checkBoxF = QCheckBox("Friday")

# QVideoWidget for the loading animation
videoWidget = QVideoWidget()
videoWidget.setVisible(False)  # Initially hidden
videoWidget.autoFillBackground()

# QMediaPlayer to play the MP4 file
mediaPlayer = QMediaPlayer()
mediaPlayer.setVideoOutput(videoWidget)

# Responsive layout
layout = QVBoxLayout()
layout.addWidget(subjectLabel)
layout.addWidget(comboBoxSubject)
layout.addWidget(termLabel)
layout.addWidget(comboBoxTerm)
layout.addWidget(timeLabel)
layout.addWidget(comboBoxTime)
layout.addWidget(checkBoxM)
layout.addWidget(checkBoxT)
layout.addWidget(checkBoxW)
layout.addWidget(checkBoxTh)
layout.addWidget(checkBoxF)
layout.addWidget(submitButton)
layout.addWidget(quitButton)
#layout.addWidget(videoWidget) #If you uncoment it, animation will be in a top left corner

layout.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Align the whole layout center
mainPage.setLayout(layout)

# Return a course code
def get_course_code() -> str:
    subject = comboBoxSubject.currentText()
    code = subject_codes.get(subject, "N/A")
    print(code)
    return code

# Return a term code
def get_term_code() -> str:
    term = comboBoxTerm.currentText()
    code = term_codes.get(term, "N/A")
    print(code)
    return code

# Return a subject name
def get_subject_name() -> str:
    subject = comboBoxSubject.currentText()
    print(subject)
    return subject

# Return a time period
def get_time_period() -> str:
    time = comboBoxTime.currentText()
    print(time)
    return time

# Returns a list of days for a meeting selected by the user 
def handle_checkboxes() -> list:
    days = [False, False, False, False, False, False, False] # padded with extra falses
    # because our days in the timetable have sat and sun
    # and in order to make it work with the enumeration there the indices have to match
    if checkBoxM.isChecked():
        days[1] = True
    if checkBoxT.isChecked():
        days[2] = True
    if checkBoxW.isChecked():
        days[3] = True
    if checkBoxTh.isChecked():
        days[4] = True
    if checkBoxF.isChecked():
        days[5] = True
    print(days)
    return days

# Function to show the loading animation
def show_loading_animation():
    videoWidget.setVisible(True)
    mediaPlayer.setSource(QUrl.fromLocalFile("Multimedia/Chef_cooking.mp4"))  
    mediaPlayer.play()

# Function to hide the loading animation
def hide_loading_animation():
    mediaPlayer.stop()
    videoWidget.setVisible(False)
    videoWidget.close()

def submit_clicked():

    show_loading_animation()
    QTimer.singleShot(3000, complete_submission) # I assume magic number here is milliseconds

def translate_days(days: list[str]) -> int:
    res = 0
    for day in days:
        match day:
            case 'M':
                res += 0b10000
            case 'T':
                res += 0b01000
            case 'W':
                res += 0b00100
            case 'R':
                res += 0b00010
            case 'F':
                res += 0b00001
    return res

def bits(n: int):
    while n:
        b = n & (~n + 1)
        yield b
        n ^= b

def complete_submission():
    hide_loading_animation()
    plt.close('all') # close all existing matplotlib windows

    courseCode = get_course_code()
    termCode = get_term_code()
    subjectName = get_subject_name()
    timePeriod = get_time_period()
    days_selected = handle_checkboxes()
    if not days_selected:
        days_selected = ['M', 'T', 'W', 'R', 'F']
    res = linkage(courseCode, termCode) # res[0] is timetable, res[1] is heatmap
    tmtbl = res[0]
    htmp = res[1]
    # display timetable
    """# commented out for debug purposes
    dlg = QMessageBox()
    dlg.setWindowTitle("Response")
    txt = ""
    for idx, day in enumerate(tmtbl):
        txt += "{day}: \n {contents}".format(day=day_name(idx),
                                             contents=day.__str__())
    dlg.setText(txt)
    box = dlg.exec()
    if box == QMessageBox.StandardButton.Ok:
        print("OK!")
    """
    for idx, day in enumerate(htmp[1:6], start=1):
        if days_selected[idx]: # would be so, so much nicer as a guard clause, but we can't use continue
            plt.figure(day_name(idx))
            plt.bar(range(len(day.table)), list(day.table.values()), align='center')
            # print(list(map(lambda x: "{s} to {t}".format(s=x[0], t=x[1]), list(htmp[1].table.keys()))))
            plt.xticks(range(len(day.table)),
                       list(map(lambda x: "{s} to {t}".format(s=x[0], t=x[1]), list(day.table.keys()))),
                       rotation='vertical')
            plt.title("Class Times: {day}".format(day=day_name(idx)))
            plt.xlabel("Times")
            plt.ylabel("Number of Classes")
            ax = plt.gca() # get current axes
            ax.set_ylim([0, 6])
            plt.subplots_adjust(bottom=0.3)  # make space at bottom of graph for labels

    plt.show()
    # display heatmap as bar plot





checkBoxM.stateChanged.connect(handle_checkboxes)
checkBoxT.stateChanged.connect(handle_checkboxes)
checkBoxW.stateChanged.connect(handle_checkboxes)
checkBoxTh.stateChanged.connect(handle_checkboxes)
checkBoxF.stateChanged.connect(handle_checkboxes)
submitButton.clicked.connect(submit_clicked)
quitButton.clicked.connect(app.quit)

mainPage.showFullScreen()
app.exec()
