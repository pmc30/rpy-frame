import datetime
from time_type import Time_type
import calendar


class Weekday(Time_type):

    def __init__(self, criteria):
         self.type_name = 'weekday'
         super().__init__(criteria)

    def set_criteria(self, criteria):
        determined_criteria = None
        days = dict(zip(calendar.day_name, range(7)))
        if isinstance(criteria, str):
            try:
                determined_criteria = days[criteria]
            except:
                self.error_message = 'Invalid ' + self.type_name + ': ' + str(criteria)

        elif isinstance(criteria, list) and len(criteria) == 2:
            if isinstance(criteria[0], str) and isinstance(criteria[1], str):
                try:
                    determined_criteria = [days[criteria[0]], days[criteria[1]]]
                except:
                    self.error_message = 'Invalid ' + self.type_name + ': ' + str(criteria)
            else:
                self.error_message = 'Invalid ' + self.type_name + '. List items must be both str: '+ str(criteria)
        else:
            self.error_message = 'Invalid ' + self.type_name + ' type: '+ str(criteria)
        
        return determined_criteria

    def check_range(self, int_in: int):
        return int_in >= 0 and int_in <=6

    def set_current_time(self):
        return datetime.datetime.now().weekday()
