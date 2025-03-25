from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout, QPushButton, QMessageBox
from PyQt6.QtCore import Qt
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
    "Music": "MUS", "Nursing – Generic Baccalaureate": "NURS", "Philosophy": "PHIL", "Physical Education – se Kinesiology": "PHED",
    "Physics": "PHYS", "Political Studies": "POLI", "Practical Nursing": "PNUR", "Prior Learning Assessment": "PLAR",
    "Professional Indigenous Land Management": "PILM", "Psychology": "PSYC", "Quantitative Methods": "QUME",
    "Recreation & Sport Management": "RSM", "Religious Studies": "RLST", "Resource Management Officer": "RMOT",
    "Social Science Interdisciplinary": "SSID", "Social Service Worker": "SSWK", "Social Work": "SOWK", "Sociology": "SOCI",
    "Spanish": "SPAN", "Studies in Women and Gender": "SWAG", "Study Skills": "STSK", "Theatre": "THEA", "Tourism Management": "TMGT"
}

term_codes = {"Fall 2024" : "F2024", "Spring 2025" : "S2025", "Fall 2025" : "F2025", "Spring 2026" : "S2026"}

app = QApplication([])
mainPage = QWidget()
mainPage.setWindowTitle("Disgusting Soup")

# Widgets
comboBoxSubject = QComboBox()
comboBoxSubject.addItems(subject_codes.keys())

comboBoxTerm = QComboBox()
comboBoxTerm.addItems(term_codes.keys())

subjectLabel = QLabel("Please, select the subject area")
subjectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

termLabel = QLabel("Please, select the term")
termLabel.setAlignment(Qt.AlignmentFlag.AlignHCenter)

submitButton = QPushButton("Submit")
quitButton = QPushButton("Quit")

# Responsive layout
layout = QVBoxLayout()
layout.addWidget(subjectLabel)
layout.addWidget(comboBoxSubject)
layout.addWidget(termLabel)
layout.addWidget(comboBoxTerm)
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

def submit_clicked():
    courseCode = get_course_code()
    termCode = get_term_code()
    subjectName = get_subject_name()
    res = linkage(courseCode, termCode) # res[0] is timetable, res[1] is heatmap
    tmtbl = res[0]
    htmp = res[1]
    # display timetable
    """ commented out for debug purposes
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
        plt.figure(day_name(idx))
        plt.bar(range(len(day.table)), list(day.table.values()), align='center')
        # print(list(map(lambda x: "{s} to {t}".format(s=x[0], t=x[1]), list(htmp[1].table.keys()))))
        plt.xticks(range(len(day.table)),
                   list(map(lambda x: "{s} to {t}".format(s=x[0], t=x[1]), list(day.table.keys()))),
                   rotation='vertical')
        plt.title("Class Times: {day}".format(day=day_name(idx)))
        plt.xlabel("Times")
        plt.ylabel("Number of Classes")
        plt.subplots_adjust(bottom=0.3)  # make space at bottom of graph for labels

    plt.show()
    # display heatmap as bar plot






submitButton.clicked.connect(submit_clicked)
quitButton.clicked.connect(app.quit)

mainPage.showFullScreen()
app.exec()
