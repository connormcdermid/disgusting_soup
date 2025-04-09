from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QLabel, QWidget, QComboBox, QVBoxLayout, QPushButton, QMessageBox, QCheckBox, QHBoxLayout, QSpacerItem, QSizePolicy, QTextBrowser
from PyQt6.QtCore import Qt, QUrl, QTimer
from PyQt6.QtMultimedia import QMediaPlayer
from PyQt6.QtMultimediaWidgets import QVideoWidget
from main import linkage
from timetable import getDayFromIndex as day_name
from matplotlib import pyplot as plt
import numpy as np
from welcomeScreen import WelcomeScreen
from algorithm import bestTimesInWeek as best_times, getClasses

subject_codes = {
    "Accounting": "ACCT", "Anthropology": "ANTH", "Art Studies (General)": "ARTS", "Asian Studies": "ASIA",
    "Astronomy": "ASTR", "Biology": "BIOL", "Chemistry": "CHEM", "Child & Youth Care": "CYC", "Chinese": "CHIN",
    "Community Health Promotion": "CHPR", "Computer Science": "CSCI", "Creative Writing": "CREW", "Criminology": "CRIM",
    "Dental Hygiene": "DHYG", "Digital Media": "DIGI", "Early Childhood Education and Care": "ECEC", "Economics": "ECON",
    "Education": "EDUC", "Education Assistant and Community Support": "EACS", "Engineering": "ENGR", "English": "ENGL",
    "Event Management": "CONV", "Film Studies": "FILM", "Finance": "FIN", "Fisheries & Aquaculture": "FISH",
    "Forestry": "FRST", "Foundations for Success": "FNFS", "French": "FRCH", "Geography": "GEOG", "Geology": "GEOL",
    "Global Studies": "GLST", "Graphic Arts": "ARTG", "Health Sciences & Human Services": "HHS", "History": "HIST",
    "Horticulture": "HORT", "Hospitality Management": "HOSP", "Human Services": "HSD", "Indigenous/Xwulmuxw Studies": "INDG",
    "Information Tech & Applied Systems": "ITAS", "Interdisciplinary Studies": "INTR", "Interior Design": "ARTI",
    "Internship": "INTP", "Japanese": "JAPA", "Kinesiology": "KIN", "Law": "LAWW", "Liberal Studies": "LBST",
    "Linguistics": "LING", "Management": "MGMT", "Marketing": "MRKT", "Mathematics": "MATH", "Media Studies": "MEDI",
    "Music": "MUSC", "Nursing – Generic Baccalaureate": "NURS", "Philosophy": "PHIL", "Physical Education – se Kinesiology": "PHED",
    "Physics": "PHYS", "Political Studies": "POLI", "Practical Nursing": "PRNU", "Prior Learning Assessment": "PLA",
    "Professional Indigenous Land Management": "PILM", "Psychology": "PSYC", "Quantitative Methods": "QUME",
    "Recreation & Sport Management": "RMGT", "Religious Studies": "RELI", "Resource Management Officer": "RMOT",
    "Social Science Interdisciplinary": "SSID", "Social Service Worker": "SOCW", "Social Work": "SOWK", "Sociology": "SOCI",
    "Spanish": "SPAN", "Studies in Women and Gender": "SWAG", "Study Skills": "STSK", "Theatre": "THEA", "Tourism Management": "TRMT"
}

term_codes = {"Fall 2024" : "F2024", "Spring 2025" : "S2025", "Fall 2025" : "F2025", "Spring 2026" : "S2026"}
time_periods = ("30 minutes", "1 hour", "1.5 hours", "2 hours")

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
checkBoxM.setChecked(True)
checkBoxT = QCheckBox("Tuesday")
checkBoxT.setChecked(True)
checkBoxW = QCheckBox("Wednesday")
checkBoxW.setChecked(True)
checkBoxTh = QCheckBox("Thursday")
checkBoxTh.setChecked(True)
checkBoxF = QCheckBox("Friday")
checkBoxF.setChecked(True)

# QVideoWidget for the loading animation
videoWidget = QVideoWidget()
videoWidget.setVisible(False)  # Initially hidden
videoWidget.autoFillBackground()

# QMediaPlayer to play the MP4 file
mediaPlayer = QMediaPlayer()
mediaPlayer.setVideoOutput(videoWidget)

