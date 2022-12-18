import datetime
from time_checking.time_type import Time_type


class Minute(Time_type):

    def __init__(self, criteria):
         super().__init__(criteria)
         self.type_name = 'minute'

    def check_range(self, int_in: int):
        return int_in >= 0 and int_in <=59

    def set_current_time(self):
        return datetime.datetime.now().minute    