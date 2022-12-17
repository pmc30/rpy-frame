import os
from day import Day
from hour import Hour
from minute import Minute
from month import Month
from week_day import Weekday
from year import Year


class Window:
    def __init__(self, json_config):
        self.is_valid = True
        self.display_times = []
        if isinstance(json_config, dict):
            try:
                self.name = json_config['name']
                self.priority = json_config['priority']
                self.folder = json_config['folder']
                self.when_to_display = json_config['when_to_display']
            except:
                self.is_valid = False
                print('Error: window must have a name, priority, folder, and when_to_display')

        self.check_input_is_valid()
        self.load_display_times()
        
    
    def check_input_is_valid(self):
        if not self.is_valid:
            return
        
        if not os.path.isdir(self.folder):
            print('Error: ' + str(self.name) + ' window has invalid folder: ' + str(self.folder))
            self.is_valid = False
        if not isinstance(self.priority, int):
            print('Error: ' + str(self.name) + ' window has invalid priority. Must be int: ' + str(self.priority))
            self.is_valid = False
        if not isinstance(self.when_to_display, dict):
            print('Error: ' + str(self.name) + ' window has invalid when_to_display. Must be dict')
            self.is_valid = False

            
    def load_display_times(self):
        if not self.is_valid:
            return
        
        checks = []
        for display_time in self.when_to_display:
            if display_time =='year':
                check = Year(self.when_to_display[display_time])
            elif display_time == 'month':
                check = Month(self.when_to_display[display_time])
            elif display_time == 'weekday':
                check = Weekday(self.when_to_display[display_time])  
            elif display_time == 'day':
                check = Day(self.when_to_display[display_time])  
            elif display_time == 'hour':
                check = Hour(self.when_to_display[display_time])
            elif display_time == 'minute':
                check = Minute(self.when_to_display[display_time])
            else:
                print('Error: ' + str(self.name) + ' window has invalid when_to_display key: ' +  str(display_time))
                self.is_valid = False
                return

            checks.append(check)
            
        for check in checks:
            if check.validate():
                self.display_times.append(check)
            else:
                print('Error: ' + str(self.name) + ' window has invalid time -  ' +  check.error_message)
                self.is_valid = False
                return                
                

    def in_display_window(self):
        return all(display_time.meets_criteria() for display_time in self.display_times)
      