from datetime import datetime,date,timedelta


def parser_time_index(start =[2019,1,1],end=[2019,12,31]):

    start, end = datetime(*start),datetime(*end)
    days = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    index = [list(map(str.lower,d.strftime("%B-%d").split("-")))  for d in days if d.weekday() in [0,3] ] 
 
    return index

class Parser:
    def __init__(self):
        pass


    @staticmethod
    def leadtime(string):

        s = string.split("/")

        ret = []
        for chunk in s:
            start,end = chunk.split("-")
            ret.extend(list(map(str,range(int(start),int(end)+24,24))))
        
        return ret

    @staticmethod
    def period(string):

        s = string.split("/")

        years = set()
        months = set()
        days = set()
        for chunk in s:
            start,end = chunk.split("-")
            start = datetime.strptime(start,"%Y%m%d")
            end = datetime.strptime(end,"%Y%m%d")
            period = [start + timedelta(days=x) for x in range(0, (end-start).days+1)]
            years.update([i.strftime("%Y") for i in period])
            months.update([i.strftime("%m") for i in period])
            days.update([i.strftime("%d") for i in period])

            
        
        return sorted(list(years)),sorted(list(months)),sorted(list(days))