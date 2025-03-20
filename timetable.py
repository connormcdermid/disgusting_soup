# parsing function
# constructs timetable array

from bs4 import BeautifulSoup as BS

def makeTimetable(filename: str = "response.xml") -> list: 
    """
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            print(f'Reading timetable" {filename} ...')
            timetable = file.read()
            dsoup = BS(timetable, "lxml-xml") # parse with XML parser
    except:
        print("ERROR: cannot open", filename)
    print(type(timetable))
    
    scheduleMap = [[[]]] # Declare 3D list
    print(dsoup)
   	# Getting all courses
    courses = dsoup.find_all('Course')
    for course in courses:
        print(course)
        courseName = dsoup.CrsID.string
        print(courseName)

    return scheduleMap

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
    makeTimetable()




