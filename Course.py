from bs4 import BeautifulSoup as BS


class Course:

    def __init__(self, course_tag: BS):
        self.name = str(course_tag.CrsID.string) + " " + str(course_tag.Section.Intake.string)
        self.times = {}
        self.sections = course_tag.find_all('Section')
        for sec in self.sections:
            self.get_times(sec)

    def get_times(self, section: BS):
        for loc in section.find_all('Location'):
            for mtg in loc.Meetings:
                days = str(mtg.DaysOfWeek.string).split()
                start_time = str(mtg.StartTime.string)
                end_time = str(mtg.EndTime.string)
                for day in days:
                    self.times[day] = (start_time, end_time)

    def print_times(self):
        print(self.name, ":\n", ["{day}: {start_time} - {end_time}".format(
            day = day, start_time = t[0], end_time = t[1]
        ) for day, t in self.times.items()])