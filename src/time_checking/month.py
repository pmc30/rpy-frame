import datetime
from time_type import Time_type
import calendar

class Month(Time_type):

    def __init__(self, criteria):
         self.type_name = 'month'
         super().__init__(criteria)         

    def set_criteria(self, criteria):
        determined_criteria = None
        month_list = list(calendar.month_name)
        if isinstance(criteria, int):
            determined_criteria =  criteria
        elif isinstance(criteria, str):
            try:
                determined_criteria = month_list.index(criteria)
            except:
                self.error_message = 'Invalid ' + self.type_name + ': ' + str(criteria)

        elif isinstance(criteria, list) and len(criteria) == 2:
            if isinstance(criteria[0], str) and isinstance(criteria[1], str):
                try:
                    determined_criteria = [month_list.index(criteria[0]), month_list.index(criteria[1])]
                except:
                    self.error_message = 'Invalid ' + self.type_name + ': ' + str(criteria)
            elif isinstance(criteria[0], int) and isinstance(criteria[1], int):
                determined_criteria =  criteria
            else:
                self.error_message = 'Invalid ' + self.type_name + '. List items must be both str or int: '+ str(criteria)
        else:
            self.error_message = 'Invalid ' + self.type_name + ' type: '+ str(criteria)
        
        return determined_criteria

    def check_range(self, int_in: int):
        return int_in >= 1 and int_in <=12

    def set_current_time(self):
        return datetime.datetime.now().month           
