
class Time_type:

    def __init__(self, criteria):
        self.is_valid = False
        self.error_message = ''
        self.criteria = self.set_criteria(criteria)

    def set_criteria(self, criteria):
        return criteria
    
    def time_in_range(self, start, end, x):
        """Return true if x is in the range [start, end]"""
        if start <= end:
            return start <= x <= end
        else:
            return start <= x or x <= end
    
    def set_current_time(self):
        """The specific measurement of time (i.e day,month) is defined in the subclass"""
        pass

    def check_range(self):
        """The valid range of time is defined in the subclass"""
        pass

    def meets_criteria(self):
        current = self.set_current_time()

        if not self.is_valid:
           return False
        
        if isinstance(self.criteria, list):
            return self.time_in_range(self.criteria[0],self.criteria[1], current)
        else:
            return current == self.criteria

    def check_value(self,value):
        try:
            return self.check_range(value)
        except:
            self.error_message = 'Invalid ' + self.type_name + ': '+ str(self.criteria) + '. Must be int'
            return False

    def validate(self):
        # If an error message has already been set, exit function to preserve the message
        if len(self.error_message) > 0:
            return False
            
        if isinstance(self.criteria, list) and len(self.criteria) == 2:
            if self.check_value(self.criteria[0]) and self.check_value(self.criteria[1]):
                self.is_valid = True
            else:
                self.error_message = 'Invalid ' + self.type_name + ' range: ' + str(self.criteria)
        elif isinstance(self.criteria, int):
            if self.check_value(self.criteria):
                self.is_valid = True
            else:
                self.error_message = 'Invalid ' + self.type_name + ': ' + str(self.criteria)
        else:
            self.error_message = 'Invalid ' + self.type_name + ' type: '+ str(self.criteria)
        
        return self.is_valid
