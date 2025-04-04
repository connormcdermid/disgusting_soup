from Day import Day
from timetable import makeTimetable


class algorithm:
    
    
    def addTime(self,a,b)->int:
        """adds a number of minutes to a time, and returns the result

        Args:
            a (_type_): the time to start with. Example "700" is 7 am.
            b (_type_): the number of Minutes to add to time a. Example "90" is one and a half hours.

        Returns:
            int: the time 'a' 'b' minutes later.
        """
        time=a+(int(b/60)*100)
        #print(time)
        time=time+(b%60)
        if(time>2400):
            time=time-2400
            
        return int(time)
        
    
    def bestTimeInDay(self, day: Day,meetingLength:int) -> list:
        """Computes a "viability" score for each possible meeting time in a day.

        Args:
            day (Day): Contains course schedule for that day
            meetingLength (int): length of the meeting in MINUTES.

        Returns:
            list: some sort of tuple with the time block start and end, and its "viability" score? 
        """

        for timeblock in day.keys():
            score=0
            start=int(timeblock[0])
            if(self.addTime(start,self.meetingLength))<2100:
                for i in range ():
                    pass
                
            
            
    
    def bestTimeInWeek(self,week:list[Day],meetingLength:int):
        """For every day in the week, compute the  3 best meeting times.

        Args:
            week (list[Day]): Represenation of all classes in a week
            meetingLength (int): length of the meeting in mintues.
        """
        
        #in this function we will select the highest scores adn return them.
        
        
        bestTimes = []
        for day in self.week:
            bestTimes.append(self.bestTimeInDay(day,meetingLength))
        
    
if __name__ == '__main__':
    a=algorithm(0,[])
    print(a.addTime(700,90))
    
    