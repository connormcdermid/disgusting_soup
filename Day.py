class Day:
    """A class to hold a day of the week that holds all of the 30 minute timeblocks for it in a table.
    Each timeblock contains the name of a Course, should that course occur wihtin that time block.
    The table will be a dictionary, it will consist of keys which are 30 minute timeblocks 
    from 0700 - 2100 represented as tuples, and the values will be empty lists, which we will append courses to.
    """
    
    def __init__(self):
        """Initializes the Day object with a dictionary containing
        all time slots for a day as keys, and a list as a value.
        The list is used to store names of the courses that occur during that time block.
        """
        self.table = {}
        #this is NOT ass
        for time in range(700, 2100, 100):
            self.table[(str(time).zfill(4), str(time+30).zfill(4))] = []
            self.table[(str(time+30).zfill(4), str(time+100).zfill(4))] = []
            
            

    def addTime(self, name: str, start_time: str, end_time: str):
        """ Add a course to the correct time blocks contained in the object, given its start and end time."""
        if (type(start_time) == int or type(end_time) == int):
            start_time = str(start_time).zfill(4)
            end_time = str(end_time).zfill(4)

        for key in self.table.keys():

            if key[0] >= start_time and key[1] <= end_time:
                self.table[key].append(name)
        
    

if __name__ == '__main__':
    a = Day()
    
    a.addTime('CSCI 375', 1415, 1600)
    a.addTime('CSCI 370', '1300', '1430')
    a.addTime('CSCI 251', '1500', '1630')
    print (a.table)