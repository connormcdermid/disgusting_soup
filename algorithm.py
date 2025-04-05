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
        score = 0
        start = int(timeblock[0])
        if(addTime(start, meetingLength)) < 2100: #check if the time is early enough to have a full meeting before the day is over (9pm)
            meetingStart = start
            prevClassScore = 0
            classScore=0
            for i in range (1, int(meetingLength / 30), 1): #count the number of 30 min blocks the meeting takes, and check that number of blocks after the supposed start
                #print("i is ",i)
                #sum number of classes in the meeting block
                #print('start',str(meetingStart).zfill(4))
                #print('end',str(self.addTime(meetingStart,i*30)).zfill(4))
                
                a = day.table[(str(meetingStart).zfill(4), str(addTime(meetingStart, 30)).zfill(4))] #the list of courses occuring at a 30 min block
                classScore += len(a)

                meetingStart = addTime(meetingStart, 30)
                #print(start)

                prevClassScore = classScore
                
                    
        dayScores[(str(start).zfill(4), str(addTime(start, meetingLength)).zfill(4), dayName)] = classScore

    keys = dayScores.keys()

    prevClassScore = 0

    for i in range(len(keys)):     
        currClassScore = dayScores[keys[i]]

        if currClassScore > 6:
            dayScores[keys[1]] = (100 - currClassScore)
        else:
            if i < len(keys) -1:   
                nextClassScore = dayScores[[i+1]]
            else:
                nextClassScore = 0

            if prevClassScore > currClassScore:
                dayScores[keys[i]] += ((prevClassScore - currClassScore) + 2) * (100 - currClassScore)

            if nextClassScore > currClassScore:
                dayScores[keys[i]] += ((nextClassScore - currClassScore) + 1) * (100 - currClassScore)

        prevClassScore = currClassScore

    # if time is further from the middle of the day, negate

    return dayScores      
            
"""
number of classes <= 6
number of classes in block before and after is much higher
time is closer to the middle of the day

timeBefore: 4
time: 2
timeAfter: 2
time is at 1300
score = 2 * 0 * 3 + 5 

score = (num. class before - num. class) * (num. class after - num. class) * (5 - num. class) + timeBonus
"""        
        

def bestTimesInWeek(week: list[Day], meetingLength: int):
    """For every day in the week, compute the  3 best meeting times.

    Args:
        week (list[Day]): Represenation of all classes in a week
        meetingLength (int): length of the meeting in mintues.
    """
    allTimes = {}
    
    for day in week:
        allTimes = allTimes | calculateDayScores(day, meetingLength, getDayFromIndex(week.index(day)))

    sorted_by_values_desc = sorted(allTimes.items(), key = lambda item: item[1], reverse = True)

    topScores = []
    for i in range(5):
        topScores.append(sorted_by_values_desc[i][0])

    return topScores

    

if __name__ == '__main__':
    soup = getSoup()
    h = get_timetable(soup)
    #print(h)

    bestTimesInWeek(h, 90)
    #print(bestTimesInWeek(h, 90))