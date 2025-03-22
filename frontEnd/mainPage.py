from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QComboBox, QVBoxLayout
from PyQt6.QtCore import Qt

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
    "Internship": "INTP", "Japanese": "JPNS", "Kinesiology": "KIN", "Law": "LAW", "Liberal Studies": "LBST",
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

# Responsive layout
layout = QVBoxLayout()
layout.addWidget(subjectLabel)
layout.addWidget(comboBoxSubject)
layout.addWidget(termLabel)
layout.addWidget(comboBoxTerm)

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

comboBoxSubject.currentIndexChanged.connect(get_course_code)
comboBoxTerm.currentIndexChanged.connect(get_term_code)

mainPage.showFullScreen()
app.exec()