# Responsive layout
layout = QVBoxLayout()
bestWindow = QMessageBox()
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

def get_time_as_int(time) -> int:
    match time:
        case '30 minutes':
            return 30
        case '1 hour':
            return 60
        case '1.5 hours':
            return 90
        case '2 hours':
            return 120
        case _:
            raise ValueError("Unrecognised time value!")

# Returns a list of days for a meeting selected by the user
def handle_checkboxes() -> list:
    days = [False, True, True, True, True, True, False] # padded with extra Trues
    # because our days in the timetable have sat and sun
    # and in order to make it work with the enumeration there the indices have to match
    
    if not checkBoxM.isChecked():
        days[1] = False
    if not checkBoxT.isChecked():
        days[2] = False
    if not checkBoxW.isChecked():
        days[3] = False
    if not checkBoxTh.isChecked():
        days[4] = False
    if not checkBoxF.isChecked():
        days[5] = False
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

def strbuild(l: list[tuple]) -> str:
    final: str = ""
    for item in l:
        final += "From {t1} to {t2} on {day}\n".format(
            t1=item[0],
            t2=item[1],
            day=item[2]
        )
    return final

currentBestTimesWidget = None

def complete_submission():
    global currentBestTimesWidget
    hide_loading_animation()
    plt.close('all')  # Close all existing matplotlib windows

    courseCode = get_course_code()
    termCode = get_term_code()
    subjectName = get_subject_name()
    timePeriod = get_time_period()
    days_selected = handle_checkboxes()
    res = linkage(courseCode, termCode)  # res[0] is timetable, res[1] is heatmap
    tmtbl = res[0]
    htmp = res[1]

    # Display timetable (existing logic)
    for idx, day in enumerate(htmp[1:6], start=1):
        if days_selected[idx]:
            plt.figure(day_name(idx))
            plt.bar(range(len(day.table)), list(day.table.values()), align='center')
            plt.xticks(range(len(day.table)),
                       list(map(lambda x: "{s} to {t}".format(s=x[0], t=x[1]), list(day.table.keys()))),
                       rotation='vertical')
            plt.title("Class Times: {day}".format(day=day_name(idx)))
            plt.xlabel("Times")
            plt.ylabel("Number of Classes")
            ax = plt.gca()  # Get current axes
            ax.set_ylim([0, 6])
            plt.subplots_adjust(bottom=0.3)  # Make space at bottom of graph for labels

    # Only try to check best times if there are days selected
    timeString = "Recommended times for your meeting:\n\n"
    if True in handle_checkboxes():
        bestTimes = getClasses(tmtbl, best_times(tmtbl, get_time_as_int(timePeriod), days_selected))

        for time, courses in bestTimes.items():
            timeString += "On " + time[2] + " from " + time[0] + " to " + time[1] + "\n"
            timeString += "Courses during this time: "
            for c in courses:
                timeString += "\n\t - " + c

            timeString += "\n \n"

        # Remove the previous bestTimes widget if it exists
        if currentBestTimesWidget is not None:
            layout.removeWidget(currentBestTimesWidget)
            currentBestTimesWidget.deleteLater()
            currentBestTimesWidget = None

        currentBestTimesWidget = QTextBrowser()
        testLayout = QVBoxLayout()

        currentBestTimesWidget.setWindowTitle("Recommended times for your meeting:")
        widget = QLabel(timeString)
        testLayout.addWidget(widget)
        currentBestTimesWidget.setLayout(testLayout)
        layout.addWidget(currentBestTimesWidget)
        currentBestTimesWidget.setVisible(True)

    plt.show()

checkBoxM.stateChanged.connect(handle_checkboxes)
checkBoxT.stateChanged.connect(handle_checkboxes)
checkBoxW.stateChanged.connect(handle_checkboxes)
checkBoxTh.stateChanged.connect(handle_checkboxes)
checkBoxF.stateChanged.connect(handle_checkboxes)
submitButton.clicked.connect(submit_clicked)
quitButton.clicked.connect(app.quit)

# Function to show the main page
def show_main_page():
    mainPage.setFixedSize(800, 800)
    mainPage.show()


# Show the welcome screen
welcomeScreen = WelcomeScreen(on_finished_callback=show_main_page)
welcomeScreen.show()

# Start the application event loop
app.exec()
