import requests

def get_course_code(dept: str) -> str:
    match dept:
        case "All Degree/Diploma" | "ALL": return "0007"
        case "Courses with Free Seats" | "FREE": return "0003"
        case "Accounting" | "ACCT": return "000X"
        case "Anthropology" | "ANTH": return "000Z"
        case "Art Studies (General)" | "ARTS": return "0011"
        case "Asian Studies" | "ASIA": return "0001"
        case "Astronomy" | "ASTR": return "0012"
        case "Biology" | "BIOL": return "0014"
        case "Chemistry" | "CHEM": return "0016"
        case "Child & Youth Care" | "CYC": return "0017"
        case "Chinese" | "CHIN": return "0018"
        case "Community Health Promotion" | "CHPR": return "000P"
        case "Computer Science" | "CSCI": return "0019"
        case "Creative Writing": return "001A"
        case "Criminology" | "CRIM": return "001B"
        case "Dental Hygiene": return "001C"
        case "Digital Media": return "001D"
        case "Early Childhood Education and Care": return "001E"
        case "Economics" | "ECON": return "001F"
        case "Education" | "EDUC": return "001G"
        case "Education Assistant and Community Support" | "EACS": return "000I"
        case "Engineering" | "ENGR": return "001J"
        case "English" | "ENGL": return "001I"
        case "English Language Intercultural Studies" | "ELIS": return "0004"
        case "Event Management": return "001K"
        case "Film Studies" | "FILM": return "001L"
        case "Finance" | "FNCE": return "001M"
        case "Fisheries & Aquaculture" | "FISH": return "001O"
        case "Forestry" | "FRST": return "001P"
        case "Foundations for Success" | "FNFS": return "0009"
        case "French" | "FRCH": return "001Q"
        case "Geography" | "GEOG": return "001R"
        case "Geology" | "GEOL": return "001S"
        case "Global Studies" | "GLST": return "001T"
        case "Graphic Arts" | "ARTG": return "000N"
        case "Health Sciences & Human Services" | "HSHS": return "000O"
        case "History" | "HIST": return "001Z"
        case "Horticulture" | "HORT": return "0020"
        case "Hospitality Management" | "HOSP": return "0021"
        case "Human Services": return "0022" # No courses offered this term
        case "Indigenous/Xwulmuxw Studies" | "INDG": return "001N"
        case "Information Tech & Applied Systems" | "ITAS": return "0023"
        case "Interdisciplinary Studies" | "INTR": return "0008"
        case "Interior Design" | "ARTI": return "000U"
        case "Internship" | "INTP": return "000S"
        case "Japanese" | "JAPA": return "0024"
        case "Kinesiology" | "KIN": return "000V"
        case "Law" | "LAWW": return "0025"
        case "Liberal Studies" | "LBST": return "0026"
        case "Linguistics": return "000J" # No courses offered this term
        case "Management" | "MGMT": return "0027"
        case "Marketing" | "MRKT": return "0028"
        case "Mathematics" | "MATH": return "0029"
        case "Media Studies" | "MEDI": return "002A"
        case "Music" | "MUSC": return "002B"
        case "Nursing - Generic Baccalaureate" | "NURS": return "002C"
        case "Philosophy" | "PHIL": return "002D"
        case "Physical Education - se Kinesiology": return "002E" # No courses offered this term
        case "Physics" | "PHYS": return "002F"
        case "Political Studies" | "POLI": return "002G"
        case "Practical Nursing" | "PRNU": return "002I"
        case "Prior Learning Assessment": return "002J" # No courses offered this term
        case "Professional Indigenous Land Management" | "PILM": return "000T"
        case "Psychology" "PSYC": return "002L"
        case "Quantitative Methods" | "QUME": return "002N"
        case "Recreation & Sport Management" | "RMGT": return "002O"
        case "Religious Studies" | "RELI": return "002P"
        case "Resource Management Officer" | "RMOT": return "002Q"
        case "Science": return "002R"
        case "Social Science Interdisciplinary": return "002S"
        case "Social Service Worker" | "SOCW": return "002T"
        case "Social Work": return "002U"
        case "Sociology" | "SOCI": return "002V"
        case "Spanish" | "SPAN": return "002W"
        case "Studies in Women and Gender" | "SWAG": return "000H"
        case "Study Skills": return "002X"
        case "Theatre" | "THEA": return "002Y"
        case "Tourism Management" | "TRMT": return "002Z"
        case _:
            raise ValueError("Unrecognised course code!")



def makeRequest(dept: str, session: str = "S2025") -> str:
    course_code = get_course_code(dept)
    url = "https://isapp.viu.ca/XMLRequest/xmlrequest"
    headers = {
        'Accept': 'application/xml, text/xml, */*; q=0.01',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Referer': 'https://isapp.viu.ca/srs/timetable.htm',
        'Content-Type': 'application/x-www-form-urlencoded',
        'DbInstance': 'DEFAULT',
        'Origin': 'https://isapp.viu.ca',
        'Connection': 'keep-alive',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'Priority': 'u=0'
    }
    payload = {'xmlrequest':
                   "<Request>"
                   + "<Transactions>"
                   + "<GetTimetable>"
                   + "<TransactionID>"
                   + "GetTimetable"
                   + "</TransactionID>"
                   + "<FormID>timetable</FormID>"
                   + "<SessionID>ACAD/{sess}</SessionID>".format(sess = session)
                   + "<Campus>N</Campus>"
                   + "<ProgramArea>0005</ProgramArea>"
                   + "<CrsArea>{code}</CrsArea>".format(code = course_code)
                   + "<CrsID/>"
                   "<CrsKeyword/>"
                   "<DeliveryMode/>"
                   "<ShowDescriptions/>"
                   "<ShowCancelledIntakes/>"
                   "<ShowContinuousIntake/>"
                   "<OperUnits>CTU</OperUnits>"
                   "<ShowInstructors>Y</ShowInstructors>"
                   "</GetTimetable>"
                   "</Transactions>"
                   "</Request>"}
    r = requests.post(url, headers=headers, data=payload)
    return r.text

if __name__ == '__main__':
    print(makeRequest("CSCI"))
