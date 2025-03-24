from bs4 import BeautifulSoup as BS


class Course:
    """A class that contains data about a particular course"""
    def __init__(self, course_tag: BS):
        """Initializes the Course object and its attributes, calls function to extract data from beautiful soup object."""
        self.name = str(course_tag.CrsID.string) + " " + str(course_tag.Section.Intake.string)
        self.times = {}
        self.sections = course_tag.find_all('Section')
        for sec in self.sections:
            self.get_times(sec)


    def get_times(self, section: BS):
        """extract times and day information from a beautiful soup object, add to the object's stored timetable """
        for loc in section.find_all('Location'):
            for mtg in loc.Meetings:
                days = str(mtg.DaysOfWeek.string).split()
                start_time = str(mtg.StartTime.string)
                end_time = str(mtg.EndTime.string)               
                for day in days:
                    if day not in self.times.keys():
                        self.times[day] = []
                    if (start_time, end_time) not in self.times[day]:
                        self.times[day].append((start_time, end_time))

    def print_times(self):
        """ Print the time/day data stored within the Course Object."""
        
        
        """
        for day in self.times.keys():
            for t in self.times[day]:
                print(self.name, ":\n", ["{day}: {start_time} - {end_time}".format(
                day = day, start_time = t[0], end_time = t[1])])
         """
        print(self.name, ":\n", end =" ")
        for day in self.times.keys():
            print(day, ': ', end ="")
            for t in self.times[day]:
                print(["{start_time} - {end_time}".format(
                start_time = t[0], end_time = t[1])], end =" ")  
        print()       
                