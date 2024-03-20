import datetime

class DateFormat():
    @classmethod
    def convert_time(cls, date):
        return datetime.datetime.strftime(date, '%d/%m/%Y/%H:%M:%S')