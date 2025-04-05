from Day import Day
from timetable import makeTimetable, getDayFromIndex
from timetable import *

def addTime(a, b) -> int:
    """adds a number of minutes to a time, and returns the result

    Args:
        a (_type_): the time to start with. Example "700" is 7 am.
        b (_type_): the number of Minutes to add to time a. Example "90" is one and a half hours.

    Returns:
        int: the time 'a' 'b' minutes later.
    """
    time = a + (int(b / 60) * 100)
    #print(time)
    time = time + (b % 60)
    if(time > 2400):
        time = time - 2400
    if(time % 100 > 59):
        time = time + 40
        
    return int(time)
    

def calculateDayScores(day: Day, meetingLength: int, dayName: str) -> dict:
    """Computes a "viability" score for each possible meeting time in a day.

    Args:
        day (Day): Contains course schedule for that day
        meetingLength (int): length of the meeting in MINUTES.
        dayName (str): the name of the day

    Returns:
        list: some sort of tuple with the time block start and end, and its "viability" score? 
    """
    dayScores = {}
    for timeblock in day.table.keys(): #we start at each 30 minute timeblock in a day
      
        start = int(timeblock[0])

        if(addTime(start, meetingLength)) < 2100: #check if the time is early enough to have a full meeting before the day is over (9pm)
            meetingStart = start
            prevClassScore = 0
            classScore=0
            for i in range (0, int(meetingLength / 30), 1): #count the number of 30 min blocks the meeting takes, and check that number of blocks after the supposed start
           
                a = day.table[(str(meetingStart).zfill(4), str(addTime(meetingStart, 30)).zfill(4))] #the list of courses occuring at a 30 min block
                classScore += len(a)

                meetingStart = addTime(meetingStart, 30)

                prevClassScore = classScore
                
                    
        dayScores[(str(start).zfill(4), str(addTime(start, meetingLength)).zfill(4), dayName)] = classScore
    keys = list(dayScores.keys())

    prevClassScore = 0

    for i in range(len(keys)):     
        currClassScore = dayScores[keys[i]]

        if i < len(keys) -1:   
            nextClassScore = dayScores[keys[i+1]]
        else:
            nextClassScore = 0
        
        if currClassScore < 6:

            if prevClassScore > currClassScore:
                dayScores[keys[i]] -= (prevClassScore - currClassScore) / ((meetingLength / 30) * 0.75)
            if nextClassScore > currClassScore:
                dayScores[keys[i]] -= (nextClassScore - currClassScore) / (meetingLength / 30)
        # if time is further from the middle of the day, negate
        if int(keys[i][0]) <= 800 or int(keys[i][0]) >= 1700:
            dayScores[keys[i]] += 3
        elif int(keys[i][0]) <= 1000 or int(keys[i][0]) >= 1530:
            dayScores[keys[i]] += 1
        prevClassScore = currClassScore

    return dayScores      
            
def bestTimesInWeek(week: list[Day], meetingLength: int) -> list[tuple]:
    """For every day in the week, compute the  3 best meeting times.

    Args:
        week (list[Day]): A timetable - Represenation of all classes in a week
        meetingLength (int): length of the meeting in mintues.
    """
    allTimes = {}
    
    for i in range(1, 6): # Exclude Saturday and Sunday
        allTimes = allTimes | calculateDayScores(week[i], meetingLength, getDayFromIndex(i))

    sorted_by_values_asc = sorted(allTimes.items(), key = lambda item: item[1], reverse = False)

    topScores = []
    for i in range(5):
        topScores.append(sorted_by_values_asc[i][0])

    return topScores

def getClasses(week: list[Day], topScores) -> dict:
    classes = {}
    for time in topScores:
        classes[time] = []
        day = week[getDayIndex(time[2])]
       
        currTime = int(time[0])
        while (currTime < int(time[1])):
            c = day.table[(str(currTime).zfill(4), str(addTime(currTime, 30)).zfill(4))]
            classes[time].extend(c)
            currTime = addTime(currTime, 30)
    return classes

if __name__ == '__main__':
    soup = getSoup()
    h = get_timetable(soup)

    print(getClasses(h, bestTimesInWeek(h, 90)))