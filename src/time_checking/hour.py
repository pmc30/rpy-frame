import datetime
from time_type import Time_type


class Hour(Time_type):

    def __init__(self, criteria):
        self.type_name = 'hour'
        super().__init__(criteria)

    def check_range(self, int_in: int):
        return int_in >= 0 and int_in <=23

    def set_current_time(self):
        return datetime.datetime.now().hour
