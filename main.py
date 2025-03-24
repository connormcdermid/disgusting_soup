from netcode import get_data_as_string as get_data
from timetable import getSoupStr as getSoup
from timetable import get_timetable, get_heatmap
from Course import Course
from Day import Day
import sys

def linkage(dept: str, session: str) -> tuple[list[Day], list[Day]]:
    """"""
    response = get_data(dept, session) # get response data from SRS server
    response_bs = getSoup(response) # Convert into BS object
    tmtbl = get_timetable(response_bs) # Fetch created timetable
    htmp = get_heatmap(response_bs) # Fetch created heatmap
    ret: tuple[list[Day], list[Day]] = (tmtbl, htmp) # return both timetable and heatmap
    return ret

if __name__ == "__main__":
    print(i for i in linkage(sys.argv[1], sys.argv[2]))
