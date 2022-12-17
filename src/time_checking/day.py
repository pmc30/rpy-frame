import datetime
from time_type import Time_type


class Day(Time_type):

    def __init__(self, criteria):
        self.type_name = 'day'
        super().__init__(criteria)

    def check_range(self, int_in: int):
        return int_in >= 1 and int_in <=31

    def set_current_time(self):
        return datetime.datetime.now().day
