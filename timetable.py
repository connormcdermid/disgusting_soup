# parsing function
# constructs timetable array

from bs4 import BeautifulSoup as BS
from Course import Course


def getSoup(filename: str = "response.xml") -> BS:
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            print(f'Reading timetable" {filename} ...')
            timetable = file.read()
            dsoup = BS(timetable, "lxml-xml") # parse with XML parser
            # print(dsoup)
            return dsoup
    except:
        print("ERROR: cannot open", filename)

def get_courses(dsoup: BS) -> list[Course]:
    tags = dsoup.find_all('Course')
    courses = []
    for course in tags:
        courses.append(Course(course)) # append a new Course object
    return courses

def makeTimetable(dsoup: BS) -> list: 
    """
    """
    schedule = [[[]]] # Declare 3D list
    
   	# Getting all courses
    courses = dsoup.find_all('Course')

    for course in courses:
        # print(course)
        courseName = course.CrsID.string
        print(courseName)
        print("Meeting Times: ")
        sections = course.find_all('Section')
        print(sections.Intake.string, ": ", )


    return schedule

    # <Course> - each course
    # <CrsID> - course name/ID
    # <Intake> - section name
    # <sessioncode> - S2025
    # <DaysOfWeekShortNames> - Su, Mo, Tu, We, Th, Fr, Sa
    # <StartTime> - 1430
    # <EndTime> - 1530


# Days: Sunday - Saturday -> 7 blocks
# Hours: 07:00 - 19:00 -> 24 blocks

if __name__ == '__main__':
    soup = getSoup()
    courses = get_courses(soup)
    for course in courses:
        course.print_times()



