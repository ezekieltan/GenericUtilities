import datetime
class DateHelper:
    __instance__ = None
    def __init__(self):
        if DateHelper.__instance__ is None:
            DateHelper.__instance__ = self
        else:
            pass
    @staticmethod
    def getInstance():
        if not DateHelper.__instance__:
            DateHelper()
        return DateHelper.__instance__
    
    
    @staticmethod
    def now():
        return datetime.datetime.now()
    @staticmethod
    def today():
        return DateHelper.getDateOnly(DateHelper.now())
    
    @staticmethod
    def getDateOnly(date):
        return date.replace(hour=0,minute=0,second=0,microsecond=0)
    @staticmethod
    def getISO8601String(date):
        return date.strftime("%Y-%m-%dT%H:%M:%SZ")
    @staticmethod
    def generateDateRange(startDate, endDate):
        if(endDate<startDate):
            temp = endDate
            endDate = startDate
            startDate = temp
        startDate = DateHelper.getDateOnly(startDate)
        endDate = DateHelper.getDateOnly(endDate)
        delta = endDate - startDate
        ranger = []
        for i in range(delta.days + 1):
            newDate = startDate + datetime.timedelta(days=i)
            newDate = DateHelper.getDateOnly(newDate)
            ranger.append(newDate)
        return ranger
        
    @staticmethod
    def getCurrentTimeZone():
        return datetime.datetime.now(datetime.timezone(datetime.timedelta(0))).astimezone().tzinfo
    @staticmethod
    def getCurrentTimeZoneOffset():
        return DateHelper.getCurrentTimeZone().utcoffset(DateHelper.now())
    @staticmethod
    def getCurrentTimeZoneName():
        return DateHelper.getCurrentTimeZone().tzname(DateHelper.now())