from bs4 import BeautifulSoup as BS
from Course import Course
from Day import Day


def getSoup(filename: str = "response.xml") -> BS:
    """
    Given an XML file, reads the file and constructs a BeautifulSoup object out of it.
    """
    try:
        with open(filename, 'r', encoding="utf-8") as file:
            print(f'Reading timetable {filename} ...')
            timetable = file.read()
            dsoup = BS(timetable, "lxml-xml") # parse with XML parser
            # print(dsoup)
            return dsoup
    except:
        print("ERROR: cannot open", filename)


def get_courses(dsoup: BS) -> list[Course]:
    """
    Given a BeautifulSoup object (parsed XML document), creates a list of Course objects to be used to make a timetable.
    """
    tags = dsoup.find_all('Course')
    courses = []
    for course in tags:
        courses.append(Course(course)) # append a new Course object
    return courses


def getDayIndex(day: str) -> int:
    """
    Gets passed a day string (of any of the 3 forms found in the XML doc), and returns the
    appropriate index for that day in a timetable.
    """
    """
    dayIndex = {0: ['U', 'Su', 'Sunday'], 
                1: ['M', 'Mo', 'Monday'],
                2: ['T', 'Tu', 'Tuesday'],         
                3: ['W', 'We', 'Wednesday'],     
                4: ['R', 'Th', 'Thursday'], 
                5: ['F', 'Fr', 'Friday'], 
                6: ['S', 'Sa', 'Saturday']}  
    
    for key, val in dayIndex.items():
        if day in val:
            return key
    
    return -1 
    """
    match day:
        case "U" | "Su" | "Sunday":
            return 0
        case "M" | "Mo" | "Monday":
            return 1
        case "T" | "Tu" | "Tuesday":
            return 2
        case "W" | "We" | "Wednesday":
            return 3
        case "R" | "Th" | "Thursday":
            return 4
        case "F" | "Fr" | "Friday":
            return 5
        case "S" | "Sa" | "Saturday":
            return 6
        case _:
            return -1 # Default case


def getDayFromIndex(index: int, form: int = 2) -> str:
    """
    Get a day of the week by index.

    Get a day of the week by an index. Sunday is 0. If keyword arg form is specified (from 0-2) the
    day will be returned in a different format.
    0: Single letter
    1: Two letter abbreviation
    2: Full name.
    :param index: Index of day of the week
    :param form: Form to retrieve day as
    :return: Day, in specified form.
    """
    dayIndex = {0: ['U', 'Su', 'Sunday'],
                1: ['M', 'Mo', 'Monday'],
                2: ['T', 'Tu', 'Tuesday'],         
                3: ['W', 'We', 'Wednesday'],     
                4: ['R', 'Th', 'Thursday'], 
                5: ['F', 'Fr', 'Friday'], 
                6: ['S', 'Sa', 'Saturday']}  
    
    return dayIndex.get(index)[form]


def makeTimetable(courses: list[Course]) -> list[Day]:
    """
    Constructs a timetable given a list of courses. This timetable is a list of 7 Day objects.
    Each Day object contains a dictionary, where the keys are timeblocks and the values are the
    courses at that timeblock.
    """
    schedule = [] 
    for i in range(7):
        schedule.append(Day()) 

    for course in courses:
        for day in course.times.keys(): 
            dayInd = getDayIndex(day)
            for time in course.times[day]:
                
                schedule[dayInd].addTime(course.name, time[0], time[1])
        
    return schedule


def scheduleHeatmap(timetable: list[Day]) -> list[Day]:
    """
    Given a timetable, creates a timetable-like list that associates each time block in a day with an integer.
    This integer represents the number of courses in session during that particular timeblock on that day.
    """
    heatmap = [] 
    for i in range(7):
        heatmap.append(Day()) 

    for day in timetable:
        dayIndex = timetable.index(day)
        for time in day.table.keys():
            heatmap[dayIndex].table[time] = len(day.table[time])
    return heatmap


if __name__ == '__main__':
    soup = getSoup()
    courses = get_courses(soup)
    s = makeTimetable(courses)
    for day in s:
        print("Day:", getDayFromIndex(s.index(day)))
        
        for time in day.table.keys():
            if (len(day.table[time]) > 0):
                print(time, "-", day.table[time])
    
    h = scheduleHeatmap(s)
    for day in h:       
        for time in day.table.keys():
            print("Number of courses at:", getDayFromIndex(h.index(day)), ":", time, "-", day.table[time])