# parsing function
# constructs timetable array

from bs4 import BeautifulSoup as BS
from Course import Course
from Day import Day

def getSoup(filename: str = "response.xml") -> BS:
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
    tags = dsoup.find_all('Course')
    courses = []
    for course in tags:
        courses.append(Course(course)) # append a new Course object
    return courses

def getDayIndex(day: str) -> int:
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

def getDayFromIndex(index: int) -> str:
    dayIndex = {0: ['U', 'Su', 'Sunday'], 
                1: ['M', 'Mo', 'Monday'],
                2: ['T', 'Tu', 'Tuesday'],         
                3: ['W', 'We', 'Wednesday'],     
                4: ['R', 'Th', 'Thursday'], 
                5: ['F', 'Fr', 'Friday'], 
                6: ['S', 'Sa', 'Saturday']}  
    
    return dayIndex.get(index)[2]

def makeTimetable(courses: list[Course]) -> list[Day]: 
    """
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
"""        
    
   	# Getting all courses
    courses = dsoup.find_all('Course')

    for course in courses:
        # print(course)
        courseName = course.CrsID.string
        print(courseName)
        print("Meeting Times: ")
        sections = course.find_all('Section')
        print(sections.Intake.string, ": ", )

"""



def scheduleHeatmap(schedule: list[Day]) -> list[Day]:
    heatmap = [] 
    for i in range(7):
        heatmap.append(Day()) 

    for day in schedule:
        dayIndex = schedule.index(day)
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
        print("Day:", getDayFromIndex(h.index(day)))
        
        for time in day.table.keys():
            print("Number of courses at:", time, "-", day.table[time])