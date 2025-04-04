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
        if(time%100>59):
            time=time+40
            
        return int(time)
        
    
    def bestTimeInDay(self,day:Day, meetingLength:int)->dict:
        """Computes a "viability" score for each possible meeting time in a day.

        Args:
            day (Day): Contains course schedule for that day
            meetingLength (int): length of the meeting in MINUTES.

        Returns:
            list: some sort of tuple with the time block start and end, and its "viability" score? 
        """
        meetingBlocks={}
        for timeblock in day.table.keys(): #we start at each 30 minute timeblock in a day
            score=0
            start=int(timeblock[0])
            if(self.addTime(start,meetingLength))<2100: #check if the time is early enough to have a full meeting before the day is over (9pm)
                meetingStart=start
                for i in range (1,int(meetingLength/30),1): #count the number of 30 min blocks the meeting takes, and check that number of blocks after the supposed start
                    print("i is ",i)
                    #sum number of classes in the meeting block
                    print('start',str(meetingStart).zfill(4))
                    print('end',str(self.addTime(meetingStart,i*30)).zfill(4))
                    
                    a=day.table[(str(meetingStart).zfill(4),str(self.addTime(meetingStart,30)).zfill(4))] #the list of courses occuring at a 30 min block
                    score += len(a)
                    meetingStart=self.addTime(meetingStart,30)
                    #print(start)
                    
                        
            meetingBlocks[(str(start).zfill(4),str(self.addTime(start,meetingLength)).zfill(4))]=score
            
        return meetingBlocks       
                
            
            
    
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
        
    
